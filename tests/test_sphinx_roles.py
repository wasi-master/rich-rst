"""Tests for Sphinx-specific interpreted-text roles.

rich-rst registers Sphinx roles (``func``, ``class``, ``meth``, etc.)
so that Python docstrings render cleanly instead of showing system-message
errors.  Each role is tested in isolation.

All roles render their content as inline literal (code-styled) text.
When a role uses the ``display name <target>`` syntax, only the display
name is shown.
"""
import pytest
from rich.text import Text

from rich_rst import _register_sphinx_roles


@pytest.fixture(autouse=True)
def ensure_sphinx_roles():
    """Register Sphinx roles once before any test in this module runs."""
    _register_sphinx_roles()


# ── Core Sphinx domain roles ──────────────────────────────────────────────────

def test_func_role(render_text):
    assert "os.path.join" in render_text(":func:`os.path.join`", sphinx_compat=True)


def test_function_role_alias(render_text):
    assert "my_func" in render_text(":function:`my_func`", sphinx_compat=True)


def test_meth_role(render_text):
    assert "str.format" in render_text(":meth:`str.format`", sphinx_compat=True)


def test_method_role_alias(render_text):
    assert "list.sort" in render_text(":method:`list.sort`", sphinx_compat=True)


def test_class_role(render_text):
    assert "pathlib.Path" in render_text(":class:`pathlib.Path`", sphinx_compat=True)


def test_mod_role(render_text):
    assert "collections.abc" in render_text(":mod:`collections.abc`", sphinx_compat=True)


def test_module_role_alias(render_text):
    assert "os.path" in render_text(":module:`os.path`", sphinx_compat=True)


def test_attr_role(render_text):
    assert "object.__name__" in render_text(":attr:`object.__name__`", sphinx_compat=True)


def test_attribute_role_alias(render_text):
    assert "cls.x" in render_text(":attribute:`cls.x`", sphinx_compat=True)


def test_obj_role(render_text):
    assert "sys.stdout" in render_text(":obj:`sys.stdout`", sphinx_compat=True)


def test_object_role_alias(render_text):
    assert "my_obj" in render_text(":object:`my_obj`", sphinx_compat=True)


def test_data_role(render_text):
    assert "sys.maxsize" in render_text(":data:`sys.maxsize`", sphinx_compat=True)


def test_exc_role(render_text):
    assert "ValueError" in render_text(":exc:`ValueError`", sphinx_compat=True)


def test_exception_role_alias(render_text):
    assert "TypeError" in render_text(":exception:`TypeError`", sphinx_compat=True)


def test_type_role(render_text):
    assert "int" in render_text(":type:`int`", sphinx_compat=True)


def test_var_role(render_text):
    assert "my_var" in render_text(":var:`my_var`", sphinx_compat=True)


def test_const_role(render_text):
    assert "MAX_SIZE" in render_text(":const:`MAX_SIZE`", sphinx_compat=True)


def test_constant_role_alias(render_text):
    assert "PI" in render_text(":constant:`PI`", sphinx_compat=True)


# ── Python domain prefix roles ────────────────────────────────────────────────

def test_py_func_role(render_text):
    assert "open" in render_text(":py:func:`open`", sphinx_compat=True)


def test_py_class_role(render_text):
    assert "dict" in render_text(":py:class:`dict`", sphinx_compat=True)


def test_py_meth_role(render_text):
    assert "list.append" in render_text(":py:meth:`list.append`", sphinx_compat=True)


def test_py_mod_role(render_text):
    assert "os.path" in render_text(":py:mod:`os.path`", sphinx_compat=True)


def test_py_attr_role(render_text):
    assert "cls.val" in render_text(":py:attr:`cls.val`", sphinx_compat=True)


def test_py_obj_role(render_text):
    assert "sys.argv" in render_text(":py:obj:`sys.argv`", sphinx_compat=True)


def test_py_data_role(render_text):
    assert "sys.maxsize" in render_text(":py:data:`sys.maxsize`", sphinx_compat=True)


def test_py_const_role(render_text):
    assert "NONE" in render_text(":py:const:`NONE`", sphinx_compat=True)


def test_py_exc_role(render_text):
    assert "KeyError" in render_text(":py:exc:`KeyError`", sphinx_compat=True)


# ── Explicit-title (display-name) syntax ─────────────────────────────────────

def test_func_role_explicit_title_shows_display_name(render_text):
    out = render_text(":func:`custom name <os.path.join>`", sphinx_compat=True)
    assert "custom name" in out


def test_func_role_explicit_title_hides_target(render_text):
    out = render_text(":func:`custom name <os.path.join>`", sphinx_compat=True)
    assert "os.path.join" not in out


def test_class_role_explicit_title(render_text):
    out = render_text(":class:`MyPath <pathlib.Path>`", sphinx_compat=True)
    assert "MyPath" in out
    assert "pathlib.Path" not in out


def test_meth_role_explicit_title(render_text):
    out = render_text(":meth:`format method <str.format>`", sphinx_compat=True)
    assert "format method" in out
    assert "str.format" not in out


# ── Sphinx roles render as inline literal text ────────────────────────────────

def test_sphinx_role_produces_text_renderable(make_visitor):
    visitor = make_visitor(":func:`my_function`")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "my_function" in combined


def test_sphinx_roles_in_mixed_paragraph(render_text):
    rst = (
        "This paragraph contains a :func:`function_call` and **bold text** "
        "and ``regular code`` all together."
    )
    out = render_text(rst, sphinx_compat=True)
    assert "function_call" in out
    assert "bold text" in out
    assert "regular code" in out


def test_sphinx_roles_in_bullet_list(render_text):
    rst = (
        "- Item with :meth:`method_name` reference\n"
        "- Another :func:`function_ref` here\n"
    )
    out = render_text(rst, sphinx_compat=True)
    assert "method_name" in out
    assert "function_ref" in out


# ── sphinx_compat=False does not register roles (no crash) ───────────────────

def test_completely_unknown_role_shows_system_message(render_text):
    """A truly unknown role (not in Sphinx list) produces a system message."""
    out = render_text(
        ":my_completely_unknown_role_xyz:`text`",
        sphinx_compat=False,
        show_errors=True,
    )
    assert "System Message" in out


def test_completely_unknown_role_no_crash_when_errors_hidden(render_text):
    out = render_text(
        ":my_completely_unknown_role_xyz:`text`",
        sphinx_compat=False,
        show_errors=False,
    )
    assert isinstance(out, str)
