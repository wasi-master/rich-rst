"""Docutils directive implementations and Sphinx directive registration."""
import functools
import os
import re
import textwrap
import threading
from typing import Any, Callable, Dict, List, Optional, Tuple

# Imports from rich_rst._vendor.docutils package for the parsing
import rich_rst._vendor.docutils.nodes
import rich_rst._vendor.docutils.parsers.rst.directives.tables
import rich_rst._vendor.docutils.parsers.rst.languages.en
import rich_rst._vendor.docutils.parsers.rst.roles
import rich_rst._vendor.docutils.statemachine
import rich_rst._vendor.docutils.utils  # noqa: F401

# Imports from the rich package for the printing
from rich_rst._nodes import (
    _colSpan,
    _rowSpan,
    availability,
    centered_block,
    glossary_block,
    hlist_block,
    impl_detail,
    literalinclude_stub,
    py_desc,
    seealso,
    soft_deprecated,
    toctree_stub,
    versionmodified,
)
from rich_rst._vendor import docutils
from rich_rst._vendor.docutils.parsers.rst.roles import normalize_options

# ── Docutils directive classes for Sphinx-specific directives ─────────────────

class _VersionDirective(docutils.parsers.rst.Directive):
    """Handles ``.. versionadded::``, ``.. versionchanged::``, and ``.. deprecated::``.

    Matches Sphinx's signature: the version is the first argument and an
    optional explanation is the second. ``final_argument_whitespace`` lets
    the explanation span the indented line(s) immediately following the
    directive (no blank line required), per the Python devguide form
    ``.. versionchanged:: 2.0\\n   Added the *spam* parameter.``.
    """

    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}  # type: ignore[assignment,var-annotated]
    has_content = True

    def run(self) -> List[docutils.nodes.Node]:
        node = versionmodified(type=self.name, version=self.arguments[0])
        if len(self.arguments) > 1:
            explanation = self.arguments[1]
            inline_nodes, messages = self.state.inline_text(explanation, self.lineno)
            node += docutils.nodes.paragraph(explanation, '', *inline_nodes)
            node += messages
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _SeeAlsoDirective(docutils.parsers.rst.Directive):
    """Handles ``.. seealso::``."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}  # type: ignore[assignment,var-annotated]
    has_content = True

    def run(self) -> List[docutils.nodes.Node]:
        node = seealso()
        if self.arguments:
            node += docutils.nodes.paragraph(self.arguments[0], self.arguments[0])
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _CodeBlockDirective(docutils.parsers.rst.Directive):
    """Handles ``.. code-block::``, ``.. sourcecode::``, ``.. code::``."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'linenos': docutils.parsers.rst.directives.flag,
        'emphasize-lines': docutils.parsers.rst.directives.unchanged,
        'caption': docutils.parsers.rst.directives.unchanged,
        'name': docutils.parsers.rst.directives.unchanged,
        'dedent': docutils.parsers.rst.directives.unchanged,
        'force': docutils.parsers.rst.directives.flag,
        'class': docutils.parsers.rst.directives.unchanged,
        'number-lines': docutils.parsers.rst.directives.nonnegative_int,
        'lineno-start': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self) -> List[docutils.nodes.Node]:
        language = self.arguments[0] if self.arguments else None
        code = '\n'.join(self.content)
        # Support `:dedent:` option: either an integer number of spaces
        # to remove from each line, or empty/value-less to auto-dedent.
        dedent_opt = self.options.get('dedent')
        if dedent_opt is not None:
            if dedent_opt == '' or dedent_opt is True:
                code = textwrap.dedent(code)
            else:
                try:
                    n = int(dedent_opt)
                except (TypeError, ValueError):
                    code = textwrap.dedent(code)
                else:
                    new_lines = []
                    for line in code.splitlines():
                        # Remove up to n leading spaces from each line.
                        new_lines.append(re.sub(rf'^ {{0,{n}}}', '', line))
                    code = '\n'.join(new_lines)
        node = docutils.nodes.literal_block(code, code)
        if language:
            node['classes'] = ['code', language]
        else:
            node['classes'] = ['code']
        # Preserve directive options that are relevant to rendering
        # (e.g. :caption: and :name:) so the visitor can include them
        # in panel titles or elsewhere.
        caption_opt = self.options.get('caption')
        if caption_opt:
            node['caption'] = caption_opt
        name_opt = self.options.get('name')
        if name_opt:
            node['name'] = name_opt
        # Line number options: boolean `:linenos:` and numeric start
        linenos = 'linenos' in self.options
        if linenos:
            node['linenos'] = True
        # Support both Sphinx-style `:lineno-start:` and docutils `:number-lines:`
        if 'lineno-start' in self.options:
            try:
                node['start_line'] = int(self.options.get('lineno-start'))
            except (TypeError, ValueError):
                pass
        elif 'number-lines' in self.options:
            try:
                node['start_line'] = int(self.options.get('number-lines'))
            except (TypeError, ValueError):
                pass
        # Parse emphasize-lines option into a set of integers for Syntax.highlight_lines
        emphasize = self.options.get('emphasize-lines')
        if emphasize:
            highlight_lines: set[int] = set()
            for part in emphasize.split(','):
                part = part.strip()
                if not part:
                    continue
                if '-' in part:
                    try:
                        start_s, end_s = part.split('-', 1)
                        start = int(start_s)
                        end = int(end_s)
                        if start <= end:
                            highlight_lines.update(range(start, end + 1))
                    except ValueError:
                        # ignore malformed ranges
                        continue
                else:
                    try:
                        highlight_lines.add(int(part))
                    except ValueError:
                        # ignore malformed numbers
                        continue
            if highlight_lines:
                node['highlight_lines'] = highlight_lines
        return [node]


class _MathDirective(docutils.parsers.rst.Directive):
    """Handles ``.. math::`` with Sphinx-compatible option parsing."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'class': docutils.parsers.rst.directives.class_option,
        'name': docutils.parsers.rst.directives.unchanged,
        # Sphinx-specific options. These are accepted and preserved as node
        # attributes but intentionally no-op in terminal rendering.
        'nowrap': docutils.parsers.rst.directives.flag,
        'label': docutils.parsers.rst.directives.unchanged,
    }

    def run(self) -> List[docutils.nodes.Node]:
        blocks: List[str] = []
        if self.arguments:
            argument = self.arguments[0].strip()
            if argument:
                blocks.append(argument)
        if self.content:
            blocks.extend(block for block in '\n'.join(self.content).split('\n\n') if block)

        nodes: List[docutils.nodes.Node] = []
        for block in blocks:
            node = docutils.nodes.math_block(self.block_text, block)
            node['classes'] += self.options.get('class', [])
            if 'nowrap' in self.options:
                node['nowrap'] = True
            if 'label' in self.options:
                node['label'] = self.options['label']
            source, line = self.state_machine.get_source_and_line(self.lineno)
            node.source = source
            node.line = line
            self.add_name(node)
            nodes.append(node)
        return nodes


class _HighlightDirective(docutils.parsers.rst.Directive):
    """Handles ``.. highlight::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {  # type: ignore[assignment]
        'linenothreshold': docutils.parsers.rst.directives.nonnegative_int,
        'force': docutils.parsers.rst.directives.flag,
        'class': docutils.parsers.rst.directives.class_option,
    }

    def run(self) -> List[docutils.nodes.Node]:
        return []


class _CustomBlockQuote(docutils.parsers.rst.Directive):
    has_content = True
    option_spec = {
        'class': docutils.parsers.rst.directives.class_option,
    }
    classes: List[str] = []

    def run(self) -> List[docutils.nodes.Node]:
        self.assert_has_content()
        elements = self.state.block_quote(self.content, self.content_offset)
        for element in elements:
            if isinstance(element, docutils.nodes.block_quote):
                for cls in self.classes + self.options.get('class', []):
                    if cls not in element['classes']:
                        element['classes'].append(cls)
        return elements


class _Epigraph(_CustomBlockQuote):
    classes = ['epigraph']


class _Highlights(_CustomBlockQuote):
    classes = ['highlights']


class _PullQuote(_CustomBlockQuote):
    classes = ['pull-quote']



class _SilentDirective(docutils.parsers.rst.Directive):
    """No-op directive for index, tabularcolumns, etc."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        return []


class _CurrentModuleDirective(docutils.parsers.rst.Directive):
    """No-op directive for currentmodule, py:currentmodule."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        return []


class _OnlyDirective(docutils.parsers.rst.Directive):
    """Handles ``.. only::`` — always renders content."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        container = docutils.nodes.container()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return container.children


class _CenteredDirective(docutils.parsers.rst.Directive):
    """Handles ``.. centered::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        return [centered_block(text=self.arguments[0])]


class _HlistDirective(docutils.parsers.rst.Directive):
    """Handles ``.. hlist::`` — renders as a multi-column table."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'columns': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self) -> List[docutils.nodes.Node]:
        columns = self.options.get('columns', 2) or 2
        node = hlist_block(columns=columns)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def _parse_toctree_numbered(argument: Optional[str]) -> int:
    if argument is None:
        return 0
    value = argument.strip()
    if not value:
        return 0
    return docutils.parsers.rst.directives.nonnegative_int(value)


class _ToctreeDirective(docutils.parsers.rst.Directive):
    """Handles ``.. toctree::``."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'maxdepth': docutils.parsers.rst.directives.nonnegative_int,
        'caption': docutils.parsers.rst.directives.unchanged,
        'name': docutils.parsers.rst.directives.unchanged,
        'titlesonly': docutils.parsers.rst.directives.flag,
        'glob': docutils.parsers.rst.directives.flag,
        'hidden': docutils.parsers.rst.directives.flag,
        'includehidden': docutils.parsers.rst.directives.flag,
        'reversed': docutils.parsers.rst.directives.flag,
        'numbered': _parse_toctree_numbered,
    }

    def run(self) -> List[docutils.nodes.Node]:
        caption = self.options.get('caption', 'Contents')
        maxdepth = self.options.get('maxdepth', 0)
        entries = [
            line.strip() for line in self.content
            if line.strip() and not line.strip().startswith(':')
        ]
        reversed_entries = 'reversed' in self.options
        numbered_enabled = 'numbered' in self.options
        numbered_depth = self.options.get('numbered', 0)
        node = toctree_stub()
        node['caption'] = caption
        node['entries'] = entries
        node['maxdepth'] = maxdepth
        node['reversed'] = reversed_entries
        node['numbered_enabled'] = numbered_enabled
        node['numbered'] = numbered_depth
        return [node]


class _LiteralIncludeDirective(docutils.parsers.rst.Directive):
    """Handles ``.. literalinclude::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {  # type: ignore[assignment]
        'language': docutils.parsers.rst.directives.unchanged,
        'linenos': docutils.parsers.rst.directives.flag,
        'lines': docutils.parsers.rst.directives.unchanged,
        'start-after': docutils.parsers.rst.directives.unchanged,
        'end-before': docutils.parsers.rst.directives.unchanged,
        'encoding': docutils.parsers.rst.directives.unchanged,
        'dedent': docutils.parsers.rst.directives.unchanged,
        'tab-width': docutils.parsers.rst.directives.nonnegative_int,
        'caption': docutils.parsers.rst.directives.unchanged,
        'name': docutils.parsers.rst.directives.unchanged,
        'start-at': docutils.parsers.rst.directives.unchanged,
        'end-at': docutils.parsers.rst.directives.unchanged,
        'prepend': docutils.parsers.rst.directives.unchanged,
        'append': docutils.parsers.rst.directives.unchanged,
        'force': docutils.parsers.rst.directives.flag,
        'diff': docutils.parsers.rst.directives.unchanged,
    }

    def run(self) -> List[docutils.nodes.Node]:
        node = literalinclude_stub()
        node['filename'] = self.arguments[0]

        # Attempt to resolve and read the referenced file so the visitor can
        # render real content instead of a mere placeholder.
        rel_path = self.arguments[0]
        source_file = self.state_machine.get_source(self.lineno)
        if source_file and source_file not in ('<string>', '<stdin>', '<rst-document>'):
            base_dir = os.path.dirname(os.path.abspath(source_file))
            abs_path = os.path.join(base_dir, rel_path)
        else:
            abs_path = os.path.abspath(rel_path)

        language = self.options.get('language', '')
        encoding = self.options.get('encoding', 'utf-8')
        lines_opt = self.options.get('lines', '')
        linenos = 'linenos' in self.options

        try:
            with open(abs_path, encoding=encoding) as fh:
                content = fh.read()

            # Apply the ``lines`` option if provided (e.g., "1-5,8,10-20").
            if lines_opt:
                all_lines = content.splitlines(keepends=True)
                selected = []
                for part in lines_opt.split(','):
                    part = part.strip()
                    if '-' in part:
                        start_s, end_s = part.split('-', 1)
                        selected.extend(all_lines[int(start_s) - 1 : int(end_s)])
                    elif part:
                        selected.append(all_lines[int(part) - 1])
                content = ''.join(selected)

            node['content'] = content
            node['language'] = language
            node['linenos'] = linenos
        except (OSError, ValueError, IndexError):
            # File not found or unreadable — fall back to placeholder rendering.
            pass

        return [node]


class _ProductionListDirective(docutils.parsers.rst.Directive):
    """Handles ``.. productionlist::``."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        if self.content:
            code = '\n'.join(self.content)
        elif self.arguments:
            code = self.arguments[0]
        else:
            code = ''
        node = docutils.nodes.literal_block(code, code)
        node['classes'] = ['code', 'productionlist']
        return [node]


class _IncludeDirective(docutils.parsers.rst.Directive):
    """Handles ``.. include::`` — reads an external RST file and inlines it.

    Paths are resolved relative to the source document.  When ``safe_include``
    is ``True`` (the default), path traversal outside the source directory is
    rejected.  If the file cannot be read the directive emits a warning
    admonition instead of raising an error.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {  # type: ignore[assignment]
        'encoding': docutils.parsers.rst.directives.unchanged,
        'start-line': docutils.parsers.rst.directives.nonnegative_int,
        'end-line': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self) -> List[docutils.nodes.Node]:
        rel_path = self.arguments[0]
        source_file = self.state_machine.get_source(self.lineno)
        if source_file and source_file not in ('<string>', '<stdin>', '<rst-document>'):
            base_dir = os.path.dirname(os.path.abspath(source_file))
        else:
            base_dir = os.getcwd()

        abs_path = os.path.normpath(os.path.join(base_dir, rel_path))

        # Safety: reject path traversal outside the base directory.
        try:
            common = os.path.commonpath([abs_path, base_dir])
        except ValueError:
            # commonpath raises ValueError on Windows when paths are on
            # different drives — treat that as a traversal attempt.
            common = None
        if common != base_dir:
            stub = docutils.nodes.warning()
            stub += docutils.nodes.paragraph(
                text=f"Rejected include path outside source directory: {rel_path!r}"
            )
            return [stub]

        encoding = self.options.get('encoding', 'utf-8')
        start_line = self.options.get('start-line', None)
        end_line = self.options.get('end-line', None)

        try:
            with open(abs_path, encoding=encoding) as fh:
                content = fh.read()

            if start_line is not None or end_line is not None:
                lines = content.splitlines()
                content = '\n'.join(lines[start_line or 0:end_line])

            # Parse the included RST content as a nested document.
            import rich_rst._vendor.docutils.statemachine as _sm
            content_lines = _sm.StringList(
                content.splitlines(), source=abs_path
            )
            container = docutils.nodes.container()
            self.state.nested_parse(content_lines, 0, container)
            return container.children

        except (OSError, UnicodeDecodeError):
            stub = docutils.nodes.warning()
            stub += docutils.nodes.paragraph(
                text=f"Could not include file: {rel_path!r}"
            )
            return [stub]


class _GlossaryDirective(docutils.parsers.rst.Directive):
    """Handles ``.. glossary::``."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'sorted': docutils.parsers.rst.directives.flag,
    }

    def run(self) -> List[docutils.nodes.Node]:
        container = glossary_block()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        if 'sorted' in self.options:
            for child in container.children:
                if isinstance(child, docutils.nodes.definition_list):
                    child.children.sort(
                        key=lambda item: item.children[0].astext().strip().casefold()
                        if item.children
                        else ""
                    )
        return [container]


class _DeprecatedRemovedDirective(docutils.parsers.rst.Directive):
    """Handles ``.. deprecated-removed::``."""

    required_arguments = 2
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        version_str = f"{self.arguments[0]} (removed in {self.arguments[1]})"
        node = versionmodified(type='deprecated-removed', version=version_str)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _AvailabilityDirective(docutils.parsers.rst.Directive):
    """Handles ``.. availability::``.\n\n    The version is the first required argument. An optional explanation can\n    follow on the next indented line(s).
    """

    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        node = availability(version=self.arguments[0])
        if len(self.arguments) > 1:
            explanation = self.arguments[1]
            inline_nodes, messages = self.state.inline_text(explanation, self.lineno)
            node += docutils.nodes.paragraph(explanation, '', *inline_nodes)
            node += messages
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _SoftDeprecatedDirective(docutils.parsers.rst.Directive):
    """Handles ``.. soft-deprecated::``.\n\n    The version is the first required argument. An optional explanation can\n    follow on the next indented line(s).
    """

    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        node = soft_deprecated(version=self.arguments[0])
        if len(self.arguments) > 1:
            explanation = self.arguments[1]
            inline_nodes, messages = self.state.inline_text(explanation, self.lineno)
            node += docutils.nodes.paragraph(explanation, '', *inline_nodes)
            node += messages
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _ImplDetailDirective(docutils.parsers.rst.Directive):
    """Handles ``.. impl-detail::``."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {}  # type: ignore[assignment,var-annotated]

    def run(self) -> List[docutils.nodes.Node]:
        node = impl_detail()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _PyObjectDirective(docutils.parsers.rst.Directive):
    """Handles Python/C/C++/JS domain object-description directives."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'no-index': docutils.parsers.rst.directives.flag,
        'noindex': docutils.parsers.rst.directives.flag,
        'module': docutils.parsers.rst.directives.unchanged,
        'annotation': docutils.parsers.rst.directives.unchanged,
        'type': docutils.parsers.rst.directives.unchanged,
        'value': docutils.parsers.rst.directives.unchanged,
        'async': docutils.parsers.rst.directives.flag,
        'classmethod': docutils.parsers.rst.directives.flag,
        'staticmethod': docutils.parsers.rst.directives.flag,
        'abstract': docutils.parsers.rst.directives.flag,
        'final': docutils.parsers.rst.directives.flag,
        'canonical': docutils.parsers.rst.directives.unchanged,
        'platform': docutils.parsers.rst.directives.unchanged,
        'synopsis': docutils.parsers.rst.directives.unchanged,
        'deprecated': docutils.parsers.rst.directives.flag,
    }

    def run(self) -> List[docutils.nodes.Node]:
        if ':' in self.name:
            domain, _, objtype = self.name.partition(':')
        else:
            domain = "py"
            objtype = self.name
        node = py_desc(domain=domain, objtype=objtype, sig=self.arguments[0])
        if self.options:
            node['options'] = dict(self.options)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _AutodocDirective(docutils.parsers.rst.Directive):
    """Handles autodoc directives (automodule, autoclass, etc.)."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {  # type: ignore[assignment]
        'members': docutils.parsers.rst.directives.unchanged,
        'undoc-members': docutils.parsers.rst.directives.flag,
        'show-inheritance': docutils.parsers.rst.directives.flag,
        'member-order': docutils.parsers.rst.directives.unchanged,
        'exclude-members': docutils.parsers.rst.directives.unchanged,
        'private-members': docutils.parsers.rst.directives.unchanged,
        'special-members': docutils.parsers.rst.directives.unchanged,
        'inherited-members': docutils.parsers.rst.directives.unchanged,
        'no-index': docutils.parsers.rst.directives.flag,
        'noindex': docutils.parsers.rst.directives.flag,
        'synopsis': docutils.parsers.rst.directives.unchanged,
        'platform': docutils.parsers.rst.directives.unchanged,
        'deprecated': docutils.parsers.rst.directives.flag,
        'ignore-module-all': docutils.parsers.rst.directives.flag,
    }

    def run(self) -> List[docutils.nodes.Node]:
        return []


class _ParsedLiteralDirective(docutils.parsers.rst.Directive):
    option_spec = {'class': docutils.parsers.rst.directives.class_option,
                   'name': docutils.parsers.rst.directives.unchanged}
    has_content = True

    def run(self):
        options = normalize_options(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        text_nodes, messages = self.state.inline_text(text, self.lineno)
        node = docutils.nodes.literal_block(text, '', *text_nodes, **options)
        node.setdefault('classes', []).append('parsed-literal')
        node.line = self.content_offset + 1
        self.add_name(node)
        return [node, *messages]


# ── flat-table directive ───────────────────────────────────────────────────────
# The flat-table directive is described in the Linux kernel Sphinx documentation
# guide (https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html).
# This is an independent implementation.


def _flat_table_cspan(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Any,
    options: Optional[Dict[str, Any]] = None,
    content: Optional[List[str]] = None,
) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
    """Role handler for ``:cspan:`` — extra columns a cell spans."""
    try:
        n = int(text)
        if n < 0:
            raise ValueError
    except ValueError:
        msg = inliner.reporter.error(
            f":cspan: requires a non-negative integer, got {text!r}",
            line=lineno,
        )
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    return [_colSpan(span=n)], []


def _flat_table_rspan(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Any,
    options: Optional[Dict[str, Any]] = None,
    content: Optional[List[str]] = None,
) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
    """Role handler for ``:rspan:`` — extra rows a cell spans."""
    try:
        n = int(text)
        if n < 0:
            raise ValueError
    except ValueError:
        msg = inliner.reporter.error(
            f":rspan: requires a non-negative integer, got {text!r}",
            line=lineno,
        )
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    return [_rowSpan(span=n)], []


class _FlatTableDirective(docutils.parsers.rst.directives.tables.Table):
    """Implementation of the ``flat-table`` directive.

    A flat-table is written as a two-level bullet list.  The outer items are
    rows; the inner items are cells.  Cells may carry ``:rspan:`` and
    ``:cspan:`` roles to span rows or columns.  Missing cells on the right
    side of a row are auto-extended (or filled with empty cells when
    ``:fill-cells:`` is given).
    """

    option_spec = {
        'name': docutils.parsers.rst.directives.unchanged,
        'class': docutils.parsers.rst.directives.class_option,
        'header-rows': docutils.parsers.rst.directives.nonnegative_int,
        'stub-columns': docutils.parsers.rst.directives.nonnegative_int,
        'widths': docutils.parsers.rst.directives.positive_int_list,
        'fill-cells': docutils.parsers.rst.directives.flag,
    }

    def run(self) -> List[docutils.nodes.Node]:
        if not self.content:
            error = self.state_machine.reporter.error(
                f'The "{self.name}" directive is empty; content required.',
                docutils.nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        title, messages = self.make_title()
        node = docutils.nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node)

        builder = _FlatTableBuilder(self)
        builder.parse_flat_table_node(node)
        table_node = builder.build_table_node()
        if title:
            table_node.insert(0, title)
        return [table_node, *messages]


class _FlatTableBuilder:
    """Converts a two-level bullet list into a docutils ``table`` node."""

    def __init__(self, directive: _FlatTableDirective) -> None:
        self.directive = directive
        self.rows: List[List[Any]] = []
        self.max_cols = 0

    def build_table_node(self) -> docutils.nodes.table:
        col_widths = self.directive.get_column_widths(self.max_cols)
        if isinstance(col_widths, tuple):
            col_widths = col_widths[1]

        stub_columns = self.directive.options.get('stub-columns', 0)
        header_rows = self.directive.options.get('header-rows', 0)

        table = docutils.nodes.table()
        tgroup = docutils.nodes.tgroup(cols=len(col_widths))
        table += tgroup

        remaining_stubs = stub_columns
        for colwidth in col_widths:
            colspec = docutils.nodes.colspec(colwidth=colwidth)
            if remaining_stubs:
                colspec.attributes['stub'] = 1
                remaining_stubs -= 1
            tgroup += colspec

        if header_rows:
            thead = docutils.nodes.thead()
            tgroup += thead
            for row in self.rows[:header_rows]:
                thead += self._build_row_node(row)

        tbody = docutils.nodes.tbody()
        tgroup += tbody
        for row in self.rows[header_rows:]:
            tbody += self._build_row_node(row)

        return table

    def _build_row_node(self, row_data: List[Any]) -> docutils.nodes.row:
        row = docutils.nodes.row()
        for cell in row_data:
            if cell is None:
                continue
            cspan, rspan, cell_elements = cell
            attrs: Dict[str, Any] = {'classes': []}
            if rspan:
                attrs['morerows'] = rspan
            if cspan:
                attrs['morecols'] = cspan
            entry = docutils.nodes.entry(**attrs)
            entry.extend(cell_elements)
            row += entry
        return row

    def _raise_error(self, msg: str) -> None:
        error = self.directive.state_machine.reporter.error(
            msg,
            docutils.nodes.literal_block(
                self.directive.block_text, self.directive.block_text
            ),
            line=self.directive.lineno,
        )
        from rich_rst._vendor.docutils.utils import SystemMessagePropagation
        raise SystemMessagePropagation(error)

    def parse_flat_table_node(self, node: docutils.nodes.Element) -> None:
        if len(node) != 1 or not isinstance(node[0], docutils.nodes.bullet_list):
            self._raise_error(
                f'Error parsing content block for the "{self.directive.name}" directive: '
                'exactly one bullet list expected.'
            )

        for row_num, row_item in enumerate(node[0]):
            row = self._parse_row_item(row_item, row_num)
            self.rows.append(row)

        self._build_grid()

    def _build_grid(self) -> None:
        """Assign column positions to cells and insert None placeholders for spanned slots.

        Phase 1: walk rows in order, tracking which (row, col) positions are
        already claimed by a spanning cell via an occupancy set.  Each cell
        lands in the first unoccupied column in its row.

        Phase 2: rebuild self.rows as flat lists (None for occupied slots,
        tuple for real cells) and pad the right edge with auto-span or
        fill-cells as requested.
        """
        occupied: set = set()  # (row_idx, col_idx) positions pre-filled by a span
        positioned: List[List[Any]] = []

        for r, row in enumerate(self.rows):
            col = 0
            row_cells: List[Any] = []
            for cspan, rspan, content in row:
                while (r, col) in occupied:
                    col += 1
                row_cells.append((col, cspan, rspan, content))
                for dr in range(rspan + 1):
                    for dc in range(cspan + 1):
                        if dr > 0 or dc > 0:
                            occupied.add((r + dr, col + dc))
                col += cspan + 1
            positioned.append(row_cells)

        for row_cells in positioned:
            for col, cspan, _rspan, _content in row_cells:
                self.max_cols = max(self.max_cols, col + cspan + 1)

        fill_cells = 'fill-cells' in self.directive.options
        self.rows = []
        for row_cells in positioned:
            parsed_row: List[Any] = []
            col_cursor = 0
            for col, cspan, rspan, content in row_cells:
                while col_cursor < col:
                    parsed_row.append(None)
                    col_cursor += 1
                parsed_row.append((cspan, rspan, content))
                col_cursor += cspan + 1
            missing = self.max_cols - col_cursor
            if missing > 0:
                if not fill_cells:
                    if parsed_row and parsed_row[-1] is not None:
                        cspan, rspan, content = parsed_row[-1]
                        parsed_row[-1] = (cspan + missing, rspan, content)
                    else:
                        parsed_row.append((missing - 1, 0, []))
                else:
                    for _ in range(missing):
                        parsed_row.append((0, 0, [docutils.nodes.comment()]))
            self.rows.append(parsed_row)

    def _parse_row_item(self, row_item: docutils.nodes.list_item, row_num: int) -> List[Any]:
        row: List[Any] = []
        child_no = 0
        error = False
        cell_list: Optional[docutils.nodes.bullet_list] = None

        for child in row_item.children:
            if isinstance(child, (docutils.nodes.comment, docutils.nodes.system_message)):
                pass
            elif isinstance(child, docutils.nodes.target):
                pass
            elif isinstance(child, docutils.nodes.bullet_list):
                child_no += 1
                cell_list = child
            else:
                error = True
                break

        if child_no != 1 or error:
            self._raise_error(
                f'Error parsing content block for the "{self.directive.name}" directive: '
                f'two-level bullet list expected, but row {row_num + 1} does not '
                'contain a second-level bullet list.'
            )

        assert cell_list is not None
        for cell_item in cell_list.children:
            cspan, rspan, cell_elements = self._parse_cell_item(cell_item)
            row.append((cspan, rspan, cell_elements))
        return row

    def _parse_cell_item(
        self, cell_item: docutils.nodes.list_item
    ) -> Tuple[int, int, List[docutils.nodes.Node]]:
        cspan = rspan = 0
        if not len(cell_item):
            return cspan, rspan, []
        for elem in list(cell_item.findall(_colSpan)):
            cspan = elem.get('span')
            elem.parent.remove(elem)
        for elem in list(cell_item.findall(_rowSpan)):
            rspan = elem.get('span')
            elem.parent.remove(elem)
        return cspan, rspan, list(cell_item.children)


_sphinx_directives_registered = False
# This lock serialises one-time directive and role registration within a
# single Python process.  Each worker process in a multi-process build gets
# its own GIL, its own module state, and therefore its own lock — registration
# happens independently (and correctly) in every process.
_sphinx_registration_lock = threading.Lock()


def _sphinx_registration_guard(function: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with _sphinx_registration_lock:
            return function(*args, **kwargs)

    return wrapper


def _register_sphinx_directives() -> None:
    """Register Sphinx-specific directives so they render properly instead of as errors."""
    global _sphinx_directives_registered

    with _sphinx_registration_lock:
        if _sphinx_directives_registered:
            return

        docutils.parsers.rst.directives.register_directive('versionadded', _VersionDirective)
        docutils.parsers.rst.directives.register_directive('versionchanged', _VersionDirective)
        docutils.parsers.rst.directives.register_directive('deprecated', _VersionDirective)
        docutils.parsers.rst.directives.register_directive('seealso', _SeeAlsoDirective)

        # code-block
        for name in ('code-block', 'sourcecode', 'code'):
            docutils.parsers.rst.directives.register_directive(name, _CodeBlockDirective)
        # math (accept Sphinx options like :nowrap: and :label:)
        docutils.parsers.rst.directives.register_directive('math', _MathDirective)
        # highlight
        docutils.parsers.rst.directives.register_directive('highlight', _HighlightDirective)
        # block quotes
        docutils.parsers.rst.directives.register_directive('epigraph', _Epigraph)
        docutils.parsers.rst.directives.register_directive('highlights', _Highlights)
        docutils.parsers.rst.directives.register_directive('pull-quote', _PullQuote)
        # silent no-op
        for name in ('index', 'tabularcolumns'):
            docutils.parsers.rst.directives.register_directive(name, _SilentDirective)
        # current module
        for name in ('currentmodule', 'py:currentmodule'):
            docutils.parsers.rst.directives.register_directive(name, _CurrentModuleDirective)
        # only
        docutils.parsers.rst.directives.register_directive('only', _OnlyDirective)
        # centered
        docutils.parsers.rst.directives.register_directive('centered', _CenteredDirective)
        # hlist
        docutils.parsers.rst.directives.register_directive('hlist', _HlistDirective)
        # toctree
        docutils.parsers.rst.directives.register_directive('toctree', _ToctreeDirective)
        # literalinclude
        docutils.parsers.rst.directives.register_directive('literalinclude', _LiteralIncludeDirective)
        # productionlist
        docutils.parsers.rst.directives.register_directive('productionlist', _ProductionListDirective)
        # glossary
        docutils.parsers.rst.directives.register_directive('glossary', _GlossaryDirective)
        # deprecated-removed
        docutils.parsers.rst.directives.register_directive('deprecated-removed', _DeprecatedRemovedDirective)
        # availability
        docutils.parsers.rst.directives.register_directive('availability', _AvailabilityDirective)
        # soft-deprecated
        docutils.parsers.rst.directives.register_directive('soft-deprecated', _SoftDeprecatedDirective)
        # impl-detail
        docutils.parsers.rst.directives.register_directive('impl-detail', _ImplDetailDirective)
        # include (safe custom implementation with path-traversal guard)
        docutils.parsers.rst.directives.register_directive('include', _IncludeDirective)
        # class and role: no visual output in terminal rendering; register as no-ops
        # to prevent "Unknown directive" errors in Sphinx-style documents.
        for name in ('class', 'role'):
            docutils.parsers.rst.directives.register_directive(name, _SilentDirective)
        # Python domain object descriptions
        for name in (
            'py:function', 'py:class', 'py:method', 'py:attribute', 'py:data',
            'py:exception', 'py:module', 'py:property', 'py:decorator',
            'py:classmethod', 'py:staticmethod', 'py:variable', 'py:type',
            'py:typevar', 'py:typealias', 'py:envvar', 'py:option',
            'py:coroutinefunction',
            'py:coroutinemethod', 'py:decoratorfunction', 'py:abstractmethod',
            'py:opcode', 'py:describe',
            # C domain
            'c:function', 'c:type', 'c:struct', 'c:union', 'c:enum',
            'c:enumerator', 'c:member', 'c:var', 'c:macro',
            # C++ domain
            'cpp:function', 'cpp:class', 'cpp:type', 'cpp:member', 'cpp:var',
            'cpp:enum', 'cpp:enumerator', 'cpp:concept', 'cpp:alias',
            # JavaScript domain
            'js:function', 'js:class', 'js:method', 'js:attribute', 'js:data',
            'js:module',
        ):
            docutils.parsers.rst.directives.register_directive(name, _PyObjectDirective)
        # autodoc
        for name in (
            'automodule', 'autoclass', 'autofunction', 'automethod',
            'autoattribute', 'autoexception', 'autodata', 'autoproperty',
            'autodecorator', 'autoclassmethod', 'autostaticmethod',
        ):
            docutils.parsers.rst.directives.register_directive(name, _AutodocDirective)
        # flat-table (Linux kernel docs extension)
        docutils.parsers.rst.directives.register_directive('flat-table', _FlatTableDirective)
        # cspan / rspan roles used inside flat-table cells
        import rich_rst._vendor.docutils.parsers.rst.languages.en as _en
        import rich_rst._vendor.docutils.parsers.rst.roles as _roles
        _roles.register_canonical_role('cspan', _flat_table_cspan)
        _roles.register_canonical_role('rspan', _flat_table_rspan)
        if hasattr(_en, 'roles'):
            _en.roles['cspan'] = 'cspan'
            _en.roles['rspan'] = 'rspan'

        _sphinx_directives_registered = True

