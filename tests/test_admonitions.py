"""Tests for all admonition directives.

Covers: note, warning, tip, caution, danger, hint, important, error,
attention, and the generic ``.. admonition::`` directive.

Formatting contract
-------------------
Each named admonition directive produces exactly one ``Panel`` whose:
* ``title`` is the exact string documented below (including the trailing
  colon-space).
* ``border_style`` encodes the severity of the admonition through specific
  colour and weight attributes.

Named admonition titles and border styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+------------+------------+--------------------------+
| directive  | title      | border_style             |
+============+============+==========================+
| note       | "Note: "   | bold white               |
| warning    | "Warning: "| bold yellow              |
| tip        | "Tip: "    | bold green               |
| caution    | "Caution: "| red (no bold)            |
| danger     | "DANGER: " | bold white on red        |
| hint       | "Hint: "   | yellow (no bold)         |
| important  | "IMPORTANT:"| bold blue               |
| error      | "ERROR: "  | bold red                 |
| attention  | "Attention:"| bold black on yellow    |
+------------+------------+--------------------------+
"""
from rich.panel import Panel
from rich.style import Style


def _first_panel(make_visitor, directive):
    rst = f".. {directive}::\n\n   Body text.\n"
    visitor = make_visitor(rst)
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


# ── Exact panel titles ────────────────────────────────────────────────────────

def test_note_panel_title(make_visitor):
    assert _first_panel(make_visitor, "note").title == "Note: "

def test_warning_panel_title(make_visitor):
    assert _first_panel(make_visitor, "warning").title == "Warning: "

def test_tip_panel_title(make_visitor):
    assert _first_panel(make_visitor, "tip").title == "Tip: "

def test_caution_panel_title(make_visitor):
    assert _first_panel(make_visitor, "caution").title == "Caution: "

def test_danger_panel_title(make_visitor):
    assert _first_panel(make_visitor, "danger").title == "DANGER: "

def test_hint_panel_title(make_visitor):
    assert _first_panel(make_visitor, "hint").title == "Hint: "

def test_important_panel_title(make_visitor):
    assert _first_panel(make_visitor, "important").title == "IMPORTANT: "

def test_error_panel_title(make_visitor):
    assert _first_panel(make_visitor, "error").title == "ERROR: "

def test_attention_panel_title(make_visitor):
    assert _first_panel(make_visitor, "attention").title == "Attention: "


# ── Border styles ─────────────────────────────────────────────────────────────

def test_note_border_style(make_visitor):
    bs = _first_panel(make_visitor, "note").border_style
    assert bs.bold is True and bs.color.name == "white"

def test_warning_border_style(make_visitor):
    bs = _first_panel(make_visitor, "warning").border_style
    assert bs.bold is True and bs.color.name == "yellow"

def test_tip_border_style(make_visitor):
    bs = _first_panel(make_visitor, "tip").border_style
    assert bs.bold is True and bs.color.name == "green"

def test_caution_border_style(make_visitor):
    bs = _first_panel(make_visitor, "caution").border_style
    assert bs.color.name == "red"
    # caution is NOT bold — it's a milder warning than danger/error
    assert not bs.bold

def test_danger_border_style(make_visitor):
    bs = _first_panel(make_visitor, "danger").border_style
    assert bs.bold is True
    assert bs.color.name == "white"
    assert bs.bgcolor is not None and bs.bgcolor.name == "red"

def test_hint_border_style(make_visitor):
    bs = _first_panel(make_visitor, "hint").border_style
    assert bs.color.name == "yellow"
    assert not bs.bold

def test_important_border_style(make_visitor):
    bs = _first_panel(make_visitor, "important").border_style
    assert bs.bold is True and bs.color.name == "blue"

def test_error_border_style(make_visitor):
    bs = _first_panel(make_visitor, "error").border_style
    assert bs.bold is True and bs.color.name == "red"

def test_attention_border_style(make_visitor):
    bs = _first_panel(make_visitor, "attention").border_style
    assert bs.bold is True
    assert bs.color.name == "black"
    assert bs.bgcolor is not None and bs.bgcolor.name == "yellow"


# ── Generic admonition with custom title ─────────────────────────────────────

def test_generic_admonition_produces_panel(make_visitor):
    rst = ".. admonition:: My Custom Title\n\n   Body text.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels

def test_generic_admonition_title_equals_heading(make_visitor):
    rst = ".. admonition:: My Custom Title\n\n   Body text.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "My Custom Title"


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
