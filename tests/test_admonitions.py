"""Tests for all admonition directives.

Covers: note, warning, tip, caution, danger, hint, important, error,
attention, and the generic ``.. admonition::`` directive — including the
panel title, admonition body text, and inline markup inside the body.
"""
from rich.panel import Panel


def _visitor_for(make_visitor, directive):
    """Return a visitor for a minimal admonition of *directive* type."""
    rst = f".. {directive}::\n\n   Body text.\n"
    return make_visitor(rst)


def _first_panel(make_visitor, directive):
    visitor = _visitor_for(make_visitor, directive)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, f".. {directive}:: must produce at least one Panel"
    return panels[0]


# ── Each admonition type produces a panel ────────────────────────────────────

def test_note_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "note"), Panel)


def test_warning_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "warning"), Panel)


def test_tip_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "tip"), Panel)


def test_caution_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "caution"), Panel)


def test_danger_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "danger"), Panel)


def test_hint_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "hint"), Panel)


def test_important_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "important"), Panel)


def test_error_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "error"), Panel)


def test_attention_produces_panel(make_visitor):
    assert isinstance(_first_panel(make_visitor, "attention"), Panel)


# ── Panel titles contain the admonition name ────────────────────────────────

def test_note_panel_title(make_visitor):
    assert "Note" in _first_panel(make_visitor, "note").title


def test_warning_panel_title(make_visitor):
    assert "Warning" in _first_panel(make_visitor, "warning").title


def test_tip_panel_title(make_visitor):
    assert "Tip" in _first_panel(make_visitor, "tip").title


def test_caution_panel_title(make_visitor):
    assert "Caution" in _first_panel(make_visitor, "caution").title


def test_danger_panel_title(make_visitor):
    assert "DANGER" in _first_panel(make_visitor, "danger").title


def test_hint_panel_title(make_visitor):
    assert "Hint" in _first_panel(make_visitor, "hint").title


def test_important_panel_title(make_visitor):
    assert "IMPORTANT" in _first_panel(make_visitor, "important").title


def test_error_panel_title(make_visitor):
    assert "ERROR" in _first_panel(make_visitor, "error").title


def test_attention_panel_title(make_visitor):
    assert "Attention" in _first_panel(make_visitor, "attention").title


# ── Generic admonition with custom title ─────────────────────────────────────

def test_generic_admonition_produces_panel(make_visitor):
    rst = ".. admonition:: My Custom Title\n\n   Body text.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_generic_admonition_title_in_panel(make_visitor):
    rst = ".. admonition:: My Custom Title\n\n   Body text.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert "My Custom Title" in panels[0].title


def test_generic_admonition_body_visible(render_text):
    rst = ".. admonition:: Title\n\n   Important body content.\n"
    assert "Important body content." in render_text(rst)


# ── Admonition body content ───────────────────────────────────────────────────

def test_admonition_body_plain_text_visible(render_text):
    assert "Important text here." in render_text(
        ".. note::\n\n   Important text here.\n"
    )


def test_admonition_body_bold_text_visible(render_text):
    assert "bold" in render_text(".. note::\n\n   This is **bold** text.\n")


def test_admonition_body_inline_code_visible(render_text):
    assert "caution()" in render_text(
        ".. warning::\n\n   Use ``caution()`` here.\n"
    )


def test_admonition_body_italic_text_visible(render_text):
    assert "important" in render_text(
        ".. tip::\n\n   This is *important*.\n"
    )


def test_admonition_body_with_bullet_list(render_text):
    rst = ".. note::\n\n   - first\n   - second\n"
    out = render_text(rst)
    assert "first" in out
    assert "second" in out


def test_admonition_body_with_enumerated_list(render_text):
    rst = ".. note::\n\n   #. step one\n   #. step two\n"
    out = render_text(rst)
    assert "step one" in out
    assert "step two" in out
