"""Tests for table rendering.

Covers: simple grid tables, tables with headers, tables with captions,
column counts, and multi-row bodies.
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


def test_table_header_columns_visible(render_text):
    rst = (
        "+------+------+\n"
        "| Col1 | Col2 |\n"
        "+======+======+\n"
        "| a    | b    |\n"
        "+------+------+\n"
    )
    out = render_text(rst)
    assert "Col1" in out
    assert "Col2" in out


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
    assert tables
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
    assert tables
    assert tables[0].row_count == 2, "Two body rows expected"


def test_table_header_and_body_both_visible(render_text):
    rst = (
        "+------+-------+\n"
        "| Name | Score |\n"
        "+======+=======+\n"
        "| Eve  | 100   |\n"
        "+------+-------+\n"
    )
    out = render_text(rst)
    assert "Name" in out
    assert "Score" in out
    assert "Eve" in out
    assert "100" in out


# ── Table with caption ────────────────────────────────────────────────────────

def test_table_caption_visible(render_text):
    rst = (
        ".. table:: My Caption\n\n"
        "   +---+---+\n"
        "   | A | B |\n"
        "   +===+===+\n"
        "   | 1 | 2 |\n"
        "   +---+---+\n"
    )
    assert "My Caption" in render_text(rst)


def test_table_caption_and_cell_both_visible(render_text):
    rst = (
        ".. table:: Results\n\n"
        "   +-----+-----+\n"
        "   | Win | Loss|\n"
        "   +=====+=====+\n"
        "   | 10  | 2   |\n"
        "   +-----+-----+\n"
    )
    out = render_text(rst)
    assert "Results" in out
    assert "Win" in out


# ── Table without explicit header (no ==== separator) ─────────────────────────

def test_table_without_header_row(make_visitor):
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
