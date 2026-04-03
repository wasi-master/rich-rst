"""Tests for Sphinx-specific block directives.

rich-rst registers Sphinx directives (``versionadded``, ``versionchanged``,
``deprecated``, ``seealso``) so that Python docstrings that use these
directives render as styled panels instead of system-message errors.

Formatting contract
-------------------
Each directive produces exactly one ``Panel`` whose title and border-style
follow the table below.

+---------------+--------------------------------+------------------+
| directive     | title                          | border_style     |
+===============+================================+==================+
| versionadded  | "New in version <ver>"         | bold green       |
| versionchanged| "Changed in version <ver>"     | bold cyan        |
| deprecated    | "Deprecated since version <v>" | bold yellow      |
| seealso       | "See Also"                     | bold white       |
+---------------+--------------------------------+------------------+

When no body content is supplied the panel is still emitted (empty body).
When body content is supplied it appears in the rendered output.
"""
import pytest
from rich.panel import Panel

from rich_rst import _register_sphinx_directives


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
    rst = ".. versionchanged:: 2.0\n\n   Behaviour changed significantly.\n"
    assert "Behaviour changed significantly." in render_text(rst, sphinx_compat=True)


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
