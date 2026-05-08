"""
Demonstration of the ``flat-table`` directive in rich-rst.

Run with:
    python flat_table_demo.py
"""
from rich.console import Console
from rich_rst import RestructuredText

console = Console(width=120)


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

GET = """

        \*GET General Items, Entity = ACTIVE
        ************************************

        .. flat-table:: ``Entity`` = ACTIVE, ``ENTNUM`` = 0 (or blank)
           :header-rows: 2

           * - :ref:`get`, Par, ACTIVE, 0, ``Item1``, ``IT1NUM``, ``Item2``, ``IT2NUM``
           * - Item1
             - IT1NUM
             - Description
           * - INT
             -
             - Current interactive key: 0=off, 2=on.
           * - IMME
             -
             - Current immediate key: 0=off, 1=on.
           * - MENU
             -
             - Current menu key: 0=off, 1=on.
           * - PRKEY
             -
             - Printout suppression status: 0= :ref:`nopr`, 1= :ref:`gopr` or :ref:`slashgo`
           * - UNITS
             -
             - Units specified by :ref:`units` command: 0 = USER, 1 = SI, 2 = CGS, 3 = BFT, 4 = BIN, 5 = MKS, 6 = MPA, 7 = uMKS.
           * - ROUT
             -
             - Current routine: 0 = Begin level, 17 = PREP7, 21 = SOLUTION, 31 = POST1, 36 = POST26, 52 = AUX2, 53 = AUX3, 62 = AUX12, 65 = AUX15.
           * - TIME
             - WALL,CPU
             - Current wall clock or CPU time. Current wall clock will continue to accumulate during a run and is not reset to zero at midnight.
           * - DBASE
             - LDATE
             - Date of first modification of any database quantity required for POST1 operation. The parameter returned is ``Par`` = YEAR\*10000 + MONTH\*100 + DAY.
           * - DBASE
             - LTIME
             - Time of last modification of any database quantity required for POST1 operation. The parameter returned is ``Par`` = HOURS\*10000 + MINUTES\*100 + SECONDS.
           * - REV
             -
             - Minor release revision number (5.6, 5.7, 6.0 etc.). Letter notation (for example, 5.0A) is not included.
           * - TITLE
             - 0,1,2,3,4
             - **Item2:** START **IT2NUM:**  ``N`` Current title string of the main title ( ``IT1NUM`` =0 or blank) or subtitle 1, 2, 3, or 4 ( ``IT1NUM`` =1,2,3, or 4). A character parameter of up to 8 characters, starting at position ``N``, is returned.
           * - JOBNAM
             -
             - **Item2:** START **IT2NUM:**  ``N`` Current Jobname. A character parameter of up to 8 characters, starting at position ``N``, is returned. Use :ref:`dim` and ``*DO`` to get all 32 characters.
           * - PLATFORM
             -
             - The current platform.
           * - NPROC
             - CURR, MAX, MAXP
             - The number of processors being used for the current session, or the maximum total number of processors (physical and virtual) available on the machine, or the maximum number of physical processors available on the machine. This only applies to shared-memory parallelism.
           * - NUMCPU
             -
             - Number of distributed processes being used (distributed-memory parallel solution).


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
    ("GET command table", GET),
    ("2. Column span (:cspan:)", CSPAN),
    ("3. Row span (:rspan:)", RSPAN),
    ("4. Combined spans", COMBINED),
    ("5. fill-cells vs auto-span", AUTOFILL),
]:
    console.rule(f"[bold]{title}[/bold]")
    console.print(RestructuredText(rst))
    console.print()
