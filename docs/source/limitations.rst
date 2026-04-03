Limitations and Behavior Notes
==============================

This page documents terminal-specific limitations and behavior differences so
output is predictable when rendering reStructuredText with rich-rst.

Terminal rendering constraints
------------------------------

rich-rst targets terminal output, so some docutils features cannot map 1:1 to
full HTML/Sphinx rendering.

- ``math`` (inline math) is not fully supported as a formatted equation object.
- ``math_block`` is rendered as plain math text in a labeled panel.
- Visual decorations that depend on page layout are simplified for terminals.
- Some Sphinx directives are intentionally no-op to avoid parse errors.

Sphinx compatibility behavior
-----------------------------

When ``sphinx_compat=True`` (default), rich-rst registers many Sphinx
roles/directives to improve docstring and Sphinx-source compatibility.

Important caveats:

- ``.. literalinclude::`` does not read files from disk; it renders a stub panel
  showing the referenced file name.
- ``.. only::`` always renders content; the expression is accepted but not
  evaluated.
- ``.. hlist::`` accepts ``:columns:``, but terminal output is rendered as a
  regular bullet list.
- ``.. highlight::`` is accepted silently and has no direct visual output.
- Some context directives are accepted silently (for example ``index`` and
  ``currentmodule`` variants) to prevent noisy system messages.

API vs CLI defaults
-------------------

The defaults are intentionally close, but one common difference is easy to miss:

- Python API ``RestructuredText(..., show_errors=True)`` defaults to showing
  parse/system messages.
- CLI ``python -m rich_rst ...`` defaults to hiding parse/system messages unless
  ``--show-errors`` is passed.

If you compare API and CLI output, align this option first.

What is intentionally simplified
--------------------------------

- Layout-specific HTML behavior is approximated with Rich panels, tables, and
  styled text.
- Links are rendered for terminal click/open support where possible.
- Source-level Sphinx metadata directives may be consumed with no visual output
  when their purpose is non-terminal metadata.

Reference pages
---------------

- See :doc:`elements` for full element coverage and rendering families.
- See :doc:`sphinx_heavy_demo` for practical Sphinx-oriented examples.
- See :doc:`documentation` for complete API and CLI option details.
