"""Tests for miscellaneous RST directives.

Covers: images, figures, topics, sidebars, rubrics, field lists, option
lists, citations, footnotes, and definition lists.

Formatting contract
-------------------
* **Image** — rendered as a ``Text`` starting with the 🌆 emoji; when
  alt text is supplied it follows the emoji with a ``#6088ff`` (link-style)
  coloured span.
* **Figure** — rendered as a ``Panel`` with ``border_style='blue'``,
  ``title`` equal to the caption text, and ``subtitle`` equal to the
  legend text (or ``None`` when no legend is present).
* **Topic** — rendered as a ``Panel`` whose ``title`` equals the topic
  heading.
* **Sidebar** — rendered as a ``Panel`` whose ``title`` equals the
  sidebar heading.
* **Rubric** — rendered as a ``Panel`` with ``border_style='dim italic'``
  and an ``Align('center')`` renderable containing the rubric text.
* **Field list** — rendered as a ``Table`` with column headers
  ``"Field Name"`` and ``"Field Value"``.
* **Citation** — rendered as a ``Panel`` with ``title='citation'`` and
  ``border_style='grey74'``.
* **Footnote reference** — the bracket label (e.g. ``[1]``) in the body
  is rendered with a ``grey74`` coloured span.
"""
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


# ── Images ────────────────────────────────────────────────────────────────────

def test_image_renders_picture_emoji(make_visitor):
    visitor = make_visitor(".. image:: photo.png\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert any(t.plain.startswith("🌆") for t in texts), (
        "Image must render a Text starting with the 🌆 emoji"
    )


def test_image_alt_text_colour_span(make_visitor):
    visitor = make_visitor(".. image:: photo.png\n   :alt: A beautiful photo\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    img_texts = [t for t in texts if "🌆" in t.plain]
    assert img_texts
    alt_spans = [
        s for s in img_texts[0]._spans
        if s.style.color and s.style.color.get_truecolor().hex == "#6088ff"
    ]
    assert alt_spans, "Image alt text must have a #6088ff coloured span"


def test_image_alt_text_content_in_plain(render_text):
    assert "A beautiful photo" in render_text(
        ".. image:: photo.png\n   :alt: A beautiful photo\n"
    )


def test_image_without_alt_does_not_crash(render_text):
    out = render_text(".. image:: photo.png\n")
    assert isinstance(out, str)


# ── Figures ───────────────────────────────────────────────────────────────────

def test_figure_produces_panel(make_visitor):
    visitor = make_visitor(".. figure:: img.png\n\n   Caption text\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"


def test_figure_border_style_is_blue(make_visitor):
    visitor = make_visitor(".. figure:: img.png\n\n   Caption.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert str(panels[0].border_style) == "blue", (
        f"Figure panel border_style must be 'blue', got {panels[0].border_style!r}"
    )


def test_figure_title_equals_caption(make_visitor):
    visitor = make_visitor(".. figure:: img.png\n\n   The chart caption\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "The chart caption", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )


def test_figure_without_legend_subtitle_is_none(make_visitor):
    visitor = make_visitor(".. figure:: img.png\n\n   Caption only.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].subtitle is None, "Figure without legend must have subtitle=None"


def test_figure_legend_sets_subtitle(make_visitor):
    rst = ".. figure:: img.png\n\n   Caption.\n\n   Legend text here.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].subtitle == "Legend text here.", (
        f"Figure legend must set panel subtitle, got {panels[0].subtitle!r}"
    )


def test_figure_legend_visible(make_visitor):
    rst = ".. figure:: img.png\n\n   Caption.\n\n   Legend text here.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].subtitle == "Legend text here."


# ── Topics ────────────────────────────────────────────────────────────────────

def test_topic_produces_panel(make_visitor):
    visitor = make_visitor(".. topic:: My Topic\n\n   Topic body.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_topic_title_equals_heading(make_visitor):
    visitor = make_visitor(".. topic:: Important Topic\n\n   Content here.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "Important Topic", (
        f"Topic panel title must equal the heading, got {panels[0].title!r}"
    )


def test_topic_body_visible(render_text):
    assert "Body content." in render_text(".. topic:: Title\n\n   Body content.\n")


# ── Sidebars ──────────────────────────────────────────────────────────────────

def test_sidebar_produces_panel(make_visitor):
    visitor = make_visitor(".. sidebar:: Side Note\n\n   Sidebar content.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_sidebar_title_equals_heading(make_visitor):
    visitor = make_visitor(".. sidebar:: My Sidebar\n\n   Content.\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "My Sidebar", (
        f"Sidebar panel title must equal the heading, got {panels[0].title!r}"
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


def test_rubric_panel_border_style(make_visitor):
    visitor = make_visitor(".. rubric:: My Rubric\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert str(panels[0].border_style) == "dim italic", (
        f"Rubric border_style must be 'dim italic', got {panels[0].border_style!r}"
    )


def test_rubric_panel_contains_centred_align(make_visitor):
    visitor = make_visitor(".. rubric:: Section Rubric\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    align = panels[0].renderable
    assert isinstance(align, Align), "Rubric panel renderable must be an Align"
    assert align.align == "center", "Rubric text must be centred"


def test_rubric_text_in_align_renderable(make_visitor):
    visitor = make_visitor(".. rubric:: Section Rubric\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    align = panels[0].renderable
    # Rubric text is stored as a plain string in the Align
    rubric_text = align.renderable if hasattr(align, "renderable") else str(align)
    assert "Section Rubric" in str(rubric_text), (
        f"Rubric Align renderable must contain 'Section Rubric', got {rubric_text!r}"
    )


# ── Field lists ───────────────────────────────────────────────────────────────

def test_field_list_produces_table(make_visitor):
    visitor = make_visitor(":Name: Alice\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "A field list must produce a Table renderable"


def test_field_list_column_headers(make_visitor):
    visitor = make_visitor(":Name: Alice\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert [c.header for c in tables[0].columns] == ["Field Name", "Field Value"], (
        "Field list table must have columns ['Field Name', 'Field Value']"
    )


def test_field_list_name_and_value_visible(render_text):
    out = render_text(":Color: blue\n")
    assert "Color" in out
    assert "blue" in out


def test_field_list_multiple_consecutive_fields_share_one_table(make_visitor):
    visitor = make_visitor(":Name: Alice\n:Age: 30\n")
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert len(tables) == 1, "Consecutive field list entries must share one Table"
    assert tables[0].row_count == 2


# ── Option lists ──────────────────────────────────────────────────────────────

def test_option_list_short_option_visible(render_text):
    out = render_text("-v  Enable verbose output.\n")
    assert "-v" in out
    assert "Enable verbose output" in out, (
        "Option list must render the option description alongside the flag"
    )


def test_option_list_long_option_visible(render_text):
    out = render_text("--output FILE  Write output to FILE.\n")
    assert "--output" in out
    assert "Write output to FILE" in out, (
        "Option list must render the option description alongside the long flag"
    )


def test_option_list_multiple_options_all_visible(render_text):
    out = render_text("-v  Verbose.\n-q  Quiet.\n")
    assert "-v" in out
    assert "Verbose" in out, "Option -v description must be rendered"
    assert "-q" in out
    assert "Quiet" in out, "Option -q description must be rendered"


# ── Citations ─────────────────────────────────────────────────────────────────

def test_citation_produces_panel_with_citation_title(make_visitor):
    rst = "See [Foo]_.\n\n.. [Foo] The book.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    citation_panels = [p for p in panels if p.title == "citation"]
    assert citation_panels, "Citation body must produce a Panel with title 'citation'"


def test_citation_panel_border_style_is_grey74(make_visitor):
    rst = "See [Foo]_.\n\n.. [Foo] The book.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    citation_panels = [p for p in panels if p.title == "citation"]
    assert citation_panels
    assert str(citation_panels[0].border_style) == "grey74", (
        f"Citation border_style must be 'grey74', got {citation_panels[0].border_style!r}"
    )


def test_citation_body_content_visible(render_text):
    rst = "See [Author2024]_.\n\n.. [Author2024] A great book.\n"
    assert "A great book." in render_text(rst)


def test_citation_reference_label_visible(render_text):
    rst = "See [Author2024]_.\n\n.. [Author2024] A great book.\n"
    assert "Author2024" in render_text(rst)


# ── Footnotes ─────────────────────────────────────────────────────────────────

def test_footnote_reference_bracket_label_has_grey74_span(make_visitor):
    visitor = make_visitor("Text with footnote [1]_.\n\n.. [1] Footnote body.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # Find the paragraph containing the footnote reference
    ref_texts = [t for t in texts if "[1]" in t.plain or "[1]." in t.plain.replace("\n", "")]
    assert ref_texts
    grey_spans = [
        s for s in ref_texts[0]._spans
        if s.style.color and s.style.color.name == "grey74"
    ]
    assert grey_spans, "Footnote reference [1] must have a grey74 coloured span"


def test_footnote_body_in_visitor_footer(make_visitor):
    visitor = make_visitor("Text [1]_.\n\n.. [1] Footnote body here.\n")
    assert visitor.footer, "Footnote body must populate visitor.footer"


def test_footnote_body_content_visible(render_text):
    rst = "Text [1]_.\n\n.. [1] Footnote body here.\n"
    assert "Footnote body here." in render_text(rst)


# ── Definition lists ──────────────────────────────────────────────────────────

def test_definition_list_term_visible(render_text):
    assert "apple" in render_text("apple\n    A fruit.\n")


def test_definition_list_definition_visible(render_text):
    assert "A fruit." in render_text("apple\n    A fruit.\n")


def test_definition_list_term_style_is_cyan(make_visitor):
    visitor = make_visitor("apple\n    A fruit.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # The definition-list item renders as a single Text with cyan base style
    cyan_texts = [t for t in texts if t.style and str(t.style) == "cyan"]
    assert cyan_texts, "Definition list term must have a 'cyan' base style"
    assert "apple" in cyan_texts[0].plain


def test_definition_list_multiple_items(render_text):
    rst = "cat\n    A feline.\n\ndog\n    A canine.\n"
    out = render_text(rst)
    assert "cat" in out
    assert "A feline." in out
    assert "dog" in out
    assert "A canine." in out
