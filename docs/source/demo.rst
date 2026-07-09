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

   *italicised text*

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">italicised text</span>
   </span></pre>
   </div>

Strong (bold)
~~~~~~~~~~~~~

.. code-block:: rst

   **bold text**

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-weight: bold">bold text</span>
   </span></pre>
   </div>

Inline literal (code)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Use ``print()`` to display output.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">print()</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to display output.</span>
   </span></pre>
   </div>

Hyperlink (external)
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Visit `Python <https://www.python.org>`_ for more.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Visit </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://www.python.org">Python</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for more.</span>
   </span></pre>
   </div>

Anonymous hyperlink
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See `Rich docs <https://rich.readthedocs.io>`__ for styling.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://rich.readthedocs.io">Rich docs</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for styling.</span>
   </span></pre>
   </div>

Title reference
~~~~~~~~~~~~~~~

.. code-block:: rst

   Read `The Zen of Python` for inspiration.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Read </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">The Zen of Python</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for inspiration.</span>
   </span></pre>
   </div>

Subscript role
~~~~~~~~~~~~~~

.. code-block:: rst

   H\ :sub:`2`\ O is water.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">H₂O is water.</span>
   </span></pre>
   </div>

Superscript role
~~~~~~~~~~~~~~~~

.. code-block:: rst

   E = mc\ :sup:`2`

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">E = mc²</span>
   </span></pre>
   </div>

Abbreviation role
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   :abbr:`RST (reStructuredText)` is a markup language.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;text-decoration: underline">RST (reStructuredText)</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> is a markup language.</span>
   </span></pre>
   </div>

Keyboard role
~~~~~~~~~~~~~

.. code-block:: rst

   Press :kbd:`Ctrl+C` to copy.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Press </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">Ctrl+C</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to copy.</span>
   </span></pre>
   </div>

GUI label role
~~~~~~~~~~~~~~

.. code-block:: rst

   Click :guilabel:`OK` to confirm.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Click </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">OK</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to confirm.</span>
   </span></pre>
   </div>

Menu selection role
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Go to :menuselection:`File --> Save As`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Go to </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">File ▶ Save As</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

File role
~~~~~~~~~

.. code-block:: rst

   Edit :file:`/etc/hosts` with sudo.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Edit </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">/etc/hosts</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> with sudo.</span>
   </span></pre>
   </div>

Sample (samp) role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Type :samp:`ping {host}` in the terminal.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Type </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">ping host</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> in the terminal.</span>
   </span></pre>
   </div>

Command role
~~~~~~~~~~~~

.. code-block:: rst

   Run :command:`python -m pytest`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Run </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-weight: bold">python -m pytest</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

Program role
~~~~~~~~~~~~

.. code-block:: rst

   :program:`git` is a distributed version control system.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-weight: bold">git</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> is a distributed version control system.</span>
   </span></pre>
   </div>

All inline styles combined
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   *Italic*, **bold**, ``literal``, :kbd:`Ctrl+C`,
   :guilabel:`OK`, :menuselection:`File --> Open`,
   :file:`~/.bashrc`, :command:`ls -la`,
   and :sup:`superscript`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">Italic</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color:#f8f8f2;font-weight: bold; font-style: italic">bold</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-style: italic">literal</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-style: italic">Ctrl+C</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-style: italic">OK</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-style: italic">File ▶ Open</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212; font-style: italic">~/.bashrc</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color:#f8f8f2;font-weight: bold; font-style: italic">ls -la</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, and </span>
   <span style="color:#f8f8f2;font-style: italic">ˢᵘᵖᵉʳˢᶜʳⁱᵖᵗ</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

Inline markup in a list
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   - Use **bold** for important terms
   - Use *italic* for emphasis
   - Use ``code`` for inline code samples
   - Use :kbd:`Enter` for key presses

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-weight: bold">bold</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for important terms</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">italic</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for emphasis</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">code</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for inline code samples</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">Enter</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for key presses</span>
   </span></pre>
   </div>

PEP reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :pep:`8` for Python style guidelines.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0008/">PEP 8</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for Python style guidelines.</span>
   </span></pre>
   </div>

RFC reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   HTTP is described in :rfc:`2616`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">HTTP is described in </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://datatracker.ietf.org/doc/html/rfc2616">RFC 2616</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

Definition (dfn) role
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   A :dfn:`docstring` is a string literal that documents a Python object.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">A </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">docstring</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> is a string literal that documents a Python object.</span>
   </span></pre>
   </div>

CVE reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   This vulnerability is tracked as :cve:`2024-3094`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This vulnerability is tracked as </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://www.cve.org/CVERecord?id=CVE-2024-3094">CVE-2024-3094</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

CWE reference role
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   This bug is categorized under :cwe:`79`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This bug is categorized under </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://cwe.mitre.org/data/definitions/79.html">CWE-79</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

PyPI project reference role
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Install the package from :pypi:`requests`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Install the package from </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://pypi.org/project/requests/">requests</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

Math role (inline)
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   The area of a circle is :math:`\pi r^2`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The area of a circle is </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">π r^2</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This is a plain paragraph.  Paragraphs are separated by blank lines.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">A second paragraph follows here.</span>
   </span></pre>
   </div>

Section headings (all 6 levels)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Level 1 Title
   =============
   Some body text under level 1.

   Level 2 Title
   -------------
   Some body text under level 2.

   Level 3 Title
   ~~~~~~~~~~~~~
   Some body text under level 3.

   Level 4 Title
   ^^^^^^^^^^^^^
   Some body text under level 4.

   Level 5 Title
   """""""""""""
   Some body text under level 5.

   Level 6 Title
   '''''''''''''
   Some body text under level 6.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="color:#f8f8f2">║</span><span style="color:#f8f8f2;font-weight: bold">                              Level 1 Title                               </span><span style="color:#f8f8f2">║</span>
   <span style="color:#f8f8f2">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 1.</span>

   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                              Level 2 Title                               </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 2.</span>

                                  <span style="color:#f8f8f2;font-weight: bold; text-decoration: underline">Level 3 Title</span>                                

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 3.</span>

                                  <span style="color:#f8f8f2;font-weight: bold">Level 4 Title</span>                                

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 4.</span>

                                  <span style="color:#f8f8f2;text-decoration: underline">Level 5 Title</span>                                

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 5.</span>

                                  <span style="color:#f8f8f2;font-style: italic">Level 6 Title</span>                                

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Some body text under level 6.</span>
   </span></pre>
   </div>

Section with overline decoration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   ##################
   Part-level heading
   ##################

   Body text below the overlined heading.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="color:#f8f8f2">║</span><span style="color:#f8f8f2;font-weight: bold">                            Part-level heading                            </span><span style="color:#f8f8f2">║</span>
   <span style="color:#f8f8f2">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Body text below the overlined heading.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="color:#f8f8f2">║</span><span style="color:#f8f8f2;font-weight: bold">                               My Document                                </span><span style="color:#f8f8f2">║</span>
   <span style="color:#f8f8f2">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                             A subtitle here                              </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Body text.</span>
   </span></pre>
   </div>

Multiple paragraphs with transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   First paragraph before the transition.

   ----

   Second paragraph after the first transition.

   ----

   Third paragraph after the second transition.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">First paragraph before the transition.</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">────────────────────────────────────────────────────────────────────────────</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Second paragraph after the first transition.</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">────────────────────────────────────────────────────────────────────────────</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Third paragraph after the second transition.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">First item</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Second item</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Third item</span>
   </span></pre>
   </div>

Bullet list (asterisk)
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   * Alpha
   * Beta
   * Gamma

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alpha</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Beta</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Gamma</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Parent item</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Child item one</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Child item two</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Another parent</span>
   </span></pre>
   </div>

Enumerated list (auto-numbered)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   #. First step
   #. Second step
   #. Third step

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 1.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">First step</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 2.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Second step</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 3.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Third step</span>
   </span></pre>
   </div>

Bullet list (plus sign)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   + One
   + Two
   + Three

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">One</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Two</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Three</span>
   </span></pre>
   </div>

Deeply nested bullet list
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   - Level 1 item A

     - Level 2 item A1

       - Level 3 item A1a
       - Level 3 item A1b

     - Level 2 item A2

   - Level 1 item B

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 1 item A</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 2 item A1</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">     ▪ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 3 item A1a</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">     ▪ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 3 item A1b</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 2 item A2</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Level 1 item B</span>
   </span></pre>
   </div>

Enumerated list (uppercase letters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   A. Alpha
   B. Beta
   C. Gamma

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> A.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alpha</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> B.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Beta</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> C.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Gamma</span>
   </span></pre>
   </div>

Enumerated list (uppercase roman numerals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   I.  Chapter One
   II.  Chapter Two
   III. Chapter Three

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> I.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Chapter One</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> II.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Chapter Two</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> III.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Chapter Three</span>
   </span></pre>
   </div>

Mixed ordered and unordered lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Steps to install:

   1. Download the package

      - Linux: ``apt install ...``
      - macOS: ``brew install ...``

   2. Run the installer
   3. Verify with ``--version``

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Steps to install:</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 1.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Download the package</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Linux: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">apt install ...</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">   ∘ </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">macOS: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">brew install ...</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 2.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Run the installer</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> 3.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Verify with </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">--version</span>
   </span></pre>
   </div>

Enumerated list (letters)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   a. Apple
   b. Banana
   c. Cherry

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> a.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Apple</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> b.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Banana</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> c.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Cherry</span>
   </span></pre>
   </div>

Enumerated list (roman numerals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   i. Item i
   ii. Item ii
   iii. Item iii

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> i.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Item i</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> ii.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Item ii</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> iii.</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Item iii</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">term
       Definition of the term.
         
   another term
       Its definition spans multiple lines.
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">term : <span style="color: #8be9fd; text-decoration-color: #8be9fd">string</span>
       <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">A string-typed term.</span>


   count : <span style="color: #8be9fd; text-decoration-color: #8be9fd">int</span>
       <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">An integer count.</span>
   </span></pre>
   </div>

Field list
~~~~~~~~~~

.. code-block:: rst

   :Name: John Doe
   :Email: john@example.com
   :Role: Developer

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-weight: bold">      Document Information       </span>
   ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Field Name </span>┃<span style="color:#f8f8f2;font-weight: bold"> Field Value      </span>┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
   │ <span style="color:#f8f8f2;font-weight: bold">Name      </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">John Doe        </span> │
   ├────────────┼──────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Email     </span> │ <span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="mailto:john@example.com">john@example.com</a></span> │
   ├────────────┼──────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Role      </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Developer       </span> │
   └────────────┴──────────────────┘
   </span></pre>
   </div>

Option list
~~~~~~~~~~~

.. code-block:: rst

   -v, --verbose    Enable verbose output.
   -o FILE          Write output to FILE.
   --help           Show this help message.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">-v, --verbose, 
       Enable verbose output.
   -o FILE
       Write output to FILE.
   --help
       Show this help message.
   </span></pre>
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
      * Eta
      * Theta
      * Iota

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alpha</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Beta   </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Gamma</span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Delta</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Epsilon</span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Zeta </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Eta  </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Theta  </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Iota </span> 
    <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">       </span>  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">     </span> 
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Normal paragraph.</span>

   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">This is an indented block quote.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — Attribution</span>
   </span></pre>
   </div>

Line block
~~~~~~~~~~

.. code-block:: rst

   | The first line of a poem.
   | The second line continues.
   |   An indented third line.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">The first line of a poem.
   The second line continues.
       An indented third line.
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── doctest block ──────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">&gt;&gt;&gt; </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&quot;Hello, world!&quot;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span><span style="color:#f8f8f2;background-color: #282a36">                                              </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">Hello, world!</span><span style="color:#f8f8f2;background-color: #282a36">                                                           </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">&gt;&gt;&gt; </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">+</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                               </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">2</span><span style="color:#f8f8f2;background-color: #282a36">                                                                       </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Literal block (indented)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Example code::

       def greet(name):
           print(f"Hello, {name}!")

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Example code:</span>
   <span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── text (default) ─────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">def greet(name):</span><span style="color:#f8f8f2;background-color: #282a36">                                                        </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    print(f&quot;Hello, {name}!&quot;)</span><span style="color:#f8f8f2;background-color: #282a36">                                            </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Compound directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. compound::
      :class: custom-compound-class

      The first sentence of a paragraph.

      The second paragraph of the compound block,
      rendered as a single logical paragraph.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The first sentence of a paragraph.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The second paragraph of the compound block, rendered as a single logical </span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">paragraph.</span>
   </span></pre>
   </div>

Parsed literal block
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. parsed-literal::
      :class: custom-parsed-literal-class
      :name: custom-parsed-literal-name

      **Bold** and *italic* inside a literal block.
      Also ``code`` here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">┌────────────── parsed-literal — custom-parsed-literal-name ───────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">│</span><span style="color:#f8f8f2;background-color: #282a36"> </span><span style="color:#f8f8f2;background-color: #282a36; font-weight: bold">Bold</span><span style="color:#f8f8f2;background-color: #282a36"> and </span><span style="color:#f8f8f2;background-color: #282a36; font-style: italic">italic</span><span style="color:#f8f8f2;background-color: #282a36"> inside a literal block.                                  </span><span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">│</span>
   <span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">│</span><span style="color:#f8f8f2;background-color: #282a36"> Also </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">code</span><span style="color:#f8f8f2;background-color: #282a36"> here.                                                          </span><span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">│</span>
   <span style="color: #949494; text-decoration-color: #949494; background-color: #282a36">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Epigraph directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. epigraph::
      :class: custom-epigraph-class

      No man is an island,
      entire of itself.

      -- John Donne

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">No man is an island, entire of itself.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — John Donne</span>
   </span></pre>
   </div>

Highlights directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. highlights::
      :class: custom-highlights-class

      Key takeaways:

      - Keep it simple.
      - Document everything.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">Key takeaways:</span>
   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌</span>
   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold"> • </span><span style="color: #ffffff; text-decoration-color: #ffffff">Keep it simple.</span>
   <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Document everything.</span>
   </span></pre>
   </div>

Pull-quote directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pull-quote::
      :class: custom-pull-quote-class

      The best way to predict the future
      is to invent it.

      -- Alan Kay

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">The best way to predict the future is to invent it.</span>

   <span style="color: #e4e4e4; text-decoration-color: #e4e4e4">  — Alan Kay</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b; background-color: #282a36">factorial</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(n):</span><span style="color:#f8f8f2;background-color: #282a36">                                                       </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">if</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">==</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">0</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">:</span><span style="color:#f8f8f2;background-color: #282a36">                                                          </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">        </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                        </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">*</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> factorial(n </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">-</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span><span style="color:#f8f8f2;background-color: #282a36">                                         </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">1 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                               </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">2 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">y </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">2</span><span style="color:#f8f8f2;background-color: #282a36">                                                               </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">3 </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">+</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> y)</span><span style="color:#f8f8f2;background-color: #282a36">                                                        </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code-block with lineno-start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :linenos:
      :lineno-start: 10

      x = 1
      y = 2

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">10 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                              </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">11 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">y </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">2</span><span style="color:#f8f8f2;background-color: #282a36">                                                              </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code-block with emphasize-lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :emphasize-lines: 3,5

      def some_function():
          interesting = False
          print('This line is highlighted.')
          print('This one is not...')
          print('...but this one is.')

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">1 </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b; background-color: #282a36">some_function</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">():</span><span style="color:#f8f8f2;background-color: #282a36">                                                </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">2 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    interesting </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">False</span><span style="color:#f8f8f2;background-color: #282a36">                                             </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff5555; text-decoration-color: #ff5555">❱ </span><span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">3 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&#x27;This line is highlighted.&#x27;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span><span style="color:#f8f8f2;background-color: #282a36">                              </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">4 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&#x27;This one is not...&#x27;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span><span style="color:#f8f8f2;background-color: #282a36">                                     </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff5555; text-decoration-color: #ff5555">❱ </span><span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">5 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">print</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&#x27;...but this one is.&#x27;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">)</span><span style="color:#f8f8f2;background-color: #282a36">                                    </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code-block with name
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :name: example-id

      x = 1
      y = 2

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────── python — example-id ───────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">x </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                                   </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">y </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">2</span><span style="color:#f8f8f2;background-color: #282a36">                                                                   </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code-block with dedent
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :dedent:

          def foo():
              return 1

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────────── python ─────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b; background-color: #282a36">foo</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">():</span><span style="color:#f8f8f2;background-color: #282a36">                                                              </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #ffb86c; text-decoration-color: #ffb86c; background-color: #282a36">1</span><span style="color:#f8f8f2;background-color: #282a36">                                                            </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

sourcecode alias
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sourcecode:: javascript
      :class: custom-sourcecode-class
      :name: custom-sourcecode-id
      :linenos:
      :lineno-start: 5

      const greet = (name) => `Hello, ${name}!`;
      console.log(greet('World'));

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────── javascript — custom-sourcecode-id ────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">5 </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">const</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> greet </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> (name) =&gt; </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">`Hello, ${</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">name</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">}!`</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">;</span><span style="color:#f8f8f2;background-color: #282a36">                          </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">6 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">console.log(greet(</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36">&#x27;World&#x27;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">));</span><span style="color:#f8f8f2;background-color: #282a36">                                        </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code alias (no language)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code::
      :class: custom-code-class
      :name: custom-code-id

      plain text block
      no syntax highlighting

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌──────────────────── text (default) — custom-code-id ─────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">plain text block</span><span style="color:#f8f8f2;background-color: #282a36">                                                        </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">no syntax highlighting</span><span style="color:#f8f8f2;background-color: #282a36">                                                  </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

code-block with caption
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      :linenos:
      :lineno-start: 10
      :emphasize-lines: 3
      :caption: math_utils.py
      :name: math-utils-code
      :dedent: 4
      :force:
      :class: python-utility-class

          def add(a, b):
              # This line is emphasised
              return a + b

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌──────────────────────── python — math-utils-code ────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">10 </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b; background-color: #282a36">add</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">(a, b):</span><span style="color:#f8f8f2;background-color: #282a36">                                                     </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">11 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #6272a4; text-decoration-color: #6272a4; background-color: #282a36"># This line is emphasised</span><span style="color:#f8f8f2;background-color: #282a36">                                      </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #e3e3df; text-decoration-color: #e3e3df; background-color: #282a36; font-weight: bold">  </span><span style="color: #66676e; text-decoration-color: #66676e; background-color: #282a36">12 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">    </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">return</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> a </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">+</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36"> b</span><span style="color:#f8f8f2;background-color: #282a36">                                                   </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

productionlist directive
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. productionlist:: grammar

      statement  : expression NEWLINE
      expression : term ('+' term)*
      term       : factor ('*' factor)*

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌───────────────────────────── productionlist ─────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">statement  : expression NEWLINE</span><span style="color:#f8f8f2;background-color: #282a36">                                         </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">expression : term (&#x27;+&#x27; term)*</span><span style="color:#f8f8f2;background-color: #282a36">                                           </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">term       : factor (&#x27;*&#x27; factor)*</span><span style="color:#f8f8f2;background-color: #282a36">                                       </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Admonitions
-----------

Admonitions Showcase
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. note::
      Call ``sys.exit(0)`` to terminate *successfully*,
      or ``sys.exit(1)`` for **failure**.

      Notes can contain **bold**, *italic*, and ``code``.
      They can also contain lists:

      - item one
      - item two

   .. warning::
      **Never** commit secrets to version control.
      Use environment variables or a secrets manager instead.

   .. tip::
      This is a tip.

   .. important::
      This is important.

   .. hint::
      This is a hint.

   .. attention::
      Pay attention to this.

   .. caution::
      Exercise caution here.

   .. danger::
      Danger! Proceed carefully.

   .. error::
      An error occurred.

   .. admonition:: Did you know?
      :class: custom-admonition-class
      :name: custom-admonition-id

      rich-rst supports all currently documented RST elements.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #ffffff; text-decoration-color: #ffffff">╭──────────────────────────────────</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold"> Note </span><span style="color: #ffffff; text-decoration-color: #ffffff">──────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Call </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.exit(0)</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to terminate </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">successfully</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, or </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.exit(1)</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-weight: bold">failure</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>  <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>                                                                          <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Notes can contain </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-weight: bold">bold</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">italic</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">, and </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">code</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">. They can also contain lists:</span>   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>                                                                          <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">item one</span>                                                              <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">item two</span>                                                              <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> Warning </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span> <span style="color:#f8f8f2;font-weight: bold">Never</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> commit secrets to version control. Use environment variables or a </span> <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">secrets manager instead.</span>                                                 <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╭──────────────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Tip </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">───────────────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This is a tip.</span>                                                           <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╭───────────────────────────────</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold"> IMPORTANT </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">────────────────────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This is important.</span>                                                       <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────────────────── Hint ──────────────────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This is a hint.</span>                                                          <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c">╭───────────────────────────────</span><span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c; font-weight: bold"> Attention </span><span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c">────────────────────────────────╮</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c">│</span><span style="color:#f8f8f2;background-color: #f1fa8c"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #f1fa8c">Pay attention to this.</span><span style="color:#f8f8f2;background-color: #f1fa8c">                                                   </span><span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c">│</span>
   <span style="color: #282a36; text-decoration-color: #282a36; background-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╭──────────────────────────────── Caution ─────────────────────────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Exercise caution here.</span>                                                   <span style="color: #ff5555; text-decoration-color: #ff5555">│</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555">╭─────────────────────────────────</span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555; font-weight: bold"> DANGER </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555">─────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555">│</span><span style="color:#f8f8f2;background-color: #ff5555"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #ff5555">Danger! Proceed carefully.</span><span style="color:#f8f8f2;background-color: #ff5555">                                               </span><span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff; background-color: #ff5555">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╭─────────────────────────────────</span><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold"> ERROR </span><span style="color: #ff5555; text-decoration-color: #ff5555">──────────────────────────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">An error occurred.</span>                                                       <span style="color: #ff5555; text-decoration-color: #ff5555">│</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">╭─────────────────────────────</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold"> Did you know? </span><span style="color: #ffffff; text-decoration-color: #ffffff">──────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rich-rst supports all currently documented RST elements.</span>                 <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

Tables
------

Simple table with header
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   =====  =====  ======
   Col A  Col B  Col C
   =====  =====  ======
   1      2      3
   4      5      6
   =====  =====  ======

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">┏━━━━━━━┳━━━━━━━┳━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Col A </span>┃<span style="color:#f8f8f2;font-weight: bold"> Col B </span>┃<span style="color:#f8f8f2;font-weight: bold"> Col C </span>┃
   ┡━━━━━━━╇━━━━━━━╇━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">1    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">2    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">3    </span> │
   ├───────┼───────┼───────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">4    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">5    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">6    </span> │
   └───────┴───────┴───────┘
   </span></pre>
   </div>

Grid table with row spanning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   +------------+------------+
   | Column 1   | Column 2   |
   +============+============+
   | Rows 1 & 2 | Row 1      |
   +            +------------+
   |            | Row 2      |
   +------------+------------+

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">┏━━━━━━━━━━━━┳━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Column 1</span>  <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Column 2</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Rows 1 &amp; 2</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Row 1</span>    │
   │            ├──────────┤
   │            │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Row 2</span>    │
   └────────────┴──────────┘
   </span></pre>
   </div>

Wider grid table
~~~~~~~~~~~~~~~~

.. code-block:: rst

   +--------+-------+------+---------+
   | Name   | Type  | Size | Default |
   +========+=======+======+=========+
   | width  | int   | 4    | 80      |
   +--------+-------+------+---------+
   | height | int   | 4    | 24      |
   +--------+-------+------+---------+
   | title  | str   | var  | ''      |
   +--------+-------+------+---------+

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">┏━━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Name   </span>┃<span style="color:#f8f8f2;font-weight: bold"> Type </span>┃<span style="color:#f8f8f2;font-weight: bold"> Size </span>┃<span style="color:#f8f8f2;font-weight: bold"> Default </span>┃
   ┡━━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">width </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">int </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">4   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">80     </span> │
   ├────────┼──────┼──────┼─────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">height</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">int </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">4   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">24     </span> │
   ├────────┼──────┼──────┼─────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">title </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">str </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">var </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">&#x27;&#x27;     </span> │
   └────────┴──────┴──────┴─────────┘
   </span></pre>
   </div>

list-table directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. list-table:: Comparison
      :header-rows: 1
      :stub-columns: 1
      :widths: 30 35 35
      :align: center
      :class: custom-list-table-class
      :name: custom-list-table-name

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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">          Comparison           </span>
   ┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Library  </span>┃<span style="color:#f8f8f2;font-weight: bold"> Language </span>┃<span style="color:#f8f8f2;font-weight: bold"> Stars </span>┃
   ┡━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rich    </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Python  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">50k+ </span> │
   ├──────────┼──────────┼───────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rich-rst</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Python  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">1k+  </span> │
   └──────────┴──────────┴───────┘
   </span></pre>
   </div>

CSV Table
~~~~~~~~~

.. code-block:: rst

   .. csv-table:: Data
      :header: "Name", "Value", "Unit"
      :widths: 20, 20, 20
      :delim: ,
      :quote: "
      :keepspace:
      :escape: \
      :class: custom-csv-table-class
      :name: custom-csv-table-name
      :align: center

      "Speed", "299 792 458", "m/s"
      "Charge", "1.602e-19", "C"
      "Mass", "9.109e-31", "kg" 

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">                                    Data                                    </span>
   ┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Name   </span>┃<span style="color:#f8f8f2;font-weight: bold"> &quot;Value&quot;                        </span>┃<span style="color:#f8f8f2;font-weight: bold"> &quot;Unit&quot;                         </span>┃
   ┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Speed </span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;299 792 458&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">               </span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;m/s&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">                       </span> │
   │        │                                │                                │
   ├────────┼────────────────────────────────┼────────────────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Charge</span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;1.602e-19&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">                 </span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;C&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">                         </span> │
   │        │                                │                                │
   ├────────┼────────────────────────────────┼────────────────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Mass  </span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;9.109e-31&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">                 </span> │ <span style="color: #ff79c6; text-decoration-color: #ff79c6">▌ </span><span style="color: #ffffff; text-decoration-color: #ffffff">&quot;kg&quot;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6">                        </span> │
   │        │                                │                                │
   └────────┴────────────────────────────────┴────────────────────────────────┘
   </span></pre>
   </div>

Flat Table: Basic with Stub Column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Linux Kernel Subsystems
      :header-rows: 1
      :stub-columns: 1
      :widths: 20 30 50
      :fill-cells:
      :class: custom-flat-table-class
      :name: custom-flat-table-name

      * - Subsystem
        - Maintainer
        - Description

      * - Networking
        - David S. Miller
        - TCP/IP stack and network drivers

      * - Memory Management
        - Andrew Morton
        - Virtual memory, paging, and allocators

      * - File Systems
        - Linus Torvalds
        - VFS layer and filesystem drivers

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">                          Linux Kernel Subsystems                           </span>
   ┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Subsystem         </span>┃<span style="color:#f8f8f2;font-weight: bold"> Maintainer      </span>┃<span style="color:#f8f8f2;font-weight: bold"> Description                        </span>┃
   ┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Networking       </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">David S. Miller</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">TCP/IP stack and network drivers  </span> │
   ├───────────────────┼─────────────────┼────────────────────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Memory Management</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Andrew Morton  </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Virtual memory, paging, and       </span> │
   │                   │                 │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">allocators                        </span> │
   ├───────────────────┼─────────────────┼────────────────────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">File Systems     </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Linus Torvalds </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">VFS layer and filesystem drivers  </span> │
   └───────────────────┴─────────────────┴────────────────────────────────────┘
   </span></pre>
   </div>

Flat Table: Column Span (:cspan:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Quarterly Results
      :header-rows: 1

      * - Student
        - Q1
        - Q2
        - Q3

      * - :cspan:`3` Grand total — all students, all quarters

      * - Alice
        - 90
        - 85
        - 92

      * - Bob
        - 80
        - 88
        - 76

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">             Quarterly Results              </span>
   ┏━━━━━━━━━┳━━━━┳━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Student</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q1</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q2</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q3</span>                  <span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━━━┻━━━━┻━━━━┻━━━━━━━━━━━━━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Grand total — all students, all quarters</span> │
   ├─────────┬────┬────┬──────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alice</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">90</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">85</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">92</span>                   │
   ├─────────┼────┼────┼──────────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Bob</span>     │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">80</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">88</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">76</span>                   │
   └─────────┴────┴────┴──────────────────────┘
   </span></pre>
   </div>

flat-table — wide partial column span (:cspan: > 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Regional Sales
      :header-rows: 1

      * - Region
        - Q1
        - Q2
        - Q3

      * - :cspan:`2` North + Central + South combined
        - 312

      * - North
        - 42
        - 55
        - 61

      * - Central
        - 78
        - 90
        - 83

      * - South
        - 34
        - 48
        - 55

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">              Regional Sales              </span>
   ┏━━━━━━━━━┳━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Region</span> <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q1</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q2</span>               <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Q3</span> <span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━━━┻━━━━┻━━━━━━━━━━━━━━━━━━━╇━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">North + Central + South combined</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">312</span> │
   ├─────────┬────┬───────────────────┼─────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">North</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">42</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">55</span>                │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">61</span>  │
   ├─────────┼────┼───────────────────┼─────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Central</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">78</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">90</span>                │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">83</span>  │
   ├─────────┼────┼───────────────────┼─────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">South</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">34</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">48</span>                │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">55</span>  │
   └─────────┴────┴───────────────────┴─────┘
   </span></pre>
   </div>

flat-table — row span (:rspan:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Produce Prices
      :header-rows: 1

      * - Category
        - Item
        - Price

      * - :rspan:`1` Fruit
        - Apple
        - $1.00

      * - Banana
        - $0.50

      * - :rspan:`1` Vegetable
        - Carrot
        - $0.75

      * - Broccoli
        - $1.25

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">         Produce Prices         </span>
   ┏━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Category</span> <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Item</span>    <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Price</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Fruit</span>     │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Apple</span>    │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">$1.00</span> │
   │           ├──────────┼───────┤
   │           │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Banana</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">$0.50</span> │
   ├───────────┼──────────┼───────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Vegetable</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Carrot</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">$0.75</span> │
   │           ├──────────┼───────┤
   │           │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Broccoli</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">$1.25</span> │
   └───────────┴──────────┴───────┘
   </span></pre>
   </div>

Flat Table: Combined :cspan: and :rspan:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Combined Spans
      :header-rows: 3

      * - Full-width title header

      * - :cspan:`1` header 1
        - :cspan:`1` header 2
        - :cspan:`1` header 3

      * - Sub-header 1
        - Sub-header 2
        - Sub-header 3
        - Sub-header 4
        - Sub-header 5
        - Sub-header 6

      * - :rspan:`1` :cspan:`1` Big cell spanning 2 rows and 2 column
        - :cspan:`1` Large cell spanning 2 columns
        - :cspan:`3` Large cell spanning 4 columns

      * - :rspan:`1` Tall cell spanning 2 rows
        - Cell 3
        - :rspan:`1` :cspan:`2` Big cell spanning 2 rows and 3 columns

      * - Cell 1
        - Cell 2
        - Cell 4
        - 

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">                               Combined Spans                               </span>
   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Full-width title header</span>                                                 <span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┣━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┫
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">header 1</span>             <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">header 2</span>               <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">header 3</span>              <span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┣━━━━━━━━━━━┳━━━━━━━━━━━╋━━━━━━━━━━━━┳━━━━━━━━━━━━╋━━━━━━━━━━━━┳━━━━━━━━━━━┫
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-heade</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-heade</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-header</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-header</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-header</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sub-heade</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">r 1</span>      <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">r 2</span>      <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">3</span>         <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">4</span>         <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">5</span>         <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">r 6</span>      <span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━━━━━┻━━━━━━━━━━━╇━━━━━━━━━━━━┻━━━━━━━━━━━━╇━━━━━━━━━━━━┻━━━━━━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Big cell spanning 2 </span>  │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Large cell spanning 2 </span>  │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Large cell spanning 4 </span> │
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rows and 2 column</span>     │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">columns</span>                 │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">columns</span>                │
   │                       ├────────────┬────────────┼────────────────────────┤
   │                       │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Tall cell </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Cell 3</span>     │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Big cell spanning 2 </span>   │
   │                       │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">spanning 2</span> │            │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rows and 3 columns</span>     │
   │                       │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rows</span>       │            │                        │
   ├───────────┬───────────┤            ├────────────┤                        │
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Cell 1</span>    │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Cell 2</span>    │            │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Cell 4</span>     │                        │
   └───────────┴───────────┴────────────┴────────────┴────────────────────────┘
   </span></pre>
   </div>

flat-table — single cell with :cspan: and :rspan: (2×2 block)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: 2×2 merged cell
      :header-rows: 1

      * - Task
        - Mon
        - Tue
        - Wed
        - Thu
        - Fri

      * - :cspan:`2` :rspan:`1` Planning
        - Review

      * - Deploy

      * - Others.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic">           2×2 merged cell            </span>
   ┏━━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Task</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Mon</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Tue</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Wed</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Thu</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Fri</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━┻━━━━━┻━━━━━╇━━━━━┻━━━━━┻━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Planning</span>         │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Review</span>          │
   │                  ├─────────────────┤
   │                  │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Deploy</span>          │
   ├──────────────────┴─────────────────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Others.</span>                            │
   └────────────────────────────────────┘
   </span></pre>
   </div>

flat-table — :cspan: fills merged column width without inflation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. flat-table:: Team Overview
      :header-rows: 1

      * - Name
        - Role

      * - :cspan:`1` Both columns

      * - Alice
        - Lead

      * - Bob
        - Dev

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-style: italic"> Team Overview  </span>
   ┏━━━━━━━┳━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Name</span> <span style="color:#f8f8f2;font-weight: bold"> </span>┃<span style="color:#f8f8f2;font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Role</span><span style="color:#f8f8f2;font-weight: bold"> </span>┃
   ┡━━━━━━━┻━━━━━━┩
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Both columns</span> │
   ├───────┬──────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alice</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Lead</span> │
   ├───────┼──────┤
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Bob</span>   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Dev</span>  │
   └───────┴──────┘
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">See the footnote </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for details.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1: This is the footnote text.                                            <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">First reference </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">. Second reference </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">[2]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1: First auto footnote.                                                  <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 2: Second auto footnote.                                                 <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Named auto footnote
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See [#note]_ for details.

   .. [#note] The named auto footnote.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">See </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">[1]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for details.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> 1: The named auto footnote.                                              <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Symbol footnote
~~~~~~~~~~~~~~~

.. code-block:: rst

   Marked with a symbol [*]_.

   .. [*] Symbol footnote text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Marked with a symbol </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">[*]</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> *: Symbol footnote text.                                                 <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Citation
~~~~~~~~

.. code-block:: rst

   As described in [Doe2023]_.

   .. [Doe2023] John Doe. *Python Patterns*. 2023.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">As described in </span><span style="color: #bcbcbc; text-decoration-color: #bcbcbc">Doe2023</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌──────────────────────────────── citation ────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span> Doe2023: John Doe. Python Patterns. 2023.                                <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Hyperlinks and Targets
----------------------

Standalone hyperlink
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Visit https://python.org for more.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Visit </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://python.org">https://python.org</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for more.</span>
   </span></pre>
   </div>

External hyperlink (named)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Read the `Rich documentation`_.

   .. _Rich documentation: https://rich.readthedocs.io

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Read the </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://rich.readthedocs.io">Rich documentation</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Jump to </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline">Target Section</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>

   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                              Target Section                              </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Content here.</span>
   </span></pre>
   </div>

Anonymous hyperlink
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See `this page <https://example.com>`__ for details.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://example.com">this page</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for details.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">rich-rst is written in Python.</span>
   </span></pre>
   </div>

Date substitution
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Generated on |today|.

   .. |today| date:: %Y-%m-%d

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Generated on 2026-07-09.</span>
   </span></pre>
   </div>

Unicode substitution
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Copyright |copy| 2024 The Authors.

   .. |copy| unicode:: U+00A9 .. copyright sign

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Copyright © 2024 The Authors.</span>
   </span></pre>
   </div>

Image substitution
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Click the |logo| icon.

   .. |logo| image:: https://example.com/logo.png
      :alt: Logo

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Click the </span>🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">Logo</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> icon.</span>
   </span></pre>
   </div>

Images and Figures
------------------

image directive
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. image:: https://example.com/photo.png
      :alt: A photo
      :height: 300px
      :width: 400px
      :scale: 50%
      :align: center
      :target: https://example.com
      :class: custom-image-class
      :name: custom-image-id

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="https://example.com
      :class: custom-image-class
      :name: custom-image-id">A photo</a></span>
   </span></pre>
   </div>

figure directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. figure:: https://example.com/chart.png
      :alt: A chart
      :height: 400px
      :width: 600px
      :scale: 75%
      :align: center
      :target: https://example.com
      :class: custom-figure-class
      :name: custom-figure-id
      :figwidth: 500px
      :figclass: custom-figure-container-class

      Figure caption goes here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #bd93f9; text-decoration-color: #bd93f9">╭─ Figure caption goes here. ─╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> 🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="https://example.com">A chart</a></span>                  <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╰─────────────────────────────╯</span>
   </span></pre>
   </div>

figure with legend
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. figure:: https://example.com/diagram.png
      :alt: Diagram
      :figwidth: image
      :class: custom-figure-legend-class

      Caption text.

      Legend text with more details about the figure.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #bd93f9; text-decoration-color: #bd93f9">╭───────────────── Caption text. ─────────────────╮</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> 🌆 <span style="color: #6088ff; text-decoration-color: #6088ff"><a href="Image">Diagram</a></span>                                      <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span> <span style="color: #909194; text-decoration-color: #909194">Legend text with more details about the figure.</span> <span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span>
   <span style="color: #bd93f9; text-decoration-color: #bd93f9">╰─────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

Document Structure Directives
-----------------------------

topic directive
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. topic:: Interesting Fact
      :class: custom-topic-class
      :name: custom-topic-id

      This is the topic body.
      It can contain any body elements.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Interesting Fact </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This is the topic body. It can contain any body elements.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

sidebar directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sidebar:: Note
      :subtitle: Side note
      :class: custom-sidebar-class
      :name: custom-sidebar-id

      Sidebar text goes here.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">╭───────── Note ──────────╮
   │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sidebar text goes here.</span> │
   ╰─────── Side note ───────╯
   </span></pre>
   </div>

rubric directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. rubric:: An Unnumbered Heading
      :class: custom-rubric-class
      :name: custom-rubric-id

   Following paragraph.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #909194; text-decoration-color: #909194; font-style: italic">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color: #909194; text-decoration-color: #909194; font-style: italic">│                          An Unnumbered Heading                           │</span>
   <span style="color: #909194; text-decoration-color: #909194; font-style: italic">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Following paragraph.</span>
   </span></pre>
   </div>

contents directive (table of contents)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. contents:: Table of Contents
      :depth: 2
      :local:
      :backlinks: entry
      :class: custom-contents-class

   Section A
   ---------

   Content A.

   Section B
   ---------

   Content B.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭───────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Table of Contents </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; font-weight: bold; text-decoration: underline">Section A</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                             </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; font-weight: bold; text-decoration: underline">Section B</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                             </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                                Section A                                 </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Content A.</span>

   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                                Section B                                 </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Content B.</span>
   </span></pre>
   </div>

sectnum directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. sectnum::
      :depth: 3
      :start: 1
      :prefix: Section-
      :suffix: .

   Overview
   --------

   Details
   -------

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                          Section-1.   Overview                           </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color:#f8f8f2">╭──────────────────────────────────────────────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                           Section-2.   Details                           </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

header directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. header:: My Document Header

   Main content.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╔════════════════════════════════</span><span style="color:#f8f8f2;font-weight: bold"> caption </span><span style="color:#f8f8f2">═════════════════════════════════╗</span>
   <span style="color:#f8f8f2">║</span><span style="color:#f8f8f2;font-weight: bold">                            </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">My Document Header</span><span style="color:#f8f8f2;font-weight: bold">                            </span><span style="color:#f8f8f2">║</span>
   <span style="color:#f8f8f2">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Main content.</span>
   </span></pre>
   </div>

footer directive
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Main content.

   .. footer:: Page |page|

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Main content.</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">┌───────────────────────────────── Footer ─────────────────────────────────┐</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>                                  <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Page 1</span>                                  <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">│</span>
   <span style="color: #bcbcbc; text-decoration-color: #bcbcbc">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

centered directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. centered:: IMPORTANT NOTICE

   Body text.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2">                              <span style="color:#f8f8f2;font-weight: bold">IMPORTANT NOTICE</span>                              
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Body text.</span>
   </span></pre>
   </div>

Math
----

Inline math role
~~~~~~~~~~~~~~~~

.. code-block:: rst

   The Pythagorean theorem: :math:`a^2 + b^2 = c^2`.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The Pythagorean theorem: </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; font-style: italic">a^2 + b^2 = c^2</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">.</span>
   </span></pre>
   </div>

math directive (display)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. math::

      \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌────────────────────────────────── math ──────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> ∫_-∞^∞ e^-x^2 dx = √(π)                                                  <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

math directive (labeled)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. math:: E = mc^2
      :label: einstein
      :nowrap:
      :class: custom-math-class
      :name: custom-math-id

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌──────────────────────────── math - einstein ─────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> E = mc^2                                                                 <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╔══════════════════════════════════════════════════════════════════════════╗</span>
   <span style="color:#f8f8f2">║</span><span style="color:#f8f8f2;font-weight: bold">                                My Report                                 </span><span style="color:#f8f8f2">║</span>
   <span style="color:#f8f8f2">╚══════════════════════════════════════════════════════════════════════════╝</span>
   <span style="color:#f8f8f2;font-weight: bold">       Document Information       </span>
   ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Field Name   </span>┃<span style="color:#f8f8f2;font-weight: bold"> Field Value     </span>┃
   ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
   │ <span style="color:#f8f8f2;font-weight: bold">Author      </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Jane Smith</span>      │
   ├──────────────┼─────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Date        </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">2024-01-15</span>      │
   ├──────────────┼─────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Version     </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">1.0</span>             │
   ├──────────────┼─────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Status      </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Draft</span>           │
   ├──────────────┼─────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Copyright   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">2024 Jane Smith</span> │
   ├──────────────┼─────────────────┤
   │ <span style="color:#f8f8f2;font-weight: bold">Organization</span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">ACME Corp</span>       │
   └──────────────┴─────────────────┘
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Body of the document.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2;font-weight: bold">    Document Information    </span>
   ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
   ┃<span style="color:#f8f8f2;font-weight: bold"> Field Name </span>┃<span style="color:#f8f8f2;font-weight: bold"> Field Value </span>┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
   │ <span style="color:#f8f8f2;font-weight: bold">Authors   </span> │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Alice</span>       │
   │            │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Bob</span>         │
   │            │ <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Carol</span>       │
   └────────────┴─────────────┘
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Body text.</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Before comment.</span>

   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">After comment.</span>
   </span></pre>
   </div>

Raw Directive
-------------

raw html directive
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. raw:: html
      :class: custom-raw-class

      <strong>Bold via raw HTML</strong>

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────────────── stripped raw html ────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Bold via raw HTML</span><span style="color:#f8f8f2;background-color: #282a36">                                                       </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

raw latex directive
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. raw:: latex
      :class: custom-raw-class

      \textbf{Bold via LaTeX}

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #949494; text-decoration-color: #949494">┌─────────────────────────────── raw latex ────────────────────────────────┐</span>
   <span style="color: #949494; text-decoration-color: #949494">│</span> <span style="color: #ff79c6; text-decoration-color: #ff79c6; background-color: #282a36">\textbf</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">{</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #282a36">Bold via LaTeX</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; background-color: #282a36; font-style: italic">}</span><span style="color:#f8f8f2;background-color: #282a36">                                                 </span> <span style="color: #949494; text-decoration-color: #949494">│</span>
   <span style="color: #949494; text-decoration-color: #949494">└──────────────────────────────────────────────────────────────────────────┘</span>
   </span></pre>
   </div>

Sphinx Version Directives
-------------------------

Sphinx Version Directives Showcase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. versionadded:: 2.1

      This feature was added in version 2.1.

   .. versionchanged:: 3.0

      The API changed in version 3.0.

   .. deprecated:: 1.5

      Use the new API instead.

   .. deprecated-removed:: 1.5 2.0

      Removed in 2.0. Use the new API.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭───────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> New in version 2.1 </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">───────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">This feature was added in version 2.1.</span>                                   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╭─────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Changed in version 3.0 </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">─────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The API changed in version 3.0.</span>                                          <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭──────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> Deprecated since version 1.5 </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">──────────────────────╮</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use the new API instead.</span>                                                 <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────────╯</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╭─────────────</span><span style="color: #ff5555; text-decoration-color: #ff5555; font-weight: bold"> Deprecated since version 1.5 (removed in 2.0) </span><span style="color: #ff5555; text-decoration-color: #ff5555">──────────────╮</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">│</span> <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Removed in 2.0. Use the new API.</span>                                         <span style="color: #ff5555; text-decoration-color: #ff5555">│</span>
   <span style="color: #ff5555; text-decoration-color: #ff5555">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

Sphinx Cross-Reference Roles
----------------------------

Sphinx Cross-Reference Roles Showcase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Sphinx cross-reference roles render as inline literals. Here is a showcase of all supported roles:

   - Function: :func:`os.path.join`
   - Class: :class:`pathlib.Path`
   - Method: :meth:`str.upper`
   - Attribute: :attr:`os.sep`
   - Module: :mod:`os.path`
   - Exception: :exc:`ValueError`
   - Object: :obj:`sys.path`
   - Data: :data:`sys.version`
   - Constant: :const:`math.pi`
   - Term: :term:`decorator`
   - Reference: :ref:`some-label`
   - Document: :doc:`installation`
   - Environment Variable: :envvar:`PYTHONPATH`

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Sphinx cross-reference roles render as inline literals. Here is a showcase </span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">of all supported roles:</span>

   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Function: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.path.join</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Class: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">pathlib.Path</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Method: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">str.upper</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Attribute: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.sep</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Module: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.path</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Exception: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">ValueError</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Object: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.path</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Data: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">sys.version</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Constant: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">math.pi</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Term: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">decorator</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Reference: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">some-label</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Document: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">installation</span>
   <span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> • </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Environment Variable: </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">PYTHONPATH</span>
   </span></pre>
   </div>

Python Domain Showcase
----------------------

Python domain showcase
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. py:class:: App(config)
      :module: mypackage.app
      :platform: Unix, Windows
      :synopsis: High-level application object.
      :noindex:
      :canonical: mypackage.app.App

      App ties together the main runtime pieces.

      .. py:attribute:: App.name
         :type: str
         :value: demo

         Human-readable application name.

      .. py:property:: App.ready
         :type: bool

         Whether the application is ready to serve requests.

      .. py:method:: App.run(self, *args, **kwargs) -> int
         :async:

         Run the application event loop.

      .. py:classmethod:: App.build(cls, config) -> App
         :final:

         Construct an application instance.

      .. py:staticmethod:: App.version() -> str

         Return the current version string.

      .. py:data:: App.DEFAULT_TIMEOUT
         :type: float
         :value: 3.5

         Default timeout in seconds.

      .. py:function:: parse_config(text) -> dict[str, str]
         :deprecated:
         :canonical: mypackage.app.parse_config

         Parse configuration text.

         :param text: Raw configuration text.
         :returns: A mapping of configuration keys.
         :rtype: dict[str, str]

      .. py:exception:: AppError
         :platform: OS Independent

         Base exception for application errors.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭──────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [class] App(config) </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">───────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Attributes                                                               </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   name: </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">str</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                              </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">     Human-readable application name.                                     </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   ready: </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">bool</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                            </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">     Whether the application is ready to serve requests.                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   DEFAULT_TIMEOUT: </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">float</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                 </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">     Default timeout in seconds.                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Details                                                                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Module: mypackage.app                                                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Canonical: mypackage.app.App                                           </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Platform: Unix, Windows                                                </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Synopsis: High-level application object.                               </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Flags: noindex                                                         </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">App ties together the main runtime pieces.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                               </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭───────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [method] App.run(</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">self</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">, *args, **kwargs) </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">-&gt;</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> int </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">───────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Details                                                              </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">   Flags: async                                                       </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                                      </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Run the application event loop.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                      </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [classmethod] App.build(</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">cls</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">, config) </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">-&gt;</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> App </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">─────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Details                                                              </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">   Flags: final                                                       </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                                      </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Construct an application instance.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                   </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [staticmethod] App.version() </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">-&gt;</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> str </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">─────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Return the current version string.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                   </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭──────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [function] parse_config(text) </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">-&gt;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">dict[str, str]</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">───────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> Details                                                              </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">   Canonical: mypackage.app.parse_config                              </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">   Flags: deprecated                                                  </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                                      </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Parse configuration text.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                            </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                                      </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> Parameters                                                           </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">   text                                                               </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">     Raw configuration text.                                          </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                                      </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> Returns                                                              </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">   dict[str, str]: A mapping of configuration keys.                   </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [exception] AppError </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Details                                                              </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Platform: OS Independent                                           </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                      </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Base exception for application errors.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                               </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

C Domain Showcase
-----------------

C domain showcase
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:struct:: Config
      :synopsis: Runtime configuration for the C API.
      :noindex:

      .. c:member:: int timeout

         Timeout in seconds.

      .. c:member:: const char *name

         Display name.

      .. c:enum:: Mode

         .. c:enumerator:: MODE_FAST

            Fast mode.

         .. c:enumerator:: MODE_SAFE

            Safe mode.

      .. c:function:: int init_config(struct Config *config)

         Initialize a configuration object.

      .. c:macro:: DEFAULT_TIMEOUT

         Default timeout value.

      .. c:var:: int g_config_ready

         Indicates whether the configuration is ready.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭────────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [struct] Config </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">─────────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Details                                                                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Synopsis: Runtime configuration for the C API.                         </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Flags: noindex                                                         </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [member] </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">int</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> timeout </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Timeout in seconds.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                  </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭─────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [member] </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">const</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">char</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> *name </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">──────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Display name.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                        </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enum] Mode </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭─────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enumerator] MODE_FAST </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────╮</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Fast mode.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                       </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────╯</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭─────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enumerator] MODE_SAFE </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────╮</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Safe mode.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                       </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────╯</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭─────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [function] </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">int</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> init_config(</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">struct</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> Config *config) </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">──────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Initialize a configuration object.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                   </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭──────────────────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [macro] DEFAULT_TIMEOUT </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">───────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Default timeout value.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                               </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭──────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [var] </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">int</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> g_config_ready </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">──────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Indicates whether the configuration is ready.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                        </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

C++ Domain Showcase
-------------------

C++ domain showcase
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cpp:class:: App
      :synopsis: A small C++ application wrapper.
      :noindex:

      .. cpp:member:: std::string name

         Application name.

      .. cpp:member:: std::size_t count

         Number of processed items.

      .. cpp:enum:: Mode

         .. cpp:enumerator:: Mode::Fast

            Fast mode.

         .. cpp:enumerator:: Mode::Safe

            Safe mode.

      .. cpp:function:: int run(App &app)

         Run the app.

      .. cpp:alias:: StringMap = std::unordered_map<std::string, std::string>

         Convenience alias for string maps.

      .. cpp:concept:: ConvertibleToString

         A concept for string-like types.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭──────────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [class] App </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">───────────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Details                                                                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Synopsis: A small C++ application wrapper.                             </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Flags: noindex                                                         </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭─────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [member] </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">std</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">string name </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">──────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Application name.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭─────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> [member] </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">std</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">size_t count </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">─────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Number of processed items.</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                           </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enum] Mode </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enumerator] </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">Mode</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::Fast </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────╮</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Fast mode.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                       </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────╯</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [enumerator] </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">Mode</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::Safe </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────╮</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Safe mode.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                       </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────╯</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭────────────────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [function] </span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">int</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> run(App &amp;app) </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Run the app.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                         </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">╭──</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold"> [alias] StringMap </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">=</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">std</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">unordered_map&lt;</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">std</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">string, </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">std</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">::</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">string&gt; </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">──╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Convenience alias for string maps.</span><span style="color: #bd93f9; text-decoration-color: #bd93f9; font-weight: bold">                                   </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #bd93f9; text-decoration-color: #bd93f9">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭───────────────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [concept] ConvertibleToString </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">A concept for string-like types.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                     </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

JavaScript Domain Showcase
--------------------------

JavaScript domain showcase
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. js:class:: App(config)
      :module: mypkg.app
      :synopsis: Browser or runtime application wrapper.
      :noindex:

      .. js:attribute:: App.name

         The application name.

      .. js:method:: App.run(args)
         :async:

         Run the app.

      .. js:data:: App.VERSION

         Current version string.

      .. js:function:: parseConfig(text)

         Parse configuration text.

      .. js:module:: mypkg.app

         The module that exports the application.

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭──────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [class] App(config) </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">───────────────────────────╮</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> Details                                                                  </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Module: mypkg.app                                                      </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Synopsis: Browser or runtime application wrapper.                      </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">   Flags: noindex                                                         </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                                                                          </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭────────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [attribute] App.name </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The application name.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                                </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭───────────────────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [method] App</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">run(args) </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">───────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> Details                                                              </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">   Flags: async                                                       </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                                      </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Run the app.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                                         </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╭─────────────────────────</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> [data] App.VERSION </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">─────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Current version string.</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">                                              </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╭────────────────────</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> [function] parseConfig(text) </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Parse configuration text.</span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">                                            </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #ff79c6; text-decoration-color: #ff79c6">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">╭─────────────────────────</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> [module] </span><span style="color: #ff79c6; text-decoration-color: #ff79c6; font-weight: bold">mypkg</span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">app </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">─────────────────────────╮</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">The module that exports the application.</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold">                             </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────╯</span><span style="color: #50fa7b; text-decoration-color: #50fa7b; font-weight: bold"> </span><span style="color: #50fa7b; text-decoration-color: #50fa7b">│</span>
   <span style="color: #50fa7b; text-decoration-color: #50fa7b">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #ffffff; text-decoration-color: #ffffff">╭────────────────────────────────</span><span style="color: #ffffff; text-decoration-color: #ffffff; font-weight: bold"> See Also </span><span style="color: #ffffff; text-decoration-color: #ffffff">────────────────────────────────╮</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">│</span> <span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">os.path.join</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #121212">, </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">pathlib.Path</span>                                               <span style="color: #ffffff; text-decoration-color: #ffffff">│</span>
   <span style="color: #ffffff; text-decoration-color: #ffffff">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

Toctree (Sphinx)
----------------

toctree directive
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Contents
      :name: custom-toctree-name
      :titlesonly:
      :glob:
      :hidden:
      :includehidden:
      :reversed:
      :numbered: 2

      Installation Guide <installation>
      Usage Instructions <usage>
      API Reference <api>
      guide/Advanced Topics <guide/api>

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Contents </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">────────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">  0.1. guide/Advanced Topics</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                             </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">1. API Reference</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                         </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">2. Usage Instructions</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">3. Installation Guide</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                    </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
   </div>

toctree with numbered entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. toctree::
      :numbered:

      intro
      guide/installation
      guide/usage
      guide/api

.. raw:: html

   <div style="background:#282a36;border-radius:6px;padding:12px 16px;margin:8px 0 16px 0;overflow-x:auto;">
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #8be9fd; text-decoration-color: #8be9fd">╭────────────────────────────────</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> Contents </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">────────────────────────────────╮</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">1. intro</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                                 </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">  1.1. guide/installation</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">  1.2. guide/usage</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                       </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold"> </span><span style="color: #f1fa8c; text-decoration-color: #f1fa8c; font-weight: bold">  1.3. guide/api</span><span style="color: #8be9fd; text-decoration-color: #8be9fd; font-weight: bold">                                                         </span><span style="color: #8be9fd; text-decoration-color: #8be9fd">│</span>
   <span style="color: #8be9fd; text-decoration-color: #8be9fd">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╭────────────────────────────────</span><span style="color:#f8f8f2;font-weight: bold"> Glossary </span><span style="color:#f8f8f2">────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold"> RST                                                                      </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">     reStructuredText — a lightweight markup language.                    </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                                                                          </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold"> Sphinx                                                                   </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">     A documentation generator for Python projects.                       </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color:#f8f8f2">╭────────────────────────────────</span><span style="color:#f8f8f2;font-weight: bold"> Glossary </span><span style="color:#f8f8f2">────────────────────────────────╮</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold"> Aardvark                                                                 </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">     An ant-eating mammal.                                                </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">                                                                          </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold"> Zebra                                                                    </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">│</span><span style="color:#f8f8f2;font-weight: bold">     A striped animal.                                                    </span><span style="color:#f8f8f2">│</span>
   <span style="color:#f8f8f2">╰──────────────────────────────────────────────────────────────────────────╯</span>
   </span></pre>
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
   <pre style="white-space:pre;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color:#f8f8f2"><span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Use </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">json.dumps</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> or </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">json.loads</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to serialize data. The </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">dict</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> type maps </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">str</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> keys </span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">to values. See </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0484/">PEP 484</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for type hints and </span><span style="color: #bd93f9; text-decoration-color: #bd93f9; background-color: #282a36; text-decoration: underline"><a href="https://peps.python.org/pep-0526/">PEP 526</a></span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> for variable annotations. </span>
   <span style="color: #f8f8f2; text-decoration-color: #f8f8f2">Press </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">Ctrl+D</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> or call </span><span style="color: #c6c6c6; text-decoration-color: #c6c6c6; background-color: #121212">exit</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2"> to quit the REPL.</span>
   </span></pre>
   </div>


----

*This page was generated automatically.  Run* ``python tools/generate_demo_page.py``
*from the repository root to refresh it.*
