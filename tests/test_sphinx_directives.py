"""Tests for Sphinx-specific block directives.

rich-rst registers Sphinx directives (``versionadded``, ``versionchanged``,
``deprecated``, ``seealso``, ``availability``, ``soft-deprecated``, ``impl-detail``) 
so that Python docstrings that use these directives render as styled panels instead 
of system-message errors.

Formatting contract
-------------------
Each directive produces exactly one ``Panel`` whose title and border-style
follow the table below.

+----------------+--------------------------------------+-------------------+
| directive      | title                                | border_style      |
+================+======================================+===================+
| versionadded   | "New in version <ver>"               | bold green        |
| versionchanged | "Changed in version <ver>"           | bold cyan         |
| deprecated     | "Deprecated since version <v>"       | bold yellow       |
| seealso        | "See Also"                           | bold white        |
| availability   | "Available since version <ver>"      | bold blue         |
| soft-deprecated| "Soft Deprecated since version <v>"  | bold bright_yellow|
| impl-detail    | "Implementation Detail"              | bold magenta      |
+----------------+--------------------------------------+-------------------+

When no body content is supplied the panel is still emitted (empty body).
When body content is supplied it appears in the rendered output.
"""
import pytest
from rich.panel import Panel

from rich_rst import _register_sphinx_directives
from rich.align import Align
from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich_rst import _register_sphinx_directives, _register_sphinx_roles


@pytest.fixture(autouse=True)
def ensure_sphinx_directives():
    """Register Sphinx directives once before any test in this module runs."""
    _register_sphinx_directives()


def _first_panel(make_visitor, rst):
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, f"RST must produce at least one Panel:\n{rst}"
    return panels[0]


# ── versionadded ──────────────────────────────────────────────────────────────

def test_versionadded_produces_panel(make_visitor):
    rst = ".. versionadded:: 1.0\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_versionadded_panel_title(make_visitor):
    rst = ".. versionadded:: 1.0\n"
    assert _first_panel(make_visitor, rst).title == "New in version 1.0"


def test_versionadded_border_style(make_visitor):
    rst = ".. versionadded:: 1.0\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "green"


def test_versionadded_body_content_visible(render_text):
    rst = ".. versionadded:: 2.0\n\n   Added support for widgets.\n"
    assert "Added support for widgets." in render_text(rst, sphinx_compat=True)


def test_versionadded_version_in_output(render_text):
    rst = ".. versionadded:: 3.14\n"
    assert "3.14" in render_text(rst, sphinx_compat=True)


def test_versionadded_no_body_no_crash(make_visitor):
    rst = ".. versionadded:: 1.0\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_versionadded_body_without_blank_line_not_in_title(make_visitor):
    """Body content following the directive must not leak into the panel title.

    Repro from rich-rst v2 feedback: when a ``versionadded`` directive has
    body content on the next line (no blank separator), the body is
    concatenated into the panel title rather than placed in the panel body,
    producing ``"New in version 0.47 This was added recently."`` as the
    title and an empty body row.
    """
    rst = ".. versionadded:: 0.47\n    This was added recently.\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "New in version 0.47"


# ── versionchanged ────────────────────────────────────────────────────────────

def test_versionchanged_produces_panel(make_visitor):
    rst = ".. versionchanged:: 2.0\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_versionchanged_panel_title(make_visitor):
    rst = ".. versionchanged:: 2.0\n"
    assert _first_panel(make_visitor, rst).title == "Changed in version 2.0"


def test_versionchanged_border_style(make_visitor):
    rst = ".. versionchanged:: 2.0\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "cyan"


def test_versionchanged_body_content_visible(render_text):
    rst = ".. versionchanged:: 2.0\n\n   Behavior changed significantly.\n"
    assert "Behavior changed significantly." in render_text(rst, sphinx_compat=True)


def test_versionchanged_version_in_output(render_text):
    rst = ".. versionchanged:: 2.5\n"
    assert "2.5" in render_text(rst, sphinx_compat=True)


# ── deprecated ────────────────────────────────────────────────────────────────

def test_deprecated_produces_panel(make_visitor):
    rst = ".. deprecated:: 3.0\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_deprecated_panel_title(make_visitor):
    rst = ".. deprecated:: 3.0\n"
    assert _first_panel(make_visitor, rst).title == "Deprecated since version 3.0"


def test_deprecated_border_style(make_visitor):
    rst = ".. deprecated:: 3.0\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "yellow"


def test_deprecated_body_content_visible(render_text):
    rst = ".. deprecated:: 3.0\n\n   Use :func:`new_func` instead.\n"
    assert "new_func" in render_text(rst, sphinx_compat=True)


def test_deprecated_version_in_output(render_text):
    rst = ".. deprecated:: 1.2.3\n"
    assert "1.2.3" in render_text(rst, sphinx_compat=True)


# ── seealso ───────────────────────────────────────────────────────────────────

def test_seealso_produces_panel(make_visitor):
    rst = ".. seealso::\n\n   Some related topic.\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_seealso_panel_title(make_visitor):
    rst = ".. seealso::\n\n   Some related topic.\n"
    assert _first_panel(make_visitor, rst).title == "See Also"


def test_seealso_border_style(make_visitor):
    rst = ".. seealso::\n\n   Some related topic.\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "white"


def test_seealso_body_content_visible(render_text):
    rst = ".. seealso::\n\n   Module :mod:`os.path`.\n"
    assert "os.path" in render_text(rst, sphinx_compat=True)


def test_seealso_inline_argument_visible(render_text):
    rst = ".. seealso:: :func:`os.path.join`\n"
    assert "os.path.join" in render_text(rst, sphinx_compat=True)


# ── sphinx_compat=False falls back to system messages for unknown directives ──

def test_unknown_directive_shows_system_message_without_sphinx_compat(render_text):
    """Verify that truly unknown directives still produce system messages when sphinx_compat=False."""
    rst = ".. my_completely_unknown_directive_xyz:: arg\n\n   Some content.\n"
    out = render_text(rst, sphinx_compat=False, show_errors=True)
    assert "System Message" in out


def test_unknown_directive_no_crash_when_errors_hidden(render_text):
    """Verify that truly unknown directives don't crash when errors are suppressed."""
    rst = ".. my_completely_unknown_directive_xyz:: arg\n\n   Some content.\n"
    out = render_text(rst, sphinx_compat=False, show_errors=False)
    assert isinstance(out, str)


# ── Body with inline markup ───────────────────────────────────────────────────

def test_versionadded_body_with_inline_code(render_text):
    rst = ".. versionadded:: 1.0\n\n   Use ``new_api()`` going forward.\n"
    assert "new_api()" in render_text(rst, sphinx_compat=True)


def test_versionadded_body_with_bold(render_text):
    rst = ".. versionadded:: 1.0\n\n   This is **important**.\n"
    assert "important" in render_text(rst, sphinx_compat=True)


def test_seealso_body_with_bullet_list(render_text):
    rst = ".. seealso::\n\n   - Topic one\n   - Topic two\n"
    out = render_text(rst, sphinx_compat=True)
    assert "Topic one" in out
    assert "Topic two" in out


# ── Complex version strings ───────────────────────────────────────────────────

def test_versionadded_prerelease_version(render_text):
    rst = ".. versionadded:: 2.0.0-rc1\n"
    assert "2.0.0-rc1" in render_text(rst, sphinx_compat=True)


def test_deprecated_alpha_version(render_text):
    rst = ".. deprecated:: 3.0a1\n"
    assert "3.0a1" in render_text(rst, sphinx_compat=True)


# ── availability ──────────────────────────────────────────────────────────────

def test_availability_produces_panel(make_visitor):
    rst = ".. availability:: 1.0\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_availability_panel_title(make_visitor):
    rst = ".. availability:: 1.0\n"
    assert _first_panel(make_visitor, rst).title == "Available since version 1.0"


def test_availability_border_style(make_visitor):
    rst = ".. availability:: 1.0\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "blue"


def test_availability_body_content_visible(render_text):
    rst = ".. availability:: 3.5\n\n   Available on all platforms.\n"
    assert "Available on all platforms." in render_text(rst, sphinx_compat=True)


def test_availability_version_in_output(render_text):
    rst = ".. availability:: 2.5\n"
    assert "2.5" in render_text(rst, sphinx_compat=True)


def test_availability_no_body_no_crash(make_visitor):
    rst = ".. availability:: 1.0\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_availability_body_without_blank_line(make_visitor):
    """Body content on the next line should not leak into the panel title."""
    rst = ".. availability:: 3.8\n    Works on Windows.\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "Available since version 3.8"


# ── soft-deprecated ────────────────────────────────────────────────────────────

def test_soft_deprecated_produces_panel(make_visitor):
    rst = ".. soft-deprecated:: 2.0\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_soft_deprecated_panel_title(make_visitor):
    rst = ".. soft-deprecated:: 2.0\n"
    assert _first_panel(make_visitor, rst).title == "Soft Deprecated since version 2.0"


def test_soft_deprecated_border_style(make_visitor):
    rst = ".. soft-deprecated:: 2.0\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "bright_yellow"


def test_soft_deprecated_body_content_visible(render_text):
    rst = ".. soft-deprecated:: 1.5\n\n   Use the new function instead.\n"
    assert "Use the new function instead." in render_text(rst, sphinx_compat=True)


def test_soft_deprecated_version_in_output(render_text):
    rst = ".. soft-deprecated:: 1.8\n"
    assert "1.8" in render_text(rst, sphinx_compat=True)


def test_soft_deprecated_no_body_no_crash(make_visitor):
    rst = ".. soft-deprecated:: 2.0\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_soft_deprecated_body_without_blank_line(make_visitor):
    """Body content on the next line should not leak into the panel title."""
    rst = ".. soft-deprecated:: 1.9\n    Consider using newer API.\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "Soft Deprecated since version 1.9"


# ── impl-detail ────────────────────────────────────────────────────────────────

def test_impl_detail_produces_panel(make_visitor):
    rst = ".. impl-detail::\n\n   This is an implementation detail.\n"
    assert isinstance(_first_panel(make_visitor, rst), Panel)


def test_impl_detail_panel_title(make_visitor):
    rst = ".. impl-detail::\n\n   Some detail.\n"
    assert _first_panel(make_visitor, rst).title == "Implementation Detail"


def test_impl_detail_border_style(make_visitor):
    rst = ".. impl-detail::\n\n   Some detail.\n"
    bs = _first_panel(make_visitor, rst).border_style
    assert bs.bold is True and bs.color.name == "magenta"


def test_impl_detail_body_content_visible(render_text):
    rst = ".. impl-detail::\n\n   Uses an internal caching mechanism.\n"
    assert "Uses an internal caching mechanism." in render_text(rst, sphinx_compat=True)


def test_impl_detail_no_body_no_crash(make_visitor):
    rst = ".. impl-detail::\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_impl_detail_multiple_paragraphs(render_text):
    rst = """.. impl-detail::

   This is implemented differently on Windows.
   
   The POSIX version uses signals."""
    out = render_text(rst, sphinx_compat=True)
    assert "Windows" in out and "POSIX" in out

@pytest.fixture(autouse=True)
def ensure_sphinx_compat():
    _register_sphinx_directives()
    _register_sphinx_roles()


def _panels(make_visitor, rst):
    visitor = make_visitor(rst)
    return [r for r in visitor.renderables if isinstance(r, Panel)]


def _first_panel(make_visitor, rst):
    panels = _panels(make_visitor, rst)
    assert panels, f"Must produce at least one Panel:\n{rst}"
    return panels[0]


def _render(render_text, rst, **kw):
    return render_text(rst, sphinx_compat=True, **kw)


# ── code-block ────────────────────────────────────────────────────────────────

def test_codeblock_with_language_produces_panel(make_visitor):
    rst = ".. code-block:: python\n\n   x = 1\n"
    assert _panels(make_visitor, rst), "code-block should produce a Panel"


def test_codeblock_language_in_panel_title(make_visitor):
    rst = ".. code-block:: python\n\n   x = 1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "python"


def test_codeblock_content_appears_in_output(render_text):
    rst = ".. code-block:: python\n\n   x = 42\n"
    assert "x = 42" in _render(render_text, rst)


def test_codeblock_without_language_renders(make_visitor):
    rst = ".. code-block::\n\n   some text\n"
    visitor = make_visitor(rst)
    assert visitor.renderables, "code-block without language should produce renderables"


def test_sourcecode_works_like_codeblock(render_text):
    rst = ".. sourcecode:: python\n\n   y = 2\n"
    assert "y = 2" in _render(render_text, rst)


def test_sourcecode_produces_panel(make_visitor):
    rst = ".. sourcecode:: python\n\n   z = 3\n"
    assert _panels(make_visitor, rst), "sourcecode should produce a Panel"


# ── highlight ─────────────────────────────────────────────────────────────────

def test_highlight_produces_no_output(make_visitor):
    rst = ".. highlight:: python\n"
    visitor = make_visitor(rst)
    panels = _panels(make_visitor, rst)
    assert not panels, "highlight should produce no Panel"


def test_highlight_no_crash(render_text):
    rst = ".. highlight:: python\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── index / tabularcolumns ────────────────────────────────────────────────────

def test_index_produces_no_output(make_visitor):
    rst = ".. index:: myterm\n"
    panels = _panels(make_visitor, rst)
    assert not panels, "index should produce no Panel"


def test_index_no_crash(render_text):
    rst = ".. index:: some term\n\nSome text.\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_tabularcolumns_produces_no_output(make_visitor):
    rst = ".. tabularcolumns:: |L|L|\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_tabularcolumns_no_crash(render_text):
    rst = ".. tabularcolumns:: |L|L|\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── currentmodule / py:currentmodule ─────────────────────────────────────────

def test_currentmodule_produces_no_output(make_visitor):
    rst = ".. currentmodule:: os.path\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_currentmodule_no_crash(render_text):
    rst = ".. currentmodule:: os.path\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_py_currentmodule_produces_no_output(make_visitor):
    rst = ".. py:currentmodule:: os.path\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_py_currentmodule_no_crash(render_text):
    rst = ".. py:currentmodule:: os.path\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── only ──────────────────────────────────────────────────────────────────────

def test_only_always_renders_content(render_text):
    rst = ".. only:: html\n\n   This is html only content.\n"
    out = _render(render_text, rst)
    assert "This is html only content." in out


def test_only_with_latex_expression(render_text):
    rst = ".. only:: latex\n\n   LaTeX only text here.\n"
    out = _render(render_text, rst)
    assert "LaTeX only text here." in out


# ── centered ──────────────────────────────────────────────────────────────────

def test_centered_produces_output(render_text):
    rst = ".. centered:: My Centered Title\n"
    out = _render(render_text, rst)
    assert "My Centered Title" in out


def test_centered_produces_align(make_visitor):
    rst = ".. centered:: Center Me\n"
    visitor = make_visitor(rst)
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert aligns, "centered should produce an Align renderable"


# ── hlist ─────────────────────────────────────────────────────────────────────

def test_hlist_content_appears_in_output(render_text):
    rst = ".. hlist::\n   :columns: 2\n\n   * Item one\n   * Item two\n"
    out = _render(render_text, rst)
    assert "Item one" in out
    assert "Item two" in out


def test_hlist_no_crash(make_visitor):
    rst = ".. hlist::\n\n   * Alpha\n   * Beta\n"
    visitor = make_visitor(rst)
    assert isinstance(visitor.renderables, list)


def test_highlights_bullets_render_on_same_line(render_text):
    rst = (
        ".. highlights::\n\n"
        "   Key takeaways:\n\n"
        "   - Keep it simple.\n"
        "   - Document everything.\n"
    )
    out = _render(render_text, rst)
    lines = out.splitlines()
    assert any("•" in line and "Keep it simple." in line for line in lines)
    assert any("•" in line and "Document everything." in line for line in lines)


# ── toctree ───────────────────────────────────────────────────────────────────

def test_toctree_renders_as_panel(make_visitor):
    rst = ".. toctree::\n   :maxdepth: 2\n\n   intro\n   usage\n"
    panels = _panels(make_visitor, rst)
    assert panels, "toctree should produce a Panel"


def test_toctree_entries_visible(render_text):
    rst = ".. toctree::\n\n   intro\n   advanced\n"
    out = _render(render_text, rst)
    assert "intro" in out
    assert "advanced" in out


def test_toctree_caption_used(make_visitor):
    rst = ".. toctree::\n   :caption: My Table of Contents\n\n   page1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "My Table of Contents"


def test_toctree_default_caption(make_visitor):
    rst = ".. toctree::\n\n   page1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "Contents"


def test_toctree_nested_entries_indented(render_text):
    """Entries with path separators must be visually indented relative to root entries."""
    rst = (
        ".. toctree::\n\n"
        "   intro\n"
        "   guide/installation\n"
        "   guide/usage\n"
    )
    out = _render(render_text, rst)
    # Root entry has no indentation; sub-entries are indented.
    lines = [l for l in out.splitlines() if "intro" in l or "installation" in l or "usage" in l]
    intro_lines = [l for l in lines if "intro" in l]
    sub_lines = [l for l in lines if "installation" in l or "usage" in l]
    assert intro_lines, "Root entry 'intro' must appear in output"
    assert sub_lines, "Sub-entries 'installation' / 'usage' must appear in output"
    # Compare the column where the entry text starts inside the line.
    # Panel border chars (│) are non-whitespace so we measure from the first
    # space character after the border.
    def entry_text_col(line, text):
        idx = line.find(text)
        return idx if idx >= 0 else len(line)

    intro_col = entry_text_col(intro_lines[0], "intro")
    sub_col = entry_text_col(sub_lines[0], "installation")
    assert sub_col > intro_col, (
        f"Sub-entry column ({sub_col}) must be greater than root entry column ({intro_col})"
    )


def test_toctree_maxdepth_hides_deep_entries(render_text):
    """Entries deeper than maxdepth must be omitted from the rendered output."""
    rst = (
        ".. toctree::\n"
        "   :maxdepth: 1\n\n"
        "   intro\n"
        "   guide/installation\n"
    )
    out = _render(render_text, rst)
    assert "intro" in out, "Root entry must be visible"
    assert "installation" not in out, "Entry at depth 1 must be hidden when maxdepth=1"


def test_toctree_explicit_title_used(render_text):
    """Entries in 'Title <docname>' format must show the explicit title."""
    rst = ".. toctree::\n\n   My Guide <guide/intro>\n"
    out = _render(render_text, rst)
    assert "My Guide" in out, "Explicit title must be shown"


def test_toctree_reversed_order(render_text):
    rst = (
        ".. toctree::\n"
        "   :reversed:\n\n"
        "   first\n"
        "   second\n"
        "   third\n"
    )
    out = _render(render_text, rst)
    assert out.find("third") < out.find("first"), "Entries must be reversed"


def test_toctree_numbered_entries(render_text):
    rst = (
        ".. toctree::\n"
        "   :numbered:\n\n"
        "   intro\n"
        "   guide/installation\n"
    )
    out = _render(render_text, rst)
    assert "1. intro" in out
    assert "1.1. guide/installation" in out


# ── literalinclude ────────────────────────────────────────────────────────────

def test_literalinclude_renders_as_panel(make_visitor):
    rst = ".. literalinclude:: myfile.py\n"
    panels = _panels(make_visitor, rst)
    assert panels, "literalinclude should produce a Panel"


def test_literalinclude_filename_visible(render_text):
    rst = ".. literalinclude:: path/to/myfile.py\n"
    out = _render(render_text, rst)
    assert "path/to/myfile.py" in out


def test_literalinclude_panel_title(make_visitor):
    rst = ".. literalinclude:: example.py\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "literalinclude"


def test_literalinclude_reads_actual_file(tmp_path, render_text):
    """When the file exists, its content must appear in the rendered output."""
    src = tmp_path / "sample.py"
    src.write_text("x = 42\ny = 'hello'\n")

    # Write an RST document whose source_path is inside tmp_path so that
    # the directive can resolve the relative filename.
    rst_file = tmp_path / "doc.rst"
    rst_file.write_text(".. literalinclude:: sample.py\n")

    from rich.console import Console
    from rich_rst import RestructuredText
    console = Console(force_terminal=True, width=120, record=True)
    console.print(
        RestructuredText(
            rst_file.read_text(),
            sphinx_compat=True,
            filename=str(rst_file),
        )
    )
    out = console.export_text()
    assert "x = 42" in out, "File content must appear in the output"
    assert "y = 'hello'" in out, "File content must appear in the output"


def test_literalinclude_missing_file_shows_placeholder(render_text):
    """When the file does not exist, a placeholder panel must still appear."""
    rst = ".. literalinclude:: does_not_exist_xyz.py\n"
    out = _render(render_text, rst)
    # Either the filename or the 'literalinclude' title must be visible.
    assert "does_not_exist_xyz.py" in out or "literalinclude" in out


def test_literalinclude_lines_option(tmp_path):
    """The :lines: option must restrict the displayed content to chosen lines."""
    src = tmp_path / "multi.py"
    src.write_text("line1\nline2\nline3\nline4\nline5\n")
    rst_file = tmp_path / "doc.rst"
    rst_file.write_text(".. literalinclude:: multi.py\n   :lines: 2-3\n")

    from rich.console import Console
    from rich_rst import RestructuredText
    console = Console(force_terminal=True, width=120, record=True)
    console.print(
        RestructuredText(
            rst_file.read_text(),
            sphinx_compat=True,
            filename=str(rst_file),
        )
    )
    out = console.export_text()
    assert "line2" in out
    assert "line3" in out
    assert "line1" not in out
    assert "line4" not in out


# ── productionlist ────────────────────────────────────────────────────────────

def test_productionlist_content_appears(render_text):
    rst = ".. productionlist::\n   statement: assignment\n   assignment: NAME '=' expr\n"
    out = _render(render_text, rst)
    assert "statement" in out


def test_productionlist_produces_panel(make_visitor):
    rst = ".. productionlist::\n   rule: token\n"
    panels = _panels(make_visitor, rst)
    assert panels, "productionlist should produce a Panel"


def test_productionlist_panel_title_is_productionlist(make_visitor):
    rst = ".. productionlist::\n   rule: token\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "productionlist"


# ── glossary ──────────────────────────────────────────────────────────────────

def test_glossary_content_appears(render_text):
    rst = ".. glossary::\n\n   term1\n      Definition of term1.\n"
    out = _render(render_text, rst)
    assert "term1" in out


def test_glossary_produces_panel_titled_glossary(make_visitor):
    rst = ".. glossary::\n\n   term1\n      Definition of term1.\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "Glossary"


def test_glossary_no_crash(make_visitor):
    rst = ".. glossary::\n\n   myterm\n      The definition.\n"
    visitor = make_visitor(rst)
    assert isinstance(visitor.renderables, list)


def test_glossary_sorted_option_sorts_terms(render_text):
    rst = (
        ".. glossary::\n"
        "   :sorted:\n\n"
        "   zebra\n"
        "      Last entry.\n\n"
        "   apple\n"
        "      First entry.\n"
    )
    out = _render(render_text, rst)
    assert out.index("apple") < out.index("zebra")


# ── math directive options ────────────────────────────────────────────────────

def test_math_nowrap_and_label_options_are_accepted(render_text):
    rst = (
        ".. math::\n"
        "   :nowrap:\n"
        "   :label: eq-energy\n\n"
        "   E = mc^2\n"
    )
    out = _render(render_text, rst)
    assert "unknown option" not in out.lower()
    assert "E = mc^2" in out


# ── deprecated-removed ────────────────────────────────────────────────────────

def test_deprecated_removed_produces_panel(make_visitor):
    rst = ".. deprecated-removed:: 3.0 4.0\n"
    panels = _panels(make_visitor, rst)
    assert panels, "deprecated-removed should produce a Panel"


def test_deprecated_removed_both_versions_visible(render_text):
    rst = ".. deprecated-removed:: 3.0 4.0\n\n   Use the new API.\n"
    out = _render(render_text, rst)
    assert "3.0" in out
    assert "4.0" in out


def test_deprecated_removed_body_visible(render_text):
    rst = ".. deprecated-removed:: 3.0 4.0\n\n   Use the new API instead.\n"
    out = _render(render_text, rst)
    assert "Use the new API instead." in out


# ── Python domain directives ──────────────────────────────────────────────────

def test_py_function_produces_panel(make_visitor):
    rst = ".. py:function:: my_func(arg1, arg2)\n\n   Does something.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "py:function should produce a Panel"


def test_py_function_signature_visible(render_text):
    rst = ".. py:function:: compute(x, y)\n\n   Computes a value.\n"
    out = _render(render_text, rst)
    assert "compute(x, y)" in out


def test_py_class_produces_panel(make_visitor):
    rst = ".. py:class:: MyClass(base)\n\n   A class.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_py_method_produces_panel(make_visitor):
    rst = ".. py:method:: MyClass.my_method(self, arg)\n\n   A method.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_py_attribute_produces_panel(make_visitor):
    rst = ".. py:attribute:: MyClass.attr\n\n   An attribute.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_py_function_field_list_renders_api_sections(render_text):
    rst = (
        ".. py:function:: greet(name: str) -> str\n\n"
        "   Return a greeting for *name*.\n\n"
        "   :param name: The name to greet.\n"
        "   :type name: str\n"
        "   :returns: A greeting string.\n"
        "   :rtype: str\n"
    )
    out = _render(render_text, rst)
    assert "Parameters" in out
    assert "Name" not in out
    assert "Type" not in out
    assert "Description" not in out
    assert "name: str" in out
    assert "name" in out and "The name to greet." in out
    assert "Returns" in out and "str: A greeting string." in out
    assert "Field Name" not in out and "Field Value" not in out


def test_py_method_field_list_uses_same_format(render_text):
    rst = (
        ".. py:method:: Greeter.greet(name: str) -> str\n\n"
        "   Greet a person.\n\n"
        "   :param name: Person name.\n"
        "   :type name: str\n"
        "   :returns: Greeting text.\n"
        "   :rtype: str\n"
    )
    out = _render(render_text, rst)
    assert "Parameters" in out
    assert "name: str" in out
    assert "Returns" in out
    assert "name" in out and "Person name." in out
    assert "str: Greeting text." in out


def test_py_field_list_sections_do_not_render_as_tables(make_visitor):
    rst = (
        ".. py:function:: parse(text)\n\n"
        "   :param text: Input text.\n"
        "   :type text: str\n"
        "   :raises ValueError: On invalid input.\n"
    )
    visitor = make_visitor(rst)
    assert not any(isinstance(renderable, Table) for renderable in visitor.renderables)


def test_py_data_value_option_is_visible(render_text):
    rst = (
        ".. py:data:: MAX_RETRIES\n"
        "   :value: 3\n\n"
        "   Maximum number of retry attempts.\n"
    )
    out = _render(render_text, rst)
    assert "Details" in out
    assert "Value" in out
    assert "3" in out
    assert "Maximum number of retry attempts." in out


def test_py_data_details_do_not_render_as_table(make_visitor):
    rst = (
        ".. py:data:: MAX_RETRIES\n"
        "   :value: 3\n\n"
        "   Maximum number of retry attempts.\n"
    )
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.renderable, Group)
    assert not any(isinstance(r, Table) for r in panel.renderable.renderables)


def test_py_attribute_type_option_is_visible(render_text):
    rst = (
        ".. py:attribute:: MyClass.value\n"
        "   :type: int\n\n"
        "   The current value.\n"
    )
    out = _render(render_text, rst)
    assert "Details" in out
    assert "Type" in out
    assert "int" in out
    assert "The current value." in out


def test_py_function_additional_options_are_visible(render_text):
    rst = (
        ".. py:function:: pkg.compute(x)\n"
        "   :module: pkg.core\n"
        "   :annotation: static\n"
        "   :canonical: pkg.core.compute\n"
        "   :deprecated:\n\n"
        "   Compute something.\n"
    )
    out = _render(render_text, rst)
    assert "Module" in out and "pkg.core" in out
    assert "Annotation" in out and "static" in out
    assert "Canonical" in out and "pkg.core.compute" in out
    assert "Flags" in out and "deprecated" in out


@pytest.mark.parametrize(
    "directive, signature",
    [
        ("py:envvar", "DATABASE_URL"),
        ("py:option", "--verbose"),
        ("py:coroutinefunction", "fetch_data(self, timeout: int = 3) -> bool"),
        ("py:coroutinemethod", "Client.fetch(self, timeout: int = 3) -> bool"),
        ("py:decoratorfunction", "cached(func)"),
        ("py:abstractmethod", "Base.run(self, retries: int = 3) -> bool"),
        ("py:opcode", "LOAD_FAST index"),
        ("py:describe", "my_symbol"),
    ],
)
def test_additional_py_domain_directives_produce_panels(make_visitor, directive, signature):
    rst = f".. {directive}:: {signature}\n\n   Description.\n"
    panels = _panels(make_visitor, rst)
    assert panels, f"{directive} should produce a Panel"


def _span_covers_token(title: Text, token: str, predicate):
    """Return True when a span covering ``token`` satisfies ``predicate``."""
    try:
        start = title.plain.index(token)
    except ValueError:
        return False
    end = start + len(token)
    return any(span.start <= start and span.end >= end and predicate(span.style) for span in title.spans)


def test_py_function_signature_title_highlighting_rules(make_visitor):
    rst = ".. py:function:: compute(self, value: int = 3, active: bool = True) -> bool\n"
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.title, Text)
    title = panel.title

    assert _span_covers_token(title, "compute", lambda style: style.bold)
    assert _span_covers_token(title, "self", lambda style: style.color is not None)
    assert _span_covers_token(title, "->", lambda style: style.bold or style.color is not None)
    assert _span_covers_token(title, "int", lambda style: style.color is not None)
    assert _span_covers_token(title, "bool", lambda style: style.color is not None)
    assert _span_covers_token(title, "True", lambda style: style.color is not None)
    assert _span_covers_token(title, "3", lambda style: style.color is not None)


def test_py_desc_panel_colors_vary_by_object_type(make_visitor):
    function_panel = _first_panel(make_visitor, ".. py:function:: compute(x)\n")
    class_panel = _first_panel(make_visitor, ".. py:class:: MyClass\n")
    method_panel = _first_panel(make_visitor, ".. py:method:: MyClass.run(self)\n")

    assert str(function_panel.border_style) != str(class_panel.border_style)
    assert str(function_panel.border_style) != str(method_panel.border_style)
    assert str(class_panel.border_style) != str(method_panel.border_style)


def test_class_typed_attributes_render_in_attributes_section(render_text):
    rst = (
        ".. py:class:: Counter\n\n"
        "   .. py:attribute:: Counter.value\n"
        "      :type: int\n\n"
        "      Current counter value.\n"
    )
    out = _render(render_text, rst)
    assert "Attributes" in out
    assert "value: int" in out
    assert "Current counter value." in out


# ── C domain directives ───────────────────────────────────────────────────────

def test_c_function_produces_panel(make_visitor):
    rst = ".. c:function:: int my_func(int x)\n\n   A C function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "c:function should produce a Panel"


def test_c_type_produces_panel(make_visitor):
    rst = ".. c:type:: my_type\n\n   A C type.\n"
    panels = _panels(make_visitor, rst)
    assert panels


# ── C++ domain directives ─────────────────────────────────────────────────────

def test_cpp_function_produces_panel(make_visitor):
    rst = ".. cpp:function:: void my_func(int x)\n\n   A C++ function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "cpp:function should produce a Panel"


def test_cpp_class_produces_panel(make_visitor):
    rst = ".. cpp:class:: MyClass\n\n   A C++ class.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_c_function_signature_title_highlighting_rules(make_visitor):
    rst = ".. c:function:: int my_func(int value)\n\n   A C function.\n"
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.title, Text)
    title = panel.title

    assert _span_covers_token(title, "my_func", lambda style: style.bold)
    assert _span_covers_token(title, "int", lambda style: style.color is not None)


def test_cpp_alias_signature_title_highlighting_rules(make_visitor):
    rst = ".. cpp:alias:: StringMap = std::unordered_map<std::string, int>\n\n   Alias.\n"
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.title, Text)
    title = panel.title

    assert _span_covers_token(title, "StringMap", lambda style: style.bold)
    assert _span_covers_token(title, "=", lambda style: style.bold or style.color is not None)
    assert _span_covers_token(title, "std", lambda style: style.color is not None)
    assert _span_covers_token(title, "int", lambda style: style.color is not None)


def test_c_cpp_desc_panel_colors_vary_by_object_type(make_visitor):
    c_enum_panel = _first_panel(make_visitor, ".. c:enum:: color\n")
    c_member_panel = _first_panel(make_visitor, ".. c:member:: int color.value\n")
    cpp_class_panel = _first_panel(make_visitor, ".. cpp:class:: Widget\n")
    cpp_alias_panel = _first_panel(make_visitor, ".. cpp:alias:: StringMap = std::unordered_map\n")

    assert c_enum_panel.border_style != c_member_panel.border_style
    assert cpp_class_panel.border_style != cpp_alias_panel.border_style


# ── JS domain directives ──────────────────────────────────────────────────────

def test_js_function_produces_panel(make_visitor):
    rst = ".. js:function:: myFunc(arg)\n\n   A JS function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "js:function should produce a Panel"


def test_js_method_signature_title_highlighting_rules(make_visitor):
    rst = ".. js:method:: UserManager.authenticate(user, retries = 3)\n\n   A JS method.\n"
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.title, Text)
    title = panel.title

    assert _span_covers_token(title, "authenticate", lambda style: style.bold)
    assert _span_covers_token(title, ".", lambda style: style.bold or style.color is not None)
    assert _span_covers_token(title, "3", lambda style: style.color is not None)


def test_js_module_signature_title_highlighting_rules(make_visitor):
    rst = ".. js:module:: analytics.core\n\n   A JS module.\n"
    panel = _first_panel(make_visitor, rst)
    assert isinstance(panel.title, Text)
    title = panel.title

    assert _span_covers_token(title, "analytics", lambda style: style.color is not None)
    assert _span_covers_token(title, "core", lambda style: style.bold)


def test_js_desc_panel_colors_vary_by_object_type(make_visitor):
    function_panel = _first_panel(make_visitor, ".. js:function:: parseConfiguration(config)\n")
    class_panel = _first_panel(make_visitor, ".. js:class:: UserManager\n")
    data_panel = _first_panel(make_visitor, ".. js:data:: API_VERSION\n")

    assert function_panel.border_style != class_panel.border_style
    assert class_panel.border_style != data_panel.border_style


# ── autodoc directives ────────────────────────────────────────────────────────

def test_automodule_produces_no_output(make_visitor):
    rst = ".. automodule:: mymodule\n   :members:\n"
    panels = _panels(make_visitor, rst)
    assert not panels, "automodule should produce no Panel"


def test_automodule_no_crash(render_text):
    rst = ".. automodule:: mymodule\n   :members:\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_autoclass_produces_no_output(make_visitor):
    rst = ".. autoclass:: mymodule.MyClass\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_autofunction_no_crash(render_text):
    rst = ".. autofunction:: mymodule.my_func\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)