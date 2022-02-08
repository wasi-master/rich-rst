.. rich-rst documentation master file, created by
   sphinx-quickstart on Mon Feb  7 21:28:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

rich-rst
=========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   demonstration.rst
   documentation.rst

Firstly, I'd like to thank you for using rich-rst.

Installation
~~~~~~~~~~~~

Run the following command to install

.. code-block:: bash

   python -m pip install rich-rst

If you want to live on the edge and install from master branch that may be unstable, run the following command.

.. code-block:: bash

   python -m pip install "git+https://github.com/wasi-master/rich-rst"

Here, you may need to replace ``python`` with ``python3`` on Linux and Mac and with ``py`` on Windows

Usage
~~~~~
If you want to print a RST document then you can use the following code

.. code-block:: python

   import rich
   from rich_rst import RestructuredText

   # Documentation for discord.py: https://pypi.org/project/discord.py
   docs = "Hello *World!*"

   rich.print(RestructuredText(docs, code_theme="dracula", show_errors=False))

Here docs is just a example and you should change it to your desired RST text.
The parameters are documented in :doc:`documentation <./documentation>`

Contributing
~~~~~~~~~~~~

Since the project is open source and `The source code is available on github`_
so you can easily see the repository `issues page`_ and help in that way. I
am open to new pull requests and issues and will look into each and every
one of them


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :doc:`./documentation`
* :doc:`./demonstration`


.. _The source code is available on github: https://github.com/wasi-master/rich-rst
.. _issues page: https://github.com/wasi-master/rich-rst/issues