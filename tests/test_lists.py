"""Tests for list elements.

Covers: bullet lists, enumerated lists, nested bullet lists, nested
enumerated lists, mixed (bullet-in-enumerated / enumerated-in-bullet)
lists, and lists containing code blocks.
"""
from rich.console import NewLine
from rich.text import Text


# ── Bullet lists ─────────────────────────────────────────────────────────────

def test_bullet_list_single_item_visible(render_text):
    assert "single item" in render_text("* single item\n")


def test_bullet_list_multiple_items_all_visible(render_text):
    out = render_text("* alpha\n* beta\n* gamma\n")
    assert "alpha" in out
    assert "beta" in out
    assert "gamma" in out


def test_bullet_list_marker_is_bullet_character(make_visitor):
    visitor = make_visitor("* item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "•" in combined


def test_bullet_list_followed_by_newline(make_visitor):
    visitor = make_visitor("* item\n")
    newlines = [r for r in visitor.renderables if isinstance(r, NewLine)]
    assert newlines, "Bullet list must be followed by a NewLine renderable"


def test_bullet_list_dash_syntax(render_text):
    # Docutils also accepts '-' as a bullet marker
    out = render_text("- first\n- second\n")
    assert "first" in out
    assert "second" in out


def test_bullet_list_plus_syntax(render_text):
    out = render_text("+ one\n+ two\n")
    assert "one" in out
    assert "two" in out


# ── Enumerated lists ──────────────────────────────────────────────────────────

def test_enumerated_list_single_item_visible(render_text):
    assert "first" in render_text("#. first\n")


def test_enumerated_list_multiple_items_all_visible(render_text):
    out = render_text("#. one\n#. two\n#. three\n")
    assert "one" in out
    assert "two" in out
    assert "three" in out


def test_enumerated_list_numeric_marker_present(make_visitor):
    visitor = make_visitor("#. item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "1" in combined


def test_enumerated_list_explicit_numbers(render_text):
    out = render_text("1. alpha\n2. beta\n3. gamma\n")
    assert "alpha" in out
    assert "beta" in out
    assert "gamma" in out


def test_enumerated_list_followed_by_newline(make_visitor):
    visitor = make_visitor("#. item\n")
    newlines = [r for r in visitor.renderables if isinstance(r, NewLine)]
    assert newlines, "Enumerated list must be followed by a NewLine renderable"


def test_enumerated_list_alpha(render_text):
    out = render_text("a. alpha\nb. beta\n")
    assert "alpha" in out
    assert "beta" in out


# ── Nested bullet lists ───────────────────────────────────────────────────────

def test_nested_bullet_two_levels_both_visible(render_text):
    rst = "* outer\n\n  * inner\n"
    out = render_text(rst)
    assert "outer" in out
    assert "inner" in out


def test_nested_bullet_three_levels_all_visible(render_text):
    rst = "* a\n\n  * b\n\n    * c\n"
    out = render_text(rst)
    assert "a" in out
    assert "b" in out
    assert "c" in out


def test_nested_bullet_inner_marker_different(make_visitor):
    rst = "* outer\n\n  * inner\n"
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    # At least one bullet marker must be present
    assert "•" in combined or "∘" in combined or "▪" in combined


def test_nested_bullet_indentation_in_output(render_text):
    rst = "* outer\n\n  * inner\n"
    out = render_text(rst)
    # inner item must be indented relative to outer
    outer_col = out.index("outer")
    inner_col = out.index("inner")
    assert inner_col > outer_col


# ── Nested enumerated lists ───────────────────────────────────────────────────

def test_nested_enumerated_both_levels_visible(render_text):
    rst = "#. outer\n\n   #. inner\n"
    out = render_text(rst)
    assert "outer" in out
    assert "inner" in out


def test_nested_enumerated_three_levels(render_text):
    rst = "#. a\n\n   #. b\n\n      #. c\n"
    out = render_text(rst)
    assert "a" in out
    assert "b" in out
    assert "c" in out


# ── Mixed nesting ─────────────────────────────────────────────────────────────

def test_bullet_list_inside_enumerated(render_text):
    rst = "#. numbered\n\n   * bullet sub-item\n"
    out = render_text(rst)
    assert "numbered" in out
    assert "bullet sub-item" in out


def test_enumerated_list_inside_bullet(render_text):
    rst = "* bullet\n\n  #. numbered sub-item\n"
    out = render_text(rst)
    assert "bullet" in out
    assert "numbered sub-item" in out


# ── Lists containing code blocks ──────────────────────────────────────────────

def test_bullet_list_item_with_code_block(render_text):
    rst = "* item with code::\n\n    print('hello')\n"
    assert "print" in render_text(rst)


def test_enumerated_list_item_with_code_block(render_text):
    rst = "#. step one::\n\n    x = 1\n"
    assert "x = 1" in render_text(rst)
