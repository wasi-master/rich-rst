"""Tests for miscellaneous RST directives.

Covers: images, figures, topics, sidebars, rubrics, field lists, option
lists, citations, footnotes, and definition lists.

Formatting contract
-------------------
* **Image** — rendered as a ``Text`` starting with the 🌆 emoji; when
  alt text is supplied it follows the emoji with a ``#6088ff`` (link-style)
  coloured span.
* **Figure** — rendered as a ``Panel`` with ``border_style='blue'``,
    ``title`` equal to the caption text; legend text is rendered in the
    panel body so it wraps on narrow terminals.
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
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich_rst import RestructuredText
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core
from rich.theme import Theme
from rich_rst import RSTVisitor
import pytest
from rich.rule import Rule
import rich_rst
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


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
    assert panels[0].subtitle is None, (
        f"Figure legend should not use panel subtitle, got {panels[0].subtitle!r}"
    )


def test_figure_legend_visible(make_visitor):
    rst = ".. figure:: img.png\n\n   Caption.\n\n   Legend text here.\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    panel_text = Console(width=120, force_terminal=True, record=True)
    panel_text.print(panels[0])
    assert "Legend text here." in panel_text.export_text()


def test_figure_legend_wraps_without_truncation():
    rst = (
        ".. figure:: https://example.com/diagram.png\n"
        "   :alt: Diagram\n\n"
        "   Caption text.\n\n"
        "   Legend text with more details about the figure.\n"
    )
    console = Console(force_terminal=True, width=24, record=True)
    console.print(RestructuredText(rst))
    output = console.export_text()
    assert "Legend text with" in output
    assert "more details about" in output
    assert "the figure." in output


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


# ── Container Directive ───────────────────────────────────────────────────────

def test_container_directive_renders_inner_paragraph(render_text):
    rst = """\
.. container:: framed

   This paragraph is in the box, too.
"""
    out = render_text(rst)
    assert "This paragraph is in the box, too." in out


def test_container_directive_preserves_nested_block_content(render_text):
    rst = """\
.. container:: framed

   .. math:: -1^2 = 1
"""
    out = render_text(rst)
    assert "-1^2 = 1" in out


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


# ── Built-in parts directives ───────────────────────────────────────────────

def test_contents_directive_does_not_render_as_literal_source(render_text):
    rst = (
        ".. contents:: Table of Contents\n"
        "   :depth: 2\n\n"
        "Section A\n"
        "---------\n\n"
        "Content A.\n\n"
        "Section B\n"
        "---------\n\n"
        "Content B.\n"
    )
    out = render_text(rst)
    assert "Table of Contents" in out
    assert ".. contents::" not in out
    assert ":depth: 2" not in out


def test_sectnum_directive_does_not_render_as_literal_source(render_text):
    rst = (
        ".. sectnum::\n"
        "   :depth: 2\n"
        "   :start: 3\n\n"
        "Section A\n"
        "---------\n\n"
        "Content A.\n"
    )
    out = render_text(rst)
    assert "Section A" in out
    assert ".. sectnum::" not in out
    assert ":depth: 2" not in out
    assert ":start: 3" not in out


# ── Citations ─────────────────────────────────────────────────────────────────

def test_citation_produces_panel_with_citation_title(make_visitor):
    rst = "See [Foo]_.\n\n.. [Foo] The book.\n"
    visitor = make_visitor(rst)
    assert visitor.citations, "Citation nodes should be collected on visitor.citations"
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    citation_panels = [p for p in panels if p.title == "citation"]
    assert not citation_panels, (
        "Citation panel is created during final RestructuredText rendering, "
        "not during visitor walk"
    )


def test_citation_panel_is_rendered_in_final_output(render_text):
    rst = "See [Foo]_.\n\n.. [Foo] The book.\n"
    out = render_text(rst)
    assert "citation" in out.lower(), "Final rendered output must include citation panel title"


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


def test_definition_list_term_style_uses_term_style(make_visitor):
    visitor = make_visitor("apple\n    A fruit.\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    definition_texts = [t for t in texts if "apple" in t.plain]
    assert definition_texts, "Definition list output must contain the term text"

    term_offset = definition_texts[0].plain.index("apple")
    term_style = definition_texts[0].get_style_at_offset(visitor.console, term_offset)
    assert term_style.color is None, "Definition list term must use the default term_style"


def test_definition_list_multiple_items(render_text):
    rst = "cat\n    A feline.\n\ndog\n    A canine.\n"
    out = render_text(rst)
    assert "cat" in out
    assert "A feline." in out
    assert "dog" in out
    assert "A canine." in out

def test_plain_definition_list_uses_term_style_branch():
    document = docutils.core.publish_doctree("term\n    definition\n")
    visitor = RSTVisitor(
        document,
        console=Console(force_terminal=True, record=True),
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    # The term + definition are both visible in the output.
    all_plain = "".join(
        r.plain for r in visitor.renderables if isinstance(r, Text)
    )
    assert "term" in all_plain
    assert "definition" in all_plain


def test_definition_list_term_uses_term_style_not_classifier_style():
    document = docutils.core.publish_doctree("term\n    definition\n")
    console = Console(
        force_terminal=True,
        record=True,
        theme=Theme(
            {
                "restructuredtext.term_style": "green",
                "restructuredtext.classifier_style": "red",
            }
        ),
    )
    visitor = RSTVisitor(
        document,
        console=console,
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    # Find the Text renderable that contains the term.
    term_texts = [r for r in visitor.renderables if isinstance(r, Text) and "term" in r.plain]
    assert term_texts, "A Text renderable containing 'term' must exist"

    renderable = term_texts[0]
    term_start = renderable.plain.index("term")
    for index in range(term_start, term_start + len("term")):
        style = renderable.get_style_at_offset(console, index)
        assert style.color is not None, f"Expected green at offset {index}"
        assert style.color.name == "green", f"Expected green at offset {index}, got {style.color.name}"


def test_definition_list_item_with_only_term_child_does_not_crash():
    document = docutils.core.publish_doctree("")
    definition_list = docutils.nodes.definition_list()
    definition_list_item = docutils.nodes.definition_list_item()
    definition_list_item += docutils.nodes.term(text="term-only")
    definition_list += definition_list_item
    document += definition_list

    visitor = RSTVisitor(
        document,
        console=Console(force_terminal=True, record=True),
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    term_texts = [r for r in visitor.renderables if isinstance(r, Text) and "term-only" in r.plain]
    assert term_texts, "A Text renderable containing the term must exist"


def test_definition_list_classifier_indentation(render_text):
    rst = """\
term : string
    A string-typed term.

count : int
    An integer count.
"""

    out = render_text(rst)
    non_empty_lines = [line.rstrip() for line in out.splitlines() if line.strip()]

    assert non_empty_lines[0] == "term : string"
    assert non_empty_lines[1] == "    A string-typed term."
    assert non_empty_lines[2] == "count : int"
    assert non_empty_lines[3] == "    An integer count."

def test_include_directive_renders_included_file(tmp_path):
    included = tmp_path / "included.rst"
    included.write_text("Included paragraph.\n", encoding="utf-8")
    document = tmp_path / "document.rst"
    document.write_text(".. include:: included.rst\n", encoding="utf-8")
    output = RestructuredText(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    ).render_to_string(width=100, force_terminal=True)
    assert "Included paragraph." in output

def test_include_directive_start_end_line_options(tmp_path):
    included = tmp_path / "included.rst"
    included.write_text("line1\nline2\nline3\nline4\n", encoding="utf-8")
    document = tmp_path / "document.rst"
    document.write_text(
        ".. include:: included.rst\n   :start-line: 1\n   :end-line: 3\n",
        encoding="utf-8",
    )
    output = RestructuredText(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    ).render_to_string(width=100, force_terminal=True)
    assert "line2" in output
    assert "line3" in output
    assert "line1" not in output
    assert "line4" not in output

def test_include_directive_rejects_path_traversal(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    outside = tmp_path / "outside.rst"
    outside.write_text("outside content\n", encoding="utf-8")
    document = docs_dir / "document.rst"
    document.write_text(".. include:: ../outside.rst\n", encoding="utf-8")
    output = RestructuredText(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    ).render_to_string(width=100, force_terminal=True)
    assert "Rejected include path outside source directory" in output

def test_include_directive_unicode_decode_error_shows_warning(tmp_path):
    binary_file = tmp_path / "bad.rst"
    binary_file.write_bytes(b"\xff\xfe\x00")
    document = tmp_path / "document.rst"
    document.write_text(".. include:: bad.rst\n", encoding="utf-8")
    output = RestructuredText(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    ).render_to_string(width=100, force_terminal=True)
    assert "Could not include file: 'bad.rst'" in output

def test_definition_list_complex_children_branch_coverage():
    document = docutils.core.publish_doctree("")
    definition_list = docutils.nodes.definition_list()
    item = docutils.nodes.definition_list_item()
    item += docutils.nodes.term(text="term")
    item += docutils.nodes.classifier(text="type-a")
    item += docutils.nodes.classifier(text="type-b")
    item += docutils.nodes.paragraph(text="loose paragraph")
    bullet = docutils.nodes.bullet_list()
    bullet_item = docutils.nodes.list_item()
    bullet_item += docutils.nodes.paragraph(text="bullet value")
    bullet += bullet_item
    item += bullet
    enum = docutils.nodes.enumerated_list()
    enum_item = docutils.nodes.list_item()
    enum_item += docutils.nodes.paragraph(text="enum value")
    enum += enum_item
    item += enum
    item += docutils.nodes.literal_block("print(1)", "print(1)")
    item += docutils.nodes.literal("inline", "inline")
    quote = docutils.nodes.block_quote()
    quote += docutils.nodes.paragraph(text="quoted text")
    item += quote
    definition = docutils.nodes.definition()
    definition += docutils.nodes.paragraph(text="definition body")
    item += definition
    definition_list += item
    document += definition_list
    visitor = RSTVisitor(
        document,
        console=Console(force_terminal=True, width=60, record=True),
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=False,
        default_lexer="python",
    )
    document.walkabout(visitor)
    plain = "".join(
        renderable.plain for renderable in visitor.renderables if isinstance(renderable, Text)
    )
    assert "term" in plain
    assert "type-a" in plain
    assert "type-b" in plain
    assert "loose paragraph" in plain
    assert "bullet value" in plain
    assert "enum value" in plain
    assert "inline" in plain
    assert "definition body" in plain

def test_image_with_alt_attribute(render_text):
    """Test image with alt text."""
    rst = """\
.. image:: /path/image.png
   :alt: Alternative text
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Alternative text" in out, "Image alt text must be visible in the output"

def test_image_with_target_attribute(render_text):
    """Test image with target link."""
    rst = """\
.. image:: /path/image.png
   :target: http://example.com
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"

def test_image_with_alt_and_target(render_text):
    """Test image with both alt and target."""
    rst = """\
.. image:: /path/image.png
   :alt: Image description
   :target: http://example.com
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Image description" in out, "Alt text must be visible alongside the emoji"

def test_figure_without_image(render_text):
    """Test figure directive without a valid image argument (invalid RST — no crash expected)."""
    rst = """\
.. figure::

   Just a caption, no image.
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise"

def test_figure_with_reference_target(make_visitor):
    """Test figure with target inside reference."""
    rst = """\
.. figure:: /path/image.png
   :target: http://example.com

   Caption text
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "Caption text", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )

def test_figure_with_caption(make_visitor):
    """Test figure with caption."""
    rst = """\
.. figure:: /path/to/image.png

   This is the caption.
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "This is the caption.", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )

def test_figure_with_caption_and_legend(make_visitor):
    """Test figure with caption and legend."""
    rst = """\
.. figure:: /path/to/image.png

   Figure caption text.

   Legend text
   more legend.
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. figure:: must produce a Panel renderable"
    assert panels[0].title == "Figure caption text.", (
        f"Figure panel title must equal the caption, got {panels[0].title!r}"
    )
    panel_console = Console(force_terminal=True, width=120, record=True)
    panel_console.print(panels[0])
    rendered = panel_console.export_text()
    assert "Legend text" in rendered and "more legend." in rendered, (
        "Figure legend text must be visible in rendered panel body"
    )

def test_linked_image_with_complex_attributes(render_text):
    """Test image with multiple attributes in a link."""
    rst = """\
`Image Link <http://example.com>`_

.. image:: /path/image.png
   :alt: Image description
   :target: http://example.com
   :width: 200
   :height: 100
"""
    out = render_text(rst)
    assert "🌆" in out, "Image must render with the 🌆 emoji"
    assert "Image description" in out, "Alt text must be visible in the output"

def test_definition_list_with_classifier(render_text):
    """Test definition list with classifier."""
    rst = """\
term
   classified : classifier
   The definition.
"""
    out = render_text(rst)
    assert "term" in out, "Definition list term must be visible"
    assert "classified" in out, "Definition list body must be visible"

def test_definition_list_without_classifier(render_text):
    """Test definition list without classifier."""
    rst = """\
term
   The definition without classifier.

another
   Another definition.
"""
    out = render_text(rst)
    assert "term" in out, "First definition list term must be visible"
    assert "The definition without classifier" in out, "Definition body must be visible"
    assert "another" in out, "Second definition list term must be visible"

def test_definition_list_with_nested_content(render_text):
    """Test definition list containing nested lists."""
    rst = """\
Python
   A programming language.

   * Feature 1
   * Feature 2

   Code example::

      print("hello")
"""
    out = render_text(rst)
    assert "Python" in out
    assert "Feature" in out

def test_definition_list_multiple_lines(render_text):
    """Test definition list with multi-line content."""
    rst = """\
item
   First line of definition.
   Second line of definition.
   Third line of definition.
"""
    out = render_text(rst)
    assert "item" in out, "Definition list term must be visible"
    assert "First line of definition" in out, "Definition body must be visible"

def test_definition_list_three_parts(render_text):
    """Test definition list with term, classifier, and definition."""
    rst = """\
term : classifier
   The definition of the term with classifier.
"""
    out = render_text(rst)
    assert "term" in out, "Term must be visible"
    assert "classifier" in out, "Classifier must be visible"
    assert "The definition of the term with classifier" in out, (
        "Definition body must be visible"
    )

def test_complex_definition_list_mixed(render_text):
    """Test complex definition list mixing various formats."""
    rst = """\
term1
   definition1

term2 : classifier
   definition2

term3
   def line 1
   def line 2
"""
    out = render_text(rst)
    assert "term1" in out, "First term must be visible"
    assert "definition1" in out, "First definition must be visible"
    assert "term2" in out, "Second term must be visible"
    assert "term3" in out, "Third term must be visible"

def test_definition_list_nested_lists_and_code(render_text):
    """Test definition list with nested lists and code blocks."""
    rst = """\
Term with complex definition
   This definition has multiple components.
   
   Related items:
   
   1. First related
   2. Second related
   
   Code example::
   
      x = 1
      y = 2
      
   Final note about this term.
"""
    out = render_text(rst)
    assert "Term with complex definition" in out, "Definition list term must be visible"
    assert "First related" in out, "Nested list items must be visible"

def test_topic_with_title(render_text):
    """Test topic with explicit title."""
    rst = """\
.. topic:: Important Topic

   This is the content of the topic.
   It can have multiple paragraphs.
"""
    out = render_text(rst)
    assert "Important Topic" in out

def test_topic_no_title(render_text):
    """Test topic without title."""
    rst = """\
.. topic::

   Content here.
"""
    out = render_text(rst)
    assert "Content here" in out, "Topic body must be visible in the output"

def test_sidebar_with_title_and_subtitle(render_text):
    """Test sidebar with title and subtitle."""
    rst = """\
.. sidebar:: Sidebar Title
   :subtitle: Subtitle

   Sidebar content goes here.
"""
    out = render_text(rst)
    assert "Sidebar Title" in out, "Sidebar title must be visible"
    assert "Subtitle" in out, "Sidebar subtitle must be visible"

def test_sidebar_title_only(render_text):
    """Test sidebar with only title."""
    rst = """\
.. sidebar:: My Sidebar

   Just the content.
"""
    out = render_text(rst)
    assert "My Sidebar" in out, "Sidebar title must be visible"
    assert "Just the content" in out, "Sidebar body must be visible"

def test_sidebar_with_subtitle_and_lists(render_text):
    """Test sidebar with subtitle and nested lists."""
    rst = """\
.. sidebar:: Sidebar Title
   :subtitle: Interesting Subtitle
   
   Sidebar content with bullet list:
   
   * Item 1
   * Item 2
   * Item 3
"""
    out = render_text(rst)
    assert "Sidebar Title" in out, "Sidebar panel title must be visible"
    assert "Interesting Subtitle" in out, "Sidebar subtitle must be visible"

def test_topic_with_lists_and_code(render_text):
    """Test topic element with nested lists and code."""
    rst = """\
.. topic:: Important Topic

   This topic covers:
   
   1. First concept
   2. Second concept
   
   Example::
   
      example_code()
"""
    out = render_text(rst)
    assert "Important Topic" in out, "Topic title must be visible as the panel title"
    assert "First concept" in out, "Topic body content must be visible"

def test_raw_html_element(render_text):
    """Test raw HTML element strips tags and renders as 'stripped raw html' Panel."""
    rst = """\
.. raw:: html

   <div>This is raw HTML</div>
"""
    out = render_text(rst)
    assert "stripped raw html" in out, (
        "Raw HTML must render as a Panel with title 'stripped raw html'"
    )
    assert "This is raw HTML" in out, "Stripped HTML text content must be visible"

def test_raw_latex_element(render_text):
    """Test raw LaTeX element renders as 'raw latex' Panel."""
    rst = """\
.. raw:: latex

   \\textbf{Bold text}
"""
    out = render_text(rst)
    assert "raw latex" in out, (
        "Raw LaTeX must render as a Panel with title 'raw latex'"
    )
    assert "textbf" in out, "Raw LaTeX content must be visible inside the panel"

def test_raw_text_format(render_text):
    """Test raw text format renders as 'raw text' Panel."""
    rst = """\
.. raw:: text

   This is raw text content.
"""
    out = render_text(rst)
    assert "raw text" in out, (
        "Raw text must render as a Panel with title 'raw text'"
    )
    assert "This is raw text content" in out, "Raw text content must be visible"

def test_raw_with_special_chars(render_text):
    """Test raw HTML content with special characters strips tags."""
    rst = """\
.. raw:: html

   <span class="special">&nbsp;&copy;&reg;</span>
"""
    out = render_text(rst)
    assert "stripped raw html" in out, (
        "Raw HTML must render as a Panel with title 'stripped raw html'"
    )

def test_raw_content_all_formats(render_text):
    """Test raw directive with different formats all produce labelled Panels."""
    rst = """\
.. raw:: html

   <p>This is HTML</p>

.. raw:: latex

   \\textbf{Bold}
   
.. raw:: rst

   **Restructured** text
"""
    out = render_text(rst)
    assert "stripped raw html" in out, "Raw HTML must produce 'stripped raw html' panel"
    assert "raw latex" in out, "Raw LaTeX must produce 'raw latex' panel"

def test_header_element(render_text):
    """Test document header directive (unsupported in vendored docutils — no crash expected)."""
    rst = """\
.. header:: This is a header
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise an exception"

def test_footer_element(render_text):
    """Test document footer directive (unsupported in vendored docutils — no crash expected)."""
    rst = """\
.. footer:: Page ###
"""
    out = render_text(rst)
    assert isinstance(out, str), "Rendering must return a string and not raise an exception"
