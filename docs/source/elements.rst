Elements and Rendering
======================

This page lists all standard docutils element names and explains how rich-rst
renders them in the terminal.

The canonical support matrix is maintained in ``ELEMENTS.md`` in the repository.
This page focuses on rendering behavior by element family.

Rendering legend
----------------

- Supported: rendered directly by rich-rst.
- Simplified: rendered, but adapted for terminal constraints.
- Not implemented: currently not rendered with dedicated behavior.
- Not possible: no practical terminal equivalent.

All Standard Docutils Elements (98)
-----------------------------------

Document structure and metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rendered as document-level flow, headings, metadata tables, and structural panels.

- ``document``
- ``section``
- ``title``
- ``subtitle``
- ``topic``
- ``sidebar``
- ``rubric``
- ``transition``
- ``docinfo``
- ``author``
- ``authors``
- ``organization``
- ``address``
- ``contact``
- ``version``
- ``revision``
- ``status``
- ``date``
- ``copyright``
- ``meta``
- ``header``
- ``footer``
- ``generated``

Paragraph and inline text
~~~~~~~~~~~~~~~~~~~~~~~~~

Rendered as Rich text with inline styles and links.

- ``paragraph``
- ``emphasis``
- ``strong``
- ``literal``
- ``reference``
- ``target``
- ``title-reference``
- ``abbreviation``
- ``acronym``
- ``subscript``
- ``superscript``
- ``problematic``

Admonitions and notices
~~~~~~~~~~~~~~~~~~~~~~~

Rendered as styled panels.

- ``admonition``
- ``attention``
- ``caution``
- ``danger``
- ``error``
- ``hint``
- ``important``
- ``note``
- ``tip``
- ``warning``
- ``system-message``

Lists and blocks
~~~~~~~~~~~~~~~~

Rendered as indented list structures and block content.

- ``bullet-list``
- ``enumerated-list``
- ``list-item``
- ``definition-list``
- ``definition-list-item``
- ``term``
- ``classifier``
- ``definition``
- ``description``
- ``line-block``
- ``line``
- ``block-quote``
- ``attribution``
- ``option-list``
- ``option-list-item``
- ``option-group``
- ``option``
- ``option-string``
- ``option-argument``

Tables and field lists
~~~~~~~~~~~~~~~~~~~~~~

Rendered as Rich tables.

- ``table``
- ``tgroup``
- ``colspec``
- ``thead``
- ``tbody``
- ``row``
- ``entry``
- ``field-list``
- ``field``
- ``field-name``
- ``field-body``

Code and raw content
~~~~~~~~~~~~~~~~~~~~

Rendered as syntax-highlighted panels/blocks when possible.

- ``literal-block``
- ``doctest-block``
- ``raw``
- ``pending``

Media and figure content
~~~~~~~~~~~~~~~~~~~~~~~~

Rendered as text/link representations with figure grouping.

- ``image``
- ``figure``
- ``caption``
- ``legend``

Citations and footnotes
~~~~~~~~~~~~~~~~~~~~~~~

Rendered inline or block-style depending on node type.

- ``citation``
- ``citation-reference``
- ``footnote``
- ``footnote-reference``
- ``label``

Substitutions and transform output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rendered after docutils transforms, then styled in terminal output.

- ``substitution-definition``
- ``substitution-reference``
- ``decoration``

No visual output (compatibility)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accepted and processed, with little or no direct visual output.

- ``comment``

Not implemented
~~~~~~~~~~~~~~~

- ``compound``
- ``inline``

No documentation / incomplete behavior notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Known gap in element-specific behavior notes.

- ``container``

Math handling
~~~~~~~~~~~~~

- ``math``: not possible to faithfully render as terminal-native equation layout.
- ``math-block``: rendered in a labeled panel as text.

See also
--------

- :doc:`limitations`
- :doc:`demo`
- :doc:`documentation`
