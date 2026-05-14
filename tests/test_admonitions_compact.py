"""Tests for ``admonition_style="compact"`` rendering.

Compact mode collapses each admonition directive to a styled inline title
prefix (with optional severity glyph) instead of a bordered Rich Panel.
This is intended for narrow-width contexts such as CLI ``--help`` panels.

Compact rendering shape
-----------------------
Generic admonitions render as ``"<glyph><Title>: <body>"``. Severity glyphs:

+--------------+--------+
| directive    | glyph  |
+==============+========+
| warning      | "⚠ "   |
| caution      | "⚠ "   |
| attention    | "⚠ "   |
| danger       | "✖ "   |
| error        | "✖ "   |
| important    | (none) |
| note         | (none) |
| hint         | (none) |
| tip          | (none) |
| seealso      | (none) |
| admonition   | (none) |
+--------------+--------+

Version directives (``versionadded``, ``versionchanged``, ``deprecated``,
``deprecated-removed``) collapse to a bracketed inline tag using shortened
phrasing — ``[Added in v0.47]`` / ``[Changed in v0.47]`` / ``⚠ [Deprecated in
v0.47]`` / ``✖ [Deprecated in v0.47 (removed in 1.0)]``. ``deprecated`` gets
the ⚠ glyph (warning-tone) and ``deprecated-removed`` gets ✖ (danger-tone);
``versionadded``/``versionchanged`` stay glyphless. Empty bodies render as
the bracketed tag alone; single-paragraph bodies render as ``[Added in v0.47:
<body>]``; multi-paragraph or structural bodies fall back to the
non-bracketed title-prefix shape.

Panel mode (the default) is the byte-for-byte regression target covered by
``test_admonitions.py`` and ``test_sphinx_directives.py``.
"""
import pytest
from rich.panel import Panel

from rich_rst import RestructuredText, _register_sphinx_directives


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
    # Three short content lines in compact mode.
    assert len(compact_nonblank) == 3, compact_lines
    # Panel mode produces many more lines (panel borders + padding × 3 directives).
    assert len(panel_nonblank) >= 9, panel_lines
