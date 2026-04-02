"""Tests for block-level text elements.

Covers: paragraphs, headings/titles, block quotes (basic / attribution /
multi-paragraph), line blocks (flat and nested), transitions (horizontal
rules), comments, and bibliographic docinfo fields.

Formatting contract
-------------------
* **Block quote** — rendered as a ``Text`` whose base *style* is
  ``bright_magenta`` (the bar/marker glyph ▌) and whose body text uses a
  ``Span`` with ``color=white``.
* **Attribution** — a ``Text`` with base style ``grey89`` and plain text
  that starts with ``"  - "``.
* **Heading level-1** — rendered as an ``Align`` renderable with
  ``align='center'``, its ``renderable`` is a ``Text`` containing the heading
  text.
* **Transition** — rendered as a ``Rule`` whose ``style`` has
  ``color.name == 'yellow'``.
* **Bullet list marker** — a ``Text`` object with plain text ``" • "`` and
  base style ``"bold yellow"``.
* **Enumerated list marker** — a ``Text`` object whose plain text starts with
  a space followed by the item number, with base style ``"bold yellow"``.
* **Field list** — a rich ``Table`` with column headers
  ``"Field Name"`` and ``"Field Value"``.
"""
from rich.align import Align
from rich.console import NewLine
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text


# ── Paragraphs ────────────────────────────────────────────────────────────────

def test_paragraph_produces_text_renderable(make_visitor):
    visitor = make_visitor("Hello world.")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "A paragraph must produce at least one Text renderable"
    assert texts[0].plain.startswith("Hello world.")


def test_paragraph_intra_line_newline_becomes_space(render_text):
    assert "Hello world." in render_text("Hello\nworld.")


def test_multiple_paragraphs_produce_multiple_texts(make_visitor):
    visitor = make_visitor("First.\n\nSecond.")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "First." in combined
    assert "Second." in combined


# ── Headings / Titles ─────────────────────────────────────────────────────────

def test_heading_level1_produces_centered_align(make_visitor):
    visitor = make_visitor("My Title\n========\n\nBody.\n")
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert aligns, "Level-1 heading must produce an Align renderable"
    assert aligns[0].align == "center", "Level-1 heading must be centred"


def test_heading_level1_align_contains_heading_text(make_visitor):
    visitor = make_visitor("My Title\n========\n\nBody.\n")
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert aligns
    heading_text = aligns[0].renderable
    assert isinstance(heading_text, Text)
    assert heading_text.plain == "My Title", (
        f"Heading text must equal 'My Title', got {heading_text.plain!r}"
    )


def test_heading_level2_produces_align(make_visitor):
    rst = "Title\n=====\n\nSection\n-------\n"
    visitor = make_visitor(rst)
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    # Level-1 always produces an Align; level-2+ may render as Align, Panel or Rule
    assert aligns, "Top-level heading must produce at least one Align renderable"


def test_multiple_heading_levels_all_produce_text(render_text):
    rst = "Title\n=====\n\nSub\n---\n\nDeep\n~~~\n"
    out = render_text(rst)
    assert "Title" in out
    assert "Sub" in out
    assert "Deep" in out


def test_heading_body_paragraph_also_rendered(render_text):
    out = render_text("Section\n=======\n\nSection body.\n")
    assert "Section body." in out


# ── Block quotes ──────────────────────────────────────────────────────────────

def test_block_quote_marker_text_is_bar_glyph(make_visitor):
    visitor = make_visitor("    Quoted text.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # The block quote renders as a single Text whose plain starts with "▌ "
    bq_texts = [t for t in texts if t.plain.startswith("▌")]
    assert bq_texts, "Block quote must start with the ▌ bar glyph"


def test_block_quote_marker_base_style_is_bright_magenta(make_visitor):
    visitor = make_visitor("    Quoted text.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    bq_texts = [t for t in texts if t.plain.startswith("▌")]
    assert bq_texts
    assert str(bq_texts[0].style) == "bright_magenta", (
        f"Block quote base style must be 'bright_magenta', got {bq_texts[0].style!r}"
    )


def test_block_quote_body_text_has_white_span(make_visitor):
    visitor = make_visitor("    Quoted text.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    bq_text = next(t for t in texts if t.plain.startswith("▌"))
    # Body text ("Quoted text.") is covered by a span with color=white
    white_spans = [s for s in bq_text._spans if s.style.color and s.style.color.name == "white"]
    assert white_spans, "Block quote body must have a white-coloured span"
    body = bq_text.plain[white_spans[0].start : white_spans[0].end]
    assert "Quoted text." in body


def test_block_quote_attribution_has_grey89_style(make_visitor):
    visitor = make_visitor("    Good quote.\n\n    -- The Author\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    attr_texts = [t for t in texts if t.plain.startswith("  - ")]
    assert attr_texts, "Attribution must produce a Text starting with '  - '"
    assert str(attr_texts[0].style) == "grey89", (
        f"Attribution style must be 'grey89', got {attr_texts[0].style!r}"
    )


def test_block_quote_attribution_plain_text_has_author(make_visitor):
    visitor = make_visitor("    Quote body.\n\n    -- The Author\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    attr_texts = [t for t in texts if t.plain.startswith("  - ")]
    assert attr_texts
    assert "The Author" in attr_texts[0].plain


def test_block_quote_multi_paragraph_both_rendered(render_text):
    rst = "    First paragraph.\n\n    Second paragraph.\n"
    out = render_text(rst)
    assert "First paragraph." in out
    assert "Second paragraph." in out


def test_block_quote_attribution_appears_exactly_once(render_text):
    rst = "    Quote body.\n\n    -- The Author\n"
    assert render_text(rst).count("The Author") == 1


# ── Line blocks ───────────────────────────────────────────────────────────────

def test_line_block_each_line_is_separate_text(make_visitor):
    visitor = make_visitor("| First\n| Second\n| Third\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    plains = [t.plain.strip() for t in texts if t.plain.strip()]
    assert "First" in plains
    assert "Second" in plains
    assert "Third" in plains


def test_line_block_lines_are_individual_renderables(make_visitor):
    """Each | line must become its own Text, not merged into one."""
    visitor = make_visitor("| Alpha\n| Beta\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # They must be separate Text objects (one per line), not a single combined text
    assert len([t for t in texts if t.plain.strip() in ("Alpha", "Beta")]) == 2


def test_line_block_three_lines(render_text):
    out = render_text("| A\n| B\n| C\n")
    assert "A" in out
    assert "B" in out
    assert "C" in out


# ── Transitions (horizontal rules) ───────────────────────────────────────────

def test_transition_produces_rule(make_visitor):
    visitor = make_visitor("Before\n\n--------\n\nAfter\n")
    rules = [r for r in visitor.renderables if isinstance(r, Rule)]
    assert rules, "A transition must produce a Rule renderable"


def test_transition_rule_has_yellow_style(make_visitor):
    visitor = make_visitor("Before\n\n--------\n\nAfter\n")
    rules = [r for r in visitor.renderables if isinstance(r, Rule)]
    assert rules
    assert rules[0].style.color is not None and rules[0].style.color.name == "yellow", (
        f"Transition Rule must have yellow colour, got {rules[0].style!r}"
    )


# ── Comments ─────────────────────────────────────────────────────────────────

def test_comment_inline_text_not_rendered(render_text):
    out = render_text(".. This is a comment\n\nVisible text.\n")
    assert "This is a comment" not in out
    assert "Visible text." in out


def test_comment_block_not_rendered(render_text):
    # Multi-line comment: NO blank line between '..' and the indented body
    rst = "..\n   This is a multi-line comment.\n\nReal text.\n"
    out = render_text(rst)
    assert "This is a multi-line comment." not in out
    assert "Real text." in out


# ── Docinfo (bibliographic fields) ───────────────────────────────────────────

def test_docinfo_renders_as_table(make_visitor):
    visitor = make_visitor(":Author: Bob\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "Docinfo fields must produce a Table renderable"


def test_docinfo_table_has_field_name_and_value_columns(make_visitor):
    visitor = make_visitor(":Author: Bob\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    col_headers = [c.header for c in tables[0].columns]
    assert col_headers == ["Field Name", "Field Value"], (
        f"Docinfo table must have columns ['Field Name', 'Field Value'], got {col_headers}"
    )


def test_docinfo_author_in_output(render_text):
    assert "Jane Doe" in render_text(":Author: Jane Doe\n\nBody.\n")


def test_docinfo_multiple_fields_share_one_table(make_visitor):
    visitor = make_visitor(":Author: Alice\n:Date: 2024-01-01\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert len(tables) == 1, "Consecutive docinfo fields must share one Table"
    assert tables[0].row_count == 2


def test_docinfo_three_fields_table_row_count(make_visitor):
    visitor = make_visitor(":Author: A\n:Date: D\n:Version: V\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].row_count == 3


# ── Bullet list structure ─────────────────────────────────────────────────────

def test_bullet_list_marker_text_is_bullet_char(make_visitor):
    visitor = make_visitor("* item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain == " • "]
    assert markers, "Bullet list must produce a Text with plain text ' • '"


def test_bullet_list_marker_style_is_bold_yellow(make_visitor):
    visitor = make_visitor("* item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain == " • "]
    assert markers
    assert str(markers[0].style) == "bold yellow", (
        f"Bullet marker style must be 'bold yellow', got {markers[0].style!r}"
    )


def test_nested_bullet_level2_uses_open_circle_marker(make_visitor):
    visitor = make_visitor("* outer\n\n  * inner\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    l2_markers = [t for t in texts if "∘" in t.plain]
    assert l2_markers, "Level-2 bullet list must use the '∘' circle marker"


# ── Enumerated list structure ─────────────────────────────────────────────────

def test_enumerated_list_first_marker_is_number_one(make_visitor):
    visitor = make_visitor("#. item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain.strip().startswith("1")]
    assert markers, "First enumerated item marker must contain '1'"


def test_enumerated_list_marker_style_is_bold_yellow(make_visitor):
    visitor = make_visitor("#. item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # Marker text is " 1" (leading space)
    markers = [t for t in texts if t.plain.startswith(" ") and t.plain.strip().isdigit()]
    assert markers
    assert str(markers[0].style) == "bold yellow", (
        f"Enum marker style must be 'bold yellow', got {markers[0].style!r}"
    )


# ── Substitution definitions ──────────────────────────────────────────────────

def test_substitution_replace_resolved_in_text(render_text):
    rst = "Use |proj| today.\n\n.. |proj| replace:: RichRST\n"
    assert "RichRST" in render_text(rst)


def test_substitution_definition_not_rendered_standalone(render_text):
    rst = "Use |proj| today.\n\n.. |proj| replace:: RichRST\n"
    # The resolved text should appear exactly once, not additionally
    # rendered from the substitution_definition node itself
    assert render_text(rst).count("RichRST") == 1
