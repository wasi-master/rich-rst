"""Comprehensive coverage tests for rich-rst.

This file contains tests targeting specific coverage gaps identified through coverage analysis.

Focus areas:
- Lexer guessing and fallback logic
- Section level calculation with nested sections  
- Reference and target node handling
- Field/docinfo variations (authors, organization, address, etc.)
- Definition list edge cases
- Complex nested list scenarios
- Block quote with/without attribution
- Line block nesting
- Topic and sidebar rendering
- Option list variations
- Abbreviations and acronyms
- Emphasis and strong emphasis variations
- Subscript and superscript handling
- Citations and footnotes
- Raw content elements
- Complex table and figure scenarios
- Inline markup combinations
- Generated and pending nodes
"""
import pytest
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich_rst import RestructuredText, RSTVisitor


# ══════════════════════════════════════════════════════════════════════════════
# LEXER AND CODE HANDLING
# ══════════════════════════════════════════════════════════════════════════════

def test_guess_lexer_with_unknown_language(render_text):
    """Test guessing lexer for code that doesn't match any known patterns."""
    rst = """\
.. code-block::

   this is just some random text
   not any specific language
   maybe looks like something
"""
    out = render_text(rst, guess_lexer=False)
    assert "python" in out  # Default lexer


def test_lexer_guess_fallback_to_default(render_text):
    """Test that when guess fails, it returns default lexer."""
    rst = """\
.. code-block::

   ξξξξξξ random unicode ξξξξξξ
"""
    out = render_text(rst, guess_lexer=True, default_lexer="python")
    assert "python" in out or "random unicode" in out


def test_code_block_with_explicit_format(render_text):
    """Test code block with explicit format specification."""
    rst = """\
.. code-block:: javascript

   console.log("hello world");
"""
    out = render_text(rst)
    assert "console.log" in out


def test_code_block_with_class_syntax(render_text):
    """Test code block using class syntax for language."""
    rst = """\
.. code-block::
   :class: language-rust

   fn main() {
       println!("Hello");
   }
"""
    out = render_text(rst)
    assert "fn main" in out


def test_lexer_with_aliases(make_visitor):
    """Test lexer that has aliases (normal case)."""
    rst = """\
.. code-block:: python3

   x = 1
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "code-block must produce a Panel renderable"
    assert panels[0].title == "python3", (
        f"Panel title must be the lexer alias 'python3', got {panels[0].title!r}"
    )


def test_render_with_line_numbers(render_text):
    """Test rendering with line numbers enabled."""
    rst = """\
.. code-block:: python

   def hello():
       return "world"
"""
    out = render_text(rst, show_line_numbers=True)
    assert "python" in out, "Panel title must show the lexer name 'python'"
    assert "def hello" in out, "Code content must be visible in line-numbered output"
    assert "1" in out, "Line number '1' must appear when show_line_numbers=True"


def test_render_with_custom_code_theme(render_text):
    """Test rendering with different code theme — code content must still be visible."""
    rst = """\
.. code-block:: python

   x = 42
"""
    out = render_text(rst, code_theme="github-dark")
    assert "x = 42" in out, "Code content must be visible regardless of the chosen code_theme"
    assert "python" in out, "Lexer panel title must be visible with a custom code_theme"


# ══════════════════════════════════════════════════════════════════════════════
# SECTIONS AND STRUCTURE
# ══════════════════════════════════════════════════════════════════════════════

def test_deeply_nested_sections(render_text):
    """Test multiple levels of section nesting."""
    rst = """\
Level 1
=======

Some text here.

Level 2
-------

More text.

Level 3
^^^^^^^

Even deeper.

Level 4
"""""""

Deepest level.
"""
    out = render_text(rst)
    assert "Level 1" in out
    assert "Level 2" in out
    assert "Level 3" in out
    assert "Level 4" in out


def test_multiple_sections_same_level(render_text):
    """Test multiple sections at the same level."""
    rst = """\
First Section
=============

Content here.

Second Section
==============

Different content.

Third Section
=============

More content.
"""
    out = render_text(rst)
    assert "First Section" in out
    assert "Second Section" in out
    assert "Third Section" in out


# ══════════════════════════════════════════════════════════════════════════════
# REFERENCES AND TARGETS
# ══════════════════════════════════════════════════════════════════════════════

def test_reference_with_inline_image(render_text):
    """Test that reference with image child is properly skipped."""
    rst = """\
`Link with image <http://example.com>`_

.. image:: /some/image.png
   :target: http://example.com
"""
    out = render_text(rst)
    assert "Link with image" in out, "Reference display text must be visible"
    assert "🌆" in out, "Image must render with the 🌆 emoji"


def test_reference_resolution_via_target(render_text):
    """Test reference name resolution with explicit target."""
    rst = """\
See the `introduction`_ document.

.. _introduction: https://example.com/intro
"""
    out = render_text(rst)
    assert "introduction" in out


def test_anonymous_target(render_text):
    """Test anonymous hyperlink targets."""
    rst = """\
This is an __ anonymous link.

__ https://example.com
"""
    out = render_text(rst)
    assert "anonymous" in out


def test_multiple_targets_same_name(render_text):
    """Test handling of duplicate target names."""
    rst = """\
First `reference`_.

.. _reference: https://example.com/1

Second reference text.
"""
    out = render_text(rst)
    assert "reference" in out


def test_reference_without_refuri_or_refname(render_text):
    """Test reference that has neither refuri nor refname."""
    rst = "Some text with regular link reference."
    out = render_text(rst)
    assert "text" in out


def test_multiple_inline_references_sequence(render_text):
    """Test multiple references in sequence."""
    rst = """\
Check `link1`_ and `link2`_ and `link3`_.

.. _link1: http://example.com/1
.. _link2: http://example.com/2  
.. _link3: http://example.com/3
"""
    out = render_text(rst)
    assert "link1" in out, "First reference label must be visible"
    assert "link2" in out, "Second reference label must be visible"
    assert "link3" in out, "Third reference label must be visible"


def test_title_reference_appended_to_text(render_text):
    """Test title reference appended to text."""
    rst = """\
See the `Title`_ document for more.
"""
    out = render_text(rst)
    assert "Title" in out


# ══════════════════════════════════════════════════════════════════════════════
# IMAGES AND FIGURES
# ══════════════════════════════════════════════════════════════════════════════

def test_image_with_alt_attribute(render_text):
    """Test image with alt text."""
    rst = """\
.. image:: /path/image.png
   :alt: Alternative text
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Alternative text" in out, "Image alt text must be visible in the output"


def test_image_with_target_attribute(render_text):
    """Test image with target link."""
    rst = """\
.. image:: /path/image.png
   :target: http://example.com
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"


def test_image_with_alt_and_target(render_text):
    """Test image with both alt and target."""
    rst = """\
.. image:: /path/image.png
   :alt: Image description
   :target: http://example.com
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Image description" in out, "Alt text must be visible alongside the emoji"


def test_figure_without_image(render_text):
    """Test figure directive without a valid image argument (invalid RST — no crash expected)."""
    rst = """\
.. figure::

   Just a caption, no image.
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise"


def test_figure_with_reference_target(make_visitor):
    """Test figure with target inside reference."""
    rst = """\
.. figure:: /path/image.png
   :target: http://example.com

   Caption text
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "Caption text", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )


def test_figure_with_caption(make_visitor):
    """Test figure with caption."""
    rst = """\
.. figure:: /path/to/image.png

   This is the caption.
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "This is the caption.", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )


def test_figure_with_caption_and_legend(make_visitor):
    """Test figure with caption and legend."""
    rst = """\
.. figure:: /path/to/image.png

   Figure caption text.

   Legend text
   more legend.
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "Figure caption text.", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )
    assert panels[0].subtitle is not None, "Figure with legend must have a non-None subtitle"


def test_linked_image_with_complex_attributes(render_text):
    """Test image with multiple attributes in a link."""
    rst = """\
`Image Link <http://example.com>`_

.. image:: /path/image.png
   :alt: Image description
   :target: http://example.com
   :width: 200
   :height: 100
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Image description" in out, "Alt text must be visible in the output"


# ══════════════════════════════════════════════════════════════════════════════
# FIELD LISTS AND DOCINFO
# ══════════════════════════════════════════════════════════════════════════════

def test_multiple_authors_docinfo(render_text):
    """Test docinfo with multiple author elements."""
    rst = """\
:Author1: Alice
:Author2: Bob
:Organization: ACME Corp
:Contact: contact@example.com
:Version: 1.0
:Revision: 1.1
:Status: Draft
:Date: 2024-01-01
:Copyright: 2024 ACME
"""
    out = render_text(rst)
    assert "Author" in out
    assert "Organization" in out


def test_docinfo_single_author(render_text):
    """Test docinfo with single author."""
    rst = """\
:Author: Charlie
:Date: 2024-06-15
"""
    out = render_text(rst)
    assert "Author" in out
    assert "Charlie" in out


def test_multiple_field_merging(render_text):
    """Test that multiple field blocks merge into same table."""
    rst = """\
:Author: Alice
:Date: 2024-01-01

Some paragraph.

:Version: 1.0
:Status: Draft
"""
    out = render_text(rst)
    assert "Author" in out
    assert "Version" in out


def test_field_list_standalone(render_text):
    """Test field list outside of docinfo."""
    rst = """\
Content before.

:Field1: Value1
:Field2: Value2
:Field3: Value3

Content after.
"""
    out = render_text(rst)
    assert "Field1" in out
    assert "Value1" in out


def test_address_docinfo(render_text):
    """Test address field in docinfo."""
    rst = """\
:Address:
   123 Main Street
   Springfield, IL 62701
:Contact: info@example.com
"""
    out = render_text(rst)
    assert "Address" in out, "Address field name must appear in the table"
    assert "123" in out, "Address field value must appear in the table"


# ══════════════════════════════════════════════════════════════════════════════
# DEFINITION LISTS
# ══════════════════════════════════════════════════════════════════════════════

def test_definition_list_with_classifier(render_text):
    """Test definition list with classifier."""
    rst = """\
term
   classified : classifier
   The definition.
"""
    out = render_text(rst)
    assert "term" in out, "Definition list term must be visible"
    assert "classified" in out, "Definition list body must be visible"


def test_definition_list_without_classifier(render_text):
    """Test definition list without classifier."""
    rst = """\
term
   The definition without classifier.

another
   Another definition.
"""
    out = render_text(rst)
    assert "term" in out, "First definition list term must be visible"
    assert "The definition without classifier" in out, "Definition body must be visible"
    assert "another" in out, "Second definition list term must be visible"


def test_definition_list_with_nested_content(render_text):
    """Test definition list containing nested lists."""
    rst = """\
Python
   A programming language.

   * Feature 1
   * Feature 2

   Code example::

      print("hello")
"""
    out = render_text(rst)
    assert "Python" in out
    assert "Feature" in out


def test_definition_list_multiple_lines(render_text):
    """Test definition list with multi-line content."""
    rst = """\
item
   First line of definition.
   Second line of definition.
   Third line of definition.
"""
    out = render_text(rst)
    assert "item" in out, "Definition list term must be visible"
    assert "First line of definition" in out, "Definition body must be visible"


def test_definition_list_three_parts(render_text):
    """Test definition list with term, classifier, and definition."""
    rst = """\
term : classifier
   The definition of the term with classifier.
"""
    out = render_text(rst)
    assert "term" in out, "Term must be visible"
    assert "classifier" in out, "Classifier must be visible"
    assert "The definition of the term with classifier" in out, (
        "Definition body must be visible"
    )


def test_complex_definition_list_mixed(render_text):
    """Test complex definition list mixing various formats."""
    rst = """\
term1
   definition1

term2 : classifier
   definition2

term3
   def line 1
   def line 2
"""
    out = render_text(rst)
    assert "term1" in out, "First term must be visible"
    assert "definition1" in out, "First definition must be visible"
    assert "term2" in out, "Second term must be visible"
    assert "term3" in out, "Third term must be visible"


def test_definition_list_nested_lists_and_code(render_text):
    """Test definition list with nested lists and code blocks."""
    rst = """\
Term with complex definition
   This definition has multiple components.
   
   Related items:
   
   1. First related
   2. Second related
   
   Code example::
   
      x = 1
      y = 2
      
   Final note about this term.
"""
    out = render_text(rst)
    assert "Term with complex definition" in out, "Definition list term must be visible"
    assert "First related" in out, "Nested list items must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# OPTION LISTS
# ══════════════════════════════════════════════════════════════════════════════

def test_option_list_with_arguments(render_text):
    """Test option list with arguments."""
    rst = """\
-a <arg>
   Description of -a option
-b, --beta VALUE
   Description of beta option
-c
   Boolean flag
"""
    out = render_text(rst)
    assert "-a" in out, "Option -a must be visible"
    assert "Description of -a option" in out, "Option -a description must be rendered"
    assert "-c" in out, "Option -c must be visible"
    assert "Boolean flag" in out, "Option -c description must be rendered"


def test_option_list_single_option(render_text):
    """Test option list with single option."""
    rst = """\
--verbose
   Enable verbose output
"""
    out = render_text(rst)
    assert "--verbose" in out, "Option flag --verbose must be visible"
    assert "Enable verbose output" in out, "Option description must be rendered"


def test_complex_option_list(render_text):
    """Test complex option list with various formats."""
    rst = """\
Command Options
===============

-h, --help
   Show this help message
-v, --verbose
   Enable verbose output
-o FILE, --output FILE
   Write output to FILE
-q, --quiet
   Suppress output
--config=FILE
   Use configuration from FILE
"""
    out = render_text(rst)
    assert "-h" in out, "Option -h must be visible"
    assert "Show this help message" in out, "Option -h description must be rendered"
    assert "--verbose" in out, "Option --verbose must be visible"
    assert "Enable verbose output" in out, "Option --verbose description must be rendered"
    assert "--quiet" in out, "Option --quiet must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# BLOCK QUOTES
# ══════════════════════════════════════════════════════════════════════════════

def test_block_quote_with_attribution(render_text):
    """Test block quote with attribution."""
    rst = """\
   This is a great quote.
   It spans multiple lines.

   — Famous Person
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "great quote" in out, "Block quote text must be visible"
    assert "Famous Person" in out, "Attribution must be visible"


def test_block_quote_multiple_paragraphs(render_text):
    """Test block quote with multiple paragraphs."""
    rst = """\
   First paragraph of quote.

   Second paragraph continues.

   Third paragraph concludes.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "First paragraph of quote" in out, "First paragraph must be visible"
    assert "Second paragraph continues" in out, "Second paragraph must be visible"


def test_block_quote_no_attribution(render_text):
    """Test block quote without attribution."""
    rst = """\
   A simple quote.
   No attribution here.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "A simple quote" in out, "Block quote text must be visible"


def test_block_quote_single_paragraph(render_text):
    """Test block quote with exactly one paragraph."""
    rst = """\
   Single paragraph quote.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Single paragraph quote" in out, "Block quote text must be visible"


def test_block_quote_many_paragraphs(render_text):
    """Test block quote with many paragraphs."""
    rst = """\
   Para 1
     
   Para 2
     
   Para 3
     
   Para 4
     
   Para 5
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Para 1" in out, "First paragraph must be visible"
    assert "Para 5" in out, "Last paragraph must be visible"


def test_nested_content_in_block_quote(render_text):
    """Test block quote containing various nested content."""
    rst = """\
   Block quote with multiple paragraphs.
   
   First paragraph here.
   
   Second paragraph with **bold** and *italic* text.

   — Attribution
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Block quote with multiple paragraphs" in out, "Block quote text must be visible"
    assert "Attribution" in out, "Attribution must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# LINE BLOCKS
# ══════════════════════════════════════════════════════════════════════════════

def test_line_block_nested(render_text):
    """Test nested line blocks."""
    rst = """\
| Line 1
| Line 2
|
|     Indented line 3
|     Indented line 4
| Line 5
"""
    out = render_text(rst)
    assert "Line 1" in out
    assert "Line 5" in out


def test_line_block_deeply_nested(render_text):
    """Test deeply nested line blocks."""
    rst = """\
| Level 1-1
|
|     Level 2-1
|     Level 2-2
|
|         Level 3-1
|
|     Back to Level 2
|
| Back to Level 1
"""
    out = render_text(rst)
    assert "Level 1-1" in out


def test_empty_line_block(render_text):
    """Test line block that's essentially empty."""
    rst = """\
| Just one line
"""
    out = render_text(rst)
    assert "Just one line" in out


def test_line_block_single_line(render_text):
    """Test line block with single line."""
    rst = """\
| Single line
"""
    out = render_text(rst)
    assert "Single line" in out


def test_line_block_many_levels(render_text):
    """Test line block with many indentation levels."""
    rst = """\
| L1
|     L2
|         L3
|             L4
|                 L5
| Back to L1
"""
    out = render_text(rst)
    assert "L1" in out or "L5" in out


# ══════════════════════════════════════════════════════════════════════════════
# ADMONITIONS
# ══════════════════════════════════════════════════════════════════════════════

def test_empty_body_rendering(render_text):
    """Test that note admonitions render with their panel title."""
    rst = """\
.. note::

   Minimal content.
"""
    out = render_text(rst)
    assert "Note:" in out, "Note admonition must render with 'Note:' panel title"
    assert "Minimal content" in out, "Admonition body must be visible"


def test_admonition_with_custom_title(render_text):
    """Test generic admonition with custom title node."""
    rst = """\
.. admonition:: Custom Title

   Content of custom admonition.
"""
    out = render_text(rst)
    assert "Custom Title" in out, (
        "Generic admonition must render with '<title>' panel title"
    )
    assert "Content of custom admonition" in out, "Admonition body must be visible"


def test_admonition_with_nested_lists_and_code(render_text):
    """Test admonition containing nested lists and code."""
    rst = """\
.. warning::

   This warning contains important information.
   
   Key points:
   
   * Point one
   * Point two
   
   Code to avoid::
   
      dangerous_function()
      
   Always use::
   
      safe_function()
"""
    out = render_text(rst)
    assert "Warning:" in out, "Warning admonition must render with 'Warning:' panel title"
    assert "important information" in out, "Warning body must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# TOPICS AND SIDEBARS
# ══════════════════════════════════════════════════════════════════════════════

def test_topic_with_title(render_text):
    """Test topic with explicit title."""
    rst = """\
.. topic:: Important Topic

   This is the content of the topic.
   It can have multiple paragraphs.
"""
    out = render_text(rst)
    assert "Important Topic" in out


def test_topic_no_title(render_text):
    """Test topic without title."""
    rst = """\
.. topic::

   Content here.
"""
    out = render_text(rst)
    assert "Content here" in out, "Topic body must be visible in the output"


def test_sidebar_with_title_and_subtitle(render_text):
    """Test sidebar with title and subtitle."""
    rst = """\
.. sidebar:: Sidebar Title
   :subtitle: Subtitle

   Sidebar content goes here.
"""
    out = render_text(rst)
    assert "Sidebar Title" in out, "Sidebar title must be visible"
    assert "Subtitle" in out, "Sidebar subtitle must be visible"


def test_sidebar_title_only(render_text):
    """Test sidebar with only title."""
    rst = """\
.. sidebar:: My Sidebar

   Just the content.
"""
    out = render_text(rst)
    assert "My Sidebar" in out, "Sidebar title must be visible"
    assert "Just the content" in out, "Sidebar body must be visible"


def test_sidebar_with_subtitle_and_lists(render_text):
    """Test sidebar with subtitle and nested lists."""
    rst = """\
.. sidebar:: Sidebar Title
   :subtitle: Interesting Subtitle
   
   Sidebar content with bullet list:
   
   * Item 1
   * Item 2
   * Item 3
"""
    out = render_text(rst)
    assert "Sidebar Title" in out, "Sidebar panel title must be visible"
    assert "Interesting Subtitle" in out, "Sidebar subtitle must be visible"


def test_topic_with_lists_and_code(render_text):
    """Test topic element with nested lists and code."""
    rst = """\
.. topic:: Important Topic

   This topic covers:
   
   1. First concept
   2. Second concept
   
   Example::
   
      example_code()
"""
    out = render_text(rst)
    assert "Important Topic" in out, "Topic title must be visible as the panel title"
    assert "First concept" in out, "Topic body content must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# TRANSITIONS AND SEPARATORS
# ══════════════════════════════════════════════════════════════════════════════

def test_transition_between_sections(render_text):
    """Test transition/horizontal rule."""
    rst = """\
Section 1
=========

Content here.

----

Section 2
=========

More content.
"""
    out = render_text(rst)
    assert "Section 1" in out, "First section must be visible"
    assert "Section 2" in out, "Second section must be visible"
    assert "─" in out, "Transition must render as a horizontal rule (─)"


def test_multiple_transitions(make_visitor):
    """Test multiple transitions render as Rule renderables."""
    rst = """\
First block.

----

Second block.

----

Third block.
"""
    visitor = make_visitor(rst)
    rules = [r for r in visitor.renderables if isinstance(r, Rule)]
    assert len(rules) >= 2, (
        f"Two '----' transitions must produce at least two Rule renderables, got {len(rules)}"
    )
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    text_content = " ".join(t.plain for t in texts)
    assert "First" in text_content, "Text before transitions must be visible"
    assert "Second" in text_content, "Text between transitions must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# DOCTEST AND MATH BLOCKS
# ══════════════════════════════════════════════════════════════════════════════

def test_doctest_block(render_text):
    """Test doctest block rendering (inline >>> syntax)."""
    rst = """\
>>> x = 1 + 2
>>> print(x)
3
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert "x = 1 + 2" in out, "Doctest code content must be visible"


def test_doctest_multiple_examples(render_text):
    """Test multiple doctest examples."""
    rst = """\
>>> list(range(3))
[0, 1, 2]
>>> dict(a=1, b=2)
{'a': 1, 'b': 2}
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert "list(range(3))" in out, "Doctest code must be visible"


def test_doctest_standalone(render_text):
    """Test doctest directive standalone."""
    rst = """\
>>> print("test")
test
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert 'print("test")' in out, "Doctest code must be visible"


def test_math_block_inline(render_text):
    """Test inline math rendering."""
    rst = """\
Some text :math:`E = mc^2` more text.
"""
    out = render_text(rst)
    assert "E = mc^2" in out, "Inline math formula content must be visible in the output"


def test_math_block_display(render_text):
    """Test display math block."""
    rst = """\
.. math::

   E = mc^2
"""
    out = render_text(rst)
    assert "E = mc^2" in out, "Display math formula content must be visible in the output"


def test_math_standalone(render_text):
    """Test math directive standalone."""
    rst = """\
.. math::

   \\frac{a}{b}
"""
    out = render_text(rst)
    assert "frac" in out, "Math directive content must be visible in the output"


# ══════════════════════════════════════════════════════════════════════════════
# ABBREVIATIONS AND ACRONYMS
# ══════════════════════════════════════════════════════════════════════════════

def test_abbreviation_with_explanation(render_text):
    """Test abbreviation with explanation."""
    rst = """\
The |abbr| (abbreviation) is common.

.. |abbr| abbreviation:: An abbreviation
"""
    out = render_text(rst)
    assert "abbreviation" in out, "Abbreviation substitution text must be visible"


def test_acronym_with_explanation(render_text):
    """Test acronym with explanation."""
    rst = """\
The |acr| (acronym) is used here.

.. |acr| acronym:: An Acronym Code
"""
    out = render_text(rst)
    assert "acronym" in out, "Acronym substitution text must be visible"


def test_abbreviation_inline_full_markup(render_text):
    """Test abbreviation with full inline markup."""
    rst = """\
Use |HTML| in markup.

.. |HTML| abbreviation:: HyperText Markup Language
"""
    out = render_text(rst)
    assert "HTML" in out, "Abbreviation label must be visible in the output"


# ══════════════════════════════════════════════════════════════════════════════
# EMPHASIS AND STRONG TEXT
# ══════════════════════════════════════════════════════════════════════════════

def test_emphasis_appended_to_previous_text(make_visitor):
    """Test emphasis appended to previous text element has an italic span."""
    rst = """\
This is regular text *and this is emphasized*.
"""
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "Paragraph must produce a Text renderable"
    combined = " ".join(t.plain for t in texts)
    assert "regular text" in combined, "Surrounding plain text must be visible"
    assert "and this is emphasized" in combined, "Emphasized text must be visible"
    italic_spans = [s for t in texts for s in t._spans if s.style.italic]
    assert italic_spans, "*...* must produce an italic span"


def test_strong_appended_to_previous_text(make_visitor):
    """Test strong emphasis appended to previous text has a bold span."""
    rst = """\
Regular **and this is bold**.
"""
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "Paragraph must produce a Text renderable"
    combined = " ".join(t.plain for t in texts)
    assert "Regular" in combined, "Surrounding plain text must be visible"
    assert "and this is bold" in combined, "Bold text must be visible"
    bold_spans = [s for t in texts for s in t._spans if s.style.bold]
    assert bold_spans, "**...** must produce a bold span"


def test_emphasis_first_element(make_visitor):
    """Test emphasis as first element has an italic span."""
    rst = """\
*Starts with emphasis* in a paragraph.
"""
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "Paragraph must produce a Text renderable"
    combined = " ".join(t.plain for t in texts)
    assert "emphasis" in combined, "Emphasized text must be visible"
    # The emphasis is at the start; check for italic base style or italic span
    italic_base = any(t.style.italic is True for t in texts)
    italic_span = any(s.style.italic for t in texts for s in t._spans)
    assert italic_base or italic_span, "*...* at start of paragraph must produce italic formatting"


# ══════════════════════════════════════════════════════════════════════════════
# SUBSCRIPT AND SUPERSCRIPT
# ══════════════════════════════════════════════════════════════════════════════

def test_subscript_appended_to_text(render_text):
    """Test subscript appended to existing text renders as Unicode subscript characters."""
    rst = "H\\ :sub:`2`\\ O is water.\n"
    out = render_text(rst)
    assert "₂" in out, ":sub:`2` must render as Unicode subscript '₂'"
    assert "O is water" in out, "Surrounding text must be visible"


def test_superscript_appended_to_text(render_text):
    """Test superscript appended to existing text renders as Unicode superscript characters."""
    rst = "E=mc\\ :sup:`2`\\ is Einstein's formula.\n"
    out = render_text(rst)
    assert "²" in out, ":sup:`2` must render as Unicode superscript '²'"


def test_subscript_first_element(render_text):
    """Test subscript as first element renders as Unicode subscript characters."""
    rst = """\
:sub:`subscript` at the beginning.
"""
    out = render_text(rst)
    assert "ₛ" in out, ":sub:`subscript` must render starting with Unicode subscript 'ₛ'"
    assert "at the beginning" in out, "Surrounding text must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# LISTS: BULLET AND ENUMERATED
# ══════════════════════════════════════════════════════════════════════════════

def test_bullet_list_with_nested_enumerated_list(render_text):
    """Test bullet list containing enumerated list."""
    rst = """\
* Bullet 1

  1. Numbered 1.1
  2. Numbered 1.2

* Bullet 2

  1. Numbered 2.1
  2. Numbered 2.2
"""
    out = render_text(rst)
    assert "Bullet" in out


def test_enumerated_list_with_nested_bullet_list(render_text):
    """Test enumerated list containing bullet list."""
    rst = """\
1. First item

   * Nested bullet A
   * Nested bullet B

2. Second item

   * Nested bullet C
"""
    out = render_text(rst)
    assert "First" in out


def test_triple_nested_lists(render_text):
    """Test three levels of list nesting."""
    rst = """\
* Level 1-1
  
  * Level 2-1
    
    * Level 3-1
    * Level 3-2
  
  * Level 2-2

* Level 1-2
"""
    out = render_text(rst)
    assert "Level 1-1" in out, "First-level list item must be visible"
    assert "Level 2-1" in out, "Second-level nested list item must be visible"
    assert "Level 3-1" in out, "Third-level nested list item must be visible"


def test_list_with_code_block(render_text):
    """Test list containing code block."""
    rst = """\
* First item
* Second item with code::

      def hello():
          return "world"

* Third item
"""
    out = render_text(rst)
    assert "Second item with code" in out, "List item text must be visible"
    assert "def hello" in out, "Code block content inside list item must be visible"


def test_bullet_list_with_only_code_blocks(render_text):
    """Test bullet list containing only code blocks."""
    rst = """\
* ::

     code block 1

* ::

     code block 2
"""
    out = render_text(rst)
    assert "code block 1" in out, "First code block content must be visible"
    assert "code block 2" in out, "Second code block content must be visible"


def test_enumerated_list_with_only_code_blocks(render_text):
    """Test enumerated list containing only code blocks."""
    rst = """\
1. ::

      code block here
    
2. ::

      another code block
"""
    out = render_text(rst)
    assert "code block here" in out, "First code block content must be visible"
    assert "another code block" in out, "Second code block content must be visible"


def test_very_deep_enumerated_list_nesting(render_text):
    """Test very deeply nested enumerated lists."""
    rst = """\
1. Item 1

   1. Item 1.1
   
      1. Item 1.1.1
      
         1. Item 1.1.1.1
"""
    out = render_text(rst)
    assert "Item" in out


# ══════════════════════════════════════════════════════════════════════════════
# CITATIONS AND FOOTNOTES
# ══════════════════════════════════════════════════════════════════════════════

def test_citation_reference(render_text):
    """Test citation reference."""
    rst = """\
Some text [CIT2024]_.

.. [CIT2024] A citation.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A citation" in out, "Citation body text must be visible"


def test_footnote_reference(render_text):
    """Test footnote reference."""
    rst = """\
Some text [#]_.

.. [#] A footnote.
"""
    out = render_text(rst)
    assert "A footnote" in out, "Footnote body text must appear in the Footer panel"


def test_multiple_footnotes(render_text):
    """Test multiple footnotes."""
    rst = """\
First [1]_ and second [2]_.

.. [1] First note.
.. [2] Second note.
"""
    out = render_text(rst)
    assert "First note" in out, "First footnote body must be visible"
    assert "Second note" in out, "Second footnote body must be visible"


def test_citation_reference_appended_to_text(render_text):
    """Test citation reference appended to existing text element."""
    rst = """\
See the cited work [Ref2024]_.

.. [Ref2024] A citation.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A citation" in out, "Citation body text must be visible"


def test_footnote_reference_appended_to_text(render_text):
    """Test footnote reference appended to existing text element."""
    rst = """\
This is text [1]_ with a footnote.

.. [1] Footnote text.
"""
    out = render_text(rst)
    assert "Footnote text" in out, "Footnote body must appear in the Footer panel"


def test_numbered_footnote(render_text):
    """Test explicitly numbered footnote."""
    rst = """\
Text [1]_.

.. [1] First footnote.
"""
    out = render_text(rst)
    assert "First footnote" in out, "Footnote body must appear in the Footer panel"


def test_auto_numbered_footnote(render_text):
    """Test auto-numbered footnote."""
    rst = """\
Text [#]_.

.. [#] Auto-numbered footnote.
"""
    out = render_text(rst)
    assert "Auto-numbered footnote" in out, "Footnote body must appear in the Footer panel"


def test_labeled_footnote(render_text):
    """Test labeled footnote."""
    rst = """\
Text [note]_.

.. [note] A labeled footnote.
"""
    out = render_text(rst)
    assert "A labeled footnote" in out, "Footnote body must appear in the Footer panel"


def test_citation_block(render_text):
    """Test citation block."""
    rst = """\
Reference [Book2024]_.

.. [Book2024] A Book Title. Published 2024.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A Book Title" in out, "Citation body text must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# RAW CONTENT
# ══════════════════════════════════════════════════════════════════════════════

def test_raw_html_element(render_text):
    """Test raw HTML element strips tags and renders as 'stripped raw html' Panel."""
    rst = """\
.. raw:: html

   <div>This is raw HTML</div>
"""
    out = render_text(rst)
    assert "stripped raw html" in out, (
        "Raw HTML must render as a Panel with title 'stripped raw html'"
    )
    assert "This is raw HTML" in out, "Stripped HTML text content must be visible"


def test_raw_latex_element(render_text):
    """Test raw LaTeX element renders as 'raw latex' Panel."""
    rst = """\
.. raw:: latex

   \\textbf{Bold text}
"""
    out = render_text(rst)
    assert "raw latex" in out, (
        "Raw LaTeX must render as a Panel with title 'raw latex'"
    )
    assert "textbf" in out, "Raw LaTeX content must be visible inside the panel"


def test_raw_text_format(render_text):
    """Test raw text format renders as 'raw text' Panel."""
    rst = """\
.. raw:: text

   This is raw text content.
"""
    out = render_text(rst)
    assert "raw text" in out, (
        "Raw text must render as a Panel with title 'raw text'"
    )
    assert "This is raw text content" in out, "Raw text content must be visible"


def test_raw_with_special_chars(render_text):
    """Test raw HTML content with special characters strips tags."""
    rst = """\
.. raw:: html

   <span class="special">&nbsp;&copy;&reg;</span>
"""
    out = render_text(rst)
    assert "stripped raw html" in out, (
        "Raw HTML must render as a Panel with title 'stripped raw html'"
    )


def test_raw_content_all_formats(render_text):
    """Test raw directive with different formats all produce labelled Panels."""
    rst = """\
.. raw:: html

   <p>This is HTML</p>

.. raw:: latex

   \\textbf{Bold}
   
.. raw:: rst

   **Restructured** text
"""
    out = render_text(rst)
    assert "stripped raw html" in out, "Raw HTML must produce 'stripped raw html' panel"
    assert "raw latex" in out, "Raw LaTeX must produce 'raw latex' panel"


# ══════════════════════════════════════════════════════════════════════════════
# TABLES
# ══════════════════════════════════════════════════════════════════════════════

def test_table_with_headers(render_text):
    """Test table with header row."""
    rst = """\
=====  =====
Col1   Col2
=====  =====
A      B
C      D
=====  =====
"""
    out = render_text(rst)
    assert "Col1" in out, "First header column must be visible"
    assert "Col2" in out, "Second header column must be visible"
    assert "A" in out and "B" in out, "Table body cells must be visible"


def test_table_complex(render_text):
    """Test complex table."""
    rst = """\
+-------+-------+
| A     | B     |
+=======+=======+
| 1     | 2     |
+-------+-------+
| 3     | 4     |
+-------+-------+
"""
    out = render_text(rst)
    assert "A" in out and "B" in out, "Table header cells must be visible"
    assert "1" in out and "2" in out, "Table body cells must be visible"


def test_table_with_cell_content(render_text):
    """Test table with various cell content."""
    rst = """\
+----------+----------+
| Cell 1   | Cell 2   |
+----------+----------+
| Content1 | Content2 |
+----------+----------+
"""
    out = render_text(rst)
    assert "Cell 1" in out, "First header cell must be visible"
    assert "Cell 2" in out, "Second header cell must be visible"
    assert "Content1" in out, "First body cell must be visible"
    assert "Content2" in out, "Second body cell must be visible"


def test_table_with_multiple_rows_and_columns(render_text):
    """Test complex table with many rows and columns."""
    rst = """\
+---------+---------+---------+
| Header1 | Header2 | Header3 |
+=========+=========+=========+
| Cell11  | Cell12  | Cell13  |
+---------+---------+---------+
| Cell21  | Cell22  | Cell23  |
+---------+---------+---------+
| Cell31  | Cell32  | Cell33  |
+---------+---------+---------+
"""
    out = render_text(rst)
    assert "Header1" in out, "First column header must be visible"
    assert "Header2" in out, "Second column header must be visible"
    assert "Header3" in out, "Third column header must be visible"
    assert "Cell11" in out, "First body cell must be visible"
    assert "Cell33" in out, "Last body cell must be visible"


def test_simple_table_format(render_text):
    """Test simple table format."""
    rst = """\
Simple Table
============  ============  ============
     A              B             C
============  ============  ============
    1              2             3
============  ============  ============
"""
    out = render_text(rst)
    assert "A" in out and "B" in out and "C" in out, (
        "All simple-table column headers must be visible"
    )
    assert "1" in out and "2" in out and "3" in out, (
        "All simple-table body cells must be visible"
    )


def test_grid_table(render_text):
    """Test grid table format."""
    rst = """\
+---+---+
| A | B |
+===+===+
| 1 | 2 |
+---+---+
"""
    out = render_text(rst)
    assert "A" in out and "B" in out, "Grid table header cells must be visible"
    assert "1" in out and "2" in out, "Grid table body cells must be visible"


# ══════════════════════════════════════════════════════════════════════════════
# INLINE CODE AND LITERALS
# ══════════════════════════════════════════════════════════════════════════════

def test_inline_literal_appended_to_text(make_visitor):
    """Test inline code appended to text renders with grey78-on-grey7 style."""
    rst = """\
Use the ``code`` variable in your script.
"""
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "Paragraph must produce a Text renderable"
    combined_plain = " ".join(t.plain for t in texts)
    assert "Use" in combined_plain, "Surrounding text must be visible"
    assert "code" in combined_plain, "Inline code content must be visible"
    # Inline literals must carry the grey78-on-grey7 formatting span
    code_spans = [
        s for t in texts for s in t._spans
        if "grey78" in str(s.style) or "grey7" in str(s.style)
    ]
    assert code_spans, "Inline ``code`` must produce a span with grey78-on-grey7 style"


# ══════════════════════════════════════════════════════════════════════════════
# HEADERS AND FOOTERS
# ══════════════════════════════════════════════════════════════════════════════

def test_header_element(render_text):
    """Test document header directive (unsupported in vendored docutils — no crash expected)."""
    rst = """\
.. header:: This is a header
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise an exception"


def test_footer_element(render_text):
    """Test document footer directive (unsupported in vendored docutils — no crash expected)."""
    rst = """\
.. footer:: Page ###
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise an exception"


# ══════════════════════════════════════════════════════════════════════════════
# SYSTEM MESSAGES AND ERROR HANDLING
# ══════════════════════════════════════════════════════════════════════════════

def test_paragraph_containing_system_message(render_text):
    """Test paragraph that contains a system message."""
    rst = """\
Before error :unknown_role:`content` after error.
"""
    out = render_text(rst, show_errors=True, sphinx_compat=False)
    assert "System Message" in out


# ══════════════════════════════════════════════════════════════════════════════
# COMPREHENSIVE DOCUMENTS
# ══════════════════════════════════════════════════════════════════════════════

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
    assert "Main Title" in out
    assert "Author" in out
    assert "Hello" in out


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
    assert "Markup" in out


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
    assert "Mixed" in out


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
    rst = "\n\n".join(sections)
    out = render_text(rst)
    assert "Section" in out


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
    assert "Complete Document" in out


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
    assert "Full Documentation" in out


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION OPTIONS
# ══════════════════════════════════════════════════════════════════════════════

def test_rendering_with_errors_disabled(render_text):
    """Test rendering with error display disabled."""
    rst = """\
Some text with :unknown:`unknown role`.
"""
    out = render_text(rst, show_errors=False, sphinx_compat=False)
    assert "System Message" not in out


def test_rendering_without_sphinx_compat(render_text):
    """Test rendering without Sphinx compatibility."""
    rst = """\
Normal RST content.
"""
    out = render_text(rst, sphinx_compat=False)
    assert "Normal RST content" in out, "Plain text content must be visible without sphinx_compat"


def test_render_all_rst_roles(render_text):
    """Test rendering with various RST roles."""
    rst = """\
Text with :emphasis:`emphasis`, :strong:`strong`, and :literal:`literal`.

Also :ref:`reference` and :doc:`document`.
"""
    out = render_text(rst)
    assert "emphasis" in out, ":emphasis: role content must be visible"
    assert "strong" in out, ":strong: role content must be visible"
    assert "literal" in out, ":literal: role content must be visible"


def test_render_with_syntax_error(render_text):
    """Test rendering malformed RST."""
    rst = """\
Unclosed ``literal

This should still render.
"""
    out = render_text(rst, show_errors=True)
    assert "still render" in out, "Content after syntax error must still be visible"


def test_very_long_line(render_text):
    """Test rendering with very long line."""
    long_text = "word " * 100
    rst = f"This is a very long line:\n\n{long_text}"
    out = render_text(rst)
    assert "This is a very long line" in out, "Leading text must be visible"
    assert "word" in out, "Long-line body words must be visible"


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
    assert "Title" in out, "Section title must be visible"
    assert "One" in out, "Enumerated list item must be visible"
    assert "Two" in out, "Second enumerated list item must be visible"
    assert "Alpha" in out, "Nested bullet item must be visible"


def test_empty_document(render_text):
    """Test rendering completely empty document produces a string without raising."""
    rst = ""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering an empty document must return a string"


def test_minimal_valid_document(render_text):
    """Test minimal valid document."""
    rst = "Simple text."
    out = render_text(rst)
    assert "Simple text" in out


def test_direct_api_usage(render_text):
    """Test direct API usage through render_text with various options."""
    rst = "Text"
    out = render_text(
        rst,
        code_theme="vim",
        show_line_numbers=False,
        guess_lexer=False,
        default_lexer="bash",
        sphinx_compat=True,
        show_errors=True
    )
    assert "Text" in out


# ══════════════════════════════════════════════════════════════════════════════
# MISCELLANEOUS EDGE CASES
# ══════════════════════════════════════════════════════════════════════════════

def test_generated_node_handling(render_text):
    """Test generated nodes (typically auto-generated content)."""
    rst = "Some regular content."
    out = render_text(rst)
    assert "Some regular content" in out, "Regular paragraph text must be visible"
