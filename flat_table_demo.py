"""
Demonstration of the ``flat-table`` directive in rich-rst.

Run with:
    python flat_table_demo.py
"""
from rich.console import Console
from rich_rst import RestructuredText

console = Console(width=90)


# ── 1. Basic table with header row ────────────────────────────────────────────

BASIC = """
.. flat-table:: Linux Kernel Subsystems
   :header-rows: 1
   :stub-columns: 1

   * - Subsystem
     - Maintainer
     - Description

   * - Networking
     - David S. Miller
     - TCP/IP stack and network drivers

   * - Memory Management
     - Andrew Morton
     - Virtual memory, paging, and allocators

   * - File Systems
     - Linus Torvalds
     - VFS layer and filesystem drivers
"""

# ── 2. Column span with :cspan: ───────────────────────────────────────────────
# NOTE: Rich's Table does not support cell merging, so :cspan: is represented
# by leaving the extra columns empty.  The morecols attribute is correctly set
# on the underlying docutils node; only the terminal visual is limited.

CSPAN = """
.. flat-table:: Column Span (:cspan: in body rows)
   :header-rows: 1

   * - Name
     - Q1
     - Q2
     - Q3

   * - :cspan:`3` Grand total — all students, all quarters

   * - Alice
     - 90
     - 85
     - 92

   * - Bob
     - 80
     - 88
     - 76

   * - Carol
     - 95
     - 91
     - 89
"""

# ── 3. Row span with :rspan: ──────────────────────────────────────────────────

RSPAN = """
.. flat-table:: Row Span (:rspan:)
   :header-rows: 1

   * - Category
     - Item
     - Price

   * - :rspan:`1` Fruit
     - Apple
     - $1.00

   * - Banana
     - $0.50

   * - :rspan:`1` Vegetable
     - Carrot
     - $0.75

   * - Broccoli
     - $1.25
"""

# ── 4. Combined cspan + rspan ─────────────────────────────────────────────────

COMBINED = """
.. flat-table:: Combined Spans
   :header-rows: 1
   :fill-cells:

   * - :cspan:`2` Full-width header

   * - :rspan:`1` Tall cell
     - Top-right
     - Also top-right

   * - Bottom-right
     - Also bottom-right
"""

# ── 5. Auto-fill missing cells (:fill-cells:) vs auto-span (default) ──────────

AUTOFILL = """
.. flat-table:: Auto-fill (fill-cells option)
   :header-rows: 1
   :fill-cells:

   * - A
     - B
     - C

   * - only one cell here

.. flat-table:: Auto-span (default — last cell stretches right)
   :header-rows: 1

   * - A
     - B
     - C

   * - only one cell here
"""

for title, rst in [
    ("1. Basic table", BASIC),
    ("2. Column span (:cspan:)", CSPAN),
    ("3. Row span (:rspan:)", RSPAN),
    ("4. Combined spans", COMBINED),
    ("5. fill-cells vs auto-span", AUTOFILL),
]:
    console.rule(f"[bold]{title}[/bold]")
    console.print(RestructuredText(rst))
    console.print()
