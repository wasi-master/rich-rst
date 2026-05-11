import pytest
from unittest.mock import Mock

import rich_rst
from rich_rst import RestructuredText


def _render(markup: str, **kwargs) -> str:
    return RestructuredText(markup, **kwargs).render_to_string(width=100, force_terminal=True)


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

    output = _render(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    )
    assert "Included paragraph." in output


def test_include_directive_start_end_line_options(tmp_path):
    included = tmp_path / "included.rst"
    included.write_text("line1\nline2\nline3\nline4\n", encoding="utf-8")
    document = tmp_path / "document.rst"
    document.write_text(
        ".. include:: included.rst\n   :start-line: 1\n   :end-line: 3\n",
        encoding="utf-8",
    )

    output = _render(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    )
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

    output = _render(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    )
    assert "Rejected include path outside source directory" in output


def test_include_directive_unicode_decode_error_shows_warning(tmp_path):
    binary_file = tmp_path / "bad.rst"
    binary_file.write_bytes(b"\xff\xfe\x00")
    document = tmp_path / "document.rst"
    document.write_text(".. include:: bad.rst\n", encoding="utf-8")

    output = _render(
        document.read_text(encoding="utf-8"),
        filename=str(document),
        sphinx_compat=True,
        show_errors=True,
    )
    assert "Could not include file: 'bad.rst'" in output


def test_flat_table_invalid_cspan_reports_error():
    inliner = Mock()
    message = object()
    problematic = object()
    inliner.reporter.error.return_value = message
    inliner.problematic.return_value = problematic

    nodes, messages = rich_rst._flat_table_cspan("cspan", ":cspan:`-1`", "-1", 10, inliner)
    assert nodes == [problematic]
    assert messages == [message]
    inliner.reporter.error.assert_called_once()
    inliner.problematic.assert_called_once()


def test_flat_table_invalid_rspan_reports_error():
    inliner = Mock()
    message = object()
    problematic = object()
    inliner.reporter.error.return_value = message
    inliner.problematic.return_value = problematic

    nodes, messages = rich_rst._flat_table_rspan("rspan", ":rspan:`-1`", "-1", 10, inliner)
    assert nodes == [problematic]
    assert messages == [message]
    inliner.reporter.error.assert_called_once()
    inliner.problematic.assert_called_once()


def test_flat_table_empty_content_reports_error():
    output = _render(".. flat-table::\n", show_errors=True)
    assert 'directive is empty; content required.' in output


def test_code_block_malformed_emphasize_lines_is_ignored(make_visitor):
    rst = """.. code-block:: python
   :emphasize-lines: 1,not-a-number,7-2,3-4

   a = 1
   b = 2
   c = 3
   d = 4
"""
    visitor = make_visitor(rst)
    panels = [renderable for renderable in visitor.renderables if hasattr(renderable, "renderable")]
    syntax = panels[0].renderable
    assert syntax.highlight_lines == {1, 3, 4}


def test_code_block_with_number_lines_sets_start_line(make_visitor):
    rst = """.. code-block:: python
   :number-lines: 12

   x = 1
"""
    visitor = make_visitor(rst)
    panels = [renderable for renderable in visitor.renderables if hasattr(renderable, "renderable")]
    syntax = panels[0].renderable
    assert syntax.start_line == 12


def test_code_block_dedent_non_numeric_falls_back_to_auto_dedent(make_visitor):
    rst = """.. code-block:: python
   :dedent: not-a-number

       def foo():
           return 1
"""
    visitor = make_visitor(rst)
    panels = [renderable for renderable in visitor.renderables if hasattr(renderable, "renderable")]
    syntax = panels[0].renderable
    assert syntax.code.lstrip().startswith("def foo")


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


def test_definition_list_with_multiple_classifiers_renders_all_content(render_text):
    rst = """\
term : type-a : type-b
    Intro paragraph.

    * bullet value

    #. enum value

    ``inline``

    ::

        print(1)
"""
    output = render_text(rst)
    assert "term : type-a : type-b" in output
    assert "Intro paragraph." in output
    assert "bullet value" in output
    assert "enum value" in output
    assert "inline" in output
    assert "print(1)" in output
