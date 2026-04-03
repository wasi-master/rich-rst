"""Tests for standard reStructuredText interpreted-text roles.

Covers all roles defined in the RST specification:
  :emphasis:, :strong:, :literal:, :code:, :math:,
  :pep-reference: / :PEP:, :rfc-reference: / :RFC:,
  :sub: / :subscript:, :sup: / :superscript:,
  :title-reference: / :title: / :t:

Each role is tested independently.  Where a role applies formatting, the
test verifies the correct ``rich.style.Style`` attributes rather than just
the presence of the text in the output.

Formatting contract (in-sentence context)
-----------------------------------------
* ``:emphasis:``     → italic span
* ``:strong:``       → bold span
* ``:literal:``      → grey78-on-grey7 span
* ``:code:``         → grey78-on-grey7 span
* ``:title-reference:`` / ``:title:`` / ``:t:`` → italic span (or base style)
* ``:sub:`` / ``:subscript:``   → digit/letter translated to subscript Unicode
* ``:sup:`` / ``:superscript:`` → digit/letter translated to superscript Unicode
"""
from rich.text import Text


def _get_text(make_visitor, rst):
    visitor = make_visitor(rst)
    return next(r for r in visitor.renderables if isinstance(r, Text))


def _italic_spans(t):
    return [s for s in t._spans if s.style.italic]


def _bold_spans(t):
    return [s for s in t._spans if s.style.bold]


def _code_spans(t):
    return [
        s for s in t._spans
        if s.style.color and s.style.color.name == "grey78"
        and s.style.bgcolor and s.style.bgcolor.name == "grey7"
    ]


# ── :emphasis: ───────────────────────────────────────────────────────────────

def test_role_emphasis_standalone_has_italic_base_style(make_visitor):
    t = _get_text(make_visitor, ":emphasis:`italic text`")
    italic_base = t.style.italic is True
    italic_span = bool(_italic_spans(t))
    assert italic_base or italic_span, ":emphasis: must produce italic formatting"


def test_role_emphasis_in_sentence_has_italic_span(make_visitor):
    t = _get_text(make_visitor, "Text :emphasis:`hello` here.")
    spans = _italic_spans(t)
    assert spans, ":emphasis: in sentence must produce an italic span"
    assert t.plain[spans[0].start : spans[0].end] == "hello"


# ── :strong: ─────────────────────────────────────────────────────────────────

def test_role_strong_standalone_has_bold_base_style(make_visitor):
    t = _get_text(make_visitor, ":strong:`bold text`")
    bold_base = t.style.bold is True
    bold_span = bool(_bold_spans(t))
    assert bold_base or bold_span, ":strong: must produce bold formatting"


def test_role_strong_in_sentence_has_bold_span(make_visitor):
    t = _get_text(make_visitor, "Text :strong:`hello` here.")
    spans = _bold_spans(t)
    assert spans, ":strong: in sentence must produce a bold span"
    assert t.plain[spans[0].start : spans[0].end] == "hello"


# ── :literal: ────────────────────────────────────────────────────────────────

def test_role_literal_standalone_has_code_style(make_visitor):
    t = _get_text(make_visitor, ":literal:`code text`")
    assert t.style.color and t.style.color.name == "grey78", (
        ":literal: standalone must have grey78 foreground"
    )
    assert t.style.bgcolor and t.style.bgcolor.name == "grey7", (
        ":literal: standalone must have grey7 background"
    )


def test_role_literal_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Use :literal:`value` here.")
    spans = _code_spans(t)
    assert spans, ":literal: in sentence must produce a grey78-on-grey7 span"
    assert t.plain[spans[0].start : spans[0].end] == "value"


# ── :code: ───────────────────────────────────────────────────────────────────

def test_role_code_standalone_has_code_style(make_visitor):
    t = _get_text(make_visitor, ":code:`import os`")
    assert t.style.color and t.style.color.name == "grey78"
    assert t.style.bgcolor and t.style.bgcolor.name == "grey7"


def test_role_code_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Run :code:`import os` first.")
    spans = _code_spans(t)
    assert spans, ":code: in sentence must produce a grey78-on-grey7 span"


# ── :math: (inline) ──────────────────────────────────────────────────────────

def test_role_math_content_in_plain_text(make_visitor):
    t = _get_text(make_visitor, ":math:`x^2`")
    assert "x^2" in t.plain, "Inline math must include the LaTeX source in plain text"


def test_role_math_in_sentence_content_visible(render_text):
    assert "E = mc^2" in render_text("The formula :math:`E = mc^2`.")


# ── :pep-reference: / :PEP: ──────────────────────────────────────────────────

def test_role_pep_number_in_output(render_text):
    out = render_text(":PEP:`8`")
    assert "PEP 8" in out, f":PEP: must render as 'PEP 8', got {out!r}"


def test_role_pep_reference_long_form_number(render_text):
    out = render_text(":pep-reference:`287`")
    assert "PEP 287" in out, f":pep-reference: must render as 'PEP 287', got {out!r}"


# ── :rfc-reference: / :RFC: ──────────────────────────────────────────────────

def test_role_rfc_number_in_output(render_text):
    out = render_text(":RFC:`2822`")
    assert "RFC 2822" in out, f":RFC: must render as 'RFC 2822', got {out!r}"


def test_role_rfc_reference_long_form_number(render_text):
    out = render_text(":rfc-reference:`1945`")
    assert "RFC 1945" in out, f":rfc-reference: must render as 'RFC 1945', got {out!r}"


# ── :sub: / :subscript: ──────────────────────────────────────────────────────

def test_role_sub_digit_translated_to_subscript_unicode(make_visitor):
    t = _get_text(make_visitor, ":sub:`2`")
    assert "₂" in t.plain, ":sub:`2` must translate to '₂'"


def test_role_subscript_full_name_digit_translation(make_visitor):
    t = _get_text(make_visitor, ":subscript:`2`")
    assert "₂" in t.plain, ":subscript:`2` must translate to '₂'"


def test_role_sub_multiple_digits(make_visitor):
    t = _get_text(make_visitor, ":sub:`12`")
    assert "₁₂" in t.plain, ":sub:`12` must translate to '₁₂'"


def test_role_sub_letter_translated(make_visitor):
    t = _get_text(make_visitor, ":sub:`n`")
    assert "ₙ" in t.plain, ":sub:`n` must translate to 'ₙ'"


# ── :sup: / :superscript: ────────────────────────────────────────────────────

def test_role_sup_digit_translated_to_superscript_unicode(make_visitor):
    t = _get_text(make_visitor, ":sup:`2`")
    assert "²" in t.plain, ":sup:`2` must translate to '²'"


def test_role_superscript_full_name_digit_translation(make_visitor):
    t = _get_text(make_visitor, ":superscript:`2`")
    assert "²" in t.plain, ":superscript:`2` must translate to '²'"


def test_role_sup_multiple_digits(make_visitor):
    t = _get_text(make_visitor, ":sup:`10`")
    assert "¹⁰" in t.plain, ":sup:`10` must translate to '¹⁰'"


# ── :title-reference: / :title: / :t: ────────────────────────────────────────

def test_role_title_reference_standalone_italic(make_visitor):
    t = _get_text(make_visitor, ":title-reference:`My Book`")
    italic_base = t.style.italic is True
    italic_span = bool(_italic_spans(t))
    assert italic_base or italic_span, ":title-reference: must produce italic formatting"


def test_role_title_reference_in_sentence_italic_span(make_visitor):
    t = _get_text(make_visitor, "Read :title-reference:`Design Patterns` for more.")
    spans = _italic_spans(t)
    assert spans, ":title-reference: in sentence must produce an italic span"
    assert t.plain[spans[0].start : spans[0].end] == "Design Patterns"


def test_role_title_alias_is_italic(make_visitor):
    t = _get_text(make_visitor, ":title:`Dune`")
    italic_base = t.style.italic is True
    italic_span = bool(_italic_spans(t))
    assert italic_base or italic_span, ":title: alias must produce italic formatting"


def test_role_t_alias_is_italic(make_visitor):
    t = _get_text(make_visitor, ":t:`Dune`")
    italic_base = t.style.italic is True
    italic_span = bool(_italic_spans(t))
    assert italic_base or italic_span, ":t: alias must produce italic formatting"
