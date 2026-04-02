"""Tests for inline markup elements.

Covers: emphasis, strong, inline literal/code, title-reference,
subscript, superscript, abbreviation, and acronym — both via the
asterisk / backtick shorthand syntax and via explicit roles.
"""
from rich.text import Text


# ── Emphasis ──────────────────────────────────────────────────────────────────

def test_emphasis_star_syntax_appears_in_output(render_text):
    assert "hello" in render_text("*hello*")


def test_emphasis_produces_text_renderable(make_visitor):
    visitor = make_visitor("*hello*")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("hello" in t.plain for t in texts)


def test_emphasis_mixed_in_paragraph(render_text):
    out = render_text("Before *italic* after.")
    assert "Before" in out
    assert "italic" in out
    assert "after." in out


def test_emphasis_role_equivalent_to_star(render_text):
    assert "italic text" in render_text(":emphasis:`italic text`")


def test_emphasis_multiword(render_text):
    assert "two words" in render_text("*two words*")


# ── Strong ────────────────────────────────────────────────────────────────────

def test_strong_double_star_appears_in_output(render_text):
    assert "hello" in render_text("**hello**")


def test_strong_produces_text_renderable(make_visitor):
    visitor = make_visitor("**bold**")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("bold" in t.plain for t in texts)


def test_strong_mixed_in_paragraph(render_text):
    out = render_text("Before **bold** after.")
    assert "Before" in out
    assert "bold" in out
    assert "after." in out


def test_strong_role_equivalent_to_double_star(render_text):
    assert "bold text" in render_text(":strong:`bold text`")


# ── Inline literal / code ─────────────────────────────────────────────────────

def test_inline_literal_double_backtick(render_text):
    assert "print()" in render_text("Use ``print()`` here.")


def test_inline_literal_produces_text_renderable(make_visitor):
    visitor = make_visitor("``value``")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("value" in t.plain for t in texts)


def test_inline_literal_role(render_text):
    assert "value" in render_text(":literal:`value`")


def test_code_role(render_text):
    assert "import os" in render_text(":code:`import os`")


def test_inline_literal_with_spaces(render_text):
    assert "x = 1" in render_text("``x = 1``")


# ── Title reference ───────────────────────────────────────────────────────────

def test_title_reference_default_backtick(render_text):
    assert "Design Patterns" in render_text("`Design Patterns`")


def test_title_reference_explicit_role(render_text):
    assert "The Hobbit" in render_text(":title-reference:`The Hobbit`")


def test_title_role_short_alias(render_text):
    assert "Dune" in render_text(":title:`Dune`")


def test_t_role_alias(render_text):
    assert "Dune" in render_text(":t:`Dune`")


def test_title_reference_produces_text_renderable(make_visitor):
    visitor = make_visitor(":title-reference:`My Book`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("My Book" in t.plain for t in texts)


# ── Subscript ─────────────────────────────────────────────────────────────────

def test_subscript_sub_role_translates_digit(make_visitor):
    visitor = make_visitor(":sub:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "₂" in combined


def test_subscript_subscript_role_alias(make_visitor):
    visitor = make_visitor(":subscript:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "₂" in combined


def test_subscript_in_context(render_text):
    out = render_text(r"H\ :sub:`2`\ O")
    assert "₂" in out or "2" in out  # at minimum the digit appears


def test_subscript_letters(make_visitor):
    visitor = make_visitor(":sub:`n`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    # 'n' maps to 'ₙ' in the subscript table
    assert "ₙ" in combined or "n" in combined


# ── Superscript ──────────────────────────────────────────────────────────────

def test_superscript_sup_role_translates_digit(make_visitor):
    visitor = make_visitor(":sup:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "²" in combined


def test_superscript_superscript_role_alias(make_visitor):
    visitor = make_visitor(":superscript:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "²" in combined


def test_superscript_in_context(render_text):
    out = render_text(r"E = mc\ :sup:`2`")
    assert "²" in out or "2" in out


# ── Abbreviation ─────────────────────────────────────────────────────────────

def test_abbreviation_text_visible(render_text):
    out = render_text("The :abbreviation:`HTML` standard.")
    assert "HTML" in out


def test_abbreviation_with_parenthetical_expansion(render_text):
    out = render_text("The :abbreviation:`CSS (Cascading Style Sheets)` standard.")
    assert "CSS" in out
    assert "Cascading Style Sheets" in out


def test_abbreviation_produces_text_renderable(make_visitor):
    visitor = make_visitor(":abbreviation:`XML`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("XML" in t.plain for t in texts)


# ── Acronym ───────────────────────────────────────────────────────────────────

def test_acronym_text_visible(render_text):
    out = render_text("The :acronym:`API` endpoint.")
    assert "API" in out


def test_acronym_with_parenthetical_expansion(render_text):
    out = render_text("The :acronym:`RST (reStructuredText)` format.")
    assert "RST" in out
    assert "reStructuredText" in out


def test_acronym_produces_text_renderable(make_visitor):
    visitor = make_visitor(":acronym:`URL`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("URL" in t.plain for t in texts)


# ── Mixed inline elements in the same paragraph ───────────────────────────────

def test_bold_and_italic_in_same_paragraph(render_text):
    out = render_text("This has **bold** and *italic* in the same line.")
    assert "bold" in out
    assert "italic" in out


def test_code_and_text_in_same_paragraph(render_text):
    out = render_text("Use ``print()`` to display output.")
    assert "print()" in out
    assert "display output" in out


def test_multiple_inline_elements_in_paragraph(render_text):
    out = render_text("**A**, *B*, ``C``.")
    assert "A" in out
    assert "B" in out
    assert "C" in out
