"""Tests for csv-table and list-table directives (item 9a).

Both directives are provided by docutils and produce standard ``table`` nodes
that are handled by the existing ``visit_table`` visitor method.

Formatting contract
-------------------
* A ``.. csv-table::`` directive renders as a :class:`rich.table.Table`.
* A ``.. list-table::`` directive renders as a :class:`rich.table.Table`.
* Column headers specified via ``:header:`` / ``header-rows: 1`` appear as
  column header names in the Rich Table.
* The rendered plain-text output contains the cell values.
* A caption set with the ``title`` argument appears as the Table title.
"""
from rich.table import Table


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
