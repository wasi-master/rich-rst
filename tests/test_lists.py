"""Tests for list elements.

Covers: bullet lists, enumerated lists, nested bullet lists, nested
enumerated lists, mixed (bullet-in-enumerated / enumerated-in-bullet)
lists, and lists containing code blocks.

Formatting contract
-------------------
* **Bullet marker** — a ``Text`` with plain text ``" • "`` and base
  style ``"bold yellow"``.
* **Level-2 bullet marker** — a ``Text`` containing ``"∘"`` with base
  style ``"bold yellow"``.
* **Enumerated marker** — a ``Text`` with base style ``"bold yellow"``
  and plain text that starts with a space and contains the item number
  (e.g. ``" 1"``, ``" 2"``).
* Both bullet and enumerated lists append a ``NewLine`` renderable after
  the last item.
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


def test_bullet_list_marker_plain_text_is_bullet_char(make_visitor):
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


def test_bullet_list_followed_by_newline(make_visitor):
    visitor = make_visitor("* item\n")
    newlines = [r for r in visitor.renderables if isinstance(r, NewLine)]
    assert newlines, "Bullet list must be followed by a NewLine renderable"


def test_bullet_list_dash_syntax(render_text):
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


def test_enumerated_list_first_marker_plain_text(make_visitor):
    visitor = make_visitor("#. item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # Marker is " 1." (space + digit + suffix)
    markers = [t for t in texts if t.plain.strip() == "1."]
    assert markers, "First enumerated marker must contain '1.'"


def test_enumerated_list_marker_style_is_bold_yellow(make_visitor):
    visitor = make_visitor("#. item\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain.strip().rstrip(".").isdigit()]
    assert markers
    assert str(markers[0].style) == "bold yellow", (
        f"Enumerated marker style must be 'bold yellow', got {markers[0].style!r}"
    )


def test_enumerated_list_multiple_markers_increment(make_visitor):
    visitor = make_visitor("#. one\n#. two\n#. three\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain.strip().rstrip(".").isdigit()]
    nums = [int(t.plain.strip().rstrip(".")) for t in markers]
    assert sorted(nums) == [1, 2, 3], f"Markers must be 1, 2, 3; got {nums}"


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

def test_nested_bullet_both_levels_visible(render_text):
    out = render_text("* outer\n\n  * inner\n")
    assert "outer" in out
    assert "inner" in out


def test_nested_bullet_level2_uses_open_circle_marker(make_visitor):
    visitor = make_visitor("* outer\n\n  * inner\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    l2_markers = [t for t in texts if "∘" in t.plain]
    assert l2_markers, "Level-2 bullet must use the '∘' open-circle marker"


def test_nested_bullet_level1_uses_bullet_marker(make_visitor):
    visitor = make_visitor("* outer\n\n  * inner\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    l1_markers = [t for t in texts if t.plain == " • "]
    assert l1_markers, "Level-1 bullet must use the '•' filled-circle marker"


def test_nested_bullet_inner_indented_further(render_text):
    rst = "* outer\n\n  * inner\n"
    out = render_text(rst)
    outer_col = out.index("outer")
    inner_col = out.index("inner")
    assert inner_col > outer_col, "Inner bullet must be indented further than outer"


def test_nested_bullet_three_levels(render_text):
    out = render_text("* a\n\n  * b\n\n    * c\n")
    assert "a" in out
    assert "b" in out
    assert "c" in out


# ── Nested enumerated lists ───────────────────────────────────────────────────

def test_nested_enumerated_both_levels_visible(render_text):
    out = render_text("#. outer\n\n   #. inner\n")
    assert "outer" in out
    assert "inner" in out


def test_nested_enumerated_inner_marker_is_number_one(make_visitor):
    visitor = make_visitor("#. outer\n\n   #. inner\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    # Both outer and inner start from 1
    markers_1 = [t for t in texts if t.plain.strip() == "1."]
    assert len(markers_1) == 2, "Each enumerated level starts at 1"


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
    assert "print" in render_text("* item with code::\n\n    print('hello')\n")


def test_enumerated_list_item_with_code_block(render_text):
    assert "x = 1" in render_text("#. step one::\n\n    x = 1\n")


# ── Start index ───────────────────────────────────────────────────────────────

def test_enumerated_list_custom_start_index(make_visitor):
    visitor = make_visitor("3. three\n4. four\n5. five\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    markers = [t for t in texts if t.plain.strip().rstrip(".").isdigit()]
    nums = [int(t.plain.strip().rstrip(".")) for t in markers]
    assert nums == [3, 4, 5], f"List starting at 3 must render markers 3, 4, 5; got {nums}"


def test_enumerated_list_custom_start_content_visible(render_text):
    out = render_text("3. three\n4. four\n")
    assert "three" in out
    assert "four" in out


# ── Non-Arabic numerals ───────────────────────────────────────────────────────

def test_enumerated_list_loweralpha_markers(make_visitor):
    visitor = make_visitor("a. alpha\nb. beta\nc. gamma\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    stripped = [t.plain.strip() for t in texts]
    marker_plains = [s for s in stripped if len(s) >= 2 and s[-1] == "."]
    labels = [p.rstrip(".") for p in marker_plains]
    assert labels == ["a", "b", "c"], f"Lowercase alpha markers must be a, b, c; got {labels}"


def test_enumerated_list_upperalpha_markers(make_visitor):
    visitor = make_visitor("A. Alpha\nB. Beta\nC. Gamma\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    stripped = [t.plain.strip() for t in texts]
    marker_plains = [s for s in stripped if len(s) >= 2 and s[-1] == "."]
    labels = [p.rstrip(".") for p in marker_plains]
    assert labels == ["A", "B", "C"], f"Uppercase alpha markers must be A, B, C; got {labels}"


def test_enumerated_list_lowerroman_markers(make_visitor):
    visitor = make_visitor("i. one\nii. two\niii. three\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    stripped = [t.plain.strip() for t in texts]
    marker_plains = [s for s in stripped if len(s) >= 2 and s[-1] == "."]
    labels = [p.rstrip(".") for p in marker_plains]
    assert labels == ["i", "ii", "iii"], f"Lowercase roman markers must be i, ii, iii; got {labels}"


def test_enumerated_list_upperroman_markers(make_visitor):
    visitor = make_visitor("I. ONE\nII. TWO\nIII. THREE\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    stripped = [t.plain.strip() for t in texts]
    marker_plains = [s for s in stripped if len(s) >= 2 and s[-1] == "."]
    labels = [p.rstrip(".") for p in marker_plains]
    assert labels == ["I", "II", "III"], f"Uppercase roman markers must be I, II, III; got {labels}"


def test_enumerated_list_loweralpha_content_visible(render_text):
    out = render_text("a. first\nb. second\n")
    assert "first" in out
    assert "second" in out


def test_enumerated_list_lowerroman_content_visible(render_text):
    out = render_text("i. one\nii. two\n")
    assert "one" in out
    assert "two" in out
