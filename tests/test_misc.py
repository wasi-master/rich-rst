"""Miscellaneous tests."""


def test_paragraph_containing_system_message(render_text):
    """Test paragraph that contains a system message."""
    rst = """\
Before error :unknown_role:`content` after error.
"""
    out = render_text(rst, show_errors=True, sphinx_compat=False)
    assert 'System Message' in out


def test_complex_mixed_content(render_text):
    """Test complex document with mixed content types."""
    rst = """\
Main Title
==========

:Author: Test Author
:Date: 2024-06-15

Introduction paragraph with **bold** and *italic* text.

.. note::
   This is a note with more content.

Definition List
===============

term one
   Definition of term one with ``code``.

   * Nested bullet
   * Another bullet

term two
   Definition of term two.

Code Block Example
==================

.. code-block:: python
   :linenos:

   def example():
       return "Hello, World!"

Section with References
=======================

See `Google`_ for search.

.. _Google: https://google.com

----

Final Section
=============

Ending content.
"""
    out = render_text(rst)
    assert 'Main Title' in out
    assert 'Author' in out
    assert 'Hello' in out


def test_rst_with_all_inline_markup(render_text):
    """Test RST with all inline markup types combined."""
    rst = """\
Inline Markup Test
==================

Text with **bold**, *italic*, **_bold italic_** and ``literal`` all together.

Also includes :sub:`subscript`, :sup:`superscript` and references to `some target`_.

.. _some target: http://example.com

Line with `emphasis`_, **strong**, and ``code`` in one go.
"""
    out = render_text(rst)
    assert 'Markup' in out


def test_mixed_formatting_and_elements(render_text):
    """Test document with mixed formatting throughout."""
    rst = """\
Mixed Content
=============

Some text with `links <http://example.com>`_, **bold**, *italics*.

.. note:: Important note

   With nested **formatting**.

A paragraph before code::

   code block

After code, regular text continues.

* List item one

  With nested paragraph.

* List item two
"""
    out = render_text(rst)
    assert 'Mixed' in out


def test_long_document_rendering(render_text):
    """Test rendering of a longer document to ensure it completes."""
    sections = []
    for i in range(5):
        sections.append(f"""\
Section {i}
{'-' * (10 + len(str(i)))}

Content for section {i}.

* Item 1 for section {i}
* Item 2 for section {i}

Example::

   code_{i}()
""")
    rst = '\n\n'.join(sections)
    out = render_text(rst)
    assert 'Section' in out


def test_entire_document_with_all_element_types(render_text):
    """Test complete document with as many element types as possible."""
    rst = """\
Complete Document
=================

:Author: Test
:Date: 2024-06-15

.. note:: A note

Introduction with |sub| and |sup|.

.. |sub| replace:: subscript-like
.. |sup| replace:: superscript-like

Bullet List
-----------

* Item 1
* Item 2

  * Nested

Enum List
---------

1. First
2. Second

Definition
----------

term
   definition

Quote
-----

   A quoted passage here.

Code::

   code sample

Raw
---

.. raw:: html

   <div>HTML</div>

Footer Test
-----------

.. footer:: Footer text
"""
    out = render_text(rst)
    assert 'Complete Document' in out


def test_complex_comprehensive_document(render_text):
    """Test very comprehensive document using all major features."""
    rst = """\
Full Documentation
==================

:Author: John Doe
:Date: 2024-06-15
:Version: 2.0
:Status: Final

Abstract
--------

This is a comprehensive example covering multiple features.

.. note::
   An informational note.

Introduction
============

Section with **bold**, *italic*, and ``monospace`` text.

Features List
=============

* Feature One
* Feature Two

  * Sub-feature Alpha
  * Sub-feature Beta

* Feature Three

Numbered Items
==============

1. First item
2. Second item

   i. Sub-item 1
   ii. Sub-item 2

3. Third item

Glossary
========

Python
   A programming language.

   * Fast development
   * Easy to learn

RST
   ReStructuredText markup language.

Examples
========

Code example::

   def hello():
       return "world"

Another section
===============

| Line block example
| Second line here
|
|     Indented content
|
| Back to regular

Quotation
---------

   "The best way to predict the future is to invent it."

   — Alan Kay

Reference
---------

See the `Python docs`_ for more.

.. _Python docs: https://python.org

.. footer:: Page footer text
"""
    out = render_text(rst)
    assert 'Full Documentation' in out


def test_rendering_with_errors_disabled(render_text):
    """Test rendering with error display disabled."""
    rst = """\
Some text with :unknown:`unknown role`.
"""
    out = render_text(rst, show_errors=False, sphinx_compat=False)
    assert 'System Message' not in out


def test_rendering_without_sphinx_compat(render_text):
    """Test rendering without Sphinx compatibility."""
    rst = """\
Normal RST content.
"""
    out = render_text(rst, sphinx_compat=False)
    assert 'Normal RST content' in out, 'Plain text content must be visible without sphinx_compat'


def test_render_all_rst_roles(render_text):
    """Test rendering with various RST roles."""
    rst = """\
Text with :emphasis:`emphasis`, :strong:`strong`, and :literal:`literal`.

Also :ref:`reference` and :doc:`document`.
"""
    out = render_text(rst)
    assert 'emphasis' in out, ':emphasis: role content must be visible'
    assert 'strong' in out, ':strong: role content must be visible'
    assert 'literal' in out, ':literal: role content must be visible'


def test_render_with_syntax_error(render_text):
    """Test rendering malformed RST."""
    rst = """\
Unclosed ``literal

This should still render.
"""
    out = render_text(rst, show_errors=True)
    assert 'still render' in out, 'Content after syntax error must still be visible'


def test_very_long_line(render_text):
    """Test rendering with very long line."""
    long_text = 'word ' * 100
    rst = f'This is a very long line:\n\n{long_text}'
    out = render_text(rst)
    assert 'This is a very long line' in out, 'Leading text must be visible'
    assert 'word' in out, 'Long-line body words must be visible'


def test_many_nested_elements(render_text):
    """Test document with many nested elements."""
    rst = """\
Title
=====

Multiple inline styles: **bold *and italic* and ``code``** text.

Nested lists:

1. One

   * Alpha
   * Beta

     - i
     - ii

2. Two

   a. A
   b. B
"""
    out = render_text(rst)
    assert 'Title' in out, 'Section title must be visible'
    assert 'One' in out, 'Enumerated list item must be visible'
    assert 'Two' in out, 'Second enumerated list item must be visible'
    assert 'Alpha' in out, 'Nested bullet item must be visible'


def test_empty_document(render_text):
    """Test rendering completely empty document produces a string without raising."""
    rst = ''
    out = render_text(rst)
    assert isinstance(out, str), 'Rendering an empty document must return a string'


def test_minimal_valid_document(render_text):
    """Test minimal valid document."""
    rst = 'Simple text.'
    out = render_text(rst)
    assert 'Simple text' in out


def test_direct_api_usage(render_text):
    """Test direct API usage through render_text with various options."""
    rst = 'Text'
    out = render_text(
        rst,
        code_theme='vim',
        show_line_numbers=False,
        guess_lexer=False,
        default_lexer='bash',
        sphinx_compat=True,
        show_errors=True,
    )
    assert 'Text' in out


def test_generated_node_handling(render_text):
    """Test generated nodes (typically auto-generated content)."""
    rst = 'Some regular content.'
    out = render_text(rst)
    assert 'Some regular content' in out, 'Regular paragraph text must be visible'


def test_sphinx_registration_guard():
    from rich_rst import _sphinx_registration_guard

    called = []

    @_sphinx_registration_guard
    def dummy(x):
        called.append(x)
        return x * 2

    res = dummy(5)
    assert res == 10
    assert called == [5]


def test_custom_role(render_text):
    rst = """\
.. role:: custom
   :class: my-custom-class

This is a :custom:`custom text` role.
"""
    out = render_text(rst)
    assert 'custom text' in out


def test_blockquote_with_bullet_list(render_text):
    rst = """\
   This is a blockquote.

   * Item 1
   * Item 2
"""
    out = render_text(rst)
    assert 'Item 1' in out
    assert 'Item 2' in out


def test_visitor_subclass_registration():
    from rich_rst import RSTVisitor
    from rich_rst._vendor import docutils

    class SubVisitor(RSTVisitor):
        pass

    SubVisitor.register_visitor(docutils.nodes.Node, lambda self, node: None)
    assert docutils.nodes.Node in SubVisitor._custom_visitors


def test_dispatch_cache_concurrency(make_visitor):
    visitor = make_visitor('')
    from rich_rst._vendor import docutils

    # Trigger visit cache hit under concurrency simulation by subclassing dict
    class MockVisitDict(dict):
        def get(self, key, default=None):
            # Populate the cache right when get() is called (representing concurrent caching)
            self[key] = getattr(visitor, 'visit_paragraph')
            return None

    visitor._visit_dispatch_cache = MockVisitDict()
    visitor._resolve_visit_handler(docutils.nodes.paragraph)

    # Trigger depart cache hit under concurrency simulation by subclassing dict
    class MockDepartDict(dict):
        def get(self, key, default=None):
            self[key] = getattr(visitor, 'depart_paragraph')
            return None

    visitor._depart_dispatch_cache = MockDepartDict()
    visitor._resolve_depart_handler(docutils.nodes.paragraph)


def test_translate_with_fallback_none_mapping(make_visitor):
    visitor = make_visitor('')
    res = visitor._translate_with_fallback('abc', {ord('a'): None})
    assert res == 'abc'


def test_guess_lexer_name_class_not_found(make_visitor):
    visitor = make_visitor('')
    _lexer, ok = visitor._guess_lexer_name('!!!non-code-garbage!!!')
    assert not ok


def test_format_labelled_node_variants(make_visitor):
    visitor = make_visitor('')
    from rich_rst._vendor import docutils

    # No body, only label
    node1 = docutils.nodes.footnote()
    node1 += docutils.nodes.label('', 'MyLabel')
    res1 = visitor._format_labelled_node(node1)
    assert res1 == 'MyLabel:'

    # No label, only body
    node2 = docutils.nodes.footnote()
    node2 += docutils.nodes.paragraph('', 'MyBody')
    res2 = visitor._format_labelled_node(node2)
    assert res2 == 'MyBody'


def test_named_hyperlink_resolution(render_text):
    rst = """\
See `My Link`_.

.. _My Link: https://example.com
"""
    out = render_text(rst)
    assert 'My Link' in out


def test_paragraph_with_system_message_parent(make_visitor):
    visitor = make_visitor('')
    import pytest

    from rich_rst._vendor import docutils

    sys_msg = docutils.nodes.system_message(
        'Warning message',
        level=2,
        type='WARNING',
        source='test_source',
        line=1,
    )
    p = docutils.nodes.paragraph()
    sys_msg += p
    p.parent = sys_msg

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_paragraph(p)
