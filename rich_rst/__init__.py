# -*- coding: utf-8 -*-

"""
reStructuredText parser for rich

Initial few lines gotten from: https://github.com/willmcgugan/rich/discussions/1263#discussioncomment-808898
There are a lot of improvements are added by me
"""
from io import StringIO
from html.parser import HTMLParser
from typing import Optional, Union

# Imports from rich_rst._vendor.docutils package for the parsing
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core
import rich_rst._vendor.docutils.frontend
import rich_rst._vendor.docutils.io
import rich_rst._vendor.docutils.nodes
import rich_rst._vendor.docutils.parsers.rst
import rich_rst._vendor.docutils.parsers.rst.directives
import rich_rst._vendor.docutils.utils

# Imports from the rich package for the printing
import rich
from rich import box
from rich.align import Align
from rich.console import Console, ConsoleOptions, RenderResult, NewLine, Group
from rich.jupyter import JupyterMixin
from rich.panel import Panel
from rich.style import Style
from rich.syntax import Syntax, SyntaxTheme
from rich.text import Text
from rich.table import Table
from rich.rule import Rule

from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

__all__ = ("RST", "ReStructuredText", "reStructuredText", "RestructuredText")
__author__ = "Arian Mollik Wasi (aka. Wasi Master)"
__version__ = "1.3.2"


# ── Custom nodes for Sphinx directives ───────────────────────────────────────

class versionmodified(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node produced by the versionadded, versionchanged, and deprecated directives."""
    pass


class seealso(docutils.nodes.Admonition, docutils.nodes.Element):
    """Node produced by the seealso directive."""
    pass


class centered_block(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. centered:: directive."""
    pass


class py_desc(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for Python/C/C++/JS domain object-description directives."""
    pass


class toctree_stub(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. toctree:: directive."""
    pass


class literalinclude_stub(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. literalinclude:: directive."""
    pass


class glossary_block(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. glossary:: directive."""
    pass


# ── Docutils directive classes for Sphinx-specific directives ─────────────────

class _VersionDirective(docutils.parsers.rst.Directive):
    """Handles ``.. versionadded::``, ``.. versionchanged::``, and ``.. deprecated::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    def run(self):
        node = versionmodified(type=self.name, version=self.arguments[0])
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _SeeAlsoDirective(docutils.parsers.rst.Directive):
    """Handles ``.. seealso::``."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    def run(self):
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
    option_spec = {
        'linenos': docutils.parsers.rst.directives.flag,
        'emphasize-lines': docutils.parsers.rst.directives.unchanged,
        'caption': docutils.parsers.rst.directives.unchanged,
        'name': docutils.parsers.rst.directives.unchanged,
        'dedent': docutils.parsers.rst.directives.unchanged,
        'force': docutils.parsers.rst.directives.flag,
        'class': docutils.parsers.rst.directives.unchanged,
        'number-lines': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self):
        language = self.arguments[0] if self.arguments else None
        code = '\n'.join(self.content)
        node = docutils.nodes.literal_block(code, code)
        if language:
            node['classes'] = ['code', language]
        else:
            node['classes'] = ['code']
        return [node]


class _HighlightDirective(docutils.parsers.rst.Directive):
    """Handles ``.. highlight::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'linenothreshold': docutils.parsers.rst.directives.nonnegative_int,
        'force': docutils.parsers.rst.directives.flag,
    }

    def run(self):
        return []


class _SilentDirective(docutils.parsers.rst.Directive):
    """No-op directive for index, tabularcolumns, etc."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}

    def run(self):
        return []


class _CurrentModuleDirective(docutils.parsers.rst.Directive):
    """No-op directive for currentmodule, py:currentmodule."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {}

    def run(self):
        return []


class _OnlyDirective(docutils.parsers.rst.Directive):
    """Handles ``.. only::`` — always renders content."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {}

    def run(self):
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
    option_spec = {}

    def run(self):
        return [centered_block(text=self.arguments[0])]


class _HlistDirective(docutils.parsers.rst.Directive):
    """Handles ``.. hlist::`` — renders as plain bullet list."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'columns': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self):
        container = docutils.nodes.container()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return container.children


class _ToctreeDirective(docutils.parsers.rst.Directive):
    """Handles ``.. toctree::``."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'maxdepth': docutils.parsers.rst.directives.nonnegative_int,
        'caption': docutils.parsers.rst.directives.unchanged,
        'name': docutils.parsers.rst.directives.unchanged,
        'titlesonly': docutils.parsers.rst.directives.flag,
        'glob': docutils.parsers.rst.directives.flag,
        'hidden': docutils.parsers.rst.directives.flag,
        'includehidden': docutils.parsers.rst.directives.flag,
        'reversed': docutils.parsers.rst.directives.flag,
        'numbered': docutils.parsers.rst.directives.nonnegative_int,
    }

    def run(self):
        caption = self.options.get('caption', 'Contents')
        entries = [
            line.strip() for line in self.content
            if line.strip() and not line.strip().startswith(':')
        ]
        node = toctree_stub()
        node['caption'] = caption
        node['entries'] = entries
        return [node]


class _LiteralIncludeDirective(docutils.parsers.rst.Directive):
    """Handles ``.. literalinclude::``."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {
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

    def run(self):
        node = literalinclude_stub()
        node['filename'] = self.arguments[0]
        return [node]


class _ProductionListDirective(docutils.parsers.rst.Directive):
    """Handles ``.. productionlist::``."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}

    def run(self):
        if self.content:
            code = '\n'.join(self.content)
        elif self.arguments:
            code = self.arguments[0]
        else:
            code = ''
        node = docutils.nodes.literal_block(code, code)
        node['classes'] = ['code', 'text']
        return [node]


class _GlossaryDirective(docutils.parsers.rst.Directive):
    """Handles ``.. glossary::``."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'sorted': docutils.parsers.rst.directives.flag,
    }

    def run(self):
        container = glossary_block()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


class _DeprecatedRemovedDirective(docutils.parsers.rst.Directive):
    """Handles ``.. deprecated-removed::``."""

    required_arguments = 2
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {}

    def run(self):
        version_str = f"{self.arguments[0]} (removed in {self.arguments[1]})"
        node = versionmodified(type='deprecated-removed', version=version_str)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _PyObjectDirective(docutils.parsers.rst.Directive):
    """Handles Python/C/C++/JS domain object-description directives."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
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

    def run(self):
        if ':' in self.name:
            _, _, objtype = self.name.partition(':')
        else:
            objtype = self.name
        node = py_desc(objtype=objtype, sig=self.arguments[0])
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class _AutodocDirective(docutils.parsers.rst.Directive):
    """Handles autodoc directives (automodule, autoclass, etc.)."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
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

    def run(self):
        return []


_sphinx_directives_registered = False


def _register_sphinx_directives():
    """Register Sphinx-specific directives so they render properly instead of as errors."""
    global _sphinx_directives_registered

    if _sphinx_directives_registered:
        return

    docutils.parsers.rst.directives.register_directive('versionadded', _VersionDirective)
    docutils.parsers.rst.directives.register_directive('versionchanged', _VersionDirective)
    docutils.parsers.rst.directives.register_directive('deprecated', _VersionDirective)
    docutils.parsers.rst.directives.register_directive('seealso', _SeeAlsoDirective)

    # code-block
    for name in ('code-block', 'sourcecode', 'code'):
        docutils.parsers.rst.directives.register_directive(name, _CodeBlockDirective)
    # highlight
    docutils.parsers.rst.directives.register_directive('highlight', _HighlightDirective)
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
    # Python domain object descriptions
    for name in (
        'py:function', 'py:class', 'py:method', 'py:attribute', 'py:data',
        'py:exception', 'py:module', 'py:property', 'py:decorator',
        'py:classmethod', 'py:staticmethod', 'py:variable', 'py:type',
        'py:typevar', 'py:typealias',
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

    _sphinx_directives_registered = True


_sphinx_roles_registered = False



class MLStripper(HTMLParser):
    """Utility class to strip out html for raw html source"""
    def __init__(self):
        super().__init__()
        self.reset()
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    try:
        s.feed(html)
        s.close()
    except Exception:
        return html
    return s.get_data()


def _register_sphinx_roles():
    """
    Register common Sphinx roles to gracefully handle Sphinx-specific markup.

    Sphinx roles like :func:, :class:, :meth: are very common in Python docstrings
    but are not available in standard docutils. This function registers them to
    render as inline code/literal text instead of showing errors.
    """
    global _sphinx_roles_registered

    if _sphinx_roles_registered:
        return

    from rich_rst._vendor import docutils
    import rich_rst._vendor.docutils.parsers.rst.roles
    import rich_rst._vendor.docutils.parsers.rst.languages.en

    def sphinx_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        """
        Generic Sphinx role handler that renders as inline literal text.

        Parameters
        ----------
        name : str
            The role name
        rawtext : str
            The entire role text including role markup
        text : str
            The interpreted text content
        lineno : int
            The line number where the interpreted text begins
        inliner : Inliner
            The inliner instance that called this role function
        options : dict
            Directive options for customization
        content : list
            The directive content for customization

        Returns
        -------
        tuple
            A tuple of (nodes, messages)
        """
        display_text = text
        if '<' in text and text.endswith('>'):
            bracket_pos = text.rfind('<')
            potential_display = text[:bracket_pos].strip()
            if potential_display:
                display_text = potential_display

        node = docutils.nodes.literal(rawtext, display_text)
        return [node], []

    sphinx_roles = [
        'func', 'function',
        'meth', 'method',
        'class',
        'mod', 'module',
        'attr', 'attribute',
        'obj', 'object',
        'data',
        'const', 'constant',
        'exc', 'exception',
        'var', 'variable',
        'type',
        'py:func', 'py:meth', 'py:class', 'py:mod', 'py:attr',
        'py:obj', 'py:data', 'py:const', 'py:exc',
        # Standard domain cross-reference roles
        'envvar', 'token', 'option', 'term', 'ref', 'doc', 'any', 'numref', 'download',
        # Misc
        'mailheader', 'mimetype', 'newsgroup', 'makevar', 'regexp',
        # Keyboard/GUI
        'kbd', 'guilabel',
        # Unix man pages
        'manpage',
        # Python domain additional
        'py:variable', 'py:type', 'py:property', 'py:parameter', 'py:typevar',
        # C domain
        'c:func', 'c:type', 'c:struct', 'c:union', 'c:enum', 'c:enumerator',
        'c:member', 'c:var', 'c:macro', 'c:expr', 'c:texpr',
        # C++ domain
        'cpp:func', 'cpp:class', 'cpp:type', 'cpp:member', 'cpp:var',
        'cpp:enum', 'cpp:enumerator', 'cpp:concept', 'cpp:expr', 'cpp:texpr',
        # JavaScript domain
        'js:mod', 'js:func', 'js:data', 'js:attr', 'js:class', 'js:meth',
    ]

    for role in sphinx_roles:
        docutils.parsers.rst.roles.register_canonical_role(role, sphinx_role)
        # Also register in language module to avoid INFO messages
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles[role] = role

    import re as _re

    # `:command:` and `:program:` → bold literal
    def _bold_literal_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        display_text = text
        if '<' in text and text.endswith('>'):
            bracket_pos = text.rfind('<')
            potential_display = text[:bracket_pos].strip()
            if potential_display:
                display_text = potential_display
        node = docutils.nodes.strong(rawtext, display_text)
        return [node], []

    for _role_name in ('command', 'program'):
        docutils.parsers.rst.roles.register_canonical_role(_role_name, _bold_literal_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles[_role_name] = _role_name

    # `:dfn:` → emphasis (italic)
    def _dfn_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        node = docutils.nodes.emphasis(rawtext, text)
        return [node], []

    docutils.parsers.rst.roles.register_canonical_role('dfn', _dfn_role)
    if hasattr(docutils.parsers.rst.languages.en, 'roles'):
        docutils.parsers.rst.languages.en.roles['dfn'] = 'dfn'

    # `:abbr:` → abbreviation node with explanation
    _abbr_re = _re.compile(r'\((.*)\)$', _re.DOTALL)

    def _abbr_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        matched = _abbr_re.search(text)
        if matched:
            abbr_text = text[:matched.start()].strip()
            explanation = matched.group(1)
        else:
            abbr_text = text
            explanation = ''
        node = docutils.nodes.abbreviation(rawtext, abbr_text, explanation=explanation)
        return [node], []

    docutils.parsers.rst.roles.register_canonical_role('abbr', _abbr_role)
    if hasattr(docutils.parsers.rst.languages.en, 'roles'):
        docutils.parsers.rst.languages.en.roles['abbr'] = 'abbr'

    # `:menuselection:` → replace `-->` with ` ▶ `
    def _menuselection_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        text = text.replace('-->', '\u25b6')
        node = docutils.nodes.literal(rawtext, text)
        return [node], []

    docutils.parsers.rst.roles.register_canonical_role('menuselection', _menuselection_role)
    if hasattr(docutils.parsers.rst.languages.en, 'roles'):
        docutils.parsers.rst.languages.en.roles['menuselection'] = 'menuselection'

    # `:samp:` and `:file:` → literal with {} stripped
    _braces_re = _re.compile(r'\{([^}]*)\}')

    def _samp_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        clean = _braces_re.sub(r'\1', text)
        node = docutils.nodes.literal(rawtext, clean)
        return [node], []

    for _role_name in ('samp', 'file'):
        docutils.parsers.rst.roles.register_canonical_role(_role_name, _samp_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles[_role_name] = _role_name

    # `:pep:` → bold text with clickable PEP link
    def _pep_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        parts = text.split('#', 1)
        pep_num_str = parts[0].strip()
        anchor = ('#' + parts[1]) if len(parts) > 1 else ''
        try:
            pep_num = int(pep_num_str)
            url = f"https://peps.python.org/pep-{pep_num:04d}/{anchor}"
        except ValueError:
            url = "https://peps.python.org/"
        display = f"PEP {pep_num_str} <{url}>"
        ref = docutils.nodes.reference(rawtext, display, refuri=url)
        return [ref], []

    docutils.parsers.rst.roles.register_canonical_role('pep', _pep_role)
    if hasattr(docutils.parsers.rst.languages.en, 'roles'):
        docutils.parsers.rst.languages.en.roles['pep'] = 'pep'

    # `:rfc:` → bold text with clickable RFC link
    def _rfc_role(name, rawtext, text, lineno, inliner, options=None, content=None):
        parts = text.split('#', 1)
        rfc_num_str = parts[0].strip()
        anchor = ('#' + parts[1]) if len(parts) > 1 else ''
        try:
            rfc_num = int(rfc_num_str)
            url = f"https://datatracker.ietf.org/doc/html/rfc{rfc_num}{anchor}"
        except ValueError:
            url = "https://datatracker.ietf.org/"
        display = f"RFC {rfc_num_str} <{url}>"
        ref = docutils.nodes.reference(rawtext, display, refuri=url)
        return [ref], []

    docutils.parsers.rst.roles.register_canonical_role('rfc', _rfc_role)
    if hasattr(docutils.parsers.rst.languages.en, 'roles'):
        docutils.parsers.rst.languages.en.roles['rfc'] = 'rfc'

    _sphinx_roles_registered = True


# pylama:ignore=D,C0116
class RSTVisitor(docutils.nodes.SparseNodeVisitor):
    """A visitor that produces rich renderables"""

    def __init__(
        self,
        document: docutils.nodes.document,
        console: Console,
        code_theme: Union[str, SyntaxTheme] = "monokai",
        show_line_numbers: Optional[bool] = False,
        guess_lexer: Optional[bool] = True,
        default_lexer: Optional[str] = "python",
    ) -> None:
        super().__init__(document)
        self.console = console
        self.code_theme = code_theme
        self.show_line_numbers = show_line_numbers
        self.renderables = []
        self.superscript = str.maketrans(
            "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=+-*/×÷",
            "¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ⁼⁺⁻*/×÷",
        )
        self.subscript = str.maketrans(
            "1234567890abcdefghijklmnopqrstuvwxyz=+-*/×÷", "₁₂₃₄₅₆₇₈₉₀abcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz₌₊₋*/×÷"
        )
        self.errors = []
        self.footer = []
        self.guess_lexer = guess_lexer
        self.default_lexer = default_lexer
        self.refname_to_renderable = {}

    def _guess_lexer_name(self, text):
        try:
            lexer = guess_lexer(text)
        except ClassNotFound:
            return self.default_lexer, False
        guessed = lexer.aliases[0] if lexer.aliases else None
        if guessed == "text" or guessed is None:
            return self.default_lexer, False
        return guessed, True

    def _find_lexer(self, node):
        lexer = (
            node["classes"][1] if len(node.get("classes")) >= 2 else (node["format"] if node.get("format") else None)
        )
        if lexer is not None:
            return lexer, "explicit"
        if self.guess_lexer:
            guessed_lexer, was_guessed = self._guess_lexer_name(node.astext())
            return guessed_lexer, "guessed" if was_guessed else "default"
        return self.default_lexer, "default"

    def _section_level(self, node):
        level = -1
        parent = getattr(node, "parent", None)
        while parent is not None:
            if isinstance(parent, docutils.nodes.section):
                level += 1
            parent = getattr(parent, "parent", None)
        return level

    def _render_heading(self, text, level):
        heading_levels = [
            ("restructuredtext.title.level.1", "bold", box.DOUBLE),
            ("restructuredtext.title.level.2", "bold", box.ROUNDED),
            ("restructuredtext.title.level.3", "bold underline", None),
            ("restructuredtext.title.level.4", "bold", None),
            ("restructuredtext.title.level.5", "underline", None),
            ("restructuredtext.title.level.6", "italic", None),
        ]
        index = min(level, len(heading_levels) - 1)
        style_name, default_style, panel_box = heading_levels[index]
        style = self.console.get_style(style_name, default=default_style)
        if panel_box is None:
            self.renderables.append(Align(Text(text, style=style), "center"))
            self.renderables.append(NewLine())
        else:
            self.renderables.append(Panel(Align(text, "center"), box=panel_box, style=style, border_style=style))

    def visit_reference(self, node):
        if len(node.children) == 1 and isinstance(node.children[0], docutils.nodes.image):
            return
        refuri = node.attributes.get("refuri")
        style = self.console.get_style("restructuredtext.reference", default="blue underline on default")
        if refuri:
            style = style.update_link(refuri)
        renderable = Text(node.astext().replace("\n", " "), style=style, end="")
        if self.renderables and isinstance(self.renderables[-1], Text):
            renderable.end = " "
            start = len(self.renderables[-1])
            # Calculate end based on what we're appending to avoid stale counter after merge.
            # Account for both the renderable text and its trailing space character.
            end = start + len(renderable) + len(renderable.end)
            self.renderables[-1].append_text(renderable)
        else:
            start = 0
            # Account for the trailing space character in the renderable.
            end = len(renderable) + len(renderable.end)
            self.renderables.append(renderable)

        if not refuri:
            # We'll get the URL reference later in visit_target.
            refname = node.attributes.get("refname")
            if refname:
                self.refname_to_renderable[refname] = (self.renderables[-1], start, end)
        raise docutils.nodes.SkipChildren()

    def visit_target(self, node):
        uri = node.get("refuri")
        if uri:
            for name in node["names"]:
                try:
                    renderable, start, end = self.refname_to_renderable[name]
                except KeyError:
                    continue
                style = renderable.get_style_at_offset(self.console, start)
                style = style.update_link(uri)
                renderable.stylize(style, start, end)
        raise docutils.nodes.SkipChildren()

    def visit_paragraph(self, node):
        if hasattr(node, "parent") and isinstance(node.parent, docutils.nodes.system_message):
            self.visit_system_message(node.parent)
            raise docutils.nodes.SkipChildren()

    def depart_paragraph(self, node):  # pylint: disable=unused-argument
        if self.renderables and isinstance(self.renderables[-1], Text):
            if self.renderables[-1]:
                self.renderables[-1].append("\n\n")

    def visit_title(self, node):
        level = self._section_level(node)
        self._render_heading(node.astext(), level)
        raise docutils.nodes.SkipChildren()

    def visit_rubric(self, node):
        style = self.console.get_style("restructuredtext.rubric", default="italic dim")
        self.renderables.append(Panel(Align(node.astext(), "center"), box=box.ROUNDED, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_Text(self, node):
        style = self.console.get_style("restructuredtext.text", default="default on default not underline")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            return
        self.renderables.append(Text(node.astext().replace("\n", " "), end="", style=style))

    def visit_comment(self, node):
        raise docutils.nodes.SkipChildren()

    def visit_substitution_definition(self, node):
        raise docutils.nodes.SkipChildren()

    def _render_admonition_body(self, children):
        """Render admonition body children using a sub-visitor to preserve inline markup."""
        sub_visitor = RSTVisitor(
            self.document,
            console=self.console,
            code_theme=self.code_theme,
            show_line_numbers=self.show_line_numbers,
            guess_lexer=self.guess_lexer,
            default_lexer=self.default_lexer,
        )
        for child in children:
            child.walkabout(sub_visitor)
        return sub_visitor.renderables

    def _render_child_inline(self, child):
        """Render a single child node using a sub-visitor to preserve inline markup.

        This is used for list items and other contexts where we want to preserve
        bold, italic, links, inline code, and other inline markup instead of
        stripping to plain text via astext().
        """
        sub_visitor = RSTVisitor(
            self.document,
            console=self.console,
            code_theme=self.code_theme,
            show_line_numbers=self.show_line_numbers,
            guess_lexer=self.guess_lexer,
            default_lexer=self.default_lexer,
        )
        child.walkabout(sub_visitor)
        return sub_visitor.renderables

    def visit_admonition(self, node):
        style = self.console.get_style("restructuredtext.admonition", default="bold white")
        # Generic admonition: first child is the user-supplied title node
        if node.children and isinstance(node.children[0], docutils.nodes.title):
            title = node.children[0].astext()
            body_children = node.children[1:]
        else:
            title = "Admonition: "
            body_children = node.children
        body = self._render_admonition_body(body_children)
        self.renderables.append(Panel(Group(*body) if body else "", title=title, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_attention(self, node):
        style = self.console.get_style("restructuredtext.attention", default="bold black on yellow")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Attention: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_caution(self, node):
        style = self.console.get_style("restructuredtext.caution", default="red")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Caution: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_danger(self, node):
        style = self.console.get_style("restructuredtext.danger", default="bold white on red")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="DANGER: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_error(self, node):
        style = self.console.get_style("restructuredtext.error", default="bold red")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="ERROR: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_hint(self, node):
        style = self.console.get_style("restructuredtext.hint", default="yellow")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Hint: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_important(self, node):
        style = self.console.get_style("restructuredtext.important", default="bold blue")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="IMPORTANT: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_note(self, node):
        style = self.console.get_style("restructuredtext.note", default="bold white")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Note: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_tip(self, node):
        style = self.console.get_style("restructuredtext.tip", default="bold green")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Tip: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_warning(self, node):
        style = self.console.get_style("restructuredtext.warning", default="bold yellow")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="Warning: ", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_versionmodified(self, node):
        type_ = node.get("type", "versionadded")
        version = node.get("version", "")
        style_map = {
            "versionadded": ("restructuredtext.versionadded", "bold green"),
            "versionchanged": ("restructuredtext.versionchanged", "bold cyan"),
            "deprecated": ("restructuredtext.deprecated", "bold yellow"),
            "deprecated-removed": ("restructuredtext.deprecated_removed", "bold red"),
        }
        title_map = {
            "versionadded": f"New in version {version}",
            "versionchanged": f"Changed in version {version}",
            "deprecated": f"Deprecated since version {version}",
            "deprecated-removed": f"Deprecated since version {version}",
        }
        style_name, default_style = style_map.get(type_, ("restructuredtext.versionadded", "bold green"))
        title = title_map.get(type_, f"{type_} {version}")
        style = self.console.get_style(style_name, default=default_style)
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title=title, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def depart_versionmodified(self, node):
        pass

    def visit_seealso(self, node):
        style = self.console.get_style("restructuredtext.seealso", default="bold white")
        body = self._render_admonition_body(node.children)
        self.renderables.append(Panel(Group(*body) if body else "", title="See Also", style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def depart_seealso(self, node):
        pass

    def visit_centered_block(self, node):
        style = self.console.get_style("restructuredtext.centered", default="bold")
        text = node.get('text', '')
        self.renderables.append(Align(Text(text, style=style), "center"))
        raise docutils.nodes.SkipChildren()

    def depart_centered_block(self, node):
        pass

    def visit_py_desc(self, node):
        objtype = node.get('objtype', 'object')
        sig = node.get('sig', '')
        style = self.console.get_style("restructuredtext.py_desc", default="bold blue")
        body = self._render_admonition_body(node.children)
        self.renderables.append(
            Panel(Group(*body) if body else "", title=f"[{objtype}] {sig}",
                  style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_py_desc(self, node):
        pass

    def visit_toctree_stub(self, node):
        style = self.console.get_style("restructuredtext.toctree", default="bold cyan")
        caption = node.get('caption', 'Contents')
        entries = node.get('entries', [])
        marker_style = self.console.get_style("restructuredtext.bullet_list_marker", default="bold yellow")
        renderables = [Text(" • " + e, style=marker_style) for e in entries if e]
        self.renderables.append(
            Panel(Group(*renderables) if renderables else "", title=caption,
                  style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_toctree_stub(self, node):
        pass

    def visit_literalinclude_stub(self, node):
        style = self.console.get_style("restructuredtext.literalinclude", default="grey58")
        filename = node.get('filename', '<unknown file>')
        self.renderables.append(
            Panel(Text(filename), title="literalinclude", border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_literalinclude_stub(self, node):
        pass

    def visit_glossary_block(self, node):
        style = self.console.get_style("restructuredtext.glossary", default="bold")
        body = self._render_admonition_body(node.children)
        self.renderables.append(
            Panel(Group(*body) if body else "", title="Glossary", style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_glossary_block(self, node):
        pass

    def visit_subscript(self, node):
        style = self.console.get_style("restructuredtext.subscript", default="none")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().translate(self.subscript), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().translate(self.subscript), end="", style=style))
        raise docutils.nodes.SkipChildren()

    def visit_superscript(self, node):
        style = self.console.get_style("restructuredtext.superscript", default="none")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().translate(self.superscript), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().translate(self.superscript), end="", style=style))
        raise docutils.nodes.SkipChildren()

    def visit_emphasis(self, node):
        style = self.console.get_style("restructuredtext.emphasis", default="italic")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_strong(self, node):
        style = self.console.get_style("restructuredtext.strong", default="bold")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def _make_image_text(self, node, link_override=None):
        alt, target = None, None
        if ":target:" in node.rawsource:
            target = node.rawsource.split(":target:")[-1].strip()
        if ":alt:" in node.rawsource:
            alt = node.rawsource.split(":alt:")[-1].strip()
        link = link_override or node.get("target", target or "Image") or node.get("uri")
        return Text("🌆 ") + Text(
            node.get("alt", alt or "Image"),
            style=Style(link=link, color="#6088ff"),
        )


    def _render_inline_with_explanation(self, node, style_name):
        style = self.console.get_style(style_name, default="underline")
        explanation = node.get("explanation", "")
        text = node.astext().replace("\n", " ")
        if explanation:
            text = f"{text} ({explanation})"
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(text, style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(text, style=style, end=""))
        raise docutils.nodes.SkipChildren()


    def visit_abbreviation(self, node):
        self._render_inline_with_explanation(node, "restructuredtext.abbreviation")


    def visit_acronym(self, node):
        self._render_inline_with_explanation(node, "restructuredtext.acronym")


    def visit_image(self, node):
        self.renderables.append(self._make_image_text(node))
        raise docutils.nodes.SkipChildren()

    def visit_figure(self, node):
        # When :target: is given, docutils wraps the image in a reference node
        ref_node = next((c for c in node.children if isinstance(c, docutils.nodes.reference)), None)
        image_node = next((c for c in node.children if isinstance(c, docutils.nodes.image)), None)
        if image_node is None and ref_node is not None:
            image_node = next((c for c in ref_node.children if isinstance(c, docutils.nodes.image)), None)
        caption_node = next((c for c in node.children if isinstance(c, docutils.nodes.caption)), None)
        legend_node = next((c for c in node.children if isinstance(c, docutils.nodes.legend)), None)

        if image_node is not None:
            link_override = ref_node.get("refuri") if ref_node is not None else None
            image_text = self._make_image_text(image_node, link_override=link_override)
        else:
            image_text = Text("🌆 Image")
        caption = caption_node.astext() if caption_node is not None else None
        subtitle = legend_node.astext().replace("\n", " ") if legend_node is not None else None

        border_style = self.console.get_style("restructuredtext.figure_border", default="blue")
        self.renderables.append(Panel(image_text, title=caption, subtitle=subtitle, border_style=border_style, expand=False))
        raise docutils.nodes.SkipChildren()

    _BULLET_LIST_MARKERS = [" • ", " ∘ ", " ▪ "]

    def _render_bullet_list(self, node, level=0):
        """Recursively render a bullet list with support for unlimited nesting and any child elements."""
        marker_style = self.console.get_style("restructuredtext.bullet_list_marker", default="bold yellow")
        text_style = self.console.get_style("restructuredtext.bullet_list_text", default="none")
        indent = "  " * level
        marker = self._BULLET_LIST_MARKERS[min(level, len(self._BULLET_LIST_MARKERS) - 1)]
        for list_item in node.children:
            first_content = True
            for child in list_item.children:
                if isinstance(child, docutils.nodes.bullet_list):
                    self._render_bullet_list(child, level + 1)
                elif isinstance(child, docutils.nodes.enumerated_list):
                    self._render_enumerated_list(child, level + 1)
                elif isinstance(child, docutils.nodes.literal_block):
                    if first_content:
                        self.renderables.append(Text(indent + marker, end="", style=marker_style))
                        first_content = False
                    try:
                        self.visit_literal_block(child)
                    except docutils.nodes.SkipChildren:
                        pass
                else:
                    # Use sub-visitor to preserve inline markup (bold, italic, links, etc.)
                    child_renderables = self._render_child_inline(child)
                    if first_content:
                        self.renderables.append(Text(indent + marker, end="", style=marker_style))
                        self.renderables.extend(child_renderables)
                        first_content = False
                    else:
                        # Prepend continuation indent to first renderable if it's text
                        if child_renderables:
                            if isinstance(child_renderables[0], Text):
                                child_renderables[0].stylize(text_style)
                            self.renderables.extend(child_renderables)

    def visit_bullet_list(self, node):
        self._render_bullet_list(node, level=0)
        self.renderables.append(NewLine())
        raise docutils.nodes.SkipChildren()

    @staticmethod
    def _make_enum_marker(enumtype, i):
        """Convert an integer *i* to the appropriate enumeration label."""
        from rich_rst._vendor.docutils.utils._roman_numerals import RomanNumeral
        if enumtype == "loweralpha":
            return chr(ord("a") + i - 1)
        elif enumtype == "upperalpha":
            return chr(ord("A") + i - 1)
        elif enumtype == "lowerroman":
            return str(RomanNumeral(i)).lower()
        elif enumtype == "upperroman":
            return str(RomanNumeral(i))
        else:  # arabic (default)
            return str(i)

    def _render_enumerated_list(self, node, level=0):
        """Recursively render an enumerated list with support for unlimited nesting and any child elements."""
        marker_style = self.console.get_style("restructuredtext.enumerated_list_marker", default="bold yellow")
        text_style = self.console.get_style("restructuredtext.enumerated_text", default="none")
        indent = "  " * level
        enumtype = node.get("enumtype", "arabic")
        prefix = node.get("prefix", "")
        suffix = node.get("suffix", ".")
        start = node.get("start", 1)
        for idx, list_item in enumerate(node.children):
            i = start + idx
            marker = f"{indent} {prefix}{self._make_enum_marker(enumtype, i)}{suffix}"
            first_content = True
            for child in list_item.children:
                if isinstance(child, docutils.nodes.bullet_list):
                    self._render_bullet_list(child, level + 1)
                elif isinstance(child, docutils.nodes.enumerated_list):
                    self._render_enumerated_list(child, level + 1)
                elif isinstance(child, docutils.nodes.literal_block):
                    if first_content:
                        self.renderables.append(Text(marker, end=" ", style=marker_style))
                        first_content = False
                    try:
                        self.visit_literal_block(child)
                    except docutils.nodes.SkipChildren:
                        pass
                else:
                    # Use sub-visitor to preserve inline markup (bold, italic, links, etc.)
                    child_renderables = self._render_child_inline(child)
                    if first_content:
                        self.renderables.append(Text(marker, end=" ", style=marker_style))
                        self.renderables.extend(child_renderables)
                        first_content = False
                    else:
                        # Prepend continuation indent to first renderable if it's text
                        if child_renderables:
                            if isinstance(child_renderables[0], Text):
                                child_renderables[0].stylize(text_style)
                            self.renderables.extend(child_renderables)

    def visit_enumerated_list(self, node):
        self._render_enumerated_list(node, level=0)
        self.renderables.append(NewLine())
        raise docutils.nodes.SkipChildren()

    def visit_literal(self, node):
        style = self.console.get_style("restructuredtext.inline_codeblock", default="grey78 on grey7")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_title_reference(self, node):
        style = self.console.get_style("restructuredtext.title_reference", default="italic")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_literal_block(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].rstrip()
            self.renderables[-1].append_text(Text("\n"))
        lexer, lexer_source = self._find_lexer(node)
        title = lexer if lexer_source == "explicit" else f"{lexer} ({lexer_source})"
        self.renderables.append(
            Panel(
                Syntax(node.astext(), lexer, theme=self.code_theme, line_numbers=self.show_line_numbers),
                border_style=style,
                box=box.SQUARE,
                title=title,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_system_message(self, node):
        self.errors.append(
            Panel(
                Text(node.astext()),
                title=f"System Message: {node.attributes.get('type', '?')}/{node.attributes.get('level', '?')} ({node.attributes.get('source', '?')}, line {node.attributes.get('line', '?')});",
                border_style={None: "none", "INFO": "bold cyan", "WARNING": "bold yellow", "ERROR": "bold red", "SEVERE": "bold magenta", "DEBUG": "bold white"}.get(
                    node.attributes.get("type"), "bold red"
                )
            ),
        )

        # Preserve the offending source snippet in normal output so invalid
        # markup does not silently disappear when show_errors=False.
        for child in node.children:
            if isinstance(child, docutils.nodes.literal_block):
                snippet = child.astext().replace("\n", " ")
                if snippet:
                    if self.renderables and isinstance(self.renderables[-1], Text):
                        self.renderables[-1].append_text(Text(snippet, end=" "))
                    else:
                        self.renderables.append(Text(snippet, end=""))
        raise docutils.nodes.SkipChildren()

    def _add_to_field_table(self, field_name, field_value):
        """Add a row to the shared field table, creating it if necessary."""
        field_name_style = self.console.get_style("restructuredtext.field_name", default="bold")
        field_value_style = self.console.get_style("restructuredtext.field_value", default="none")
        if self.renderables and isinstance(self.renderables[-1], Table):
            possible_table = self.renderables[-1]
            if (possible_table.columns[0].header == "Field Name") and (possible_table.columns[1].header == "Field Value"):
                possible_table.add_row(Text(field_name, style=field_name_style), Text(field_value, style=field_value_style))
                return
        table = Table("Field Name", "Field Value", show_lines=True)
        table.add_row(Text(field_name, style=field_name_style), Text(field_value, style=field_value_style))
        self.renderables.append(table)

    def visit_field(self, node):
        self._add_to_field_table(node.children[0].astext(), node.children[1].astext())
        raise docutils.nodes.SkipChildren()

    def visit_docinfo(self, node):
        pass  # let the visitor descend into child docinfo nodes

    def visit_author(self, node):
        self._add_to_field_table("Author", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_authors(self, node):
        for author in node.children:
            self._add_to_field_table("Author", author.astext())
        raise docutils.nodes.SkipChildren()

    def visit_organization(self, node):
        self._add_to_field_table("Organization", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_address(self, node):
        self._add_to_field_table("Address", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_contact(self, node):
        self._add_to_field_table("Contact", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_version(self, node):
        self._add_to_field_table("Version", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_revision(self, node):
        self._add_to_field_table("Revision", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_status(self, node):
        self._add_to_field_table("Status", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_date(self, node):
        self._add_to_field_table("Date", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_copyright(self, node):
        self._add_to_field_table("Copyright", node.astext())
        raise docutils.nodes.SkipChildren()

    def visit_definition_list(self, node):
        term_style = self.console.get_style("restructuredtext.term_style", default="none")
        classifier_style = self.console.get_style("restructuredtext.classifier_style", default="cyan")
        definitions_style = self.console.get_style("restructuredtext.definitions_style", default="none")
        for child in node.children:
            child_children = child.children
            if not child_children:
                continue

            if len(child_children) == 3:
                term, classifier, definitions = child_children[:3]
                self.renderables.append(
                    Text("    ")
                    + Text(term.astext(), style=term_style, end="")
                    + Text(" : ", end="")
                    + Text(classifier.astext(), style=classifier_style)
                    + Text("\n      ", end="")
                    + Text(definitions.astext().replace("\n", " "), style=definitions_style)
                    + Text("\n", end="")
                )
            elif len(child_children) >= 2:
                term, classifier = child_children[0], child_children[1]
                if len(child_children) > 2:
                    for children in child_children[2:]:
                        if isinstance(children, docutils.nodes.bullet_list):
                            self.visit_bullet_list(children)
                        elif isinstance(children, docutils.nodes.literal_block):
                            self.visit_literal_block(children)
                        elif isinstance(children, docutils.nodes.literal):
                            self.visit_literal(children)
                        elif isinstance(children, docutils.nodes.block_quote):
                            self.visit_block_quote(children)
                else:
                    self.renderables.append(
                        Text(term.astext(), style=term_style)
                        + Text("\n    ", end="")
                        + Text(classifier.astext().replace("\n", " "), style=definitions_style)
                        + Text("\n      ", end="")
                    )
            else:
                term = child_children[0]
                self.renderables.append(Text(term.astext(), style=term_style) + Text("\n", end=""))
        raise docutils.nodes.SkipChildren()

    def visit_option_list(self, node):
        option_string_style = self.console.get_style("restructuredtext.option_string", default="none")
        option_argument_style = self.console.get_style("restructuredtext.option_argument", default="none")
        option_child_text_separator_style = self.console.get_style(
            "restructuredtext.option_child_text_separator", default="none"
        )
        option_description_style = self.console.get_style("restructuredtext.option_description", default="none")
        for option_list_item in node.children:
            option_group, description = option_list_item.children
            # option_group.child_text_separator.join(map(lambda x: x.astext(), option_group.children)))
            option_text = Text(end="")
            for option in option_group.children:
                try:
                    option_string, option_argument = option.children
                except ValueError:
                    option_string, option_argument = option.children[0], None
                option_text += (
                    Text(option_string.astext(), style=option_string_style)
                    + (Text(option_argument.astext(), style=option_argument_style) if option_argument else Text())
                    + (
                        Text(option_group.child_text_separator, style=option_child_text_separator_style)
                        if len(option_group.children) > 1
                        else Text()
                    )
                )
            if description:
                option_text += Text("\n    ")
                option_text += Text(description.astext(), style=option_description_style)
            self.renderables.append(option_text + Text("\n"))
        raise docutils.nodes.SkipChildren()

    def visit_doctest_block(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        self.renderables.append(
            Panel(
                Syntax(node.astext(), "pycon", theme=self.code_theme, line_numbers=self.show_line_numbers),
                border_style=style,
                box=box.SQUARE,
                title="doctest block",
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_block_quote(self, node):
        text_style = self.console.get_style("restructuredtext.blockquote_text", default="white")
        marker_style = self.console.get_style(
            "restructuredtext.blockquote_attribution_marker", default="bright_magenta"
        )
        author_style = self.console.get_style("restructuredtext.blockquote_attribution_text", default="grey89")
        children = list(node.children)
        attribution = children[-1] if children and isinstance(children[-1], docutils.nodes.attribution) else None
        paragraphs = children[:-1] if attribution else children

        for index, paragraph in enumerate(paragraphs):
            paragraph_text = paragraph.astext().replace("\n", " ")
            if index:
                self.renderables.append(NewLine())
                self.renderables.append(NewLine())
            self.renderables.append(Text("▌ ", style=marker_style) + Text(paragraph_text, style=text_style))

        if attribution:
            self.renderables.append(NewLine())
            self.renderables.append(Text("  - " + attribution.astext(), style=author_style))
        else:
            self.renderables.append(NewLine())

        raise docutils.nodes.SkipChildren()

    def _render_line_block(self, node, indent=0):
        """Recursively render a line_block node, preserving nested indentation."""
        prefix = "    " * indent
        for child in node.children:
            if isinstance(child, docutils.nodes.line_block):
                self._render_line_block(child, indent + 1)
            elif isinstance(child, docutils.nodes.line):
                self.renderables.append(Text(prefix + child.astext()))

    def visit_line_block(self, node):
        self._render_line_block(node)
        raise docutils.nodes.SkipChildren()

    def _collect_body_renderables(self, children):
        """Render a list of body nodes into renderables, returning the collected list.

        Handles bullet_list, enumerated_list, and paragraph nodes explicitly;
        other node types fall back to plain text via ``astext()``.
        """
        saved = self.renderables
        self.renderables = []
        for child in children:
            if isinstance(child, docutils.nodes.bullet_list):
                self._render_bullet_list(child, level=0)
            elif isinstance(child, docutils.nodes.enumerated_list):
                self._render_enumerated_list(child, level=0)
            elif isinstance(child, docutils.nodes.paragraph):
                self.renderables.append(Text(child.astext().replace("\n", " ")))
            else:
                text = child.astext().replace("\n", " ")
                if text:
                    self.renderables.append(Text(text))
        body = self.renderables
        self.renderables = saved
        return body

    def visit_topic(self, node):
        style = self.console.get_style("restructuredtext.topic", default="bold cyan")
        children = list(node.children)
        title = ""
        body_start = 0
        if children and isinstance(children[0], docutils.nodes.title):
            title = children[0].astext()
            body_start = 1

        body_renderables = self._collect_body_renderables(children[body_start:])

        if body_renderables:
            self.renderables.append(
                Panel(Group(*body_renderables), title=title, style=style, border_style=style)
            )
        else:
            self.renderables.append(Panel("", title=title, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_sidebar(self, node):
        children = list(node.children)
        title = children[0] if children else ""
        subtitle = ""
        body_children = children[1:]

        if body_children and isinstance(body_children[0], docutils.nodes.subtitle):
            subtitle = body_children[0].astext()
            body_children = body_children[1:]

        paragraph = "\n\n".join(child.astext() for child in body_children)

        self.renderables.append(Panel(paragraph, title=title.astext(), subtitle=subtitle, expand=False))

        raise docutils.nodes.SkipChildren()

    def visit_transition(self, node):
        style = self.console.get_style("restructuredtext.hr", default="yellow")
        self.renderables.append(Rule(style=style))

    def visit_math_block(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].rstrip()
            self.renderables[-1].append_text(Text("\n"))
        self.renderables.append(
            Panel(
                Text(node.astext()),
                border_style=style,
                box=box.SQUARE,
                title="math",
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_citation(self, node):
        border_style = self.console.get_style("restructuredtext.citation_border", default="grey74")
        self.renderables.append(Panel(node.astext(), title="citation", border_style=border_style))
        raise docutils.nodes.SkipChildren()

    def visit_citation_reference(self, node):
        style = self.console.get_style("restructuredtext.citation_reference", default="grey74")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(node.astext().replace("\n", " "), style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_header(self, node):
        style = self.console.get_style("restructuredtext.caption", default="bold")
        self.renderables.insert(0, Panel(Align(node.astext(), "center"), title="caption", box=box.DOUBLE, style=style))
        raise docutils.nodes.SkipChildren()

    def visit_footer(self, node):
        self.footer.append(Align(node.astext(), "center"))
        raise docutils.nodes.SkipChildren()

    def visit_footnote_reference(self, node):
        style = self.console.get_style("restructuredtext.footnote_reference", default="grey74")
        newline = '\n'
        text = f"[{node.astext().replace(newline, ' ')}]"
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(text, style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(text, style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_substitution_reference(self, node):
        style = self.console.get_style("restructuredtext.substitution_reference", default="none")
        text = node.astext().replace("\n", " ")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(text, style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(text, style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_footnote(self, node):
        self.footer.append(Align(node.astext(), "left"))
        raise docutils.nodes.SkipChildren()

    def visit_generated(self, node):
        self.footer.append(Align(node.astext(), "left"))
        raise docutils.nodes.SkipChildren()

    def visit_pending(self, node):
        raise docutils.nodes.SkipChildren()

    def visit_problematic(self, node):
        # Keep problematic inline source visible in the main render output.
        problematic_style = self.console.get_style("restructuredtext.problematic", default="none")
        problematic_text = node.astext().replace("\n", " ")
        if problematic_text:
            if self.renderables and isinstance(self.renderables[-1], Text):
                self.renderables[-1].append(problematic_text, style=problematic_style)
            else:
                self.renderables.append(Text(problematic_text, style=problematic_style, end=""))

        self.errors.append(
            Panel(
                Syntax(node.astext(), lexer="rst", theme=self.code_theme),
                title=f"System Message: Problematic Element",
                border_style="bold red",
            ),
        )
        raise docutils.nodes.SkipChildren()

    def visit_raw(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        lexer, _ = self._find_lexer(node)
        text = node.astext()
        title = ("stripped raw html" if lexer == "html" else "raw " + lexer)

        if lexer == "html":
            text = strip_tags(text)
            lexer = self._guess_lexer_name(text) if self.guess_lexer else self.default_lexer

        self.renderables.append(
            Panel(
                Syntax(text, lexer, theme=self.code_theme, line_numbers=self.show_line_numbers),
                border_style=style,
                box=box.SQUARE,
                title=title,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_table(self, node):
        header_style = self.console.get_style("restructuredtext.table_header", default="bold")
        cell_style = self.console.get_style("restructuredtext.table_cell", default="none")

        # Extract optional caption/title and the tgroup
        title = None
        tgroup = None
        for child in node.children:
            if isinstance(child, (docutils.nodes.title, docutils.nodes.caption)):
                title = child.astext()
            elif isinstance(child, docutils.nodes.tgroup):
                tgroup = child

        if tgroup is None:
            raise docutils.nodes.SkipChildren()

        # Count total columns from colspec elements (authoritative column count)
        num_cols = sum(1 for c in tgroup.children if isinstance(c, docutils.nodes.colspec))

        # Find thead and tbody within tgroup
        thead = None
        tbody = None
        for child in tgroup.children:
            if isinstance(child, docutils.nodes.thead):
                thead = child
            elif isinstance(child, docutils.nodes.tbody):
                tbody = child

        if tbody is None:
            raise docutils.nodes.SkipChildren()

        # Fallback column count when colspec elements are absent
        if num_cols == 0:
            if thead is not None and thead.children:
                num_cols = sum(1 + e.get("morecols", 0) for e in thead.children[0].children)
            elif tbody.children:
                num_cols = sum(1 + e.get("morecols", 0) for e in tbody.children[0].children)

        def _render_entry_content(entry):
            """Render an entry node with a sub-visitor to preserve inline RST markup."""
            sub_visitor = RSTVisitor(
                self.document,
                console=self.console,
                code_theme=self.code_theme,
                show_line_numbers=self.show_line_numbers,
                guess_lexer=self.guess_lexer,
                default_lexer=self.default_lexer,
            )
            for child in entry.children:
                child.walkabout(sub_visitor)
            renderables = sub_visitor.renderables
            if not renderables:
                return Text("", style=cell_style)
            # depart_paragraph appends "\n\n" to trailing Text renderables; strip
            # it so cells don't carry extra vertical whitespace.  Other renderable
            # types (Panel, Table, …) manage their own spacing.
            for r in renderables:
                if isinstance(r, Text):
                    r.rstrip()
            if len(renderables) == 1:
                return renderables[0]
            return Group(*renderables)

        def _build_row_cells(row, occupied_cols):
            """Build cell renderables for one body row.

            Accounts for columns already occupied by rowspans from earlier rows
            and for cells that span multiple columns (morecols).  Returns a tuple
            of (cells, new_rowspans) where new_rowspans maps col_idx to the
            morerows value for any spanning cells introduced by this row.
            """
            cells = []
            new_rowspans = {}
            col_idx = 0
            entry_iter = iter(row.children)

            while col_idx < num_cols:
                if col_idx in occupied_cols:
                    # Column is covered by a rowspan from a previous row
                    cells.append(Text("", style=cell_style))
                    col_idx += 1
                    continue

                entry = next(entry_iter, None)
                if entry is None:
                    # All entries for this row have been consumed; pad remaining
                    # columns with empty cells (can happen with complex spanning).
                    cells.append(Text("", style=cell_style))
                    col_idx += 1
                    continue

                morecols = entry.get("morecols", 0)
                morerows = entry.get("morerows", 0)

                cells.append(_render_entry_content(entry))

                # Record any new rowspan introduced by this cell
                if morerows > 0:
                    for span_col in range(col_idx, col_idx + 1 + morecols):
                        new_rowspans[span_col] = morerows

                # Pad empty cells for additional spanned columns (colspan)
                for _ in range(morecols):
                    cells.append(Text("", style=cell_style))

                col_idx += 1 + morecols

            return cells, new_rowspans

        # Build the rich Table
        has_header = thead is not None and bool(thead.children)
        rich_table = Table(
            show_header=has_header,
            title=title,
            header_style=header_style,
            show_lines=True,
        )

        # Add columns, using header-row entries as column labels when thead exists.
        # Cells with morecols > 0 produce morecols extra unnamed columns so that
        # the total column count matches the table definition.
        if thead is not None and thead.children:
            header_row = thead.children[0]
            col_idx = 0
            for entry in header_row.children:
                morecols = entry.get("morecols", 0)
                rich_table.add_column(entry.astext().replace("\n", " "), style=cell_style)
                for _ in range(morecols):
                    rich_table.add_column("", style=cell_style)
                col_idx += 1 + morecols
            # Ensure column count matches colspec (guards against malformed tables)
            while col_idx < num_cols:
                rich_table.add_column("", style=cell_style)
                col_idx += 1
        else:
            for _ in range(num_cols):
                rich_table.add_column("", style=cell_style)

        # rowspan_remaining tracks how many more body rows each column is still
        # spanned over: {col_idx: remaining_row_count}.
        rowspan_remaining = {}

        # Add body rows, correctly handling rowspan and colspan
        for row in tbody.children:
            occupied = {col for col, rem in rowspan_remaining.items() if rem > 0}
            cells, new_rowspans = _build_row_cells(row, occupied)

            # Decrement counters for columns that were occupied this row
            for col in list(occupied):
                rowspan_remaining[col] -= 1
                if rowspan_remaining[col] <= 0:
                    del rowspan_remaining[col]

            # Register new rowspans introduced by cells in this row
            rowspan_remaining.update(new_rowspans)

            rich_table.add_row(*cells)

        self.renderables.append(rich_table)
        raise docutils.nodes.SkipChildren()


class RestructuredText(JupyterMixin):
    """A reStructuredText renderable for rich.

    Parameters
    ----------
    markup : str
        A string containing reStructuredText markup.
    code_theme : Optional[Union[str, SyntaxTheme]]
        Pygments theme for code blocks. Defaults to "monokai".
    show_line_numbers : Optional[bool]
        Whether to display line numbers for syntax-highlighted code blocks.
    show_errors : Optional[bool]
        Whether to show system_messages aka errors and warnings.
    guess_lexer : Optional[bool]
        Whether to guess lexers for code blocks without specified language.
    default_lexer : Optional[str]
        Which lexer to use if no lexer is guessed or found. Defaults to "python"
    sphinx_compat : Optional[bool]
        Enable compatibility with Sphinx roles (func, meth, class, etc.) commonly used in
        Python docstrings. When enabled, these roles render as inline code instead of errors.
        Defaults to True for better compatibility with Python documentation.
    filename : Optional[str]
        A file name to use for error messages, useful for debugging purposes. Defaults to "<rst-document>"
    """

    def __init__(
        self,
        markup: str,
        code_theme: Optional[Union[str, SyntaxTheme]] = "monokai",
        show_line_numbers: Optional[bool] = False,
        show_errors: Optional[bool] = False,
        guess_lexer: Optional[bool] = False,
        default_lexer: Optional[str] = "python",
        sphinx_compat: Optional[bool] = True,
        filename: Optional[str] = "<rst-document>"
    ) -> None:
        self.markup = markup
        self.code_theme = code_theme
        self.show_line_numbers = show_line_numbers
        self.log_errors = show_errors
        self.guess_lexer = guess_lexer
        self.default_lexer = default_lexer
        self.sphinx_compat = sphinx_compat
        self.filename = filename

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        if self.sphinx_compat:
            _register_sphinx_roles()
            _register_sphinx_directives()

        # Use the full docutils publish pipeline so that all standard transforms
        # (substitution resolution, hyperlink resolution, footnote numbering,
        # bibliographic-field promotion, …) are applied before we walk the tree.
        document = docutils.core.publish_doctree(
            self.markup,
            source_path=self.filename,
            settings_overrides={"report_level": 69, "halt_level": 69},
        )

        # Render the RST `document` using Rich.
        visitor = RSTVisitor(
            document,
            console=console,
            code_theme=self.code_theme,
            show_line_numbers=self.show_line_numbers,
            guess_lexer=self.guess_lexer,
            default_lexer=self.default_lexer,
        )
        document.walkabout(visitor)

        # Strip all trailing newlines and newline-like rich objects
        while visitor.renderables:
            if isinstance(visitor.renderables[-1], Text):
                visitor.renderables[-1].rstrip()
                visitor.renderables[-1].end = "\n"
                if visitor.renderables[-1]:  # The Text object still contains data.
                    break
                else:
                    visitor.renderables.pop()
            elif isinstance(visitor.renderables[-1], NewLine):
                visitor.renderables.pop()
            else:
                break

        for renderable in visitor.renderables:
            yield from console.render(renderable, options)
        if self.log_errors and visitor.errors:
            for error in visitor.errors:
                yield from console.render(error, options)
        style = console.get_style("restructuredtext.footer", default="none")
        border_style = console.get_style("restructuredtext.footer_border", default="grey74")
        if visitor.footer:
            yield from console.render(
                Panel(Group(*visitor.footer), title="Footer", box=box.SQUARE, border_style=border_style, style=style)
            )


RST = reST = ReStructuredText = reStructuredText = RestructuredText
