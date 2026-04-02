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
