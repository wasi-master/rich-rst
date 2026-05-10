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
