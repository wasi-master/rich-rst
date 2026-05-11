import pytest
from rich.console import Console
from rich.text import Text

import rich_rst
from rich_rst import RSTVisitor, RestructuredText
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core


def test_validate_default_lexer_name_accepts_none():
    assert rich_rst._validate_default_lexer_name(None) is None


def test_validate_default_lexer_name_rejects_unknown():
    with pytest.raises(ValueError):
        rich_rst._validate_default_lexer_name("definitely-not-a-lexer")


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


def test_spanning_table_shrinks_for_narrow_console():
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - H1\n"
        "     - H2\n\n"
        "   * - :cspan:`1` SUPERLONGUNBREAKABLETOKENAAAAAAAAAAAAAAA\n"
    )
    output = RestructuredText(rst).render_to_string(width=18, force_terminal=True)
    assert "SUPERLONGUNBRE" in output
    assert "AKABLETOKEN" in output
