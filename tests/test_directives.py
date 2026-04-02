"""Tests for miscellaneous RST directives.

Covers: images, figures, topics, sidebars, rubrics, field lists, option
lists, citations, footnotes, and the definition list (beyond the dedicated
test_definition_list.py file).
"""
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


# ── Images ────────────────────────────────────────────────────────────────────

def test_image_renders_picture_emoji(make_visitor):
    visitor = make_visitor(".. image:: photo.png\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "🌆" in combined


def test_image_alt_text_visible(render_text):
    rst = ".. image:: photo.png\n   :alt: A beautiful photo\n"
    assert "A beautiful photo" in render_text(rst)


def test_image_without_alt_does_not_crash(render_text):
    out = render_text(".. image:: photo.png\n")
    assert isinstance(out, str)


# ── Figures ───────────────────────────────────────────────────────────────────

def test_figure_produces_panel(make_visitor):
    rst = ".. figure:: img.png\n\n   Caption text\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"


def test_figure_caption_visible(render_text):
    assert "The chart caption" in render_text(
        ".. figure:: chart.png\n\n   The chart caption\n"
    )


def test_figure_legend_visible(render_text):
    rst = ".. figure:: img.png\n\n   Caption.\n\n   Legend text here.\n"
    assert "Legend text here." in render_text(rst)


# ── Topics ────────────────────────────────────────────────────────────────────

def test_topic_produces_panel(make_visitor):
    rst = ".. topic:: My Topic\n\n   Topic body.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_topic_title_in_panel(make_visitor):
    rst = ".. topic:: Important Topic\n\n   Content here.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert "Important Topic" in panels[0].title


def test_topic_body_visible(render_text):
    assert "Body content." in render_text(
        ".. topic:: Title\n\n   Body content.\n"
    )


def test_topic_body_with_bullet_list(render_text):
    rst = ".. topic:: Index\n\n   * item one\n   * item two\n"
    out = render_text(rst)
    assert "item one" in out
    assert "item two" in out


# ── Sidebars ──────────────────────────────────────────────────────────────────

def test_sidebar_produces_panel(make_visitor):
    rst = ".. sidebar:: Side Note\n\n   Sidebar content.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_sidebar_title_visible(render_text):
    assert "My Sidebar" in render_text(
        ".. sidebar:: My Sidebar\n\n   Content.\n"
    )


def test_sidebar_body_visible(render_text):
    assert "Some side content." in render_text(
        ".. sidebar:: Note\n\n   Some side content.\n"
    )


# ── Rubrics ───────────────────────────────────────────────────────────────────

def test_rubric_produces_panel(make_visitor):
    visitor = make_visitor(".. rubric:: My Rubric\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_rubric_title_visible(render_text):
    assert "Section Rubric" in render_text(".. rubric:: Section Rubric\n")


# ── Field lists ───────────────────────────────────────────────────────────────

def test_field_list_produces_table(make_visitor):
    visitor = make_visitor(":Name: Alice\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "A field list must produce a Table renderable"


def test_field_list_name_visible(render_text):
    assert "Color" in render_text(":Color: blue\n")


def test_field_list_value_visible(render_text):
    assert "blue" in render_text(":Color: blue\n")


def test_field_list_multiple_consecutive_share_one_table(make_visitor):
    visitor = make_visitor(":Name: Alice\n:Age: 30\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert len(tables) == 1, "Consecutive fields must share one Table"
    assert tables[0].row_count == 2


def test_field_list_three_fields(make_visitor):
    visitor = make_visitor(":A: 1\n:B: 2\n:C: 3\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].row_count == 3


# ── Option lists ──────────────────────────────────────────────────────────────

def test_option_list_short_option_visible(render_text):
    assert "-v" in render_text("-v  Enable verbose output.\n")


def test_option_list_description_visible(render_text):
    assert "verbose" in render_text("-v  Enable verbose output.\n")


def test_option_list_long_option_visible(render_text):
    assert "--output" in render_text("--output FILE  Write output to FILE.\n")


def test_option_list_multiple_options_all_visible(render_text):
    out = render_text("-v  Verbose.\n-q  Quiet.\n")
    assert "-v" in out
    assert "-q" in out


# ── Citations ─────────────────────────────────────────────────────────────────

def test_citation_body_produces_panel(make_visitor):
    rst = "See [Foo]_.\n\n.. [Foo] The book.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    citation_panels = [p for p in panels if p.title == "citation"]
    assert citation_panels, "Citation body must produce a Panel with title 'citation'"


def test_citation_body_content_visible(render_text):
    rst = "See [Author2024]_.\n\n.. [Author2024] A great book.\n"
    assert "A great book." in render_text(rst)


def test_citation_reference_label_visible(render_text):
    rst = "See [Author2024]_.\n\n.. [Author2024] A great book.\n"
    out = render_text(rst)
    assert "Author2024" in out


# ── Footnotes ─────────────────────────────────────────────────────────────────

def test_footnote_reference_bracket_label_visible(render_text):
    rst = "Text with footnote [1]_.\n\n.. [1] Footnote body.\n"
    assert "[1]" in render_text(rst)


def test_footnote_body_in_footer(make_visitor):
    rst = "Text [1]_.\n\n.. [1] Footnote body here.\n"
    visitor = make_visitor(rst)
    # Footnote body goes to visitor.footer (rendered separately)
    assert visitor.footer, "Footnote body must populate visitor.footer"


def test_footnote_body_content_visible(render_text):
    rst = "Text [1]_.\n\n.. [1] Footnote body here.\n"
    assert "Footnote body here." in render_text(rst)


def test_auto_symbol_footnote_reference_visible(render_text):
    rst = "Text [*]_.\n\n.. [*] Auto-symbol footnote.\n"
    assert "Auto-symbol footnote." in render_text(rst)


# ── Definition lists ──────────────────────────────────────────────────────────

def test_definition_list_term_visible(render_text):
    assert "apple" in render_text("apple\n    A fruit.\n")


def test_definition_list_definition_visible(render_text):
    assert "A fruit." in render_text("apple\n    A fruit.\n")


def test_definition_list_with_classifier(render_text):
    out = render_text("term : classifier\n    description\n")
    assert "term" in out
    assert "classifier" in out
    assert "description" in out


def test_definition_list_multiple_items(render_text):
    rst = "cat\n    A feline.\n\ndog\n    A canine.\n"
    out = render_text(rst)
    assert "cat" in out
    assert "A feline." in out
    assert "dog" in out
    assert "A canine." in out
