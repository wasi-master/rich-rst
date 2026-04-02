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
