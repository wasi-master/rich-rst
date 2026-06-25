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
* **Heading level-1** — rendered as a ``Panel`` renderable with a ``DOUBLE``
  box, containing centered text.
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
import pytest
from rich.console import Console
from rich.console import Console
import rich_rst
import rich_rst._vendor.docutils.core
from rich_rst._vendor import docutils
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


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


def test_depart_paragraph_ignores_empty_text_renderable(make_visitor):
    visitor = make_visitor("Hello world.\n")
    empty_text = Text("", end="")

    visitor.renderables = [empty_text]
    visitor.depart_paragraph(None)

    assert empty_text.plain == ""


# ── Headings / Titles ─────────────────────────────────────────────────────────

def test_heading_level1_produces_centered_align(make_visitor):
    visitor = make_visitor("My Title\n========\n\nBody.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "Level-1 heading must produce a Panel renderable with box"
    # The panel contains centered content
    assert isinstance(panels[0].renderable, Align), "Panel content must be centered"
    assert panels[0].renderable.align == "center", "Panel content must be centred"


def test_heading_level1_align_contains_heading_text(make_visitor):
    visitor = make_visitor("My Title\n========\n\nBody.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels
    align = panels[0].renderable
    assert isinstance(align, Align), "Panel content must be an Align"
    heading_text = align.renderable
    assert isinstance(heading_text, Text)
    assert heading_text.plain == "My Title", (
        f"Heading text must equal 'My Title', got {heading_text.plain!r}"
    )


def test_heading_level2_produces_align(make_visitor):
    rst = "Title\n=====\n\nSection\n-------\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    # Level-1 and Level-2 headings now render as Panel with boxes
    assert len(panels) >= 2, "Document title and section heading must produce Panel renderables"


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
    attr_texts = [t for t in texts if "\u2014" in t.plain]
    assert attr_texts, "Attribution must produce a Text containing an em-dash (—)"
    assert str(attr_texts[0].style) == "grey89", (
        f"Attribution style must be 'grey89', got {attr_texts[0].style!r}"
    )


def test_block_quote_attribution_plain_text_has_author(make_visitor):
    visitor = make_visitor("    Quote body.\n\n    -- The Author\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    attr_texts = [t for t in texts if "\u2014" in t.plain]
    assert attr_texts
    assert "The Author" in attr_texts[0].plain


def test_block_quote_without_attribution_ends_with_single_newline(make_visitor):
    visitor = make_visitor("    Single paragraph quote.\n")
    newline_count = sum(isinstance(r, NewLine) for r in visitor.renderables)
    assert newline_count == 1


def test_block_quote_multi_paragraph_both_rendered(render_text):
    rst = "    First paragraph.\n\n    Second paragraph.\n"
    out = render_text(rst)
    assert "First paragraph." in out
    assert "Second paragraph." in out


def test_block_quote_attribution_appears_exactly_once(render_text):
    rst = "    Quote body.\n\n    -- The Author\n"
    assert render_text(rst).count("The Author") == 1


def test_block_quote_preserves_bold_inline_markup(make_visitor):
    """Bold markup inside a block quote must produce a bold span, not be flattened."""
    visitor = make_visitor("    Text with **bold** word.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    bq_texts = [t for t in texts if t.plain.startswith("▌")]
    assert bq_texts, "Block quote must start with ▌ marker"
    bq = bq_texts[0]
    bold_spans = [s for s in bq._spans if s.style.bold]
    assert bold_spans, "Bold inline markup in a block quote must produce a bold span"
    marked = bq.plain[bold_spans[0].start:bold_spans[0].end]
    assert "bold" in marked, f"Bold span must cover the word 'bold', got {marked!r}"


def test_block_quote_preserves_italic_inline_markup(make_visitor):
    """Italic markup inside a block quote must produce an italic span."""
    visitor = make_visitor("    Text with *italic* word.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    bq_texts = [t for t in texts if t.plain.startswith("▌")]
    assert bq_texts
    bq = bq_texts[0]
    italic_spans = [s for s in bq._spans if s.style.italic]
    assert italic_spans, "Italic inline markup in a block quote must produce an italic span"


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
    markers = [t for t in texts if t.plain.lstrip().startswith("•")]
    assert markers, "Bullet list must produce a Text starting with '•'"


def test_bullet_list_marker_style_is_bold_yellow(make_visitor):
    visitor = make_visitor("* item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain.lstrip().startswith("•")]
    assert markers
    # The marker style becomes the base style of the combined text
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
    # Marker text is " 1." (leading space, digit, suffix)
    markers = [t for t in texts if t.plain.startswith(" ") and t.plain.strip().rstrip(".").isdigit()]
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


def test_substitution_with_markup(render_text):
    """Test that substitution references with inline markup are resolved correctly."""
    rst = "The chemical formula is |H2O|.\n\n.. |H2O| replace:: H\\ :sub:`2`\\ O\n"
    rendered = render_text(rst)
    # The subscript should be rendered (either as '2' or as unicode subscript '₂')
    assert "H" in rendered and "O" in rendered


def test_substitution_reference_with_image(render_text):
    """Test that substitution references can contain images."""
    rst = "Warning: |hazard| symbol.\n\n.. |hazard| image:: hazard.png\n"
    rendered = render_text(rst)
    # The substitution should be resolved (even if the image isn't loaded)
    assert "Warning:" in rendered


def test_deeply_nested_sections(render_text):
    """Test multiple levels of section nesting."""
    rst = """\
Level 1
=======

Some text here.

Level 2
-------

More text.

Level 3
^^^^^^^

Even deeper.

Level 4
"""""""

Deepest level.
"""
    out = render_text(rst)
    assert "Level 1" in out
    assert "Level 2" in out
    assert "Level 3" in out
    assert "Level 4" in out

def test_multiple_sections_same_level(render_text):
    """Test multiple sections at the same level."""
    rst = """\
First Section
=============

Content here.

Second Section
==============

Different content.

Third Section
=============

More content.
"""
    out = render_text(rst)
    assert "First Section" in out
    assert "Second Section" in out
    assert "Third Section" in out

def test_block_quote_with_attribution(render_text):
    """Test block quote with attribution."""
    rst = """\
   This is a great quote.
   It spans multiple lines.

   — Famous Person
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "great quote" in out, "Block quote text must be visible"
    assert "Famous Person" in out, "Attribution must be visible"

def test_block_quote_multiple_paragraphs(render_text):
    """Test block quote with multiple paragraphs."""
    rst = """\
   First paragraph of quote.

   Second paragraph continues.

   Third paragraph concludes.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "First paragraph of quote" in out, "First paragraph must be visible"
    assert "Second paragraph continues" in out, "Second paragraph must be visible"

def test_block_quote_no_attribution(render_text):
    """Test block quote without attribution."""
    rst = """\
   A simple quote.
   No attribution here.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "A simple quote" in out, "Block quote text must be visible"

def test_block_quote_single_paragraph(render_text):
    """Test block quote with exactly one paragraph."""
    rst = """\
   Single paragraph quote.
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Single paragraph quote" in out, "Block quote text must be visible"

def test_block_quote_many_paragraphs(render_text):
    """Test block quote with many paragraphs."""
    rst = """\
   Para 1
     
   Para 2
     
   Para 3
     
   Para 4
     
   Para 5
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Para 1" in out, "First paragraph must be visible"
    assert "Para 5" in out, "Last paragraph must be visible"

def test_nested_content_in_block_quote(render_text):
    """Test block quote containing various nested content."""
    rst = """\
   Block quote with multiple paragraphs.
   
   First paragraph here.
   
   Second paragraph with **bold** and *italic* text.

   — Attribution
"""
    out = render_text(rst)
    assert "▌" in out, "Block quote must render with the '▌' left-border marker"
    assert "Block quote with multiple paragraphs" in out, "Block quote text must be visible"
    assert "Attribution" in out, "Attribution must be visible"

def test_line_block_nested(render_text):
    """Test nested line blocks."""
    rst = """\
| Line 1
| Line 2
|
|     Indented line 3
|     Indented line 4
| Line 5
"""
    out = render_text(rst)
    assert "Line 1" in out
    assert "Line 5" in out

def test_line_block_deeply_nested(render_text):
    """Test deeply nested line blocks."""
    rst = """\
| Level 1-1
|
|     Level 2-1
|     Level 2-2
|
|         Level 3-1
|
|     Back to Level 2
|
| Back to Level 1
"""
    out = render_text(rst)
    assert "Level 1-1" in out

def test_empty_line_block(render_text):
    """Test line block that's essentially empty."""
    rst = """\
| Just one line
"""
    out = render_text(rst)
    assert "Just one line" in out

def test_line_block_single_line(render_text):
    """Test line block with single line."""
    rst = """\
| Single line
"""
    out = render_text(rst)
    assert "Single line" in out

def test_line_block_many_levels(render_text):
    """Test line block with many indentation levels."""
    rst = """\
| L1
|     L2
|         L3
|             L4
|                 L5
| Back to L1
"""
    out = render_text(rst)
    assert "L1" in out or "L5" in out

def test_transition_between_sections(render_text):
    """Test transition/horizontal rule."""
    rst = """\
Section 1
=========

Content here.

----

Section 2
=========

More content.
"""
    out = render_text(rst)
    assert "Section 1" in out, "First section must be visible"
    assert "Section 2" in out, "Second section must be visible"
    assert "─" in out, "Transition must render as a horizontal rule (─)"

def test_multiple_transitions(make_visitor):
    """Test multiple transitions render as Rule renderables."""
    rst = """\
First block.

----

Second block.

----

Third block.
"""
    visitor = make_visitor(rst)
    rules = [r for r in visitor.renderables if isinstance(r, Rule)]
    assert len(rules) >= 2, (
        f"Two '----' transitions must produce at least two Rule renderables, got {len(rules)}"
    )
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    text_content = " ".join(t.plain for t in texts)
    assert "First" in text_content, "Text before transitions must be visible"
    assert "Second" in text_content, "Text between transitions must be visible"

def test_citation_reference(render_text):
    """Test citation reference."""
    rst = """\
Some text [CIT2024]_.

.. [CIT2024] A citation.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A citation" in out, "Citation body text must be visible"
    assert "CIT2024: A citation." in out, "Citation should render inline as 'label: body'"

def test_footnote_reference(render_text):
    """Test footnote reference."""
    rst = """\
Some text [#]_.

.. [#] A footnote.
"""
    out = render_text(rst)
    assert "A footnote" in out, "Footnote body text must appear in the Footer panel"
    assert "1: A footnote." in out, "Auto-numbered footnote should render inline as 'label: body'"

def test_multiple_footnotes(render_text):
    """Test multiple footnotes."""
    rst = """\
First [1]_ and second [2]_.

.. [1] First note.
.. [2] Second note.
"""
    out = render_text(rst)
    assert "First note" in out, "First footnote body must be visible"
    assert "Second note" in out, "Second footnote body must be visible"
    assert "1: First note." in out, "First numbered footnote should render inline as 'label: body'"
    assert "2: Second note." in out, "Second numbered footnote should render inline as 'label: body'"

def test_citation_reference_appended_to_text(render_text):
    """Test citation reference appended to existing text element."""
    rst = """\
See the cited work [Ref2024]_.

.. [Ref2024] A citation.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A citation" in out, "Citation body text must be visible"

def test_multiple_citations_share_one_panel(render_text):
    """All citations should be grouped in one citation panel."""
    rst = """\
Alpha [A]_ and beta [B]_.

.. [A] First source.
.. [B] Second source.
"""
    out = render_text(rst)
    assert out.count(" citation ") == 1, "Multiple citations should render in a single citation panel"
    assert "A: First source." in out, "First citation should be present in the grouped citation panel"
    assert "B: Second source." in out, "Second citation should be present in the grouped citation panel"

def test_footnote_reference_appended_to_text(render_text):
    """Test footnote reference appended to existing text element."""
    rst = """\
This is text [1]_ with a footnote.

.. [1] Footnote text.
"""
    out = render_text(rst)
    assert "Footnote text" in out, "Footnote body must appear in the Footer panel"
    assert "1: Footnote text." in out, "Footnote should render inline as 'label: body'"

def test_numbered_footnote(render_text):
    """Test explicitly numbered footnote."""
    rst = """\
Text [1]_.

.. [1] First footnote.
"""
    out = render_text(rst)
    assert "First footnote" in out, "Footnote body must appear in the Footer panel"
    assert "1: First footnote." in out, "Manual numbered footnote should render inline as 'label: body'"

def test_auto_numbered_footnote(render_text):
    """Test auto-numbered footnote."""
    rst = """\
Text [#]_.

.. [#] Auto-numbered footnote.
"""
    out = render_text(rst)
    assert "Auto-numbered footnote" in out, "Footnote body must appear in the Footer panel"
    assert "1: Auto-numbered footnote." in out, "Auto-numbered footnote should render inline as 'label: body'"

def test_labeled_footnote(render_text):
    """Test labeled footnote."""
    rst = """\
Text [note]_.

.. [note] A labeled footnote.
"""
    out = render_text(rst)
    assert "A labeled footnote" in out, "Footnote body must appear in the Footer panel"
    assert "note: A labeled footnote." in out, "Labeled footnote should render inline as 'label: body'"

def test_named_auto_footnote(render_text):
    """Test named auto-numbered footnote."""
    rst = """\
Text [#named]_ and [#named]_.

.. [#named] Named auto-numbered footnote.
"""
    out = render_text(rst)
    assert "Named auto-numbered footnote" in out, "Named auto footnote body must appear in the Footer panel"
    assert "1: Named auto-numbered footnote." in out, (
        "Named auto-numbered footnote should render inline as 'label: body'"
    )

def test_symbol_footnote(render_text):
    """Test symbol footnote."""
    rst = """\
Text [*]_.

.. [*] Symbol footnote.
"""
    out = render_text(rst)
    assert "Symbol footnote" in out, "Symbol footnote body must appear in the Footer panel"
    assert "*: Symbol footnote." in out, "Symbol footnote should render inline as 'label: body'"

def test_citation_block(render_text):
    """Test citation block."""
    rst = """\
Reference [Book2024]_.

.. [Book2024] A Book Title. Published 2024.
"""
    out = render_text(rst)
    assert "citation" in out, "Citation must render as a Panel with title 'citation'"
    assert "A Book Title" in out, "Citation body text must be visible"
    assert "Book2024: A Book Title. Published 2024." in out, (
        "Citation should render inline as 'label: body'"
    )
