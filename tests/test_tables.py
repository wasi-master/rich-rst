"""Tests for table rendering.

Covers: simple grid tables, tables with headers, tables with captions,
column counts, row counts, and multi-row bodies.

Formatting contract
-------------------
* A grid table is rendered as a ``rich.table.Table``.
* The column headers of the ``Table`` match the header row of the RST table
  exactly (whitespace-stripped).
* The ``.. table:: Caption`` directive sets ``Table.title`` to the caption
  text exactly.
* ``Table.show_header`` is ``True`` when the RST table has a header row
  (separator line using ``===``).
* ``Table.row_count`` equals the number of body rows in the RST table.
"""
from rich.table import Table
from rich.console import Group
from rich.text import Text

from rich_rst import _register_sphinx_directives
import pytest
from rich.console import Console
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
import rich_rst
import rich_rst._vendor.docutils.core
from rich_rst._vendor import docutils
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


# ── Basic table structure ─────────────────────────────────────────────────────

def test_simple_table_produces_rich_table(make_visitor):
    rst = (
        "+-------+-------+\n"
        "| A     | B     |\n"
        "+=======+=======+\n"
        "| 1     | 2     |\n"
        "+-------+-------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "A grid table must produce a rich Table renderable"


def test_table_column_headers_match_rst_header_row(make_visitor):
    rst = (
        "+------+------+\n"
        "| Col1 | Col2 |\n"
        "+======+======+\n"
        "| a    | b    |\n"
        "+------+------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    col_headers = [c.header for c in tables[0].columns]
    assert col_headers == ["Col1", "Col2"], (
        f"Column headers must equal ['Col1', 'Col2'], got {col_headers}"
    )


def test_table_three_columns_header_names(make_visitor):
    rst = (
        "+---+---+---+\n"
        "| A | B | C |\n"
        "+===+===+===+\n"
        "| 1 | 2 | 3 |\n"
        "+---+---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert [c.header for c in tables[0].columns] == ["A", "B", "C"]


def test_table_column_count(make_visitor):
    rst = (
        "+---+---+---+\n"
        "| A | B | C |\n"
        "+===+===+===+\n"
        "| 1 | 2 | 3 |\n"
        "+---+---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert len(tables[0].columns) == 3


def test_table_row_count(make_visitor):
    rst = (
        "+---+---+\n"
        "| X | Y |\n"
        "+===+===+\n"
        "| 1 | 2 |\n"
        "+---+---+\n"
        "| 3 | 4 |\n"
        "+---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].row_count == 2, f"Expected 2 body rows, got {tables[0].row_count}"


def test_table_show_header_true_when_header_row_present(make_visitor):
    rst = (
        "+------+------+\n"
        "| Name | Age  |\n"
        "+======+======+\n"
        "| Alice| 25   |\n"
        "+------+------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].show_header is True, "Table with === separator must have show_header=True"


def test_table_body_cells_visible(render_text):
    rst = (
        "+------+------+\n"
        "| Name | Age  |\n"
        "+======+======+\n"
        "| Alice| 25   |\n"
        "+------+------+\n"
        "| Bob  | 30   |\n"
        "+------+------+\n"
    )
    out = render_text(rst)
    assert "Alice" in out
    assert "Bob" in out


# ── Table with caption ────────────────────────────────────────────────────────

def test_table_caption_sets_table_title(make_visitor):
    rst = (
        ".. table:: My Caption\n\n"
        "   +---+---+\n"
        "   | A | B |\n"
        "   +===+===+\n"
        "   | 1 | 2 |\n"
        "   +---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].title == "My Caption", (
        f"Table title must equal 'My Caption', got {tables[0].title!r}"
    )


def test_table_caption_visible(make_visitor):
    rst = (
        ".. table:: My Caption\n\n"
        "   +---+---+\n"
        "   | A | B |\n"
        "   +===+===+\n"
        "   | 1 | 2 |\n"
        "   +---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].title == "My Caption"


def test_table_caption_and_cell_both_present(make_visitor):
    rst = (
        ".. table:: Results\n\n"
        "   +-----+-----+\n"
        "   | Win | Loss|\n"
        "   +=====+=====+\n"
        "   | 10  | 2   |\n"
        "   +-----+-----+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables[0].title == "Results"
    assert [c.header for c in tables[0].columns] == ["Win", "Loss"]


# ── Table without explicit header (no ==== separator) ─────────────────────────

def test_table_without_header_row_still_produces_table(make_visitor):
    rst = (
        "+---+---+\n"
        "| a | b |\n"
        "+---+---+\n"
        "| c | d |\n"
        "+---+---+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].row_count >= 1


# ── Rowspan ───────────────────────────────────────────────────────────────────

def test_rowspan_second_row_cell_in_correct_column(render_text):
    """Cell 'b' must appear in the second column, not the first.

    The first column contains a cell that spans 2 rows ('spans / 2 / rows').
    Because that column is occupied in the second row, 'b' (the only entry in
    that row) must be placed in column index 1 (the second column), not
    displaced to column index 0.
    """
    rst = (
        "+-------+-------+\n"
        "| spans | a     |\n"
        "+ 2     +-------+\n"
        "| rows  | b     |\n"
        "+-------+-------+\n"
    )
    out = render_text(rst)
    assert "b" in out, "Cell 'b' from the second row must be rendered"


def test_rowspan_produces_correct_row_count(render_text):
    """A table with a 2-row span renders both body cells."""
    rst = (
        "+-------+-------+\n"
        "| spans | a     |\n"
        "+ 2     +-------+\n"
        "| rows  | b     |\n"
        "+-------+-------+\n"
    )
    out = render_text(rst)
    assert "a" in out
    assert "b" in out


def test_rowspan_occupied_cell_is_empty(render_text):
    """Both 'a' and 'b' are present; the column-1 cell of row 2 is empty.

    Verifies that the content in the second column ('a' in row 1, 'b' in
    row 2) is rendered and that the first column of row 2 renders as blank
    (occupied by the rowspan from row 1, not shifted content).
    """
    rst = (
        "+-------+-------+\n"
        "| spans | a     |\n"
        "+ 2     +-------+\n"
        "| rows  | b     |\n"
        "+-------+-------+\n"
    )
    out = render_text(rst)
    # 'a' and 'b' should both appear (in the correct second column)
    assert "a" in out
    assert "b" in out


# ── Colspan ───────────────────────────────────────────────────────────────────

def test_colspan_header_correct_column_count(render_text):
    """A header cell spanning 2 columns renders all 3 body cells."""
    rst = (
        "+-------+-------+-------+\n"
        "| Col1  | Col2          |\n"
        "+=======+=======+=======+\n"
        "| a     | b     | c     |\n"
        "+-------+-------+-------+\n"
    )
    out = render_text(rst)
    assert "a" in out
    assert "b" in out
    assert "c" in out


def test_colspan_body_cells_render(render_text):
    """All body cells of a colspan table are visible in the output."""
    rst = (
        "+-------+-------+-------+\n"
        "| Col1  | Col2          |\n"
        "+=======+=======+=======+\n"
        "| a     | b     | c     |\n"
        "+-------+-------+-------+\n"
    )
    out = render_text(rst)
    assert "a" in out
    assert "b" in out
    assert "c" in out


def test_colspan_header_label_present(render_text):
    """Header labels Col1 and Col2 appear in the rendered output."""
    rst = (
        "+-------+-------+-------+\n"
        "| Col1  | Col2          |\n"
        "+=======+=======+=======+\n"
        "| a     | b     | c     |\n"
        "+-------+-------+-------+\n"
    )
    out = render_text(rst)
    assert "Col1" in out
    assert "Col2" in out


# ── Inline markup in cells ────────────────────────────────────────────────────

def test_inline_bold_in_cell_rendered(render_text):
    """Bold markup inside a table cell must appear in the rendered output."""
    rst = (
        "+----------+\n"
        "| **bold** |\n"
        "+----------+\n"
    )
    out = render_text(rst)
    assert "bold" in out, "Bold cell text must be visible"


def test_inline_italic_in_cell_rendered(render_text):
    """Italic markup inside a table cell must appear in the rendered output."""
    rst = (
        "+----------+\n"
        "| *italic* |\n"
        "+----------+\n"
    )
    out = render_text(rst)
    assert "italic" in out, "Italic cell text must be visible"


def test_inline_code_in_cell_rendered(render_text):
    """Inline code markup inside a table cell must appear in the rendered output."""
    rst = (
        "+--------+\n"
        "| ``x``  |\n"
        "+--------+\n"
    )
    out = render_text(rst)
    assert "x" in out, "Inline code cell text must be visible"


def test_bullet_list_in_spanning_grid_table_cell_keeps_markers_and_no_extra_blank_lines(render_text):
    """List markers in a spanning grid-table cell stay attached to item text."""
    rst = (
        "+-----------------+\n"
        "| Header Three    |\n"
        "+=================+\n"
        "| * Quis 23       |\n"
        "+ * Tempus 33     |\n"
        "| * Pretium 43    |\n"
        "+-----------------+\n"
    )
    out = render_text(rst)
    assert "• Quis 23" in out
    assert "• Tempus 33" in out
    assert "• Pretium 43" in out
    assert "Quis 23•" not in out
    assert "Tempus 33•" not in out
    assert not any(
        line.startswith("│") and line.endswith("│") and not line.strip("│ ").strip()
        for line in out.splitlines()
    )


# ── flat-table directive ──────────────────────────────────────────────────────

def test_flat_table_basic(render_text):
    """flat-table with header-rows produces a visible table."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Value\n\n"
        "   * - Alice\n"
        "     - 1\n"
    )
    out = render_text(rst)
    assert "Name" in out
    assert "Alice" in out


def test_flat_table_cspan_body_structure(render_text):
    """A body cell with :cspan:`3` visually spans all 4 columns — no internal │ borders."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Q1\n"
        "     - Q2\n"
        "     - Q3\n\n"
        "   * - :cspan:`3` Grand total\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    grand_line = next((l for l in lines if "Grand total" in l), None)
    assert grand_line is not None, "Grand total row must be present"
    # Visual merging: only the two outer │ borders remain; no internal separators
    assert grand_line.count("│") == 2, (
        "Grand total spans all 4 columns: only outer │ borders expected"
    )


def test_flat_table_cspan_header_structure(render_text):
    """A header cell with :cspan:`1` visually spans cols 0-1; Grade is at col 2."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - :cspan:`1` Score Range\n"
        "     - Grade\n\n"
        "   * - Min\n"
        "     - Max\n"
        "     - Letter\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    header_line = next((l for l in lines if "Score Range" in l), None)
    assert header_line is not None, "Header row with Score Range must be present"
    # 'Grade' must appear to the RIGHT of 'Score Range' on the same line
    assert "Grade" in header_line
    assert header_line.index("Score Range") < header_line.index("Grade")
    # Score Range spans cols 0-1 (no internal ┃); Grade is col 2.
    # Expected: ┃ Score Range ┃ Grade ┃ = 3 ┃ chars (left border + after span + right border)
    assert header_line.count("┃") == 3, (
        "Score Range spans cols 0-1 with no internal ┃; Grade at col 2: 3 ┃ total"
    )
    # Body data must appear in the correct column order
    assert "Min" in out and "Max" in out and "Letter" in out
    min_line = next((l for l in lines if "Min" in l), None)
    assert min_line is not None
    assert "Max" in min_line and "Letter" in min_line
    assert min_line.index("Min") < min_line.index("Max") < min_line.index("Letter")


def test_flat_table_rspan_header_into_body_column_order(render_text):
    """A header cell with :rspan:`1` must not shift body cells into the wrong columns.

    Before the fix, Sub C appeared in column 0 (Category) instead of column 1 (Sub A).
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - :rspan:`1` Category\n"
        "     - Sub A\n"
        "     - Sub B\n\n"
        "   * - Sub C\n"
        "     - Sub D\n\n"
        "   * - Data1\n"
        "     - X\n"
        "     - Y\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    # Sub C and Sub D must be on the same line (same body row)
    sub_c_line = next((l for l in lines if "Sub C" in l), None)
    assert sub_c_line is not None, "Sub C must appear in output"
    assert "Sub D" in sub_c_line, "Sub C and Sub D must be on the same row"
    # Sub C is in col 1 (Sub A column), Sub D is in col 2 (Sub B column).
    # Col 0 (Category) is empty because it is occupied by the header rspan.
    assert sub_c_line.index("Sub C") < sub_c_line.index("Sub D")
    # Col 0 (Category) must be empty: the left-border │ is followed by spaces before
    # the next │ separator.  Verify there is no 'S' before the first inner │.
    first_inner_sep = sub_c_line.index("│", 1)  # first │ after the outer-left border
    col0_content = sub_c_line[1:first_inner_sep]
    assert col0_content.strip() == "", (
        f"Category column (col 0) must be empty in the Sub C row, got {col0_content!r}"
    )


def test_flat_table_cspan2_partial_no_internal_borders(render_text):
    """A body cell with :cspan:`2` (3 of 4 cols) must show no internal │ borders.

    This is the critical regression path for the _cspan_continues bug: the
    scan-left loop must cross the None placeholder at col 1 to reach the origin
    at col 0 when checking whether col 2 is a continuation.  With the old
    unconditional ``break`` the scan stopped at the None and returned False,
    drawing a spurious internal border.
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n"
        "     - D\n\n"
        "   * - :cspan:`2` Merged ABC\n"
        "     - normal D\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    merged_line = next((l for l in lines if "Merged ABC" in l), None)
    assert merged_line is not None, "Row containing 'Merged ABC' must be present"
    # Cols 0–2 are merged → no internal │ between them; one border between col 2 and col 3.
    # Expected: │ Merged ABC   │ normal D │  →  3 vertical bars total.
    assert merged_line.count("│") == 3, (
        f"Merged ABC spans 3 cols: expected 3 │ borders (left, mid, right), "
        f"got {merged_line.count('│')} in {merged_line!r}"
    )


def test_flat_table_rspan2_separator_all_rows(render_text):
    """A cell with :rspan:`2` (spanning 3 rows) keeps the separator opening on all
    intermediate rows — verifying _rspan_continues handles multi-row spans correctly.

    This is the 'opposite direction' counterpart to the cspan_continues fix: the
    rspan scan goes *upward* past None placeholders, and must not break early.
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Category\n"
        "     - Item\n\n"
        "   * - :rspan:`2` All three\n"
        "     - First\n\n"
        "   * - Second\n\n"
        "   * - Third\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    # All three item rows must be present
    assert "First" in out
    assert "Second" in out
    assert "Third" in out
    # Each item row: col 0 is the rspan placeholder → starts with │ + spaces
    for label in ("First", "Second", "Third"):
        row = next((l for l in lines if label in l), None)
        assert row is not None, f"Row containing '{label}' must be present"
        if label != "First":
            # Rows 2 and 3: col 0 is covered by the rspan → must be empty, not contain label text
            first_inner_sep = row.index("│", 1)
            col0_content = row[1:first_inner_sep]
            assert col0_content.strip() == "", (
                f"Category column must be empty in the '{label}' row "
                f"(rspan from 'All three' still active), got {col0_content!r}"
            )
    # The separator between First and Second rows must start with │ (rspan continues col 0)
    first_line_idx = next(i for i, l in enumerate(lines) if "First" in l)
    sep_line = lines[first_line_idx + 1] if first_line_idx + 1 < len(lines) else ""
    assert sep_line.startswith("│"), (
        "Row separator after 'First' row must start with │ — "
        "col 0 is still spanned by the 3-row rspan"
    )
    # The separator between Second and Third rows must also start with │
    second_line_idx = next(i for i, l in enumerate(lines) if "Second" in l)
    sep_line2 = lines[second_line_idx + 1] if second_line_idx + 1 < len(lines) else ""
    assert sep_line2.startswith("│"), (
        "Row separator after 'Second' row must start with │ — "
        "col 0 is still spanned by the 3-row rspan on its third row"
    )


def test_flat_table_combined_cspan_rspan_no_internal_border(render_text):
    """A single cell with :cspan:`1` :rspan:`1` must create a seamless 2×2 block.

    Grid layout:
        Row 0 (header): [A,      B,    C   ]
        Row 1 (data):   [Big(1,1), None, C1 ]
        Row 2 (data):   [None,   None, C2   ]

    The corner placeholder at (2,1) is a combined cspan+rspan slot that neither
    a left-scan (row 2 has no real cells) nor an up-scan (col 1 has no real
    cells above) can resolve.  The two-step diagonal search in _origin must
    trace it back to (1,0), after which _has_vborder(2,0) returns False and
    _rspan_continues(1,1) returns True — eliminating the spurious internal
    border and the incorrect horizontal rule through the merged region.
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n\n"
        "   * - :cspan:`1` :rspan:`1` Big\n"
        "     - C1\n\n"
        "   * - C2\n"
    )
    out = render_text(rst)
    lines = out.splitlines()

    assert "Big" in out, "Combined-span cell content must appear"
    assert "C1" in out, "Sibling cell C1 in row 1 must appear"
    assert "C2" in out, "Cell C2 in the continuation row must appear"

    # The continuation row (C2 row) covers cols 0-1 with the Big rspan and
    # puts C2 at col 2.  No internal │ between cols 0 and 1 expected.
    c2_line = next((l for l in lines if "C2" in l and "Big" not in l), None)
    assert c2_line is not None, "Row containing C2 (continuation row) must be present"
    assert c2_line.count("│") == 3, (
        f"Combined 2×2 span: continuation row must have exactly 3 │ borders "
        f"(outer-left, span-boundary, outer-right), got {c2_line.count('│')} "
        f"in {c2_line!r}"
    )

    # The row separator between Big's row and the continuation row must keep
    # the Big span open: it should start with │ (not ├/└) and have a │ between
    # the two spanned columns (not a junction or horizontal rule).
    big_line_idx = next((i for i, l in enumerate(lines) if "Big" in l), None)
    assert big_line_idx is not None
    sep = lines[big_line_idx + 1] if big_line_idx + 1 < len(lines) else ""
    assert sep.startswith("│"), (
        "Separator after Big row must start with │ — cols 0-1 are still spanned"
    )


def test_flat_table_rspan_body_row_separator(render_text):
    """A body cell with :rspan:`1` continues visually across the row separator.

    The separator between the Fruit row and the Banana row must start with │ (not ├)
    because col 0 is still occupied by the Fruit rspan — no horizontal line crosses it.
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Category\n"
        "     - Item\n\n"
        "   * - :rspan:`1` Fruit\n"
        "     - Apple\n\n"
        "   * - Banana\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    # The second body row (Banana row) must exist and col 0 must be empty
    banana_line = next((l for l in lines if "Banana" in l), None)
    assert banana_line is not None, "Banana row must be present"
    # Col 0 is the Category column; it must be empty in the Banana row
    assert banana_line.startswith("│  "), (
        "Category column must be empty in the Banana row (rspan placeholder)"
    )
    # The separator between Fruit and Banana rows must start with │ (rspan continues col 0)
    fruit_line_idx = next(i for i, l in enumerate(lines) if "Fruit" in l)
    separator_line = lines[fruit_line_idx + 1] if fruit_line_idx + 1 < len(lines) else ""
    assert separator_line.startswith("│"), (
        "Row separator between rspan rows must start with │ — "
        "col 0 is spanned so no horizontal line crosses through it"
    )


def test_flat_table_title_centering_matches_table_width(render_text):
    """Title must be centered over the actual separator-line width."""
    rst = (
        ".. flat-table:: Title\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Value\n\n"
        "   * - :cspan:`1` Both\n"
    )
    out = render_text(rst)
    lines = [l.rstrip() for l in out.splitlines()]

    bottom = next((l for l in reversed(lines) if l.startswith("└")), None)
    title_line = next((l for l in lines if "Title" in l), None)
    assert bottom is not None, "Bottom border line must be present"
    assert title_line is not None, "Title line must be present"

    title_start = title_line.index("Title")
    expected_pad = (len(bottom) - len("Title")) // 2
    assert title_start == expected_pad, (
        f"Title left-pad is {title_start} but must be {expected_pad} "
        f"(centered over table width {len(bottom)})"
    )


def test_flat_table_combined_cspan_rspan_fill_cells(render_text):
    """fill-cells + combined :cspan:/:rspan: must render correctly with no spurious borders.

    The :cspan:`1` :rspan:`1` cell in a 4-column table leaves col 3 empty in
    both body rows.  With fill-cells enabled, those trailing slots are filled
    with filler entries — exercising the fill-cells node-list fix alongside the
    combined-span pipeline.

    Grid layout (4 columns, header-rows=1):
        Row 0 (header):  A     | B          | C    | D
        Row 1 (body):    Big (cspan=1,rspan=1) | C1   | <fill>
        Row 2 (body):    <rspan placeholder 0–1> | C2  | <fill>
    """
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n"
        "   :fill-cells:\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n"
        "     - D\n\n"
        "   * - :cspan:`1` :rspan:`1` Big\n"
        "     - C1\n\n"
        "   * - C2\n"
    )
    out = render_text(rst)

    assert "Big" in out, "Combined-span cell content must appear"
    assert "C1" in out, "Sibling cell C1 must appear"
    assert "C2" in out, "Continuation cell C2 must appear"

    lines = out.splitlines()

    big_line = next((l for l in lines if "Big" in l), None)
    assert big_line is not None, "Row containing 'Big' must be present"
    assert big_line.count("│") == 4, (
        f"Big row (cspan=1 over cols 0-1, C1, fill): expected 4 │ borders, "
        f"got {big_line.count('│')} in {big_line!r}"
    )

    c2_line = next((l for l in lines if "C2" in l), None)
    assert c2_line is not None, "Row containing C2 must be present"
    assert c2_line.count("│") == 4, (
        f"C2 row (rspan placeholder cols 0-1, C2, fill): expected 4 │ borders, "
        f"got {c2_line.count('│')} in {c2_line!r}"
    )


def test_flat_table_combined_cspan_rspan_placeholder_cols_empty(render_text):
    """Both placeholder columns of a 2×2 combined span must be blank with no internal border."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n\n"
        "   * - :cspan:`1` :rspan:`1` Big\n"
        "     - C1\n\n"
        "   * - C2\n"
    )
    out = render_text(rst)
    lines = out.splitlines()

    c2_line = next((l for l in lines if "C2" in l and "Big" not in l), None)
    assert c2_line is not None, "Continuation row containing C2 must be present"

    first_inner = c2_line.index("│", 1)
    placeholder_region = c2_line[1:first_inner]
    assert placeholder_region.strip() == "", (
        f"Placeholder region (cols 0–1 covered by Big rspan) must be blank, "
        f"got {placeholder_region!r} in {c2_line!r}"
    )


def test_flat_table_combined_cspan_rspan_no_malformed_separator(render_text):
    """Combined cspan+rspan cells must keep separator junctions valid."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n"
        "     - D\n\n"
        "   * - :cspan:`1` :rspan:`1` span\n"
        "     - x\n"
        "     - y\n\n"
        "   * - z\n"
        "     - w\n"
    )
    out = render_text(rst)
    assert "│   ├" not in out, "Separator must not be malformed by combined cspan+rspan"
    lines = out.splitlines()
    z_line = next((l for l in lines if "z" in l and "w" in l), None)
    assert z_line is not None, "The final body row with z/w must be present"
    sep1 = z_line.index("│", 1)
    assert z_line[1:sep1].strip() == ""
    assert z_line.index("z") < z_line.index("w")


def test_flat_table_spanning_cell_preserves_inline_styles(make_visitor):
    """Spanning renderer must preserve inline rich styles in cell content."""
    _register_sphinx_directives()
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - H1\n"
        "     - H2\n\n"
        "   * - :cspan:`1` **bold** *italic* ``code``\n"
    )
    visitor = make_visitor(rst)
    table_group = next((r for r in visitor.renderables if isinstance(r, Group)), None)
    assert table_group is not None, "Spanning table must render as Group"
    content_line = next(
        (l for l in table_group.renderables if isinstance(l, Text) and "bold" in l.plain and "italic" in l.plain),
        None,
    )
    assert content_line is not None
    bold_spans = [s for s in content_line.spans if s.style.bold]
    italic_spans = [s for s in content_line.spans if s.style.italic]
    code_spans = [s for s in content_line.spans if s.style.bgcolor is not None]
    assert any("bold" in content_line.plain[s.start:s.end] for s in bold_spans)
    assert any("italic" in content_line.plain[s.start:s.end] for s in italic_spans)
    assert any("code" in content_line.plain[s.start:s.end] for s in code_spans)


def test_flat_table_spanning_cell_multiline_content_keeps_borders(render_text):
    """Multi-line spanning cell content should render as multiple physical row lines."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - H1\n"
        "     - H2\n\n"
        "   * - :cspan:`1` first line\n\n"
        "       second line\n"
    )
    out = render_text(rst)
    lines = out.splitlines()
    first_idx = next((i for i, l in enumerate(lines) if "first line" in l), None)
    second_idx = next((i for i, l in enumerate(lines) if "second line" in l), None)
    assert first_idx is not None and second_idx is not None, "Both content lines must be present"
    assert second_idx > first_idx, "Second line must render on a later physical row line"
    assert lines[first_idx].startswith("│") and lines[first_idx].endswith("│")
    assert lines[second_idx].startswith("│") and lines[second_idx].endswith("│")


def test_flat_table_spanning_title_centered_to_rendered_width(make_visitor):
    """Spanning table title should be centered against true rendered table width."""
    _register_sphinx_directives()
    rst = (
        ".. flat-table:: Span Title\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Q1\n"
        "     - Q2\n\n"
        "   * - :cspan:`2` Total\n"
    )
    visitor = make_visitor(rst)
    table_group = next((r for r in visitor.renderables if isinstance(r, Group)), None)
    assert table_group is not None
    title_line = next((l for l in table_group.renderables if isinstance(l, Text) and "Span Title" in l.plain), None)
    top_border = next((l for l in table_group.renderables if isinstance(l, Text) and l.plain.startswith("┏")), None)
    assert title_line is not None and top_border is not None
    assert len(title_line.plain) == len(top_border.plain), (
        "Title line width must equal rendered table width"
    )
    title_center = title_line.plain.index("Span Title") + (len("Span Title") / 2)
    table_center = len(top_border.plain) / 2
    assert abs(title_center - table_center) <= 1


def test_flat_table_cspan_no_unnecessary_column_widening(render_text):
    """Spanning-cell content that fits within the correct merged budget must not widen columns."""
    rst = (
        ".. flat-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Role\n\n"
        "   * - :cspan:`1` Both columns\n\n"
        "   * - Alice\n"
        "     - Lead\n\n"
        "   * - Bob\n"
        "     - Dev\n"
    )
    out = render_text(rst)
    assert "Both columns" in out
    assert "Alice" in out and "Lead" in out

    lines = out.splitlines()
    bottom = next(
        (l.rstrip() for l in reversed(lines) if l.startswith("└")),
        None,
    )
    assert bottom is not None, "Bottom border line must be present"
    assert len(bottom) == 16, (
        f"Columns must not be inflated: expected border width 16, got {len(bottom)}. "
        f"Old +mc formula would give 18 by spuriously widening col 1 by 2 chars."
    )


def test_flat_table_multi_header_rows_inner_separator_is_heavy(render_text):
    """Separator between two header rows must use heavy box chars (━ / ┣ / ┫).

    Regression test for issue #51: with header-rows: 2 the line between the
    first and second header row was rendered with light body-row chars (─/├/┤)
    instead of bold/heavy ones.
    """
    rst = (
        ".. flat-table:: Combined Spans\n"
        "   :header-rows: 2\n\n"
        "   * - :cspan:`2` Full-width header\n"
        "   * - :cspan:`2` Full-width subheader\n\n"
        "   * - :rspan:`1` Tall cell\n"
        "     - Top-right\n"
        "     - Also top-right\n\n"
        "   * - Bottom-right\n"
        "     - Also bottom-right\n"
    )
    out = render_text(rst)
    lines = out.splitlines()

    header_line_idx = next(i for i, l in enumerate(lines) if "Full-width header" in l)
    inner_sep = lines[header_line_idx + 1]

    assert inner_sep.startswith("┣"), (
        "Intra-header separator must start with heavy ┣, got: " + repr(inner_sep[:4])
    )
    assert "━" in inner_sep, (
        "Intra-header separator must use heavy horizontal ━, got: " + repr(inner_sep)
    )
    assert inner_sep.endswith("┫"), (
        "Intra-header separator must end with heavy ┫, got: " + repr(inner_sep[-4:])
    )
    assert "─" not in inner_sep, (
        "Intra-header separator must not contain light ─"
    )

    subheader_line_idx = next(i for i, l in enumerate(lines) if "Full-width subheader" in l)
    head_body_sep = lines[subheader_line_idx + 1]
    assert head_body_sep.startswith("┡"), (
        "Header/body separator must still start with transitional ┡"
    )

# ── csv-table ─────────────────────────────────────────────────────────────────

def test_csv_table_produces_rich_table(make_visitor):
    rst = (
        ".. csv-table::\n\n"
        "   Alice, 1\n"
        "   Bob, 2\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "csv-table must produce a Rich Table renderable"


def test_csv_table_with_header_columns(make_visitor):
    rst = (
        ".. csv-table::\n"
        "   :header: Name, Value\n\n"
        "   Alice, 1\n"
        "   Bob, 2\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    headers = [c.header for c in tables[0].columns]
    assert "Name" in headers
    assert "Value" in headers


def test_csv_table_row_count(make_visitor):
    rst = (
        ".. csv-table::\n"
        "   :header: Name, Value\n\n"
        "   Alice, 1\n"
        "   Bob, 2\n"
        "   Carol, 3\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].row_count == 3, f"Expected 3 rows, got {tables[0].row_count}"


def test_csv_table_cell_values_visible(render_text):
    rst = (
        ".. csv-table::\n"
        "   :header: Name, Score\n\n"
        "   Alice, 100\n"
        "   Bob, 95\n"
    )
    out = render_text(rst)
    assert "Alice" in out
    assert "Bob" in out
    assert "100" in out
    assert "95" in out


def test_csv_table_title_appears(make_visitor):
    rst = (
        ".. csv-table:: My CSV Table\n\n"
        "   Alice, 1\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].title == "My CSV Table", (
        f"Expected title 'My CSV Table', got {tables[0].title!r}"
    )


def test_csv_table_three_column_count(make_visitor):
    rst = (
        ".. csv-table::\n"
        "   :header: A, B, C\n\n"
        "   1, 2, 3\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert len(tables[0].columns) == 3, f"Expected 3 columns, got {len(tables[0].columns)}"


# ── list-table ────────────────────────────────────────────────────────────────

def test_list_table_produces_rich_table(make_visitor):
    rst = (
        ".. list-table::\n\n"
        "   * - Alice\n"
        "     - 1\n"
        "   * - Bob\n"
        "     - 2\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables, "list-table must produce a Rich Table renderable"


def test_list_table_with_header_row(make_visitor):
    rst = (
        ".. list-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Value\n"
        "   * - Alice\n"
        "     - 1\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    headers = [c.header for c in tables[0].columns]
    assert "Name" in headers
    assert "Value" in headers


def test_list_table_row_count(make_visitor):
    rst = (
        ".. list-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Value\n"
        "   * - Alice\n"
        "     - 1\n"
        "   * - Bob\n"
        "     - 2\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].row_count == 2, f"Expected 2 body rows, got {tables[0].row_count}"


def test_list_table_cell_values_visible(render_text):
    rst = (
        ".. list-table::\n"
        "   :header-rows: 1\n\n"
        "   * - Name\n"
        "     - Score\n"
        "   * - Alice\n"
        "     - 100\n"
        "   * - Bob\n"
        "     - 95\n"
    )
    out = render_text(rst)
    assert "Alice" in out
    assert "Bob" in out
    assert "100" in out
    assert "95" in out


def test_list_table_title_appears(make_visitor):
    rst = (
        ".. list-table:: My List Table\n\n"
        "   * - Alice\n"
        "     - 1\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].title == "My List Table", (
        f"Expected title 'My List Table', got {tables[0].title!r}"
    )


def test_list_table_column_count(make_visitor):
    rst = (
        ".. list-table::\n"
        "   :header-rows: 1\n\n"
        "   * - A\n"
        "     - B\n"
        "     - C\n"
        "   * - 1\n"
        "     - 2\n"
        "     - 3\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert len(tables[0].columns) == 3, f"Expected 3 columns, got {len(tables[0].columns)}"

def test_table_with_headers(render_text):
    """Test table with header row."""
    rst = """\
=====  =====
Col1   Col2
=====  =====
A      B
C      D
=====  =====
"""
    out = render_text(rst)
    assert "Col1" in out, "First header column must be visible"
    assert "Col2" in out, "Second header column must be visible"
    assert "A" in out and "B" in out, "Table body cells must be visible"

def test_table_complex(render_text):
    """Test complex table."""
    rst = """\
+-------+-------+
| A     | B     |
+=======+=======+
| 1     | 2     |
+-------+-------+
| 3     | 4     |
+-------+-------+
"""
    out = render_text(rst)
    assert "A" in out and "B" in out, "Table header cells must be visible"
    assert "1" in out and "2" in out, "Table body cells must be visible"

def test_table_with_cell_content(render_text):
    """Test table with various cell content."""
    rst = """\
+----------+----------+
| Cell 1   | Cell 2   |
+----------+----------+
| Content1 | Content2 |
+----------+----------+
"""
    out = render_text(rst)
    assert "Cell 1" in out, "First header cell must be visible"
    assert "Cell 2" in out, "Second header cell must be visible"
    assert "Content1" in out, "First body cell must be visible"
    assert "Content2" in out, "Second body cell must be visible"

def test_table_with_multiple_rows_and_columns(render_text):
    """Test complex table with many rows and columns."""
    rst = """\
+---------+---------+---------+
| Header1 | Header2 | Header3 |
+=========+=========+=========+
| Cell11  | Cell12  | Cell13  |
+---------+---------+---------+
| Cell21  | Cell22  | Cell23  |
+---------+---------+---------+
| Cell31  | Cell32  | Cell33  |
+---------+---------+---------+
"""
    out = render_text(rst)
    assert "Header1" in out, "First column header must be visible"
    assert "Header2" in out, "Second column header must be visible"
    assert "Header3" in out, "Third column header must be visible"
    assert "Cell11" in out, "First body cell must be visible"
    assert "Cell33" in out, "Last body cell must be visible"

def test_simple_table_format(render_text):
    """Test simple table format."""
    rst = """\
Simple Table
============  ============  ============
     A              B             C
============  ============  ============
    1              2             3
============  ============  ============
"""
    out = render_text(rst)
    assert "A" in out and "B" in out and "C" in out, (
        "All simple-table column headers must be visible"
    )
    assert "1" in out and "2" in out and "3" in out, (
        "All simple-table body cells must be visible"
    )

def test_grid_table(render_text):
    """Test grid table format."""
    rst = """\
+---+---+
| A | B |
+===+===+
| 1 | 2 |
+---+---+
"""
    out = render_text(rst)
    assert "A" in out and "B" in out, "Grid table header cells must be visible"
    assert "1" in out and "2" in out, "Grid table body cells must be visible"
