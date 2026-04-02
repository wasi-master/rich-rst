"""Tests for block-level text elements.

Covers: paragraphs, headings/titles (all six levels), block quotes
(basic / attribution / multi-paragraph), line blocks (flat and nested),
transitions (horizontal rules), comments, and bibliographic docinfo fields.
"""
from rich.align import Align
from rich.console import NewLine
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text


# ── Paragraphs ────────────────────────────────────────────────────────────────

def test_paragraph_plain_text_appears(render_text):
    assert "Hello world." in render_text("Hello world.")


def test_paragraph_intra_line_newline_becomes_space(render_text):
    # RST treats a single newline inside a paragraph as a space
    assert "Hello world." in render_text("Hello\nworld.")


def test_multiple_paragraphs_all_appear(render_text):
    out = render_text("First.\n\nSecond.")
    assert "First." in out
    assert "Second." in out


def test_paragraph_produces_text_renderable(make_visitor):
    visitor = make_visitor("Hello.")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts


# ── Headings / Titles ─────────────────────────────────────────────────────────

def test_heading_text_appears_in_output(render_text):
    assert "My Section" in render_text("My Section\n==========\n\nBody.\n")


def test_heading_level1_produces_panel_or_align(make_visitor):
    visitor = make_visitor("Top Level\n=========\n\nSome text.")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert panels or aligns, "Level-1 heading must produce a Panel or Align"


def test_heading_level2_produces_panel_or_align(make_visitor):
    rst = "Chapter\n=======\n\nSection\n-------\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert panels or aligns


def test_heading_level3_produces_renderable(render_text):
    assert "Subsection" in render_text(
        "Title\n=====\n\nSection\n-------\n\nSubsection\n~~~~~~~~~~\n\nBody.\n"
    )


def test_multiple_heading_levels_all_visible(render_text):
    rst = "Title\n=====\n\nSub\n---\n\nDeep\n~~~\n"
    out = render_text(rst)
    assert "Title" in out
    assert "Sub" in out
    assert "Deep" in out


def test_heading_body_paragraph_also_visible(render_text):
    out = render_text("Section\n=======\n\nSection body.\n")
    assert "Section" in out
    assert "Section body." in out


# ── Block quotes ──────────────────────────────────────────────────────────────

def test_block_quote_content_visible(render_text):
    assert "This is a block quote." in render_text("    This is a block quote.\n")


def test_block_quote_has_bar_marker(make_visitor):
    visitor = make_visitor("    Quoted text.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "▌" in combined


def test_block_quote_with_attribution(render_text):
    rst = "    Good quote.\n\n    -- Author Name\n"
    out = render_text(rst)
    assert "Good quote." in out
    assert "Author Name" in out


def test_block_quote_multi_paragraph_both_paragraphs_visible(render_text):
    rst = "    First paragraph.\n\n    Second paragraph.\n"
    out = render_text(rst)
    assert "First paragraph." in out
    assert "Second paragraph." in out


def test_block_quote_attribution_only_shown_once(render_text):
    # The attribution should appear exactly once (not duplicated)
    rst = "    Quote body.\n\n    -- The Author\n"
    out = render_text(rst)
    assert out.count("The Author") == 1


# ── Line blocks ───────────────────────────────────────────────────────────────

def test_line_block_all_lines_visible(render_text):
    out = render_text("| Line one\n| Line two\n")
    assert "Line one" in out
    assert "Line two" in out


def test_line_block_each_line_is_separate_renderable(make_visitor):
    visitor = make_visitor("| First\n| Second\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    lines = [t.plain.strip() for t in texts if t.plain.strip()]
    assert "First" in lines
    assert "Second" in lines


def test_line_block_nested_indentation_visible(render_text):
    out = render_text("| Outer\n|     Indented\n")
    assert "Outer" in out
    assert "Indented" in out


def test_line_block_three_lines(render_text):
    out = render_text("| A\n| B\n| C\n")
    assert "A" in out
    assert "B" in out
    assert "C" in out


# ── Transitions (horizontal rules) ───────────────────────────────────────────

def test_transition_produces_rule(make_visitor):
    visitor = make_visitor("Before\n\n--------\n\nAfter\n")
    rules = [r for r in visitor.renderables if isinstance(r, Rule)]
    assert rules, "A transition directive must produce a Rule renderable"


def test_transition_surrounding_text_visible(render_text):
    out = render_text("Before\n\n--------\n\nAfter\n")
    assert "Before" in out
    assert "After" in out


# ── Comments ─────────────────────────────────────────────────────────────────

def test_comment_text_not_rendered(render_text):
    out = render_text(".. This is a comment\n\nVisible text.\n")
    assert "This is a comment" not in out
    assert "Visible text." in out


def test_comment_block_not_rendered(render_text):
    rst = "..\n\n   This is a multi-line comment.\n\nReal text.\n"
    out = render_text(rst)
    assert "This is a multi-line comment." not in out
    assert "Real text." in out


# ── Docinfo (bibliographic fields) ───────────────────────────────────────────

def test_docinfo_author_appears(render_text):
    assert "Jane Doe" in render_text(":Author: Jane Doe\n\nBody.\n")


def test_docinfo_date_appears(render_text):
    assert "2024-01-01" in render_text(":Date: 2024-01-01\n\nBody.\n")


def test_docinfo_version_appears(render_text):
    assert "1.2.3" in render_text(":Version: 1.2.3\n\nBody.\n")


def test_docinfo_copyright_appears(render_text):
    assert "2024 Org" in render_text(":Copyright: 2024 Org\n\nBody.\n")


def test_docinfo_organization_appears(render_text):
    assert "ACME Corp" in render_text(":Organization: ACME Corp\n\nBody.\n")


def test_docinfo_renders_as_table(make_visitor):
    visitor = make_visitor(":Author: Bob\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "Docinfo fields must produce a Table renderable"


def test_docinfo_multiple_fields_in_single_table(make_visitor):
    visitor = make_visitor(":Author: Alice\n:Date: 2024-01-01\n\nBody.\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].row_count >= 2, "Multiple consecutive docinfo fields share one table"


# ── Substitution definitions ──────────────────────────────────────────────────

def test_substitution_replace_resolved_in_text(render_text):
    rst = "Use |proj| today.\n\n.. |proj| replace:: RichRST\n"
    out = render_text(rst)
    assert "RichRST" in out


def test_substitution_definition_not_rendered_standalone(render_text):
    rst = "Use |proj| today.\n\n.. |proj| replace:: RichRST\n"
    out = render_text(rst)
    # Should appear exactly once (the resolved reference), not twice
    assert out.count("RichRST") == 1
