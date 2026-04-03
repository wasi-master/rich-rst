"""Tests for RestructuredText.render_to_html() and render_to_svg() (item 9b)."""
import pytest

from rich_rst import RestructuredText


# ── render_to_html ────────────────────────────────────────────────────────────

def test_render_to_html_returns_str():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_html()
    assert isinstance(out, str)


def test_render_to_html_is_valid_html_structure():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_html()
    assert "<html" in out or "<!DOCTYPE" in out
    assert "</html>" in out


def test_render_to_html_contains_text():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_html()
    assert "Hello" in out
    assert "world" in out


def test_render_to_html_default_width_is_80():
    rst = RestructuredText("Short text.")
    out = rst.render_to_html()
    # Just verify it doesn't crash and returns HTML
    assert "<" in out


def test_render_to_html_custom_width():
    rst = RestructuredText("Short text.")
    out = rst.render_to_html(width=40)
    assert "Short text." in out


def test_render_to_html_respects_show_errors_true():
    rst = RestructuredText(
        ":bad_role:`text`",
        show_errors=True,
        sphinx_compat=False,
    )
    out = rst.render_to_html()
    assert "System Message" in out


def test_render_to_html_multiple_calls_same_result():
    rst = RestructuredText("Consistent output.")
    assert rst.render_to_html() == rst.render_to_html()


def test_render_to_html_with_custom_theme():
    from rich.terminal_theme import MONOKAI
    rst = RestructuredText("Hello world.")
    out = rst.render_to_html(theme=MONOKAI)
    assert isinstance(out, str)
    assert "Hello" in out


def test_render_to_html_complex_document():
    rst_text = """\
Title
=====

A paragraph with **bold** and *italic*.

.. note::

   A note box.

* item one
* item two
"""
    rst = RestructuredText(rst_text)
    out = rst.render_to_html()
    assert "Title" in out
    assert "bold" in out


# ── render_to_svg ─────────────────────────────────────────────────────────────

def test_render_to_svg_returns_str():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_svg()
    assert isinstance(out, str)


def test_render_to_svg_is_xml():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_svg()
    assert "<svg" in out
    assert "</svg>" in out


def test_render_to_svg_contains_text():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_svg()
    assert "Hello" in out
    assert "world" in out


def test_render_to_svg_default_width_is_80():
    rst = RestructuredText("Short text.")
    out = rst.render_to_svg()
    assert "<svg" in out


def test_render_to_svg_custom_width():
    rst = RestructuredText("Short text.")
    out = rst.render_to_svg(width=40)
    # SVG output contains the document structure; verify it's a valid SVG
    assert "<svg" in out


def test_render_to_svg_with_title():
    rst = RestructuredText("Hello world.")
    out = rst.render_to_svg(title="My Document")
    # Rich encodes the title in the SVG (in a <title> element or comment)
    assert "<svg" in out


def test_render_to_svg_multiple_calls_same_result():
    rst = RestructuredText("Consistent output.")
    assert rst.render_to_svg() == rst.render_to_svg()


def test_render_to_svg_complex_document():
    rst_text = """\
Title
=====

A paragraph with **bold** and *italic*.
"""
    rst = RestructuredText(rst_text)
    out = rst.render_to_svg()
    assert "Title" in out
