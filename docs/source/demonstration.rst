Demonstration
=============


Some demos of how restructuredtext rendering looks.

The demos are possible because rich has the feature to save console
output to html files

Demo Files
----------

Console Output
~~~~~~~~~~~~~~

-  `directives.html <./directives.html>`__
-  `introduction.html <./introduction.html>`__
-  `rich_introduction.html <./rich_introduction.html>`__
-  `roles.html <./roles.html>`__
-  `specification.html <./specification.html>`__

Raw RST (Input)
~~~~~~~~~~~~~~~

-  `directives.rst <./directives.txt>`__
-  `introduction.rst <./introduction.txt>`__
-  `rich_introduction.rst <./rich_introduction.txt>`__
-  `roles.rst <./roles.txt>`__
-  `specification.rst <./specification.txt>`__

Parameters Used
---------------

The following command was used the generate every file except ``rich_introduction.rst``

On Windows:

.. code-block:: powershell

    rich_rst .\demo\filename.rst ^
        --save-html .\demo\filename.html ^
        --code-theme dracula ^
        --default-lexer rst  ^
        --soft-wrap ^
        --hide-errors

On Linux/Mac

.. code-block:: bash

    rich_rst ./demo/filename.rst \
        --save-html ./demo/filename.html \
        --code-theme dracula \
        --default-lexer rst  \
        --soft-wrap \
        --hide-errors

.. note:: There are aliases available for those parameters

For ``rich_introduction.rst``, The -dl parameter was set to python

Sources
-------

Original HTML
~~~~~~~~~~~~~

| ``directives.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/directives.html
| ``specification.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
| ``introduction.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/introduction.html
| ``mathematics.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/mathematics.html
| ``roles.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/roles.html
| ``rich_introduction.rst`` :
  https://rich.readthedocs.io/en/latest/introduction.html

Original RST
~~~~~~~~~~~~

| ``directives.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/directives.txt
| ``specification.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.txt
| ``introduction.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/introduction.txt
| ``mathematics.rst`` :
  https://docutils.sourceforge.io/docs/ref/rst/mathematics.txt
| ``roles.rst`` : https://docutils.sourceforge.io/docs/ref/rst/roles.txt
| ``rich_introduction.rst`` :
  https://github.com/Textualize/rich/raw/master/docs/source/introduction.rst

