
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

<details>
<summary><b>Other package managers</b> (and thanks to the people who maintain them)</summary>

<br>

rich-rst is packaged by volunteers across many ecosystems. A huge thank you to everyone listed below for keeping it available. Distro packages may lag behind PyPI; see [Repology](https://repology.org/project/python:rich-rst/versions) for current versions.

<a href="https://repology.org/project/python:rich-rst/versions"><img src="https://repology.org/badge/vertical-allrepos/python:rich-rst.svg?columns=3" alt="Packaging status"></a>

| Package manager | Package | Maintainer(s) | Install |
| --- | --- | --- | --- |
| PyPI | [`rich-rst`](https://pypi.org/project/rich-rst/) | [Wasi Master](https://github.com/wasi-master) | `pip install rich-rst` |
| conda-forge | [`rich-rst`](https://github.com/conda-forge/rich-rst-feedstock) | [David Brochart](https://github.com/davidbrochart) | `conda install -c conda-forge rich-rst` |
| Alpine Linux | [`py3-rich-rst`](https://pkgs.alpinelinux.org/packages?name=py3-rich-rst) | Bart Ribbers | `apk add py3-rich-rst` |
| ALT Linux | [`python3-module-rich-rst`](https://packages.altlinux.org/en/sisyphus/srpms/python3-module-rich-rst/) | Vladislav Eliseev | `apt-get install python3-module-rich-rst` |
| Arch Linux (AUR) | [`python-rich-rst`](https://aur.archlinux.org/packages/python-rich-rst) | [demizer](https://aur.archlinux.org/account/demizer) | `yay -S python-rich-rst` |
| Debian / Ubuntu<br><sub>also Kali, Parrot, Raspbian, Devuan, PureOS, deepin</sub> | [`python-rich-rst`](https://tracker.debian.org/pkg/python-rich-rst) | Nilson F. Silva & the [Debian Python Team](https://wiki.debian.org/Teams/PythonTeam) | `sudo apt install python3-rich-rst` |
| Exherbo | [`dev-python/rich-rst`](https://gitlab.exherbo.org/exherbo/python) | Timo Gurr | `cave resolve dev-python/rich-rst` |
| Fedora | [`python-rich-rst`](https://src.fedoraproject.org/rpms/python-rich-rst) | [Sam Doran](https://src.fedoraproject.org/user/samdoran) | `sudo dnf install python3-rich-rst` |
| FreeBSD | [`textproc/py-rich-rst`](https://www.freshports.org/textproc/py-rich-rst) | Po-Chuan Hsieh (sunpoet) | `cd /usr/ports/textproc/py-rich-rst && make install clean` |
| Gentoo (GURU) | [`dev-python/rich-rst`](https://gpo.zugaina.org/dev-python/rich-rst) | Florian Albrechtskirchinger | `eselect repository enable guru && emerge dev-python/rich-rst` |
| GNU Guix | [`python-rich-rst`](https://packages.guix.gnu.org/packages/python-rich-rst/) | Guix contributors | `guix install python-rich-rst` |
| MacPorts | [`py-rich_rst`](https://ports.macports.org/port/py-rich_rst/) | Unmaintained (open for adoption) | `sudo port install py313-rich_rst` |
| Mageia | [`python-rich-rst`](https://madb.mageia.org/package/show/name/python-rich-rst) | papoteur | `sudo dnf install python3-rich-rst` |
| Nixpkgs | [`python3Packages.rich-rst`](https://search.nixos.org/packages?query=rich-rst) | Nixpkgs contributors (originally Joel Koen) | `nix-shell -p python3Packages.rich-rst` |
| openSUSE | [`python-rich-rst`](https://build.opensuse.org/package/show/devel:languages:python/python-rich-rst) | Martin Pluskal & the openSUSE Python team | `sudo zypper install python313-rich-rst` |

Packaging rich-rst somewhere not listed here, or spotted a mistake? Open an issue or PR so you can be credited.

</details>

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

The main constructor options are `code_theme`, `show_line_numbers`, `show_errors`, `guess_lexer`, `default_lexer`, `sphinx_compat`, `admonition_style`, and `allow_file_access`.

Directives that read other files (`include`, `literalinclude`, and `raw`/`csv-table` with `:file:` or `:url:`) are disabled by default. Pass `allow_file_access=True` to enable them, but only for markup you trust.

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

Useful flags include ``--code-theme``, ``--show-line-numbers``, ``--guess-lexer``, ``--default-lexer``, ``--show-errors``, ``--allow-file-access``, ``--admonition-style``, ``-S/--save-html``, ``--html-theme``, ``--list-html-themes``, ``--output``, ``--debug``, and ``--version``.

## Compatibility

The renderer is designed for terminal output, so not every docutils feature can be represented visually. The current limitations and unsupported elements are documented in [ELEMENTS.md](ELEMENTS.md).

## Documentation

- [Project documentation](https://rich-rst.readthedocs.io/en/latest/)
- [Extension API guide](https://rich-rst.readthedocs.io/en/latest/extension_api.html)
- [Source code](https://github.com/wasi-master/rich-rst)
- [Issue tracker](https://github.com/wasi-master/rich-rst/issues)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
