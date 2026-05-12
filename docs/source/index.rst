rich-rst
========

**rich-rst** is a `reStructuredText`_ renderer for the `Rich`_ library.
It lets you render RST documents beautifully in the terminal, with full
support for headings, code blocks, tables, admonitions, footnotes, and
all rst elements. A kitchen sink style rendering reference can be 
viewed in :doc:`Sphinx & RST Demo Gallery <demo>`

Installation
------------

Install the latest stable release from PyPI:

.. code-block:: bash

   python -m pip install rich-rst

Install with experimental speed mode (uses ``fast-rich`` when available):

.. code-block:: bash

   python -m pip install "rich-rst[speed]"

To install the development version directly from the ``main`` branch:

.. code-block:: bash

   python -m pip install "git+https://github.com/wasi-master/rich-rst"

.. note::

   On Linux and macOS you may need to use ``python3`` instead of ``python``.
   On Windows you can use ``py`` as a shorthand.
   If ``fast-rich`` is installed, ``rich-rst`` uses it automatically (experimental).
   Set ``RICH_RST_USE_FAST_RICH=0`` to force standard Rich.

Quick start
-----------

Pass any RST string to :class:`~rich_rst.RestructuredText` and print it with
Rich:

.. code-block:: python

   from rich import print
   from rich_rst import RestructuredText

   print(RestructuredText("Hello *World!*"))

For a full list of constructor parameters see the :doc:`API reference <documentation>`.

Command-line interface
----------------------

Render a file directly from the terminal:

.. code-block:: bash

   python -m rich_rst README.rst

Read from standard input:

.. code-block:: bash

   cat README.rst | python -m rich_rst -

Run ``python -m rich_rst --help`` for the full list of options.

Benchmarking
------------

Benchmark large RST files across both backends:

.. code-block:: bash

   python tools/benchmark_speed.py

Unicode-heavy stress benchmark:

.. code-block:: bash

   python tools/benchmark_speed.py --preset unicode-stress --multiplier 1 --iterations 5 --width 120

Example result:

.. list-table::
   :header-rows: 1

   * - Backend
     - Mean (s)
   * - rich
     - 1.2972
   * - fast-rich
     - 1.2643

Contributing
------------

rich-rst is open source. The `source code`_ is hosted on GitHub. Bug reports
and pull requests are welcome on the `issue tracker`_.

.. toctree::
   :maxdepth: 2
   :caption: Documentation Contents

   documentation
   demo
   styling
   extension_api
   include_directive
   limitations



.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _Rich: https://rich.readthedocs.io/en/latest/
.. _source code: https://github.com/wasi-master/rich-rst
.. _issue tracker: https://github.com/wasi-master/rich-rst/issues
