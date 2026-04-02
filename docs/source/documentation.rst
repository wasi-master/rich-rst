API Reference
=============

Python API
----------

The main class is :class:`~rich_rst.RestructuredText`. Several aliases are
provided for convenience; they are all identical:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Name
     - Import path
   * - ``RestructuredText``
     - ``from rich_rst import RestructuredText``
   * - ``ReStructuredText``
     - ``from rich_rst import ReStructuredText``
   * - ``reStructuredText``
     - ``from rich_rst import reStructuredText``
   * - ``RST``
     - ``from rich_rst import RST``
   * - ``reST``
     - ``from rich_rst import reST``

.. autoclass:: rich_rst.RestructuredText
   :members:
   :undoc-members:

Command-line interface
----------------------

rich-rst ships with a CLI module that renders RST files (or standard input)
directly in the terminal.

Usage
~~~~~

.. code-block:: text

   python -m rich_rst PATH [options]
   python -m rich_rst - [options]     # read from stdin

Options
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-c``, ``--force-color``
     - Force ANSI colour output even on non-terminal streams.
   * - ``-e``, ``--encoding``
     - File encoding (default: ``utf-8``).
   * - ``-w``, ``--width``
     - Output width in columns (auto-detected by default).
   * - ``-hw``, ``--html-width``
     - ``max-width`` applied when saving HTML output (default: ``1675px``).
   * - ``-t``, ``--code-theme``
     - Pygments theme used for syntax-highlighted code blocks (default: ``monokai``).
   * - ``--show-line-numbers``
     - Show line numbers in syntax-highlighted code blocks.
   * - ``-html``, ``--save-html``
     - Path to save the rendered output as an HTML file.
   * - ``-r``, ``--wrap``
     - Hard-wrap long lines.
   * - ``-s``, ``--soft-wrap``
     - Enable soft-wrap mode (lines are wrapped by the terminal).
   * - ``-gl``, ``--guess-lexer``
     - Guess the syntax-highlighting language for code blocks that do not
       specify one.
   * - ``-dl``, ``--default-lexer``
     - Fallback language for code blocks when none is detected
       (default: ``python``).
   * - ``-he``, ``--hide-errors``
     - Suppress RST parse errors and warnings.
