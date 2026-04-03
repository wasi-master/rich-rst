.. _include-directive:

Include Directive
=================

rich-rst provides a custom implementation of the standard ``.. include::``
directive that resolves file paths relative to the **source document** and
includes path-traversal protection.

.. contents::
   :local:

Basic Usage
-----------

Use ``.. include::`` to insert the contents of another RST file inline in your
document:

.. code-block:: rst

   Main document text.

   .. include:: chapter1.rst

   More main document text.

The included file is parsed as RST and rendered as if its content had been
written directly in the parent document.

Path Resolution
---------------

Paths are resolved relative to the **source document's directory**:

.. code-block:: rst

   .. include:: sections/intro.rst
   .. include:: ../shared/footer.rst

When rendering from a string (i.e. no source file path is known, or the source
is ``<string>``/ ``<stdin>``), paths are resolved relative to the **current
working directory**.

Security: Path-Traversal Protection
-------------------------------------

The ``.. include::`` directive rejects paths that would escape outside the
source document's directory.  For example, the following directive will produce
a warning admonition instead of including the file:

.. code-block:: rst

   .. include:: /etc/passwd

The warning message will be rendered in place of the included content, making
security issues visible during rendering.

Options
-------

The following options are supported:

``encoding``
    Character encoding of the included file.  Defaults to ``utf-8``.

    .. code-block:: rst

       .. include:: data.rst
          :encoding: latin-1

``start-line``
    First line (0-based) of the file to include.  Lines before this index are
    omitted.

    .. code-block:: rst

       .. include:: long_file.rst
          :start-line: 10

``end-line``
    Last line (exclusive, 0-based) of the file to include.  Lines from this
    index onwards are omitted.

    .. code-block:: rst

       .. include:: long_file.rst
          :start-line: 10
          :end-line: 20

Combining ``start-line`` and ``end-line`` selects a slice of the file:

.. code-block:: rst

   .. include:: reference.rst
      :start-line: 5
      :end-line: 15

Error Handling
--------------

If the file cannot be read (missing file, permission error, encoding error),
rich-rst emits a warning admonition in place of the included content:

.. code-block:: text

   ╭──────────────────── Warning ─────────────────────╮
   │ Could not include file: 'missing_file.rst'        │
   ╰───────────────────────────────────────────────────╯

This means rendering always succeeds; errors are surfaced as visible warnings
rather than hard failures.

Enabling the Directive
----------------------

``.. include::`` is always available in rich-rst — no extra configuration is
needed.  It is registered automatically when the first RST document is
rendered.

.. note::

   This directive is separate from ``.. literalinclude::``, which includes a
   file as a **code block** rather than inlining it as RST.

See Also
--------

- :class:`~rich_rst.RestructuredText` — the main rendering class
- :doc:`elements` — full list of supported RST elements
