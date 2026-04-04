# rich-rst

[![Documentation Status](https://readthedocs.org/projects/rich-rst/badge/?version=latest)](https://rich-rst.readthedocs.io/en/latest/?badge=latest)

Render [reStructuredText](https://docutils.sourceforge.io/rst.html) with [Rich](https://rich.readthedocs.io/en/latest/). This package turns reST documents into Rich renderables so you can preview documentation, docstrings, and snippets directly in the terminal. Also includes a CLI.

## Highlights

- Supports 89 of the 98 documented docutils elements. See [ELEMENTS.md](ELEMENTS.md) for the full support matrix.
- Handles common documentation features such as headings, lists, tables, links, images, code blocks, footnotes, and many Sphinx roles.
- Provides both a Python API and a command-line interface.
- Can also export rendered output to HTML from the CLI.

## Installation

```sh
pip install rich-rst
```

## Python API

```python
from rich import print
from rich_rst import RestructuredText

document = """
rich-rst
========

This is a **test** document.

- Item one
- Item two

.. code-block:: python

   print("hello")
"""

print(RestructuredText(document))
```

The main constructor options are `code_theme`, `show_line_numbers`, `show_errors`, `guess_lexer`, `default_lexer`, and `sphinx_compat`.

## Command Line Interface

Render a file:

```sh
python -m rich_rst readme.rst
```

Render from standard input:

```sh
python -m rich_rst -
```

View all available options:

```sh
python -m rich_rst --help
```

Useful flags include `--code-theme`, `--show-line-numbers`, `--guess-lexer`, `--default-lexer`, `--show-errors`, `--save-html`, `--html-theme`, `--list-html-themes`, `--output`, and `--version`.

## Compatibility

The renderer is designed for terminal output, so not every docutils feature can be represented visually. The current limitations and unsupported elements are documented in [ELEMENTS.md](ELEMENTS.md).

## Documentation

- [Project documentation](https://rich-rst.readthedocs.io/en/latest/)
- [Extension API guide](https://rich-rst.readthedocs.io/en/latest/extension_api.html)
- [Source code](https://github.com/wasi-master/rich-rst)
- [Issue tracker](https://github.com/wasi-master/rich-rst/issues)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
