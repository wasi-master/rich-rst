"""Tests for inline markup elements.

Covers: emphasis, strong, inline literal/code, title-reference,
subscript, superscript, abbreviation, and acronym — both via the
asterisk / backtick shorthand syntax and via explicit roles.

Formatting contract
-------------------
* **Standalone** (the markup is the entire paragraph) — the rendered
  ``Text`` object carries the style as its *base* style (``text.style``).
* **In sentence** — the rendered ``Text`` carries the markup style as a
  ``Span`` covering the marked-up characters; the rest of the text resets
  to the default style.

All span assertions use ``span.style.*`` attributes, not string rendering,
so they are insensitive to colour-name capitalisation or repr format changes.
"""
from rich.text import Text
import pytest
from rich.console import Console
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
import rich_rst
import rich_rst._vendor.docutils.core
from rich_rst._vendor import docutils
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


def _get_paragraph_text(visitor):
    """Return the first Text renderable from the visitor."""
    return next(r for r in visitor.renderables if isinstance(r, Text))


def _spans_with(text_obj, *, italic=None, bold=None, color_name=None, bgcolor_name=None, underline=None):
    """Return all Spans on *text_obj* that match every provided criterion."""
    result = []
    for span in text_obj._spans:
        s = span.style
        if italic is not None and bool(s.italic) != italic:
            continue
        if bold is not None and bool(s.bold) != bold:
            continue
        if underline is not None and bool(s.underline) != underline:
            continue
        if color_name is not None:
            if s.color is None or s.color.name != color_name:
                continue
        if bgcolor_name is not None:
            if s.bgcolor is None or s.bgcolor.name != bgcolor_name:
                continue
        result.append(span)
    return result


# ── Emphasis ──────────────────────────────────────────────────────────────────

def test_emphasis_standalone_base_style_is_italic(make_visitor):
    # When *text* is the entire paragraph the base style is italic.
    t = _get_paragraph_text(make_visitor("*hello*"))
    assert t.plain.startswith("hello"), "Plain text must contain the word"
    assert t.style.italic is True, "Standalone emphasis must have italic base style"


def test_emphasis_in_sentence_has_italic_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Before *italic* after."))
    spans = _spans_with(t, italic=True)
    assert spans, "Emphasis in a sentence must produce an italic span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "italic", f"Italic span must cover the word 'italic', got {marked!r}"


def test_emphasis_role_has_italic_span(make_visitor):
    t = _get_paragraph_text(make_visitor(":emphasis:`hello`"))
    # Could be base style (standalone) or span; either way italic must apply
    italic_via_base = t.style.italic is True
    italic_via_span = bool(_spans_with(t, italic=True))
    assert italic_via_base or italic_via_span, ":emphasis: must apply italic formatting"


def test_emphasis_multiword_span_covers_full_phrase(make_visitor):
    t = _get_paragraph_text(make_visitor("Say *two words* now."))
    spans = _spans_with(t, italic=True)
    assert spans
    assert t.plain[spans[0].start : spans[0].end] == "two words"


# ── Strong ────────────────────────────────────────────────────────────────────

def test_strong_standalone_base_style_is_bold(make_visitor):
    t = _get_paragraph_text(make_visitor("**bold**"))
    assert t.plain.startswith("bold")
    assert t.style.bold is True, "Standalone strong must have bold base style"


def test_strong_in_sentence_has_bold_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Before **bold** after."))
    spans = _spans_with(t, bold=True)
    assert spans, "Strong in a sentence must produce a bold span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "bold", f"Bold span must cover 'bold', got {marked!r}"


def test_strong_role_has_bold_formatting(make_visitor):
    t = _get_paragraph_text(make_visitor(":strong:`hello`"))
    bold_via_base = t.style.bold is True
    bold_via_span = bool(_spans_with(t, bold=True))
    assert bold_via_base or bold_via_span, ":strong: must apply bold formatting"


# ── Inline literal / code ─────────────────────────────────────────────────────

def test_inline_literal_standalone_base_style(make_visitor):
    # Standalone ``code`` paragraph: base style carries the code colours.
    t = _get_paragraph_text(make_visitor("``value``"))
    assert t.plain.startswith("value")
    assert t.style.color is not None and t.style.color.name == "grey78", (
        "Inline literal base style must have grey78 foreground"
    )
    assert t.style.bgcolor is not None and t.style.bgcolor.name == "grey7", (
        "Inline literal base style must have grey7 background"
    )


def test_inline_literal_in_sentence_has_code_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Use ``print()`` here."))
    spans = _spans_with(t, color_name="grey78", bgcolor_name="grey7")
    assert spans, "Inline literal in a sentence must produce a grey78-on-grey7 span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "print()", f"Code span must cover 'print()', got {marked!r}"


def test_literal_role_in_sentence_has_code_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Use :literal:`value` here."))
    spans = _spans_with(t, color_name="grey78", bgcolor_name="grey7")
    assert spans, ":literal: in a sentence must produce a grey78-on-grey7 span"


def test_code_role_in_sentence_has_code_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Run :code:`import os` first."))
    spans = _spans_with(t, color_name="grey78", bgcolor_name="grey7")
    assert spans, ":code: role must produce a grey78-on-grey7 span"


def test_inline_literal_with_spaces(make_visitor):
    t = _get_paragraph_text(make_visitor("``x = 1``"))
    assert t.plain.startswith("x = 1")
    assert t.style.color is not None and t.style.color.name == "grey78"


# ── Title reference ───────────────────────────────────────────────────────────

def test_title_reference_standalone_base_style_is_italic(make_visitor):
    t = _get_paragraph_text(make_visitor(":title-reference:`My Book`"))
    assert t.plain.startswith("My Book")
    assert t.style.italic is True, "Standalone title-reference must have italic base style"


def test_title_reference_in_sentence_has_italic_span(make_visitor):
    t = _get_paragraph_text(make_visitor("Read :title-reference:`Design Patterns` for more."))
    spans = _spans_with(t, italic=True)
    assert spans, "Title-reference in a sentence must produce an italic span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "Design Patterns"


def test_title_role_alias_is_italic(make_visitor):
    t = _get_paragraph_text(make_visitor(":title:`Dune`"))
    italic_base = t.style.italic is True
    italic_span = bool(_spans_with(t, italic=True))
    assert italic_base or italic_span, ":title: alias must produce italic formatting"


def test_t_role_alias_is_italic(make_visitor):
    t = _get_paragraph_text(make_visitor(":t:`Dune`"))
    italic_base = t.style.italic is True
    italic_span = bool(_spans_with(t, italic=True))
    assert italic_base or italic_span, ":t: alias must produce italic formatting"


# ── Subscript ─────────────────────────────────────────────────────────────────

def test_subscript_translates_digit_to_unicode(make_visitor):
    t = _get_paragraph_text(make_visitor(":sub:`2`"))
    assert "₂" in t.plain, "Subscript digit '2' must become '₂'"


def test_subscript_full_name_alias(make_visitor):
    t = _get_paragraph_text(make_visitor(":subscript:`2`"))
    assert "₂" in t.plain, ":subscript: alias must also translate '2' to '₂'"


def test_subscript_translates_multiple_digits(make_visitor):
    t = _get_paragraph_text(make_visitor(":sub:`12`"))
    assert "₁₂" in t.plain, "Subscript '12' must become '₁₂'"


def test_subscript_translates_letter(make_visitor):
    t = _get_paragraph_text(make_visitor(":sub:`n`"))
    assert "ₙ" in t.plain, "Subscript letter 'n' must become 'ₙ'"


# ── Superscript ──────────────────────────────────────────────────────────────

def test_superscript_translates_digit_to_unicode(make_visitor):
    t = _get_paragraph_text(make_visitor(":sup:`2`"))
    assert "²" in t.plain, "Superscript '2' must become '²'"


def test_superscript_full_name_alias(make_visitor):
    t = _get_paragraph_text(make_visitor(":superscript:`2`"))
    assert "²" in t.plain, ":superscript: alias must also translate '2' to '²'"


def test_superscript_translates_multiple_digits(make_visitor):
    t = _get_paragraph_text(make_visitor(":sup:`10`"))
    assert "¹⁰" in t.plain, "Superscript '10' must become '¹⁰'"


# ── Abbreviation ─────────────────────────────────────────────────────────────

def test_abbreviation_standalone_has_underline_style(make_visitor):
    t = _get_paragraph_text(make_visitor(":abbreviation:`HTML`"))
    assert t.plain.startswith("HTML")
    assert t.style.underline is True, "Standalone abbreviation must have underline base style"


def test_abbreviation_in_sentence_has_underline_span(make_visitor):
    t = _get_paragraph_text(make_visitor("The :abbreviation:`CSS (Cascading Style Sheets)` standard."))
    spans = _spans_with(t, underline=True)
    assert spans, "Abbreviation in a sentence must produce an underline span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "CSS (Cascading Style Sheets)", (
        f"Underline span must cover the full abbreviation text, got {marked!r}"
    )


def test_abbreviation_expansion_text_included_in_plain(make_visitor):
    t = _get_paragraph_text(make_visitor(":abbreviation:`CSS (Cascading Style Sheets)`"))
    assert "CSS (Cascading Style Sheets)" in t.plain


# ── Acronym ───────────────────────────────────────────────────────────────────

def test_acronym_standalone_has_underline_style(make_visitor):
    t = _get_paragraph_text(make_visitor(":acronym:`API`"))
    assert t.plain.startswith("API")
    assert t.style.underline is True, "Standalone acronym must have underline base style"


def test_acronym_in_sentence_has_underline_span(make_visitor):
    t = _get_paragraph_text(make_visitor("The :acronym:`RST (reStructuredText)` format."))
    spans = _spans_with(t, underline=True)
    assert spans, "Acronym in a sentence must produce an underline span"


def test_acronym_expansion_text_included(make_visitor):
    t = _get_paragraph_text(make_visitor(":acronym:`RST (reStructuredText)`"))
    assert "RST (reStructuredText)" in t.plain


# ── Mixed inline elements in the same paragraph ───────────────────────────────

def test_bold_and_italic_in_same_paragraph_have_distinct_spans(make_visitor):
    t = _get_paragraph_text(make_visitor("This has **bold** and *italic* in the same line."))
    bold_spans = _spans_with(t, bold=True)
    italic_spans = _spans_with(t, italic=True)
    assert bold_spans, "Mixed paragraph must have a bold span"
    assert italic_spans, "Mixed paragraph must have an italic span"
    assert t.plain[bold_spans[0].start : bold_spans[0].end] == "bold"
    assert t.plain[italic_spans[0].start : italic_spans[0].end] == "italic"


def test_code_and_bold_and_italic_each_get_correct_span(make_visitor):
    # Put bold/italic/code in the middle of a sentence so they get spans (not base style)
    t = _get_paragraph_text(make_visitor("See **A** and *B* and ``C``."))
    bold_spans   = _spans_with(t, bold=True)
    italic_spans = _spans_with(t, italic=True)
    code_spans   = _spans_with(t, color_name="grey78", bgcolor_name="grey7")
    assert bold_spans   and t.plain[bold_spans[0].start   : bold_spans[0].end]   == "A"
    assert italic_spans and t.plain[italic_spans[0].start : italic_spans[0].end] == "B"
    assert code_spans   and t.plain[code_spans[0].start   : code_spans[0].end]   == "C"

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

def test_subscript_preserves_untranslatable_characters(render_text):
    """Unsupported subscript chars must fall back to plain text instead of disappearing."""
    rst = "x\\ :sub:`A?#`\\ y\n"
    out = render_text(rst)
    assert "A?#" in out, "Untranslatable subscript chars must remain visible"

def test_superscript_preserves_untranslatable_characters(render_text):
    """Unsupported superscript chars must fall back to plain text instead of disappearing."""
    rst = "x\\ :sup:`@_#`\\ y\n"
    out = render_text(rst)
    assert "@_#" in out, "Untranslatable superscript chars must remain visible"

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
