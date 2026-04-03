# Vendored Dependencies

This package vendors a subset of [Docutils](https://docutils.sourceforge.io/) rather than
declaring it as an install-time dependency. This document explains what was vendored, why,
and what the licensing implications are.

## Why vendoring?

Docutils is the only Python library capable of parsing reStructuredText into a document
tree that rich-rst can walk. It is mature, stable, and has no Python dependencies of its
own. However, because the Docutils distribution ships one Emacs Lisp file
(`tools/editors/emacs/rst.el`) under the GNU General Public License v3+, automated
license scanners flag the entire package as "GPL" — even though that file is never
installed by `pip` and has no relationship to the Python code. This created compliance
friction for enterprise users of libraries that depend on rich-rst (notably FastMCP via
cyclopts).

Vendoring the specific Python modules that rich-rst actually uses eliminates the
dependency entirely, removes any ambiguity for scanners, and keeps rich-rst a
zero-dependency package (aside from `rich` itself).

## What was vendored

**Source:** Docutils 0.22.4  
**Upstream URL:** https://docutils.sourceforge.io/  
**PyPI:** https://pypi.org/project/docutils/0.22.4/  
**Vendored into:** `rich_rst/_vendor/docutils/`

The following 41 Python modules were copied verbatim (aside from rewriting internal
`from docutils` / `import docutils` references to point at the vendored path
`rich_rst._vendor.docutils`):

| Module | License |
|---|---|
| `docutils/__init__.py` | Public Domain |
| `docutils/core.py` | Public Domain |
| `docutils/frontend.py` | Public Domain |
| `docutils/io.py` | Public Domain |
| `docutils/nodes.py` | Public Domain |
| `docutils/statemachine.py` | Public Domain |
| `docutils/languages/__init__.py` | Public Domain |
| `docutils/languages/en.py` | Public Domain |
| `docutils/parsers/__init__.py` | Public Domain |
| `docutils/parsers/rst/__init__.py` | Public Domain |
| `docutils/parsers/rst/roles.py` | Public Domain |
| `docutils/parsers/rst/states.py` | Public Domain |
| `docutils/parsers/rst/tableparser.py` | Public Domain |
| `docutils/parsers/rst/directives/__init__.py` | Public Domain |
| `docutils/parsers/rst/directives/admonitions.py` | Public Domain |
| `docutils/parsers/rst/directives/body.py` | Public Domain |
| `docutils/parsers/rst/directives/html.py` | Public Domain |
| `docutils/parsers/rst/directives/images.py` | Public Domain |
| `docutils/parsers/rst/directives/misc.py` | Public Domain |
| `docutils/parsers/rst/directives/parts.py` | Public Domain |
| `docutils/parsers/rst/directives/references.py` | Public Domain |
| `docutils/parsers/rst/directives/tables.py` | Public Domain |
| `docutils/parsers/rst/languages/__init__.py` | Public Domain |
| `docutils/parsers/rst/languages/en.py` | Public Domain |
| `docutils/readers/__init__.py` | Public Domain |
| `docutils/readers/doctree.py` | Public Domain |
| `docutils/readers/standalone.py` | Public Domain |
| `docutils/transforms/__init__.py` | Public Domain |
| `docutils/transforms/frontmatter.py` | Public Domain |
| `docutils/transforms/misc.py` | Public Domain |
| `docutils/transforms/references.py` | Public Domain |
| `docutils/transforms/universal.py` | Public Domain |
| `docutils/utils/__init__.py` | Public Domain |
| `docutils/utils/_roman_numerals.py` | Public Domain |
| `docutils/utils/_typing.py` | Public Domain |
| `docutils/utils/code_analyzer.py` | Public Domain |
| `docutils/utils/urischemes.py` | Public Domain |
| `docutils/utils/punctuation_chars.py` | BSD 2-Clause |
| `docutils/utils/smartquotes.py` | BSD 2-Clause (see note) |
| `docutils/writers/__init__.py` | Public Domain |
| `docutils/writers/null.py` | Public Domain |

**Note on `smartquotes.py`:** This file is a 2-Clause BSD-licensed adaptation by Günter
Milde (© 2010–2023) of SmartyPants (© 2003 John Gruber, 3-Clause BSD) and
smartypants.py (© 2004, 2007 Chad Miller, 2-Clause BSD). Full license text is in
`_vendor/LICENSES.txt`.

## What was NOT vendored

The following parts of Docutils are **not present** in this repository and are **not
used** by rich-rst at runtime:

- `tools/editors/emacs/rst.el` — the GPL v3+ Emacs Lisp file that triggers scanner
  alerts. Not a Python module; never imported.
- `docutils/utils/math/` — math rendering modules (BSD-licensed but unused by rich-rst).
- `docutils/writers/` — all output writers except `writers/null.py` (unused).
- `docutils/parsers/commonmark_wrapper.py` — CommonMark parser (unused).
- All test files, documentation, and build tools.

## Keeping the vendor copy up to date

When upgrading the vendored copy to a newer Docutils release:

1. Install the target version: `pip install docutils==X.Y.Z`
2. Run `python tools/vendor_docutils.py` (see `tools/` directory) to re-copy and
   rewrite imports.
3. Run the test suite to confirm nothing broke.
4. Update the version number in **this file**, in `_vendor/LICENSES.txt`, and in
   the `# VENDORED:` comment at the top of `rich_rst/_vendor/docutils/__init__.py`.
5. Commit the updated `rich_rst/_vendor/docutils/` tree and both docs.

The internal import rewriting performed by the vendor script is the only modification
made to the upstream source. No logic is changed.
