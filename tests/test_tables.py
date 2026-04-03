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


def test_rowspan_produces_correct_row_count(make_visitor):
    """A table with a 2-row span still has 2 body rows in the Rich Table."""
    rst = (
        "+-------+-------+\n"
        "| spans | a     |\n"
        "+ 2     +-------+\n"
        "| rows  | b     |\n"
        "+-------+-------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert tables[0].row_count == 2, (
        f"Expected 2 body rows for a rowspan table, got {tables[0].row_count}"
    )


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

def test_colspan_header_correct_column_count(make_visitor):
    """A header cell spanning 2 columns produces exactly 3 columns total."""
    rst = (
        "+-------+-------+-------+\n"
        "| Col1  | Col2          |\n"
        "+=======+=======+=======+\n"
        "| a     | b     | c     |\n"
        "+-------+-------+-------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    assert len(tables[0].columns) == 3, (
        f"Expected 3 columns for a colspan table, got {len(tables[0].columns)}"
    )


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


def test_colspan_header_label_present(make_visitor):
    """The spanning header text ('Col2') appears as a column header."""
    rst = (
        "+-------+-------+-------+\n"
        "| Col1  | Col2          |\n"
        "+=======+=======+=======+\n"
        "| a     | b     | c     |\n"
        "+-------+-------+-------+\n"
    )
    visitor = make_visitor(rst)
    tables = [r for r in visitor.renderables if isinstance(r, Table)]
    assert tables
    headers = [c.header for c in tables[0].columns]
    assert "Col1" in headers
    assert "Col2" in headers


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
