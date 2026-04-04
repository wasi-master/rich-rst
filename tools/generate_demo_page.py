#!/usr/bin/env python3
"""
Generate docs/source/sphinx_heavy_demo.rst.

Each demo entry is a dict with:
  - "title"  : section heading
  - "demos"  : list of {"name", "rst"} pairs

For every ``rst`` snippet the script renders it with rich-rst (Dracula theme,
width 76 cols) and embeds the terminal-styled HTML directly in the .rst file
via a ``.. raw:: html`` directive so the documentation page shows both the
source code and the rendered output side-by-side.

Run this script whenever the demos should be regenerated:

    python tools/generate_demo_page.py
"""

import re
import sys
import textwrap
from pathlib import Path

# ---------------------------------------------------------------------------
# Allow running from the repo root without installing.
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

from rich.console import Console
from rich.terminal_theme import TerminalTheme

# ── Dracula theme (matches existing demo HTML files) ───────────────────────

def _rgb(r, g, b):
    return (r, g, b)


_DRACULA = TerminalTheme(
    _rgb(40, 42, 54),
    _rgb(248, 248, 242),
    [
        _rgb(40, 42, 54),
        _rgb(255, 85, 85),
        _rgb(80, 250, 123),
        _rgb(241, 250, 140),
        _rgb(189, 147, 249),
        _rgb(255, 121, 198),
        _rgb(139, 233, 253),
        _rgb(255, 255, 255),
    ],
    [
        _rgb(40, 42, 54),
        _rgb(255, 85, 85),
        _rgb(80, 250, 123),
        _rgb(241, 250, 140),
        _rgb(189, 147, 249),
        _rgb(255, 121, 198),
        _rgb(139, 233, 253),
        _rgb(255, 255, 255),
    ],
)

# Background colour used for the wrapper div.
_DRACULA_BG = "#282a36"

# Width used for all demo renders (matching the existing demos).
_RENDER_WIDTH = 76

# ── Demo data ────────────────────────────────────────────────────────────────

DEMOS = [
    # ── 1. Inline markup ─────────────────────────────────────────────────────
    {
        "title": "Inline Markup",
        "demos": [
            {
                "name": "Emphasis (italic)",
                "rst": "*italicised text* and _also italic_",
            },
            {
                "name": "Strong (bold)",
                "rst": "**bold text** and __also bold__",
            },
            {
                "name": "Inline literal (code)",
                "rst": "Use ``print()`` to display output.",
            },
            {
                "name": "Hyperlink (external)",
                "rst": "Visit `Python <https://www.python.org>`_ for more.",
            },
            {
                "name": "Anonymous hyperlink",
                "rst": "See `Rich docs <https://rich.readthedocs.io>`__ for styling.",
            },
            {
                "name": "Title reference",
                "rst": "Read `The Zen of Python` for inspiration.",
            },
            {
                "name": "Subscript role",
                "rst": "H\\ :sub:`2`\\ O is water.",
            },
            {
                "name": "Superscript role",
                "rst": "E = mc\\ :sup:`2`",
            },
            {
                "name": "Abbreviation role",
                "rst": ":abbr:`RST (reStructuredText)` is a markup language.",
            },
            {
                "name": "Keyboard role",
                "rst": "Press :kbd:`Ctrl+C` to copy.",
            },
            {
                "name": "GUI label role",
                "rst": "Click :guilabel:`OK` to confirm.",
            },
            {
                "name": "Menu selection role",
                "rst": "Go to :menuselection:`File --> Save As`.",
            },
            {
                "name": "File role",
                "rst": "Edit :file:`/etc/hosts` with sudo.",
            },
            {
                "name": "Sample (samp) role",
                "rst": "Type :samp:`ping {host}` in the terminal.",
            },
            {
                "name": "Command role",
                "rst": "Run :command:`python -m pytest`.",
            },
            {
                "name": "Program role",
                "rst": ":program:`git` is a distributed version control system.",
            },
            {
                "name": "PEP reference role",
                "rst": "See :pep:`8` for Python style guidelines.",
            },
            {
                "name": "RFC reference role",
                "rst": "HTTP is described in :rfc:`2616`.",
            },
            {
                "name": "Definition (dfn) role",
                "rst": "A :dfn:`docstring` is a string literal that documents a Python object.",
            },
            {
                "name": "Math role (inline)",
                "rst": "The area of a circle is :math:`\\pi r^2`.",
            },
        ],
    },
    # ── 2. Paragraphs and sections ────────────────────────────────────────────
    {
        "title": "Paragraphs and Sections",
        "demos": [
            {
                "name": "Plain paragraph",
                "rst": textwrap.dedent("""\
                    This is a plain paragraph.  Paragraphs are separated
                    by blank lines.

                    A second paragraph follows here."""),
            },
            {
                "name": "Section headings",
                "rst": textwrap.dedent("""\
                    Level 1 Title
                    =============

                    Level 2 Title
                    -------------

                    Level 3 Title
                    ~~~~~~~~~~~~~

                    Some body text under level 3."""),
            },
            {
                "name": "Document subtitle",
                "rst": textwrap.dedent("""\
                    My Document
                    ===========

                    A subtitle here
                    ---------------

                    Body text."""),
            },
            {
                "name": "Transition",
                "rst": textwrap.dedent("""\
                    First section content.

                    ----

                    Second section content."""),
            },
        ],
    },
    # ── 3. Lists ──────────────────────────────────────────────────────────────
    {
        "title": "Lists",
        "demos": [
            {
                "name": "Bullet list (dash)",
                "rst": textwrap.dedent("""\
                    - First item
                    - Second item
                    - Third item"""),
            },
            {
                "name": "Bullet list (asterisk)",
                "rst": textwrap.dedent("""\
                    * Alpha
                    * Beta
                    * Gamma"""),
            },
            {
                "name": "Nested bullet list",
                "rst": textwrap.dedent("""\
                    - Parent item

                      - Child item one
                      - Child item two

                    - Another parent"""),
            },
            {
                "name": "Enumerated list (auto-numbered)",
                "rst": textwrap.dedent("""\
                    #. First step
                    #. Second step
                    #. Third step"""),
            },
            {
                "name": "Enumerated list (arabic numerals)",
                "rst": textwrap.dedent("""\
                    1. Item one
                    2. Item two
                    3. Item three"""),
            },
            {
                "name": "Enumerated list (letters)",
                "rst": textwrap.dedent("""\
                    a. Apple
                    b. Banana
                    c. Cherry"""),
            },
            {
                "name": "Enumerated list (roman numerals)",
                "rst": textwrap.dedent("""\
                    i. Item i
                    ii. Item ii
                    iii. Item iii"""),
            },
            {
                "name": "Definition list",
                "rst": textwrap.dedent("""\
                    term
                        Definition of the term.

                    another term
                        Its definition spans
                        multiple lines."""),
            },
            {
                "name": "Definition list with classifier",
                "rst": textwrap.dedent("""\
                    term : string
                        A string-typed term.

                    count : int
                        An integer count."""),
            },
            {
                "name": "Field list",
                "rst": textwrap.dedent("""\
                    :Name: John Doe
                    :Email: john@example.com
                    :Role: Developer"""),
            },
            {
                "name": "Option list",
                "rst": textwrap.dedent("""\
                    -v, --verbose    Enable verbose output.
                    -o FILE          Write output to FILE.
                    --help           Show this help message."""),
            },
            {
                "name": "Horizontal list (hlist)",
                "rst": textwrap.dedent("""\
                    .. hlist::
                       :columns: 3

                       * Alpha
                       * Beta
                       * Gamma
                       * Delta
                       * Epsilon
                       * Zeta"""),
            },
        ],
    },
    # ── 4. Block markup ───────────────────────────────────────────────────────
    {
        "title": "Block Markup",
        "demos": [
            {
                "name": "Block quote",
                "rst": textwrap.dedent("""\
                    Normal paragraph.

                        This is an indented block quote.

                        -- Attribution"""),
            },
            {
                "name": "Line block",
                "rst": textwrap.dedent("""\
                    | The first line of a poem.
                    | The second line continues.
                    |   An indented third line."""),
            },
            {
                "name": "Doctest block",
                "rst": textwrap.dedent("""\
                    >>> print("Hello, world!")
                    Hello, world!
                    >>> 1 + 1
                    2"""),
            },
            {
                "name": "Literal block (indented)",
                "rst": textwrap.dedent("""\
                    Example code::

                        def greet(name):
                            print(f"Hello, {name}!")"""),
            },
            {
                "name": "Epigraph directive",
                "rst": textwrap.dedent("""\
                    .. epigraph::

                       No man is an island,
                       entire of itself.

                       -- John Donne"""),
            },
            {
                "name": "Highlights directive",
                "rst": textwrap.dedent("""\
                    .. highlights::

                       Key takeaways:

                       - Keep it simple.
                       - Document everything."""),
            },
            {
                "name": "Pull-quote directive",
                "rst": textwrap.dedent("""\
                    .. pull-quote::

                       The best way to predict the future
                       is to invent it.

                       -- Alan Kay"""),
            },
        ],
    },
    # ── 5. Code blocks ────────────────────────────────────────────────────────
    {
        "title": "Code Blocks",
        "demos": [
            {
                "name": "code-block with language",
                "rst": textwrap.dedent("""\
                    .. code-block:: python

                       def factorial(n):
                           if n == 0:
                               return 1
                           return n * factorial(n - 1)"""),
            },
            {
                "name": "code-block with line numbers",
                "rst": textwrap.dedent("""\
                    .. code-block:: python
                       :linenos:

                       x = 1
                       y = 2
                       print(x + y)"""),
            },
            {
                "name": "code-block: bash",
                "rst": textwrap.dedent("""\
                    .. code-block:: bash

                       pip install rich-rst
                       python -m rich_rst README.rst"""),
            },
            {
                "name": "code-block: JSON",
                "rst": textwrap.dedent("""\
                    .. code-block:: json

                       {
                         "name": "rich-rst",
                         "version": "1.0.0",
                         "description": "RST renderer for Rich"
                       }"""),
            },
            {
                "name": "code-block: YAML",
                "rst": textwrap.dedent("""\
                    .. code-block:: yaml

                       name: rich-rst
                       dependencies:
                         - rich>=10.0
                         - docutils>=0.17"""),
            },
            {
                "name": "sourcecode alias",
                "rst": textwrap.dedent("""\
                    .. sourcecode:: javascript

                       const greet = (name) => `Hello, ${name}!`;
                       console.log(greet('World'));"""),
            },
            {
                "name": "code alias (no language)",
                "rst": textwrap.dedent("""\
                    .. code::

                       plain text block
                       no syntax highlighting"""),
            },
            {
                "name": "productionlist directive",
                "rst": textwrap.dedent("""\
                    .. productionlist::

                       statement  : expression NEWLINE
                       expression : term ('+' term)*
                       term       : factor ('*' factor)*"""),
            },
        ],
    },
    # ── 6. Admonitions ────────────────────────────────────────────────────────
    {
        "title": "Admonitions",
        "demos": [
            {
                "name": "note",
                "rst": textwrap.dedent("""\
                    .. note::

                       This is a note admonition."""),
            },
            {
                "name": "warning",
                "rst": textwrap.dedent("""\
                    .. warning::

                       This is a warning."""),
            },
            {
                "name": "tip",
                "rst": textwrap.dedent("""\
                    .. tip::

                       This is a tip."""),
            },
            {
                "name": "important",
                "rst": textwrap.dedent("""\
                    .. important::

                       This is important."""),
            },
            {
                "name": "hint",
                "rst": textwrap.dedent("""\
                    .. hint::

                       This is a hint."""),
            },
            {
                "name": "attention",
                "rst": textwrap.dedent("""\
                    .. attention::

                       Pay attention to this."""),
            },
            {
                "name": "caution",
                "rst": textwrap.dedent("""\
                    .. caution::

                       Exercise caution here."""),
            },
            {
                "name": "danger",
                "rst": textwrap.dedent("""\
                    .. danger::

                       Danger! Proceed carefully."""),
            },
            {
                "name": "error",
                "rst": textwrap.dedent("""\
                    .. error::

                       An error occurred."""),
            },
            {
                "name": "Generic admonition with custom title",
                "rst": textwrap.dedent("""\
                    .. admonition:: Did you know?

                       rich-rst supports 79 RST elements."""),
            },
            {
                "name": "Admonition with nested content",
                "rst": textwrap.dedent("""\
                    .. note::

                       Notes can contain **bold**, *italic*, and ``code``.

                       They can also contain lists:

                       - item one
                       - item two"""),
            },
        ],
    },
    # ── 7. Tables ─────────────────────────────────────────────────────────────
    {
        "title": "Tables",
        "demos": [
            {
                "name": "Simple table",
                "rst": textwrap.dedent("""\
                    =====  =====  ======
                    Col A  Col B  Col C
                    =====  =====  ======
                    1      2      3
                    4      5      6
                    =====  =====  ======"""),
            },
            {
                "name": "Grid table",
                "rst": textwrap.dedent("""\
                    +----------+----------+----------+
                    | Header 1 | Header 2 | Header 3 |
                    +==========+==========+==========+
                    | row 1    | data     | more     |
                    +----------+----------+----------+
                    | row 2    | data     | more     |
                    +----------+----------+----------+"""),
            },
            {
                "name": "list-table directive",
                "rst": textwrap.dedent("""\
                    .. list-table:: Comparison
                       :header-rows: 1
                       :widths: 30 35 35

                       * - Library
                         - Language
                         - Stars
                       * - rich
                         - Python
                         - 50k+
                       * - rich-rst
                         - Python
                         - 1k+"""),
            },
            {
                "name": "csv-table directive",
                "rst": textwrap.dedent("""\
                    .. csv-table:: Data
                       :header: "Name", "Value", "Unit"
                       :widths: 20, 20, 20

                       "Speed", "299 792 458", "m/s"
                       "Charge", "1.602e-19", "C"
                       "Mass", "9.109e-31", "kg" """),
            },
        ],
    },
    # ── 8. Footnotes and citations ────────────────────────────────────────────
    {
        "title": "Footnotes and Citations",
        "demos": [
            {
                "name": "Manual footnote",
                "rst": textwrap.dedent("""\
                    See the footnote [1]_ for details.

                    .. [1] This is the footnote text."""),
            },
            {
                "name": "Auto-numbered footnote",
                "rst": textwrap.dedent("""\
                    First reference [#]_.
                    Second reference [#]_.

                    .. [#] First auto footnote.
                    .. [#] Second auto footnote."""),
            },
            {
                "name": "Named auto footnote",
                "rst": textwrap.dedent("""\
                    See [#note]_ for details.

                    .. [#note] The named auto footnote."""),
            },
            {
                "name": "Symbol footnote",
                "rst": textwrap.dedent("""\
                    Marked with a symbol [*]_.

                    .. [*] Symbol footnote text."""),
            },
            {
                "name": "Citation",
                "rst": textwrap.dedent("""\
                    As described in [Doe2023]_.

                    .. [Doe2023] John Doe. *Python Patterns*. 2023."""),
            },
        ],
    },
    # ── 9. Hyperlinks and targets ─────────────────────────────────────────────
    {
        "title": "Hyperlinks and Targets",
        "demos": [
            {
                "name": "Standalone hyperlink",
                "rst": "Visit https://python.org for more.",
            },
            {
                "name": "External hyperlink (named)",
                "rst": textwrap.dedent("""\
                    Read the `Rich documentation`_.

                    .. _Rich documentation: https://rich.readthedocs.io"""),
            },
            {
                "name": "Internal cross-reference (indirect target)",
                "rst": textwrap.dedent("""\
                    Jump to `Target Section`_.

                    Target Section
                    ~~~~~~~~~~~~~~

                    Content here."""),
            },
            {
                "name": "Anonymous hyperlink",
                "rst": textwrap.dedent("""\
                    See `this page <https://example.com>`__ for details."""),
            },
        ],
    },
    # ── 10. Substitutions ─────────────────────────────────────────────────────
    {
        "title": "Substitutions",
        "demos": [
            {
                "name": "Text substitution",
                "rst": textwrap.dedent("""\
                    |project| is written in Python.

                    .. |project| replace:: rich-rst"""),
            },
            {
                "name": "Date substitution",
                "rst": textwrap.dedent("""\
                    Generated on |today|.

                    .. |today| date:: %Y-%m-%d"""),
            },
            {
                "name": "Unicode substitution",
                "rst": textwrap.dedent("""\
                    Copyright |copy| 2024 The Authors.

                    .. |copy| unicode:: U+00A9 .. copyright sign"""),
            },
            {
                "name": "Image substitution",
                "rst": textwrap.dedent("""\
                    Click the |logo| icon.

                    .. |logo| image:: https://example.com/logo.png
                       :alt: Logo"""),
            },
        ],
    },
    # ── 11. Images and figures ────────────────────────────────────────────────
    {
        "title": "Images and Figures",
        "demos": [
            {
                "name": "image directive",
                "rst": textwrap.dedent("""\
                    .. image:: https://example.com/photo.png
                       :alt: A photo
                       :width: 400px"""),
            },
            {
                "name": "figure directive",
                "rst": textwrap.dedent("""\
                    .. figure:: https://example.com/chart.png
                       :alt: A chart
                       :width: 600px

                       Figure caption goes here."""),
            },
            {
                "name": "figure with legend",
                "rst": textwrap.dedent("""\
                    .. figure:: https://example.com/diagram.png
                       :alt: Diagram

                       Caption text.

                       Legend text with more details about the figure."""),
            },
        ],
    },
    # ── 12. Document structure ────────────────────────────────────────────────
    {
        "title": "Document Structure Directives",
        "demos": [
            {
                "name": "topic directive",
                "rst": textwrap.dedent("""\
                    .. topic:: Interesting Fact

                       This is the topic body.
                       It can contain any body elements."""),
            },
            {
                "name": "sidebar directive",
                "rst": textwrap.dedent("""\
                    .. sidebar:: Note

                       :Subtitle: Side note

                       Sidebar text goes here."""),
            },
            {
                "name": "rubric directive",
                "rst": textwrap.dedent("""\
                    .. rubric:: An Unnumbered Heading

                    Following paragraph."""),
            },
            {
                "name": "contents directive (table of contents)",
                "rst": textwrap.dedent("""\
                    .. contents:: Table of Contents
                       :depth: 2

                    Section A
                    ---------

                    Content A.

                    Section B
                    ---------

                    Content B."""),
            },
            {
                "name": "sectnum directive",
                "rst": textwrap.dedent("""\
                    .. sectnum::

                    Overview
                    --------

                    Details
                    -------"""),
            },
            {
                "name": "header directive",
                "rst": textwrap.dedent("""\
                    .. header:: My Document Header

                    Main content."""),
            },
            {
                "name": "footer directive",
                "rst": textwrap.dedent("""\
                    Main content.

                    .. footer:: Page |page|"""),
            },
            {
                "name": "centered directive",
                "rst": textwrap.dedent("""\
                    .. centered:: IMPORTANT NOTICE

                    Body text."""),
            },
        ],
    },
    # ── 13. Math ──────────────────────────────────────────────────────────────
    {
        "title": "Math",
        "demos": [
            {
                "name": "Inline math role",
                "rst": "The Pythagorean theorem: :math:`a^2 + b^2 = c^2`.",
            },
            {
                "name": "math directive (display)",
                "rst": textwrap.dedent("""\
                    .. math::

                       \\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}"""),
            },
            {
                "name": "math directive (labeled)",
                "rst": textwrap.dedent("""\
                    .. math:: E = mc^2
                       :label: einstein"""),
            },
        ],
    },
    # ── 14. docinfo field list ────────────────────────────────────────────────
    {
        "title": "Document Info (docinfo)",
        "demos": [
            {
                "name": "Standard docinfo fields",
                "rst": textwrap.dedent("""\
                    My Report
                    =========

                    :Author: Jane Smith
                    :Date: 2024-01-15
                    :Version: 1.0
                    :Status: Draft
                    :Copyright: 2024 Jane Smith
                    :Organization: ACME Corp

                    Body of the document."""),
            },
            {
                "name": "Authors list",
                "rst": textwrap.dedent("""\
                    :Authors: - Alice
                              - Bob
                              - Carol

                    Body text."""),
            },
        ],
    },
    # ── 15. Comments ─────────────────────────────────────────────────────────
    {
        "title": "Comments",
        "demos": [
            {
                "name": "RST comment (invisible)",
                "rst": textwrap.dedent("""\
                    Before comment.

                    .. This is an RST comment and should not appear in output.

                    After comment."""),
            },
        ],
    },
    # ── 16. Raw directive ─────────────────────────────────────────────────────
    {
        "title": "Raw Directive",
        "demos": [
            {
                "name": "raw html directive",
                "rst": textwrap.dedent("""\
                    .. raw:: html

                       <strong>Bold via raw HTML</strong>"""),
            },
            {
                "name": "raw latex directive",
                "rst": textwrap.dedent("""\
                    .. raw:: latex

                       \\textbf{Bold via LaTeX}"""),
            },
        ],
    },
    # ── 17. Sphinx version directives ─────────────────────────────────────────
    {
        "title": "Sphinx Version Directives",
        "demos": [
            {
                "name": "versionadded",
                "rst": textwrap.dedent("""\
                    .. versionadded:: 2.1

                       This feature was added in version 2.1."""),
            },
            {
                "name": "versionchanged",
                "rst": textwrap.dedent("""\
                    .. versionchanged:: 3.0

                       The API changed in version 3.0."""),
            },
            {
                "name": "deprecated",
                "rst": textwrap.dedent("""\
                    .. deprecated:: 1.5

                       Use the new API instead."""),
            },
            {
                "name": "deprecated-removed",
                "rst": textwrap.dedent("""\
                    .. deprecated-removed:: 1.5 2.0

                       Removed in 2.0. Use the new API."""),
            },
        ],
    },
    # ── 18. Sphinx cross-reference roles ──────────────────────────────────────
    {
        "title": "Sphinx Cross-Reference Roles",
        "demos": [
            {
                "name": ":func: role",
                "rst": "Call :func:`os.path.join` to join paths.",
            },
            {
                "name": ":class: role",
                "rst": "Use :class:`pathlib.Path` for path handling.",
            },
            {
                "name": ":meth: role",
                "rst": "Call :meth:`str.upper` to uppercase a string.",
            },
            {
                "name": ":attr: role",
                "rst": "Access :attr:`os.sep` for the path separator.",
            },
            {
                "name": ":mod: role",
                "rst": "The :mod:`os.path` module provides path utilities.",
            },
            {
                "name": ":exc: role",
                "rst": "Raises :exc:`ValueError` when the input is invalid.",
            },
            {
                "name": ":obj: role",
                "rst": "Set :obj:`sys.path` to control module lookup.",
            },
            {
                "name": ":data: role",
                "rst": "Read :data:`sys.version` for the Python version.",
            },
            {
                "name": ":const: role",
                "rst": "The value of :const:`math.pi` is approximately 3.14.",
            },
            {
                "name": ":term: role",
                "rst": "A :term:`decorator` wraps another function.",
            },
            {
                "name": ":ref: role (cross-reference)",
                "rst": "See :ref:`some-label` for details.",
            },
            {
                "name": ":doc: role",
                "rst": "Refer to :doc:`installation` for setup instructions.",
            },
            {
                "name": ":envvar: role",
                "rst": "Set :envvar:`PYTHONPATH` before running.",
            },
        ],
    },
    # ── 19. Python domain directives ──────────────────────────────────────────
    {
        "title": "Python Domain Directives",
        "demos": [
            {
                "name": "py:function",
                "rst": textwrap.dedent("""\
                    .. py:function:: greet(name: str) -> str

                       Return a greeting for *name*.

                       :param name: The name to greet.
                       :type name: str
                       :returns: A greeting string.
                       :rtype: str"""),
            },
            {
                "name": "py:class",
                "rst": textwrap.dedent("""\
                    .. py:class:: MyClass(value)

                       A simple example class.

                       :param value: Initial value.
                       :type value: int"""),
            },
            {
                "name": "py:method",
                "rst": textwrap.dedent("""\
                    .. py:method:: MyClass.process(data)

                       Process the given *data*."""),
            },
            {
                "name": "py:attribute",
                "rst": textwrap.dedent("""\
                    .. py:attribute:: MyClass.value
                       :type: int

                       The current value."""),
            },
            {
                "name": "py:data",
                "rst": textwrap.dedent("""\
                    .. py:data:: MAX_RETRIES
                       :value: 3

                       Maximum number of retry attempts."""),
            },
            {
                "name": "py:exception",
                "rst": textwrap.dedent("""\
                    .. py:exception:: MyError

                       Raised when something goes wrong."""),
            },
            {
                "name": "py:module",
                "rst": textwrap.dedent("""\
                    .. py:module:: mypackage.core

                       Core functionality for mypackage."""),
            },
            {
                "name": "py:decorator",
                "rst": textwrap.dedent("""\
                    .. py:decorator:: cached(func)

                       Cache the return value of *func*."""),
            },
        ],
    },
    # ── 20. seealso directive ─────────────────────────────────────────────────
    {
        "title": "See Also",
        "demos": [
            {
                "name": "seealso directive",
                "rst": textwrap.dedent("""\
                    .. seealso::

                       :func:`os.path.join`, :class:`pathlib.Path`"""),
            },
            {
                "name": "seealso with inline argument",
                "rst": ".. seealso:: :mod:`json` for serialization.",
            },
        ],
    },
    # ── 21. toctree (Sphinx) ──────────────────────────────────────────────────
    {
        "title": "Toctree (Sphinx)",
        "demos": [
            {
                "name": "toctree directive",
                "rst": textwrap.dedent("""\
                    .. toctree::
                       :maxdepth: 2
                       :caption: Contents

                       installation
                       usage
                       api"""),
            },
        ],
    },
    # ── 22. glossary ─────────────────────────────────────────────────────────
    {
        "title": "Glossary",
        "demos": [
            {
                "name": "glossary directive",
                "rst": textwrap.dedent("""\
                    .. glossary::

                       RST
                           reStructuredText — a lightweight markup language.

                       Sphinx
                           A documentation generator for Python projects."""),
            },
            {
                "name": "glossary (sorted)",
                "rst": textwrap.dedent("""\
                    .. glossary::
                       :sorted:

                       Zebra
                           A striped animal.

                       Aardvark
                           An ant-eating mammal."""),
            },
        ],
    },
    # ── 23. Mixed Sphinx roles ────────────────────────────────────────────────
    {
        "title": "Mixed Sphinx Roles in Prose",
        "demos": [
            {
                "name": "Mixed roles in a paragraph",
                "rst": textwrap.dedent("""\
                    Use :func:`json.dumps` or :func:`json.loads` to serialize data.
                    The :class:`dict` type maps :class:`str` keys to values.
                    See :pep:`484` for type hints and :pep:`526` for variable annotations.
                    Press :kbd:`Ctrl+D` or call :func:`exit` to quit the REPL."""),
            },
        ],
    },
]


# ── Rendering helpers ─────────────────────────────────────────────────────────

def render_rst_to_html_fragment(rst_source: str) -> str:
    """Render *rst_source* with rich-rst and return an embeddable HTML snippet.

    The returned snippet is a ``<div>`` containing a dark-background ``<pre>``
    block with all styles inlined (no external CSS required).
    """
    from rich_rst import RestructuredText

    console = Console(
        record=True,
        width=_RENDER_WIDTH,
        force_terminal=True,
        force_jupyter=False,
    )
    rst_obj = RestructuredText(
        rst_source,
        code_theme="dracula",
        show_errors=False,
        default_lexer="text",
    )
    console.print(rst_obj, soft_wrap=True)
    html = console.export_html(inline_styles=True, theme=_DRACULA)

    # Extract the <pre> block (contains the entire rendered output).
    match = re.search(r'<pre[^>]*>.*?</pre>', html, re.DOTALL)
    if not match:
        return "<pre><!-- render failed --></pre>"
    pre_block = match.group(0)

    # Wrap in a styled container so it stands out on the docs page.
    return (
        '<div style="'
        f'background:{_DRACULA_BG};'
        'border-radius:6px;'
        'padding:12px 16px;'
        'margin:8px 0 16px 0;'
        'overflow-x:auto;'
        '">\n'
        f'{pre_block}\n'
        '</div>\n'
    )


# ── RST generation helpers ────────────────────────────────────────────────────

def _heading(text: str, char: str) -> str:
    return f"{text}\n{char * len(text)}\n"


def _indent(text: str, spaces: int = 3) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line.strip() else "" for line in text.splitlines())


def _rst_code_block(source: str) -> str:
    lines = [".. code-block:: rst", ""]
    for line in source.splitlines():
        lines.append("   " + line if line else "")
    lines.append("")
    return "\n".join(lines) + "\n"


def _raw_html_block(html_fragment: str) -> str:
    lines = [".. raw:: html", ""]
    for line in html_fragment.splitlines():
        lines.append("   " + line if line else "")
    lines.append("")
    return "\n".join(lines) + "\n"


# ── Page generator ────────────────────────────────────────────────────────────

_HEADER = """\
.. THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
   Re-generate it by running:  python tools/generate_demo_page.py

Sphinx & RST Demo Gallery
==========================

This page shows every supported RST and Sphinx element rendered by
**rich-rst**.  For each element the raw RST source is shown in a code block,
followed by the terminal-styled HTML snapshot produced by rich-rst (Dracula
theme, 76-column width).

.. contents:: On this page
   :depth: 2
   :local:

"""

_FOOTER = """\

----

*This page was generated automatically.  Run* ``python tools/generate_demo_page.py``
*from the repository root to refresh it.*
"""


def generate() -> str:
    parts = [_HEADER]

    total = sum(len(section["demos"]) for section in DEMOS)
    print(f"Rendering {total} demos across {len(DEMOS)} sections …")

    for section in DEMOS:
        parts.append(_heading(section["title"], "-") + "\n")
        for demo in section["demos"]:
            print(f"  • {section['title']} / {demo['name']}")
            parts.append(_heading(demo["name"], "~") + "\n")
            parts.append(_rst_code_block(demo["rst"]))
            try:
                html_frag = render_rst_to_html_fragment(demo["rst"])
            except Exception as exc:  # noqa: BLE001
                html_frag = f"<pre><!-- render error: {exc} --></pre>"
            parts.append(_raw_html_block(html_frag))

    parts.append(_FOOTER)
    return "".join(parts)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    output_path = REPO_ROOT / "docs" / "source" / "sphinx_heavy_demo.rst"
    print(f"Writing to {output_path}")
    content = generate()
    output_path.write_text(content, encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()
