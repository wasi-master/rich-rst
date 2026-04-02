"""Tests for standard reStructuredText interpreted-text roles.

Covers all roles defined in the RST specification:
  :emphasis:, :strong:, :literal:, :code:, :math:,
  :pep-reference: / :PEP:, :rfc-reference: / :RFC:,
  :sub: / :subscript:, :sup: / :superscript:,
  :title-reference: / :title: / :t:

Each role is tested independently so a failure identifies the exact role.
"""
from rich.text import Text


# ── :emphasis: ───────────────────────────────────────────────────────────────

def test_role_emphasis_content_visible(render_text):
    assert "italic text" in render_text(":emphasis:`italic text`")


def test_role_emphasis_produces_text_renderable(make_visitor):
    visitor = make_visitor(":emphasis:`hello`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("hello" in t.plain for t in texts)


# ── :strong: ─────────────────────────────────────────────────────────────────

def test_role_strong_content_visible(render_text):
    assert "bold text" in render_text(":strong:`bold text`")


def test_role_strong_produces_text_renderable(make_visitor):
    visitor = make_visitor(":strong:`hello`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("hello" in t.plain for t in texts)


# ── :literal: ────────────────────────────────────────────────────────────────

def test_role_literal_content_visible(render_text):
    assert "code text" in render_text(":literal:`code text`")


def test_role_literal_produces_text_renderable(make_visitor):
    visitor = make_visitor(":literal:`value`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("value" in t.plain for t in texts)


# ── :code: ───────────────────────────────────────────────────────────────────

def test_role_code_content_visible(render_text):
    assert "import os" in render_text(":code:`import os`")


# ── :math: (inline) ──────────────────────────────────────────────────────────

def test_role_math_content_visible(render_text):
    assert "x^2" in render_text(":math:`x^2`")


def test_role_math_in_sentence(render_text):
    assert "E = mc^2" in render_text("The formula :math:`E = mc^2`.")


# ── :pep-reference: / :PEP: ──────────────────────────────────────────────────

def test_role_pep_short_alias(render_text):
    # Docutils renders :PEP:`8` as a hyperlink with text "PEP 8"
    out = render_text(":PEP:`8`")
    assert "8" in out


def test_role_pep_reference_long_form(render_text):
    out = render_text(":pep-reference:`287`")
    assert "287" in out


# ── :rfc-reference: / :RFC: ──────────────────────────────────────────────────

def test_role_rfc_short_alias(render_text):
    out = render_text(":RFC:`2822`")
    assert "2822" in out


def test_role_rfc_reference_long_form(render_text):
    out = render_text(":rfc-reference:`1945`")
    assert "1945" in out


# ── :sub: / :subscript: ──────────────────────────────────────────────────────

def test_role_sub_translates_digit(make_visitor):
    visitor = make_visitor(":sub:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "₂" in combined


def test_role_subscript_full_name_translates_digit(make_visitor):
    visitor = make_visitor(":subscript:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "₂" in combined


def test_role_sub_translates_multiple_digits(make_visitor):
    visitor = make_visitor(":sub:`12`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "₁₂" in combined


# ── :sup: / :superscript: ────────────────────────────────────────────────────

def test_role_sup_translates_digit(make_visitor):
    visitor = make_visitor(":sup:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "²" in combined


def test_role_superscript_full_name_translates_digit(make_visitor):
    visitor = make_visitor(":superscript:`2`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "²" in combined


def test_role_sup_translates_multiple_digits(make_visitor):
    visitor = make_visitor(":sup:`10`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "¹⁰" in combined


# ── :title-reference: / :title: / :t: ────────────────────────────────────────

def test_role_title_reference_long_form(make_visitor):
    visitor = make_visitor(":title-reference:`My Book`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any("My Book" in t.plain for t in texts)


def test_role_title_short_alias(render_text):
    assert "Dune" in render_text(":title:`Dune`")


def test_role_t_alias(render_text):
    assert "Dune" in render_text(":t:`Dune`")


def test_role_title_reference_in_sentence(render_text):
    out = render_text("Read :title-reference:`Design Patterns` for more.")
    assert "Design Patterns" in out
