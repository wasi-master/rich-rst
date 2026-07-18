"""Sphinx role registration so Sphinx-specific markup renders gracefully."""
import re
from typing import Any, Dict, List, Optional, Tuple

# Imports from the rich package for the printing
# Imports from rich_rst._vendor.docutils package for the parsing
from rich_rst._directives import _sphinx_registration_lock

_sphinx_roles_registered = False


def _register_sphinx_roles() -> None:
    """Register common Sphinx roles to gracefully handle Sphinx-specific markup.

    Sphinx roles like :func:, :class:, :meth: are very common in Python
    docstrings but are not available in standard docutils.  This function
    registers them to render as inline code/literal text instead of errors.

    Thread safety: protected by ``_sphinx_registration_lock``, identical to
    :func:`_register_sphinx_directives`.  Per-process state only — each
    worker in a multi-process build registers independently, which is correct.
    """
    global _sphinx_roles_registered

    with _sphinx_registration_lock:
        if _sphinx_roles_registered:
            return

        import rich_rst._vendor.docutils.parsers.rst.roles  # noqa: F401
        from rich_rst._vendor import docutils

        def sphinx_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            """Generic Sphinx role handler that renders as inline literal text."""
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
            'c:func', 'c:function', 'c:type', 'c:struct', 'c:union', 'c:enum', 'c:enumerator',
            'c:member', 'c:var', 'c:macro', 'c:expr', 'c:texpr',
            # C++ domain
            'cpp:func', 'cpp:function', 'cpp:class', 'cpp:type', 'cpp:member', 'cpp:var',
            'cpp:enum', 'cpp:enumerator', 'cpp:concept', 'cpp:expr', 'cpp:texpr', 'cpp:alias',
            # JavaScript domain
            'js:mod', 'js:module', 'js:func', 'js:function', 'js:data',
            'js:attr', 'js:attribute', 'js:class', 'js:meth', 'js:method',
        ]

        for role in sphinx_roles:
            docutils.parsers.rst.roles.register_canonical_role(role, sphinx_role)
            # Also register in language module to avoid INFO messages
            if hasattr(docutils.parsers.rst.languages.en, 'roles'):
                docutils.parsers.rst.languages.en.roles[role] = role

        # `:command:` and `:program:` → bold literal
        def _bold_literal_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            display_text = text
            if '<' in text and text.endswith('>'):
                bracket_pos = text.rfind('<')
                potential_display = text[:bracket_pos].strip()
                if potential_display:
                    display_text = potential_display
            node = docutils.nodes.strong(rawtext, display_text)
            return [node], []

        for role_name in ('command', 'program'):
            docutils.parsers.rst.roles.register_canonical_role(role_name, _bold_literal_role)
            if hasattr(docutils.parsers.rst.languages.en, 'roles'):
                docutils.parsers.rst.languages.en.roles[role_name] = role_name

        # `:dfn:` → emphasis (italic)
        def _dfn_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            node = docutils.nodes.emphasis(rawtext, text)
            return [node], []

        docutils.parsers.rst.roles.register_canonical_role('dfn', _dfn_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['dfn'] = 'dfn'

        # `:abbr:` → abbreviation node with explanation
        abbr_re = re.compile(r'\((.*)\)$', re.DOTALL)

        def _abbr_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            matched = abbr_re.search(text)
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
        def _menuselection_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            text = text.replace('-->', '\u25b6')
            node = docutils.nodes.literal(rawtext, text)
            return [node], []

        docutils.parsers.rst.roles.register_canonical_role('menuselection', _menuselection_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['menuselection'] = 'menuselection'

        # `:samp:` and `:file:` → literal with {} stripped
        braces_re = re.compile(r'\{([^}]*)\}')

        def _samp_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            clean = braces_re.sub(r'\1', text)
            node = docutils.nodes.literal(rawtext, clean)
            return [node], []

        for role_name in ('samp', 'file'):
            docutils.parsers.rst.roles.register_canonical_role(role_name, _samp_role)
            if hasattr(docutils.parsers.rst.languages.en, 'roles'):
                docutils.parsers.rst.languages.en.roles[role_name] = role_name

        # `:pep:` → clickable PEP link
        def _pep_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            parts = text.split('#', 1)
            pep_num_str = parts[0].strip()
            anchor = ('#' + parts[1]) if len(parts) > 1 else ''
            try:
                pep_num = int(pep_num_str)
                url = f"https://peps.python.org/pep-{pep_num:04d}/{anchor}"
            except ValueError:
                url = "https://peps.python.org/"
            display = f"PEP {pep_num_str}"
            ref = docutils.nodes.reference(rawtext, display, refuri=url)
            return [ref], []

        docutils.parsers.rst.roles.register_canonical_role('pep', _pep_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['pep'] = 'pep'

        # `:rfc:` → clickable RFC link
        def _rfc_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any, options: Optional[Dict[str, Any]] = None, content: Optional[List[str]] = None) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            parts = text.split('#', 1)
            rfc_num_str = parts[0].strip()
            anchor = ('#' + parts[1]) if len(parts) > 1 else ''
            try:
                rfc_num = int(rfc_num_str)
                url = f"https://datatracker.ietf.org/doc/html/rfc{rfc_num}{anchor}"
            except ValueError:
                url = "https://datatracker.ietf.org/"
            display = f"RFC {rfc_num_str}"
            ref = docutils.nodes.reference(rawtext, display, refuri=url)
            return [ref], []

        docutils.parsers.rst.roles.register_canonical_role('rfc', _rfc_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['rfc'] = 'rfc'

        # `:cve:` → clickable CVE link
        def _cve_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any,
                    options: Optional[Dict[str, Any]] = None,
                    content: Optional[List[str]] = None
                    ) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            cve_id = text.strip().lstrip("CVE-")
            url = f"https://www.cve.org/CVERecord?id=CVE-{cve_id}"
            display = f"CVE-{cve_id}"
            ref = docutils.nodes.reference(rawtext, display, refuri=url)
            return [ref], []

        docutils.parsers.rst.roles.register_canonical_role('cve', _cve_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['cve'] = 'cve'

        # `:cwe:` → clickable CWE link
        def _cwe_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any,
                    options: Optional[Dict[str, Any]] = None,
                    content: Optional[List[str]] = None
                    ) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            cwe_num = text.strip()
            url = f"https://cwe.mitre.org/data/definitions/{cwe_num}.html"
            display = f"CWE-{cwe_num}"
            ref = docutils.nodes.reference(rawtext, display, refuri=url)
            return [ref], []

        docutils.parsers.rst.roles.register_canonical_role('cwe', _cwe_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['cwe'] = 'cwe'

        # `:pypi:` → clickable PyPI project link
        def _pypi_role(name: str, rawtext: str, text: str, lineno: int, inliner: Any,
                    options: Optional[Dict[str, Any]] = None,
                    content: Optional[List[str]] = None
                    ) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.system_message]]:
            project_name = text.strip()
            url = f"https://pypi.org/project/{project_name}/"
            display = project_name
            ref = docutils.nodes.reference(rawtext, display, refuri=url)
            return [ref], []

        docutils.parsers.rst.roles.register_canonical_role('pypi', _pypi_role)
        if hasattr(docutils.parsers.rst.languages.en, 'roles'):
            docutils.parsers.rst.languages.en.roles['pypi'] = 'pypi'

        _sphinx_roles_registered = True

