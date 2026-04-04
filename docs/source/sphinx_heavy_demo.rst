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

Inline Markup
-------------

Emphasis (italic)
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   *italicised text* and _also italic_

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-style: italic">italicised text</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-style: italic"> and _also </span><span style="font-style: italic">italic_</span>
   </code></pre>
   </div>

Strong (bold)
~~~~~~~~~~~~~

.. code-block:: rst

   **bold text** and __also bold__

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-weight: bold">bold text</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold"> and __also </span><span style="font-weight: bold">bold__</span>
   </code></pre>
   </div>

Inline literal (code)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Use ``print()`` to display output.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">print()</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to display output.</span>
   </code></pre>
   </div>

Hyperlink (external)
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Visit `Python <https://www.python.org>`_ for more.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Visit </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://www.python.org">Python</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for more.</span>
   </code></pre>
   </div>

Anonymous hyperlink
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See `Rich docs <https://rich.readthedocs.io>`__ for styling.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://rich.readthedocs.io">Rich docs</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for styling.</span>
   </code></pre>
   </div>

Title reference
~~~~~~~~~~~~~~~

.. code-block:: rst

   Read `The Zen of Python` for inspiration.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Read </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-style: italic">The Zen of Python</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for inspiration.</span>
   </code></pre>
   </div>

Subscript role
~~~~~~~~~~~~~~

.. code-block:: rst

   H\ :sub:`2`\ O is water.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">H₂O is water.</span>
   </code></pre>
   </div>

Superscript role
~~~~~~~~~~~~~~~~

.. code-block:: rst

   E = mc\ :sup:`2`

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">E = mc²</span>
   </code></pre>
   </div>

Abbreviation role
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   :abbr:`RST (reStructuredText)` is a markup language.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="text-decoration: underline">RST (reStructuredText)</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> is a markup language.</span>
   </code></pre>
   </div>

Keyboard role
~~~~~~~~~~~~~

.. code-block:: rst

   Press :kbd:`Ctrl+C` to copy.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Press </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">Ctrl+C</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to copy.</span>
   </code></pre>
   </div>

GUI label role
~~~~~~~~~~~~~~

.. code-block:: rst

   Click :guilabel:`OK` to confirm.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Click </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">OK</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to confirm.</span>
   </code></pre>
   </div>

Menu selection role
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Go to :menuselection:`File --> Save As`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Go to </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">File ▶ Save As</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

File role
~~~~~~~~~

.. code-block:: rst

   Edit :file:`/etc/hosts` with sudo.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Edit </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">/etc/hosts</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> with sudo.</span>
   </code></pre>
   </div>

Sample (samp) role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Type :samp:`ping {host}` in the terminal.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Type </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">ping host</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> in the terminal.</span>
   </code></pre>
   </div>

Command role
~~~~~~~~~~~~

.. code-block:: rst

   Run :command:`python -m pytest`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Run </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">python -m pytest</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

Program role
~~~~~~~~~~~~

.. code-block:: rst

   :program:`git` is a distributed version control system.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-weight: bold">git</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold"> is a distributed version control system.</span>
   </code></pre>
   </div>

PEP reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :pep:`8` for Python style guidelines.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0008/">PEP 8</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for Python style guidelines.</span>
   </code></pre>
   </div>

RFC reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   HTTP is described in :rfc:`2616`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">HTTP is described in </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://datatracker.ietf.org/doc/html/rfc2616">RFC 2616</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

Definition (dfn) role
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   A :dfn:`docstring` is a string literal that documents a Python object.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">A </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-style: italic">docstring</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> is a string literal that documents a Python object.</span>
   </code></pre>
   </div>

Math role (inline)
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   The area of a circle is :math:`\pi r^2`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">The area of a circle is </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-style: italic">π r^2</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

Paragraphs and Sections
-----------------------

Plain paragraph
~~~~~~~~~~~~~~~

.. code-block:: rst

   This is a plain paragraph.  Paragraphs are separated
   by blank lines.

   A second paragraph follows here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">This is a plain paragraph.  Paragraphs are separated by blank lines.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">A second paragraph follows here.</span>
   </code></pre>
   </div>

Section headings
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Level 1 Title
   =============

   Level 2 Title
   -------------

   Level 3 Title
   ~~~~~~~~~~~~~

   Some body text under level 3.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">                               <span style="font-style: italic">Level 1 Title</span>                                

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Level 2 Title</span><span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                              Level 3 Title                               ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Some body text under level 3.</span>
   </code></pre>
   </div>

Document subtitle
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   My Document
   ===========

   A subtitle here
   ---------------

   Body text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">                                <span style="font-style: italic">My Document</span>                                 

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">A subtitle hereBody text.</span>
   </code></pre>
   </div>

Transition
~~~~~~~~~~

.. code-block:: rst

   First section content.

   ----

   Second section content.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">First section content.</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">────────────────────────────────────────────────────────────────────────────</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Second section content.</span>
   </code></pre>
   </div>

Lists
-----

Bullet list (dash)
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   - First item
   - Second item
   - Third item

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">First item</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Second item</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Third item</span>
   </code></pre>
   </div>

Bullet list (asterisk)
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   * Alpha
   * Beta
   * Gamma

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Alpha</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Beta</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Gamma</span>
   </code></pre>
   </div>

Nested bullet list
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   - Parent item

     - Child item one
     - Child item two

   - Another parent

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Parent item</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Child item one</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Child item two</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Another parent</span>
   </code></pre>
   </div>

Enumerated list (auto-numbered)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   #. First step
   #. Second step
   #. Third step

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 1.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">First step</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 2.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Second step</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 3.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Third step</span>
   </code></pre>
   </div>

Enumerated list (arabic numerals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   1. Item one
   2. Item two
   3. Item three

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 1.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item one</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 2.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item two</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 3.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item three</span>
   </code></pre>
   </div>

Enumerated list (letters)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   a. Apple
   b. Banana
   c. Cherry

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> a.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Apple</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> b.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Banana</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> c.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Cherry</span>
   </code></pre>
   </div>

Enumerated list (roman numerals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   i. Item i
   ii. Item ii
   iii. Item iii

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> i.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item i</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> ii.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item ii</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> iii.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Item iii</span>
   </code></pre>
   </div>

Definition list
~~~~~~~~~~~~~~~

.. code-block:: rst

   term
       Definition of the term.

   another term
       Its definition spans
       multiple lines.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">term
       Definition of the term.
         
   another term
       Its definition spans multiple lines.
   </code></pre>
   </div>

Definition list with classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   term : string
       A string-typed term.

   count : int
       An integer count.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">    term : <span style="color: #8be9fd; text-decoration-color: #8be9fd">string</span>
         
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">A string-typed term.</span>


       count : <span style="color: #8be9fd; text-decoration-color: #8be9fd">int</span>
         
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">An integer count.</span>
   </code></pre>
   </div>

Field list
~~~~~~~~~~

.. code-block:: rst

   :Name: John Doe
   :Email: john@example.com
   :Role: Developer

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
   ┃<span style="font-weight: bold"> Field Name </span>┃<span style="font-weight: bold"> Field Value      </span>┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
   │ <span style="font-weight: bold">Name      </span> │ John Doe         │
   ├────────────┼──────────────────┤
   │ <span style="font-weight: bold">Email     </span> │ john@example.com │
   ├────────────┼──────────────────┤
   │ <span style="font-weight: bold">Role      </span> │ Developer        │
   └────────────┴──────────────────┘
   </code></pre>
   </div>

Option list
~~~~~~~~~~~

.. code-block:: rst

   -v, --verbose    Enable verbose output.
   -o FILE          Write output to FILE.
   --help           Show this help message.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">-v, --verbose, 
       Enable verbose output.
   -o FILE
       Write output to FILE.
   --help
       Show this help message.
   </code></pre>
   </div>

Horizontal list (hlist)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. hlist::
      :columns: 3

      * Alpha
      * Beta
      * Gamma
      * Delta
      * Epsilon
      * Zeta

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Alpha</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Beta   </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Gamma</span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Delta</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Epsilon</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Zeta </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">     </span> 
   </code></pre>
   </div>

Block Markup
------------

Block quote
~~~~~~~~~~~

.. code-block:: rst

   Normal paragraph.

       This is an indented block quote.

       -- Attribution

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Normal paragraph.</span>

   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #282a36">This is an indented block quote.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — Attribution</span>
   </code></pre>
   </div>

Line block
~~~~~~~~~~

.. code-block:: rst

   | The first line of a poem.
   | The second line continues.
   |   An indented third line.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">The first line of a poem.
   The second line continues.
       An indented third line.
   </code></pre>
   </div>

Doctest block
~~~~~~~~~~~~~

.. code-block:: rst

   >>> print("Hello, world!")
   Hello, world!
   >>> 1 + 1
   2

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── doctest block ──────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">&gt;&gt;&gt; </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&quot;Hello, world!&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span>                                               <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #44475a; text-decoration-color: #44475a; background-color: #282a36">Hello, world!</span>                                                            <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">&gt;&gt;&gt; </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">+</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span>                                                                <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #44475a; text-decoration-color: #44475a; background-color: #282a36">2</span>                                                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Literal block (indented)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Example code::

       def greet(name):
           print(f"Hello, {name}!")

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Example code:</span>
   <span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── text (default) ─────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">def greet(name):</span>                                                         <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    print(f&quot;Hello, {name}!&quot;)</span>                                             <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Epigraph directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. epigraph::

      No man is an island,
      entire of itself.

      -- John Donne

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #282a36">No man is an island, entire of itself.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — John Donne</span>
   </code></pre>
   </div>

Highlights directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. highlights::

      Key takeaways:

      - Keep it simple.
      - Document everything.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #282a36">Key takeaways:</span>


   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold"> •</span>
   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Keep it simple.</span>


   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span>
   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Document everything.</span>
   </code></pre>
   </div>

Pull-quote directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pull-quote::

      The best way to predict the future
      is to invent it.

      -- Alan Kay

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #282a36">The best way to predict the future is to invent it.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — Alan Kay</span>
   </code></pre>
   </div>

Code Blocks
-----------

code-block with language
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python

      def factorial(n):
          if n == 0:
              return 1
          return n * factorial(n - 1)

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b; background-color: #282a36">factorial</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(n):</span>                                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">if</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">==</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">0</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">:</span>                                                           <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">        </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span>                                                         <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">*</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> factorial(n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">-</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span>                                          <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

code-block with line numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :linenos:

      x = 1
      y = 2
      print(x + y)

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span>                                                                    <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">y </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">2</span>                                                                    <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">+</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> y)</span>                                                             <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

code-block: bash
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: bash

      pip install rich-rst
      python -m rich_rst README.rst

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── bash ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">pip install rich-rst</span>                                                     <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">python -m rich_rst README.rst</span>                                            <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

code-block: JSON
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: json

      {
        "name": "rich-rst",
        "version": "1.0.0",
        "description": "RST renderer for Rich"
      }

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── json ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">{</span>                                                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">  </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">&quot;name&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">: </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&quot;rich-rst&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">,</span>                                                    <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">  </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">&quot;version&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">: </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&quot;1.0.0&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">,</span>                                                    <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">  </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">&quot;description&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">: </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&quot;RST renderer for Rich&quot;</span>                                 <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">}</span>                                                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

code-block: YAML
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: yaml

      name: rich-rst
      dependencies:
        - rich>=10.0
        - docutils>=0.17

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── yaml ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">name</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">: </span><span style="background-color: #282a36">rich-rst</span>                                                           <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">dependencies</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">:</span>                                                            <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">  </span><span style="background-color: #282a36">-</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="background-color: #282a36">rich&gt;=10.0</span>                                                           <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">  </span><span style="background-color: #282a36">-</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="background-color: #282a36">docutils&gt;=0.17</span>                                                       <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

sourcecode alias
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sourcecode:: javascript

      const greet = (name) => `Hello, ${name}!`;
      console.log(greet('World'));

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────────────────── javascript ───────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">const</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> greet </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> (name) =&gt; </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">`Hello, ${</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">name</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">}!`</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">;</span>                               <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">console.log(greet(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&#x27;World&#x27;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">));</span>                                             <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

code alias (no language)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code::

      plain text block
      no syntax highlighting

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── text (default) ─────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">plain text block</span>                                                         <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">no syntax highlighting</span>                                                   <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

productionlist directive
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. productionlist::

      statement  : expression NEWLINE
      expression : term ('+' term)*
      term       : factor ('*' factor)*

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── text ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">statement  : expression NEWLINE</span>                                          <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">expression : term (&#x27;+&#x27; term)*</span>                                            <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">term       : factor (&#x27;*&#x27; factor)*</span>                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Admonitions
-----------

note
~~~~

.. code-block:: rst

   .. note::

      This is a note admonition.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╭───────────────────────────────── Note:  ─────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This is a note admonition.</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                               │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

warning
~~~~~~~

.. code-block:: rst

   .. warning::

      This is a warning.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">╭─────────────────────────────── Warning:  ────────────────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This is a warning.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                       │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">│                                                                          │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

tip
~~~

.. code-block:: rst

   .. tip::

      This is a tip.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">╭───────────────────────────────── Tip:  ──────────────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This is a tip.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                           │</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">│                                                                          │</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

important
~~~~~~~~~

.. code-block:: rst

   .. important::

      This is important.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭────────────────────────────── IMPORTANT:  ───────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This is important.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                                       │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

hint
~~~~

.. code-block:: rst

   .. hint::

      This is a hint.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭───────────────────────────────── Hint:  ─────────────────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">This is a hint.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">                                                          │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│                                                                          │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

attention
~~~~~~~~~

.. code-block:: rst

   .. attention::

      Pay attention to this.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold">╭────────────────────────────── Attention:  ───────────────────────────────╮</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Pay attention to this.</span><span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold">                                                   │</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold">│                                                                          │</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

caution
~~~~~~~

.. code-block:: rst

   .. caution::

      Exercise caution here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff5555; text-decoration-color: #ff5555">╭─────────────────────────────── Caution:  ────────────────────────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Exercise caution here.</span><span style="color: #ff5555; text-decoration-color: #ff5555">                                                   │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">│                                                                          │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

danger
~~~~~~

.. code-block:: rst

   .. danger::

      Danger! Proceed carefully.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold">╭──────────────────────────────── DANGER:  ────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Danger! Proceed carefully.</span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold">                                               │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

error
~~~~~

.. code-block:: rst

   .. error::

      An error occurred.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">╭──────────────────────────────── ERROR:  ─────────────────────────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">An error occurred.</span><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">                                                       │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">│                                                                          │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Generic admonition with custom title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. admonition:: Did you know?

      rich-rst supports 79 RST elements.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╭───────────────────────────── Did you know? ──────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">rich-rst supports 79 RST elements.</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                       │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Admonition with nested content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. note::

      Notes can contain **bold**, *italic*, and ``code``.

      They can also contain lists:

      - item one
      - item two

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╭───────────────────────────────── Note:  ─────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Notes can contain bold, </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold; font-style: italic">italic</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">, and </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-weight: bold">code</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">.</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">They can also contain lists:</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                             │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">item one</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                                              │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">item two</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                                              │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Tables
------

Simple table
~~~~~~~~~~~~

.. code-block:: rst

   =====  =====  ======
   Col A  Col B  Col C
   =====  =====  ======
   1      2      3
   4      5      6
   =====  =====  ======

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">┏━━━━━━━┳━━━━━━━┳━━━━━━━┓
   ┃<span style="font-weight: bold"> Col A </span>┃<span style="font-weight: bold"> Col B </span>┃<span style="font-weight: bold"> Col C </span>┃
   ┡━━━━━━━╇━━━━━━━╇━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">1    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">2    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">3    </span> │
   ├───────┼───────┼───────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">4    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">5    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">6    </span> │
   └───────┴───────┴───────┘
   </code></pre>
   </div>

Grid table
~~~~~~~~~~

.. code-block:: rst

   +----------+----------+----------+
   | Header 1 | Header 2 | Header 3 |
   +==========+==========+==========+
   | row 1    | data     | more     |
   +----------+----------+----------+
   | row 2    | data     | more     |
   +----------+----------+----------+

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
   ┃<span style="font-weight: bold"> Header 1 </span>┃<span style="font-weight: bold"> Header 2 </span>┃<span style="font-weight: bold"> Header 3 </span>┃
   ┡━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">row 1   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">data    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">more    </span> │
   ├──────────┼──────────┼──────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">row 2   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">data    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">more    </span> │
   └──────────┴──────────┴──────────┘
   </code></pre>
   </div>

list-table directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

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
        - 1k+

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-style: italic">          Comparison           </span>
   ┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
   ┃<span style="font-weight: bold"> Library  </span>┃<span style="font-weight: bold"> Language </span>┃<span style="font-weight: bold"> Stars </span>┃
   ┡━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">rich    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Python  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">50k+ </span> │
   ├──────────┼──────────┼───────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">rich-rst</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Python  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">1k+  </span> │
   └──────────┴──────────┴───────┘
   </code></pre>
   </div>

csv-table directive
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. csv-table:: Data
      :header: "Name", "Value", "Unit"
      :widths: 20, 20, 20

      "Speed", "299 792 458", "m/s"
      "Charge", "1.602e-19", "C"
      "Mass", "9.109e-31", "kg" 

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-style: italic">             Data              </span>
   ┏━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━┓
   ┃<span style="font-weight: bold"> Name   </span>┃<span style="font-weight: bold"> Value       </span>┃<span style="font-weight: bold"> Unit </span>┃
   ┡━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Speed </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">299 792 458</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">m/s </span> │
   ├────────┼─────────────┼──────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Charge</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">1.602e-19  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">C   </span> │
   ├────────┼─────────────┼──────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Mass  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">9.109e-31  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">kg  </span> │
   └────────┴─────────────┴──────┘
   </code></pre>
   </div>

Footnotes and Citations
-----------------------

Manual footnote
~~~~~~~~~~~~~~~

.. code-block:: rst

   See the footnote [1]_ for details.

   .. [1] This is the footnote text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See the footnote </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for details.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1                                                                        <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> This is the footnote text.                                               <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Auto-numbered footnote
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   First reference [#]_.
   Second reference [#]_.

   .. [#] First auto footnote.
   .. [#] Second auto footnote.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">First reference </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">. Second reference </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">[2]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1                                                                        <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> First auto footnote.                                                     <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 2                                                                        <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> Second auto footnote.                                                    <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Named auto footnote
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See [#note]_ for details.

   .. [#note] The named auto footnote.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for details.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1                                                                        <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> The named auto footnote.                                                 <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Symbol footnote
~~~~~~~~~~~~~~~

.. code-block:: rst

   Marked with a symbol [*]_.

   .. [*] Symbol footnote text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Marked with a symbol </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">[*]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> *                                                                        <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> Symbol footnote text.                                                    <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Citation
~~~~~~~~

.. code-block:: rst

   As described in [Doe2023]_.

   .. [Doe2023] John Doe. *Python Patterns*. 2023.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">As described in </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc; background-color: #282a36">Doe2023</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>

   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">╭──────────────────────────────── citation ────────────────────────────────╮</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> Doe2023                                                                  <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                                                          <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> John Doe. Python Patterns. 2023.                                         <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Hyperlinks and Targets
----------------------

Standalone hyperlink
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Visit https://python.org for more.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Visit </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://python.org">https://python.org</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for more.</span>
   </code></pre>
   </div>

External hyperlink (named)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Read the `Rich documentation`_.

   .. _Rich documentation: https://rich.readthedocs.io

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Read the </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://rich.readthedocs.io">Rich documentation</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

Internal cross-reference (indirect target)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Jump to `Target Section`_.

   Target Section
   ~~~~~~~~~~~~~~

   Content here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Jump to </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline">Target Section</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>

   <span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                              Target Section                              ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Content here.</span>
   </code></pre>
   </div>

Anonymous hyperlink
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See `this page <https://example.com>`__ for details.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://example.com">this page</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for details.</span>
   </code></pre>
   </div>

Substitutions
-------------

Text substitution
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   |project| is written in Python.

   .. |project| replace:: rich-rst

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">rich-rst is written in Python.</span>
   </code></pre>
   </div>

Date substitution
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Generated on |today|.

   .. |today| date:: %Y-%m-%d

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Generated on 2026-04-04.</span>
   </code></pre>
   </div>

Unicode substitution
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Copyright |copy| 2024 The Authors.

   .. |copy| unicode:: U+00A9 .. copyright sign

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Copyright © 2024 The Authors.</span>
   </code></pre>
   </div>

Image substitution
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Click the |logo| icon.

   .. |logo| image:: https://example.com/logo.png
      :alt: Logo

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Click the </span>🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">Logo</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> icon.</span>
   </code></pre>
   </div>

Images and Figures
------------------

image directive
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. image:: https://example.com/photo.png
      :alt: A photo
      :width: 400px

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">A photo</a></span>
   </code></pre>
   </div>

figure directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. figure:: https://example.com/chart.png
      :alt: A chart
      :width: 600px

      Figure caption goes here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9">╭─ Figure caption goes here. ─╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> 🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">A chart</a></span>                  <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╰─────────────────────────────╯</span>
   </code></pre>
   </div>

figure with legend
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. figure:: https://example.com/diagram.png
      :alt: Diagram

      Caption text.

      Legend text with more details about the figure.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9">╭─ Caption text. ─╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> 🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">Diagram</a></span>      <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╰─ Legend text wi─╯</span>
   </code></pre>
   </div>

Document Structure Directives
-----------------------------

topic directive
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. topic:: Interesting Fact

      This is the topic body.
      It can contain any body elements.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╭──────────────────────────── Interesting Fact ────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This is the topic body. It can contain any body elements.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│                                                                          │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

sidebar directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sidebar:: Note

      :Subtitle: Side note

      Sidebar text goes here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">╭──────────── Note ────────────╮
   │ ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━┓ │
   │ ┃<span style="font-weight: bold"> Field Name </span>┃<span style="font-weight: bold"> Field Value </span>┃ │
   │ ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━┩ │
   │ │ <span style="font-weight: bold">Subtitle  </span> │ Side note   │ │
   │ └────────────┴─────────────┘ │
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Sidebar text goes here.</span>      │
   │                              │
   ╰──────────────────────────────╯
   </code></pre>
   </div>

rubric directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. rubric:: An Unnumbered Heading

   Following paragraph.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #909194; text-decoration-color: #909194; font-style: italic">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color: #909194; text-decoration-color: #909194; font-style: italic">│                          An Unnumbered Heading                           │</span>
   <span style="color: #909194; text-decoration-color: #909194; font-style: italic">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Following paragraph.</span>
   </code></pre>
   </div>

contents directive (table of contents)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. contents:: Table of Contents
      :depth: 2

   Section A
   ---------

   Content A.

   Section B
   ---------

   Content B.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">.. contents:: Table of Contents    :depth: 2 <span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                                Section A                                 ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Content A.</span>

   <span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                                Section B                                 ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Content B.</span>
   </code></pre>
   </div>

sectnum directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sectnum::

   Overview
   --------

   Details
   -------

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">.. sectnum:: <span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                                 Overview                                 ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="font-weight: bold">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="font-weight: bold">║                                 Details                                  ║</span>
   <span style="font-weight: bold">╚══════════════════════════════════════════════════════════════════════════╝</span>
   </code></pre>
   </div>

header directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. header:: My Document Header

   Main content.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">.. header:: My Document Header <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Main content.</span>
   </code></pre>
   </div>

footer directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Main content.

   .. footer:: Page |page|

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Main content.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.. footer:: Page |page|</span>
   </code></pre>
   </div>

centered directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. centered:: IMPORTANT NOTICE

   Body text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">                              <span style="font-weight: bold">IMPORTANT NOTICE</span>                              
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Body text.</span>
   </code></pre>
   </div>

Math
----

Inline math role
~~~~~~~~~~~~~~~~

.. code-block:: rst

   The Pythagorean theorem: :math:`a^2 + b^2 = c^2`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">The Pythagorean theorem: </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-style: italic">a^2 + b^2 = c^2</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">.</span>
   </code></pre>
   </div>

math directive (display)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. math::

      \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── math ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> ∫_-∞^∞ e^-x^2 dx = √(π)                                                  <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

math directive (labeled)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. math:: E = mc^2
      :label: einstein

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">.. math:: E = mc^2    :label: einstein
   </code></pre>
   </div>

Document Info (docinfo)
-----------------------

Standard docinfo fields
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   My Report
   =========

   :Author: Jane Smith
   :Date: 2024-01-15
   :Version: 1.0
   :Status: Draft
   :Copyright: 2024 Jane Smith
   :Organization: ACME Corp

   Body of the document.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">                                 <span style="font-style: italic">My Report</span>                                  

   ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
   ┃<span style="font-weight: bold"> Field Name   </span>┃<span style="font-weight: bold"> Field Value     </span>┃
   ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
   │ <span style="font-weight: bold">Author      </span> │ Jane Smith      │
   ├──────────────┼─────────────────┤
   │ <span style="font-weight: bold">Date        </span> │ 2024-01-15      │
   ├──────────────┼─────────────────┤
   │ <span style="font-weight: bold">Version     </span> │ 1.0             │
   ├──────────────┼─────────────────┤
   │ <span style="font-weight: bold">Status      </span> │ Draft           │
   ├──────────────┼─────────────────┤
   │ <span style="font-weight: bold">Copyright   </span> │ 2024 Jane Smith │
   ├──────────────┼─────────────────┤
   │ <span style="font-weight: bold">Organization</span> │ ACME Corp       │
   └──────────────┴─────────────────┘
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Body of the document.</span>
   </code></pre>
   </div>

Authors list
~~~~~~~~~~~~

.. code-block:: rst

   :Authors: - Alice
             - Bob
             - Carol

   Body text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">┏━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
   ┃<span style="font-weight: bold"> Field Name </span>┃<span style="font-weight: bold"> Field Value </span>┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
   │ <span style="font-weight: bold">Author    </span> │ Alice       │
   ├────────────┼─────────────┤
   │ <span style="font-weight: bold">Author    </span> │ Bob         │
   ├────────────┼─────────────┤
   │ <span style="font-weight: bold">Author    </span> │ Carol       │
   └────────────┴─────────────┘
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Body text.</span>
   </code></pre>
   </div>

Comments
--------

RST comment (invisible)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Before comment.

   .. This is an RST comment and should not appear in output.

   After comment.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Before comment.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">After comment.</span>
   </code></pre>
   </div>

Raw Directive
-------------

raw html directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. raw:: html

      <strong>Bold via raw HTML</strong>

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────────────── stripped raw html ────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Bold via raw HTML</span>                                                        <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

raw latex directive
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. raw:: latex

      \textbf{Bold via LaTeX}

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────────────────── raw latex ────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">\textbf</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">{</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Bold via LaTeX</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">}</span>                                                  <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </code></pre>
   </div>

Sphinx Version Directives
-------------------------

versionadded
~~~~~~~~~~~~

.. code-block:: rst

   .. versionadded:: 2.1

      This feature was added in version 2.1.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">╭─────────────────────────── New in version 2.1 ───────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">This feature was added in version 2.1.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                   │</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">│                                                                          │</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

versionchanged
~~~~~~~~~~~~~~

.. code-block:: rst

   .. versionchanged:: 3.0

      The API changed in version 3.0.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╭───────────────────────── Changed in version 3.0 ─────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">The API changed in version 3.0.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                          │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│                                                                          │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

deprecated
~~~~~~~~~~

.. code-block:: rst

   .. deprecated:: 1.5

      Use the new API instead.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">╭────────────────────── Deprecated since version 1.5 ──────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Use the new API instead.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                 │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">│                                                                          │</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

deprecated-removed
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. deprecated-removed:: 1.5 2.0

      Removed in 2.0. Use the new API.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">╭───────────── Deprecated since version 1.5 (removed in 2.0) ──────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Removed in 2.0. Use the new API.</span><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">                                         │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">│                                                                          │</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Sphinx Cross-Reference Roles
----------------------------

:func: role
~~~~~~~~~~~

.. code-block:: rst

   Call :func:`os.path.join` to join paths.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Call </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.path.join</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to join paths.</span>
   </code></pre>
   </div>

:class: role
~~~~~~~~~~~~

.. code-block:: rst

   Use :class:`pathlib.Path` for path handling.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">pathlib.Path</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for path handling.</span>
   </code></pre>
   </div>

:meth: role
~~~~~~~~~~~

.. code-block:: rst

   Call :meth:`str.upper` to uppercase a string.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Call </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">str.upper</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to uppercase a string.</span>
   </code></pre>
   </div>

:attr: role
~~~~~~~~~~~

.. code-block:: rst

   Access :attr:`os.sep` for the path separator.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Access </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.sep</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for the path separator.</span>
   </code></pre>
   </div>

:mod: role
~~~~~~~~~~

.. code-block:: rst

   The :mod:`os.path` module provides path utilities.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">The </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.path</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> module provides path utilities.</span>
   </code></pre>
   </div>

:exc: role
~~~~~~~~~~

.. code-block:: rst

   Raises :exc:`ValueError` when the input is invalid.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Raises </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">ValueError</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> when the input is invalid.</span>
   </code></pre>
   </div>

:obj: role
~~~~~~~~~~

.. code-block:: rst

   Set :obj:`sys.path` to control module lookup.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Set </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.path</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to control module lookup.</span>
   </code></pre>
   </div>

:data: role
~~~~~~~~~~~

.. code-block:: rst

   Read :data:`sys.version` for the Python version.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Read </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.version</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for the Python version.</span>
   </code></pre>
   </div>

:const: role
~~~~~~~~~~~~

.. code-block:: rst

   The value of :const:`math.pi` is approximately 3.14.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">The value of </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">math.pi</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> is approximately 3.14.</span>
   </code></pre>
   </div>

:term: role
~~~~~~~~~~~

.. code-block:: rst

   A :term:`decorator` wraps another function.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">A </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">decorator</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> wraps another function.</span>
   </code></pre>
   </div>

:ref: role (cross-reference)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :ref:`some-label` for details.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">See </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">some-label</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for details.</span>
   </code></pre>
   </div>

:doc: role
~~~~~~~~~~

.. code-block:: rst

   Refer to :doc:`installation` for setup instructions.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Refer to </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">installation</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for setup instructions.</span>
   </code></pre>
   </div>

:envvar: role
~~~~~~~~~~~~~

.. code-block:: rst

   Set :envvar:`PYTHONPATH` before running.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Set </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">PYTHONPATH</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> before running.</span>
   </code></pre>
   </div>

Python Domain Directives
------------------------

py:function
~~~~~~~~~~~

.. code-block:: rst

   .. py:function:: greet(name: str) -> str

      Return a greeting for *name*.

      :param name: The name to greet.
      :type name: str
      :returns: A greeting string.
      :rtype: str

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭────────────────────────  greet(name: str) -&gt; str ────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Return a greeting for </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold; font-style: italic">name</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                              │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┃ Field Name ┃ Field Value        ┃                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ param name │ The name to greet. │                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ├────────────┼────────────────────┤                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ type name  │ str                │                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ├────────────┼────────────────────┤                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ returns    │ A greeting string. │                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ├────────────┼────────────────────┤                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ rtype      │ str                │                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ └────────────┴────────────────────┘                                      │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:class
~~~~~~~~

.. code-block:: rst

   .. py:class:: MyClass(value)

      A simple example class.

      :param value: Initial value.
      :type value: int

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭────────────────────────────  MyClass(value) ─────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">A simple example class.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                                  │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┃ Field Name  ┃ Field Value    ┃                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ param value │ Initial value. │                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ ├─────────────┼────────────────┤                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ │ type value  │ int            │                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ └─────────────┴────────────────┘                                         │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:method
~~~~~~~~~

.. code-block:: rst

   .. py:method:: MyClass.process(data)

      Process the given *data*.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭─────────────────────────  MyClass.process(data) ─────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Process the given </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold; font-style: italic">data</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                                  │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:attribute
~~~~~~~~~~~~

.. code-block:: rst

   .. py:attribute:: MyClass.value
      :type: int

      The current value.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭─────────────────────────────  MyClass.value ─────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">The current value.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                                       │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:data
~~~~~~~

.. code-block:: rst

   .. py:data:: MAX_RETRIES
      :value: 3

      Maximum number of retry attempts.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭──────────────────────────────  MAX_RETRIES ──────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Maximum number of retry attempts.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                        │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:exception
~~~~~~~~~~~~

.. code-block:: rst

   .. py:exception:: MyError

      Raised when something goes wrong.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭────────────────────────────────  MyError ────────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Raised when something goes wrong.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                        │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:module
~~~~~~~~~

.. code-block:: rst

   .. py:module:: mypackage.core

      Core functionality for mypackage.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭────────────────────────────  mypackage.core ─────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Core functionality for mypackage.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                        │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

py:decorator
~~~~~~~~~~~~

.. code-block:: rst

   .. py:decorator:: cached(func)

      Cache the return value of *func*.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╭─────────────────────────────  cached(func) ──────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">Cache the return value of </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold; font-style: italic">func</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">│                                                                          │</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

See Also
--------

seealso directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. seealso::

      :func:`os.path.join`, :class:`pathlib.Path`

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╭──────────────────────────────── See Also ────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-weight: bold">os.path.join</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-weight: bold">pathlib.Path</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                               │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

seealso with inline argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. seealso:: :mod:`json` for serialization.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╭──────────────────────────────── See Also ────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36; font-weight: bold">:mod:`json` for serialization.</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">                                           │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">│                                                                          │</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Toctree (Sphinx)
----------------

toctree directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Contents

      installation
      usage
      api

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╭──────────────────────────────── Contents ────────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • installation</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                          │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • usage</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                                 │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">│ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • api</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                                   │</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Glossary
--------

glossary directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. glossary::

      RST
          reStructuredText — a lightweight markup language.

      Sphinx
          A documentation generator for Python projects.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-weight: bold">╭──────────────────────────────── Glossary ────────────────────────────────╮</span>
   <span style="font-weight: bold">│ RST                                                                      │</span>
   <span style="font-weight: bold">│     reStructuredText — a lightweight markup language.                    │</span>
   <span style="font-weight: bold">│                                                                          │</span>
   <span style="font-weight: bold">│ Sphinx                                                                   │</span>
   <span style="font-weight: bold">│     A documentation generator for Python projects.                       │</span>
   <span style="font-weight: bold">│                                                                          │</span>
   <span style="font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

glossary (sorted)
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. glossary::
      :sorted:

      Zebra
          A striped animal.

      Aardvark
          An ant-eating mammal.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="font-weight: bold">╭──────────────────────────────── Glossary ────────────────────────────────╮</span>
   <span style="font-weight: bold">│ Zebra                                                                    │</span>
   <span style="font-weight: bold">│     A striped animal.                                                    │</span>
   <span style="font-weight: bold">│                                                                          │</span>
   <span style="font-weight: bold">│ Aardvark                                                                 │</span>
   <span style="font-weight: bold">│     An ant-eating mammal.                                                │</span>
   <span style="font-weight: bold">│                                                                          │</span>
   <span style="font-weight: bold">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </code></pre>
   </div>

Mixed Sphinx Roles in Prose
---------------------------

Mixed roles in a paragraph
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Use :func:`json.dumps` or :func:`json.loads` to serialize data.
   The :class:`dict` type maps :class:`str` keys to values.
   See :pep:`484` for type hints and :pep:`526` for variable annotations.
   Press :kbd:`Ctrl+D` or call :func:`exit` to quit the REPL.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">json.dumps</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> or </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">json.loads</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to serialize data. The </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">dict</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> type maps </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">str</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> keys to values. See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0484/">PEP 484</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for type hints and </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0526/">PEP 526</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> for variable annotations. Press </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">Ctrl+D</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> or call </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">exit</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> to quit the REPL.</span>
   </code></pre>
   </div>


----

*This page was generated automatically.  Run* ``python tools/generate_demo_page.py``
*from the repository root to refresh it.*
