
<p align="center">
  <a href="https://github.com/wasi-master/rich-rst">
    <img src="https://raw.githubusercontent.com/wasi-master/rich-rst/main/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h1 align="center">rich-rst</h2>
</p>

<p align="center">
   <a href="https://rich-rst.readthedocs.io/en/latest/?badge=latest"><img src="https://readthedocs.org/projects/rich-rst/badge/?version=latest" alt="Documentation Status"></a>
   <img src="https://img.shields.io/github/actions/workflow/status/wasi-master/rich-rst/tests.yaml?label=tests" alt="Tests Status">
   <img src="https://img.shields.io/github/actions/workflow/status/wasi-master/rich-rst/codeql.yml?label=codeql" alt="CodeQL Status">
   <img src="https://img.shields.io/codecov/c/github/wasi-master/rich-rst" alt="Codecov">
</p>

Render [reStructuredText](https://docutils.sourceforge.io/rst.html) with [Rich](https://rich.readthedocs.io/en/latest/). This package turns reST documents into Rich renderables so you can preview documentation, docstrings, and snippets directly in the terminal. Also includes a CLI.

## Highlights

- Supports all currently documented RST elements.
- Handles common documentation features such as headings, lists, tables, links, images, code blocks, footnotes, and many Sphinx roles.
- Provides both a Python API and a command-line interface.
- Can also export rendered output to HTML from the CLI.

## Installation

```sh
pip install rich-rst
```

Experimental speed mode (uses `fast-rich` when available):

```sh
pip install "rich-rst[speed]"
```

By default, if `fast-rich` is installed then `rich-rst` will use it automatically.
To force standard Rich, set:

```sh
RICH_RST_USE_FAST_RICH=0
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

## Benchmarking

Benchmark large RST rendering with both backends:

```sh
python tools/benchmark_speed.py
```

Unicode-heavy benchmark preset (large file stress test):

```sh
python tools/benchmark_speed.py --preset unicode-stress --multiplier 1 --iterations 5 --width 120
```

Example result on this branch:

| Backend | Mean (s) |
|---|---:|
| rich | 1.2972 |
| fast-rich | 1.2643 |

Mean speed improvement with fast-rich: **2.53%**.
