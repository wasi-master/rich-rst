"""Tests for all admonition directives.

Covers: note, warning, tip, caution, danger, hint, important, error,
attention, and the generic ``.. admonition::`` directive.

Formatting contract
-------------------
Each named admonition directive produces exactly one ``Panel`` whose:
* ``title`` is the exact string documented below (the bare label, no
  trailing colon).
* ``border_style`` encodes the severity of the admonition through specific
  colour and weight attributes.

Named admonition titles and border styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+------------+--------------+--------------------------+
| directive  | title        | border_style             |
+============+==============+==========================+
| note       | "Note"       | bold white               |
| warning    | "Warning"    | bold yellow              |
| tip        | "Tip"        | bold green               |
| caution    | "Caution"    | red (no bold)            |
| danger     | "DANGER"     | bold white on red        |
| hint       | "Hint"       | yellow (no bold)         |
| important  | "IMPORTANT"  | bold blue                |
| error      | "ERROR"      | bold red                 |
| attention  | "Attention"  | bold black on yellow     |
+------------+--------------+--------------------------+
"""
from rich.panel import Panel
from rich.style import Style
import pytest
from rich_rst import RestructuredText, _register_sphinx_directives
from rich.console import Console
from rich.console import Console
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich.text import Text
import rich_rst
import rich_rst._vendor.docutils.core
from rich_rst._vendor import docutils
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


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
    assert _first_panel(make_visitor, "note").title == "Note"

def test_warning_panel_title(make_visitor):
    assert _first_panel(make_visitor, "warning").title == "Warning"

def test_tip_panel_title(make_visitor):
    assert _first_panel(make_visitor, "tip").title == "Tip"

def test_caution_panel_title(make_visitor):
    assert _first_panel(make_visitor, "caution").title == "Caution"

def test_danger_panel_title(make_visitor):
    assert _first_panel(make_visitor, "danger").title == "DANGER"

def test_hint_panel_title(make_visitor):
    assert _first_panel(make_visitor, "hint").title == "Hint"

def test_important_panel_title(make_visitor):
    assert _first_panel(make_visitor, "important").title == "IMPORTANT"

def test_error_panel_title(make_visitor):
    assert _first_panel(make_visitor, "error").title == "ERROR"

def test_attention_panel_title(make_visitor):
    assert _first_panel(make_visitor, "attention").title == "Attention"


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

@pytest.fixture(autouse=True)
def ensure_sphinx_directives():
    """Register Sphinx directives once before any test in this module runs."""
    _register_sphinx_directives()


# ── No panels in compact mode ────────────────────────────────────────────────

@pytest.mark.parametrize("directive", [
    "note", "warning", "tip", "caution", "danger",
    "hint", "important", "error", "attention",
])
def test_compact_directive_emits_no_panel(make_visitor, directive):
    rst = f".. {directive}::\n\n   hello\n"
    visitor = make_visitor(rst, admonition_style="compact")
    assert not any(isinstance(r, Panel) for r in visitor.renderables)


def test_compact_seealso_emits_no_panel(make_visitor):
    rst = ".. seealso::\n\n   Other docs.\n"
    visitor = make_visitor(rst, admonition_style="compact")
    assert not any(isinstance(r, Panel) for r in visitor.renderables)


def test_compact_versionadded_emits_no_panel(make_visitor):
    rst = ".. versionadded:: 0.47\n"
    visitor = make_visitor(rst, admonition_style="compact")
    assert not any(isinstance(r, Panel) for r in visitor.renderables)


@pytest.mark.parametrize("directive,arg", [
    ("availability", "3.13"),
    ("soft-deprecated", "3.13"),
    ("impl-detail", ""),
])
def test_compact_new_directive_emits_no_panel(make_visitor, directive, arg):
    rst = f".. {directive}:: {arg}\n\n   hello\n" if arg else f".. {directive}::\n\n   hello\n"
    visitor = make_visitor(rst, admonition_style="compact")
    assert not any(isinstance(r, Panel) for r in visitor.renderables)


# ── Per-directive title prefixes ──────────────────────────────────────────────

@pytest.mark.parametrize("directive,expected", [
    ("note", "Note: hello"),
    ("warning", "⚠ Warning: hello"),
    ("tip", "Tip: hello"),
    ("caution", "⚠ Caution: hello"),
    ("danger", "✖ DANGER: hello"),
    ("hint", "Hint: hello"),
    ("important", "IMPORTANT: hello"),
    ("error", "✖ ERROR: hello"),
    ("attention", "⚠ Attention: hello"),
])
def test_compact_directive_title_prefix(render_text, directive, expected):
    rst = f".. {directive}::\n\n   hello\n"
    out = render_text(rst, admonition_style="compact")
    assert expected in out


def test_compact_seealso_title_prefix(render_text):
    rst = ".. seealso::\n\n   Other docs.\n"
    assert "See Also: Other docs." in render_text(rst, admonition_style="compact")


def test_compact_generic_admonition_uses_user_title(render_text):
    rst = ".. admonition:: Custom\n\n   body text.\n"
    assert "Custom: body text." in render_text(rst, admonition_style="compact")


# ── Multi-paragraph bodies ────────────────────────────────────────────────────

def test_compact_note_multi_paragraph(render_text):
    rst = ".. note::\n\n   First paragraph.\n\n   Second paragraph.\n"
    out = render_text(rst, admonition_style="compact")
    assert "Note: First paragraph." in out
    assert "Second paragraph." in out


# ── Version directives (empty body → bracketed tag) ──────────────────────────

@pytest.mark.parametrize("rst,expected", [
    (".. versionadded:: 0.47\n", "[Added in v0.47]"),
    (".. versionchanged:: 0.47\n", "[Changed in v0.47]"),
    (".. deprecated:: 0.47\n", "⚠ [Deprecated in v0.47]"),
])
def test_compact_version_directive_empty_body(render_text, rst, expected):
    out = render_text(rst, admonition_style="compact")
    assert expected in out


def test_compact_deprecated_removed_empty_body(render_text):
    """``deprecated-removed`` embeds the removal version in its version string
    (per ``_DeprecatedRemovedDirective.run``), so the compact tag renders as
    ``✖ [Deprecated in v<since> (removed in <removed>)]`` (danger-tone glyph
    since this style is ``bold red``).
    """
    rst = ".. deprecated-removed:: 0.47 1.0\n"
    out = render_text(rst, admonition_style="compact")
    assert "✖ [Deprecated in v0.47 (removed in 1.0)]" in out


def test_compact_versionadded_has_no_glyph(render_text):
    """``versionadded``/``versionchanged`` are informational; no severity glyph."""
    out = render_text(".. versionadded:: 0.47\n", admonition_style="compact")
    tag_lines = [ln for ln in out.splitlines() if "Added in v0.47" in ln]
    assert tag_lines
    for ln in tag_lines:
        assert "⚠" not in ln
        assert "✖" not in ln


def test_compact_deprecated_single_paragraph_body_has_glyph(render_text):
    """Single-paragraph deprecated body keeps the ⚠ glyph outside the bracket."""
    rst = ".. deprecated:: 1.0\n\n   Use :func:`new_thing` instead.\n"
    out = render_text(rst, admonition_style="compact")
    assert "⚠ [Deprecated in v1.0: Use " in out


def test_compact_deprecated_multiparagraph_body_has_glyph(render_text):
    """Multi-paragraph fallback (no brackets) still gets the ⚠ glyph prefix."""
    rst = ".. deprecated:: 1.0\n\n   First para.\n\n   Second para.\n"
    out = render_text(rst, admonition_style="compact")
    assert "⚠ Deprecated in v1.0: First para." in out
    assert "Second para." in out
    assert "[Deprecated in v1.0: First para." not in out


# ── availability / soft-deprecated / impl-detail (compact) ───────────────────

@pytest.mark.parametrize("rst,expected", [
    (".. availability:: 3.13\n", "[Available in v3.13]"),
    (".. soft-deprecated:: 3.13\n", "⚠ [Soft Deprecated in v3.13]"),
])
def test_compact_new_version_directive_empty_body(render_text, rst, expected):
    out = render_text(rst, admonition_style="compact")
    assert expected in out


def test_compact_availability_has_no_glyph(render_text):
    """``availability`` is informational (like ``versionadded``); no severity glyph."""
    out = render_text(".. availability:: 3.13\n", admonition_style="compact")
    tag_lines = [ln for ln in out.splitlines() if "Available in v3.13" in ln]
    assert tag_lines
    for ln in tag_lines:
        assert "⚠" not in ln
        assert "✖" not in ln


def test_compact_availability_single_paragraph_body(render_text):
    rst = ".. availability:: 3.13\n\n   Only on Linux.\n"
    out = render_text(rst, admonition_style="compact")
    assert "[Available in v3.13: Only on Linux.]" in out


def test_compact_soft_deprecated_single_paragraph_body_has_glyph(render_text):
    rst = ".. soft-deprecated:: 3.13\n\n   Prefer :func:`new_api`.\n"
    out = render_text(rst, admonition_style="compact")
    assert "⚠ [Soft Deprecated in v3.13: Prefer " in out


def test_compact_soft_deprecated_multiparagraph_body_has_glyph(render_text):
    rst = ".. soft-deprecated:: 3.13\n\n   First para.\n\n   Second para.\n"
    out = render_text(rst, admonition_style="compact")
    assert "⚠ Soft Deprecated in v3.13: First para." in out
    assert "Second para." in out
    assert "[Soft Deprecated in v3.13: First para." not in out


def test_compact_impl_detail_title_prefix(render_text):
    """``impl-detail`` has no version; renders as a plain admonition prefix."""
    rst = ".. impl-detail::\n\n   CPython-specific.\n"
    out = render_text(rst, admonition_style="compact")
    assert "Implementation Detail: CPython-specific." in out


def test_compact_impl_detail_has_no_glyph(render_text):
    rst = ".. impl-detail::\n\n   CPython-specific.\n"
    out = render_text(rst, admonition_style="compact")
    detail_lines = [ln for ln in out.splitlines() if "Implementation Detail" in ln]
    assert detail_lines
    for ln in detail_lines:
        assert "⚠" not in ln
        assert "✖" not in ln


# ── Version directives (single-paragraph body → bracketed inline) ────────────

def test_compact_versionadded_single_paragraph_body(render_text):
    rst = ".. versionadded:: 2.0\n\n   Added support for widgets.\n"
    out = render_text(rst, admonition_style="compact")
    assert "[Added in v2.0: Added support for widgets.]" in out


def test_compact_versionchanged_single_paragraph_body(render_text):
    rst = ".. versionchanged:: 2.0\n\n   Now accepts a dict.\n"
    out = render_text(rst, admonition_style="compact")
    assert "[Changed in v2.0: Now accepts a dict.]" in out


# ── Version directives (multi-paragraph body → fallback shape) ───────────────

def test_compact_versionadded_multiparagraph_falls_back(render_text):
    rst = ".. versionadded:: 2.0\n\n   First para.\n\n   Second para.\n"
    out = render_text(rst, admonition_style="compact")
    # Falls back to non-bracketed title-prefix shape.
    assert "Added in v2.0: First para." in out
    assert "Second para." in out
    # The bracketed inline shape must NOT be used for multi-paragraph bodies.
    assert "[Added in v2.0: First para." not in out


# ── Inlining version tags onto a preceding paragraph ─────────────────────────

def test_compact_versionadded_inlines_onto_preceding_paragraph(render_text):
    """Empty-body version tag should hug the previous paragraph on the same
    line, not float as a separate paragraph. Behavior implemented by
    ``_append_inline_to_prev_paragraph``."""
    rst = "Bar parameter.\n\n.. versionadded:: 0.47\n"
    out = render_text(rst, admonition_style="compact")
    lines = [ln for ln in out.splitlines() if ln.strip()]
    assert any("Bar parameter. [Added in v0.47]" in ln for ln in lines), out


def test_compact_versionadded_at_section_start_stands_alone(render_text):
    """When ``.. versionadded::`` has no preceding ``Text`` renderable,
    ``_append_inline_to_prev_paragraph`` must fall back to emitting the tag
    on its own line — the inline merge requires a paragraph to merge into."""
    rst = ".. versionadded:: 0.47\n\nFollowing prose.\n"
    out = render_text(rst, admonition_style="compact")
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
    tag_idx = next(i for i, ln in enumerate(lines) if "Added in v0.47" in ln)
    # Tag is on its own line; the following prose is on a separate line.
    assert "Following prose" not in lines[tag_idx]


def test_compact_deprecated_with_body_inlines_onto_preceding_paragraph(render_text):
    """The bracket-collapsed shape (single-paragraph body) should also inline
    onto a preceding paragraph. Verifies the second call site of
    ``_append_inline_to_prev_paragraph`` in ``_emit_version_directive``."""
    rst = "Baz parameter.\n\n.. deprecated:: 2.0\n\n   Use foo instead.\n"
    out = render_text(rst, admonition_style="compact")
    lines = [ln for ln in out.splitlines() if ln.strip()]
    merged = next(
        (ln for ln in lines if "Baz parameter." in ln and "Deprecated in v2.0" in ln),
        None,
    )
    assert merged is not None, out
    # Glyph stays outside the bracket; body goes inside.
    assert "⚠ [Deprecated in v2.0: Use foo instead.]" in merged


def test_compact_versionadded_does_not_inline_onto_preceding_compact_admonition(render_text):
    """A compact admonition's prefix line is not a prose paragraph; a following
    ``.. versionadded::`` must stand alone instead of being merged onto it.
    Regression for the guard in ``_append_inline_to_prev_paragraph`` that
    keeps directive boundaries intact."""
    rst = ".. warning:: Be careful here.\n\n.. versionadded:: 0.47\n"
    out = render_text(rst, admonition_style="compact")
    warning_line = next((ln for ln in out.splitlines() if "Be careful here" in ln), None)
    assert warning_line is not None, out
    assert "Added in v0.47" not in warning_line, out
    # Tag should appear on its own line elsewhere in the output.
    assert any("Added in v0.47" in ln and "Be careful here" not in ln for ln in out.splitlines()), out


def test_compact_versionadded_does_not_inline_onto_multiparagraph_admonition_body(render_text):
    """When the previous renderable is the last body paragraph of a preceding
    multi-paragraph admonition (appended by ``_prepend_styled_prefix``), a
    following ``.. versionadded::`` must not merge onto it. The body's last
    ``Text`` is produced by a sub-visitor's ``depart_paragraph``, so the main
    visitor's ``_last_paragraph_text`` tracker correctly excludes it."""
    rst = (
        ".. deprecated:: 1.0\n\n"
        "   First paragraph.\n\n"
        "   Second paragraph.\n\n"
        ".. versionadded:: 0.47\n"
    )
    out = render_text(rst, admonition_style="compact")
    second_para_line = next((ln for ln in out.splitlines() if "Second paragraph" in ln), None)
    assert second_para_line is not None, out
    assert "Added in v0.47" not in second_para_line, out
    assert any("Added in v0.47" in ln and "Second paragraph" not in ln for ln in out.splitlines()), out


# ── Regression: phantom padded-blank-row under justify="left" ────────────────

def test_paragraph_then_admonition_no_phantom_padded_row_under_justify_left():
    """An *intermediate* paragraph stored as ``Text("X\\n\\n", end="")`` used to
    render to three padded lines under ``options.justify == "left"`` — the
    content row plus two phantom blank-padded rows. The trailing phantom
    row then fused onto the next renderable's first row, corrupting any
    layout where directives (admonitions, version tags) follow a paragraph
    in a width-constrained justified context (e.g. Rich ``Table`` cells in
    downstream consumers like cyclopts).

    The bug requires a *non-Text* boundary (admonition / panel / version
    tag) between paragraphs — a plain paragraph→paragraph chain collapses
    into a single ``Text`` renderable that the existing rstrip cleanup
    already handles. The trailing-newline normalization in
    ``RestructuredText.__rich_console__`` covers intermediate ``Text``s too.
    """
    from rich.console import Console, ConsoleOptions, ConsoleDimensions
    # Paragraph followed by a compact admonition: the paragraph becomes
    # an intermediate Text, the admonition emits a separate Text. Pre-fix,
    # the paragraph's trailing "\n\n" produced a phantom blank-padded row
    # that fused onto the admonition's first row.
    rst = "First paragraph.\n\n.. note:: Second.\n"
    console = Console(width=80)
    opts = ConsoleOptions(
        size=ConsoleDimensions(width=80, height=25),
        legacy_windows=False, min_width=40, max_width=40,
        is_terminal=True, encoding="utf-8", max_height=25,
        justify="left", overflow="fold", no_wrap=False,
        highlight=False, markup=None, height=None,
    )
    lines = console.render_lines(RestructuredText(rst, admonition_style="compact"), opts)
    # render_lines pads to max_height; drop trailing all-whitespace rows.
    while lines and all(not s.text or s.text.isspace() for s in lines[-1]):
        lines.pop()
    rendered = ["".join(s.text for s in line).rstrip() for line in lines]
    # Exactly 3 rows: paragraph, single blank separator, note prefix+body.
    # The bug would add a 4th (extra blank-padded) row between the blank
    # and the note, or shift "Note: Second." into a row that begins with
    # the leading pad from the previous paragraph's phantom row.
    assert rendered == ["First paragraph.", "", "Note: Second."], rendered


# ── Default mode is still panel ───────────────────────────────────────────────

def test_default_mode_still_emits_panel(make_visitor):
    """Regression: omitting admonition_style preserves panel-mode output."""
    rst = ".. note::\n\n   hello\n"
    visitor = make_visitor(rst)
    assert any(isinstance(r, Panel) for r in visitor.renderables)


def test_explicit_panel_mode_emits_panel(make_visitor):
    rst = ".. note::\n\n   hello\n"
    visitor = make_visitor(rst, admonition_style="panel")
    assert any(isinstance(r, Panel) for r in visitor.renderables)


# ── Validation ────────────────────────────────────────────────────────────────

def test_invalid_admonition_style_raises():
    with pytest.raises(ValueError, match="admonition_style"):
        RestructuredText("hello", admonition_style="bogus")


# ── Inline markup is preserved in the compact body ───────────────────────────

def test_compact_note_preserves_bold_inline(render_text):
    """``**bold**`` inside a compact admonition body keeps its emphasis."""
    rst = ".. note:: Use the **--force** flag.\n"
    out = render_text(rst, admonition_style="compact")
    assert "Note: Use the --force flag." in out


def test_compact_warning_preserves_inline_code(render_text):
    rst = ".. warning:: Avoid ``rm -rf /`` at all costs.\n"
    out = render_text(rst, admonition_style="compact")
    assert "⚠ Warning: Avoid " in out
    assert "rm -rf /" in out
    assert "at all costs." in out


def test_compact_versionchanged_bracketed_preserves_inline_code(render_text):
    rst = ".. versionchanged:: 2.0\n\n   Now accepts ``dict`` instead of ``list``.\n"
    out = render_text(rst, admonition_style="compact")
    assert "[Changed in v2.0: Now accepts " in out
    assert "dict" in out and "list" in out


# ── Important must not gain a glyph ──────────────────────────────────────────

def test_compact_important_has_no_glyph(render_text):
    """``important`` is informational (Sphinx convention); no severity glyph."""
    rst = ".. important:: Back up first.\n"
    out = render_text(rst, admonition_style="compact")
    assert "IMPORTANT: Back up first." in out
    # The output line containing the title must not start with ⚠ or ✖.
    important_lines = [ln for ln in out.splitlines() if "IMPORTANT" in ln]
    assert important_lines
    for ln in important_lines:
        assert "⚠" not in ln
        assert "✖" not in ln


# ── Compact admonitions inside containers (sub-visitor propagation) ──────────

def test_compact_admonition_inside_table_cell(make_visitor):
    """``admonition_style`` must propagate into the table-cell sub-visitor
    (``_render_entry_content`` in ``__init__.py``). Inspect the table cell
    directly because narrow cell widths can truncate the rendered output."""
    from rich.table import Table as _Table
    from rich.panel import Panel as _Panel
    rst = (
        ".. list-table::\n\n"
        "   * - cell content\n\n"
        "       .. note:: nested note text.\n"
    )
    visitor = make_visitor(rst, admonition_style="compact")
    tables = [r for r in visitor.renderables if isinstance(r, _Table)]
    assert tables, "list-table must produce a Rich Table"
    cell_texts = []
    for col in tables[0].columns:
        for cell in col._cells:
            assert not isinstance(cell, _Panel), "compact mode must not produce a Panel inside a table cell"
            for sub in getattr(cell, "renderables", [cell]):
                assert not isinstance(sub, _Panel), "compact mode must not produce a Panel inside a cell Group"
                if hasattr(sub, "plain"):
                    cell_texts.append(sub.plain)
    joined = "\n".join(cell_texts)
    assert "Note: nested note text." in joined


def test_compact_admonition_inside_list_item(render_text):
    """A compact admonition under a bullet item uses the just-merged
    ``depart_paragraph`` list-item branch (commit 130ffcc) without breaking."""
    rst = (
        "* item one\n\n"
        "  .. note:: nested in a bullet.\n\n"
        "* item two\n"
    )
    out = render_text(rst, admonition_style="compact")
    assert "Note: nested in a bullet." in out
    assert "item one" in out and "item two" in out


def test_compact_note_with_only_a_code_block(render_text):
    """When the body's first renderable is non-Text (e.g. only a code block),
    the prefix is emitted on its own line above the body."""
    rst = (
        ".. note::\n\n"
        "   .. code-block:: python\n\n"
        "      print('hi')\n"
    )
    out = render_text(rst, admonition_style="compact")
    assert "Note: " in out
    assert "print" in out and "hi" in out


# ── Panel-mode title regression pins ──────────────────────────────────────────

def test_panel_mode_seealso_title_has_no_trailing_colon(make_visitor):
    """Existing tests assert ``"See Also"`` (no colon-space). Pin it here so an
    accidental "fix" to match the other admonitions' ``"X: "`` convention fails."""
    from rich.panel import Panel as _Panel
    rst = ".. seealso::\n\n   Other docs.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, _Panel)]
    assert panels
    assert panels[0].title == "See Also"


# ── Integration: vertical density win at narrow widths ───────────────────────

def test_compact_stacked_admonitions_save_lines():
    """Compact rendering of stacked admonitions must use far fewer lines than panels."""
    rst = (
        ".. note:: This is important context.\n\n"
        ".. warning:: Be careful here.\n\n"
        ".. versionadded:: 0.47\n"
    )
    panel_lines = RestructuredText(rst, admonition_style="panel").render_to_string(width=68).splitlines()
    compact_lines = RestructuredText(rst, admonition_style="compact").render_to_string(width=68).splitlines()
    panel_nonblank = [ln for ln in panel_lines if ln.strip()]
    compact_nonblank = [ln for ln in compact_lines if ln.strip()]
    # Three short content lines in compact mode — one per directive. Each compact
    # admonition occupies its own line; ``versionadded`` does NOT inline onto the
    # preceding ``warning`` because that line is not a prose paragraph.
    assert len(compact_nonblank) == 3, compact_lines
    # Panel mode produces many more lines (panel borders + padding × 3 directives).
    assert len(panel_nonblank) >= 9, panel_lines

def test_empty_body_rendering(render_text):
    """Test that note admonitions render with their panel title."""
    rst = """\
.. note::

   Minimal content.
"""
    out = render_text(rst)
    assert "Note" in out, "Note admonition must render with 'Note' panel title"
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
    assert "Warning" in out, "Warning admonition must render with 'Warning' panel title"
    assert "important information" in out, "Warning body must be visible"
