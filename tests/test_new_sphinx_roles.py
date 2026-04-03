"""Tests for new Sphinx-specific interpreted-text roles."""
import pytest
from rich.text import Text

from rich_rst import _register_sphinx_directives, _register_sphinx_roles


@pytest.fixture(autouse=True)
def ensure_sphinx_compat():
    _register_sphinx_directives()
    _register_sphinx_roles()


def _render(render_text, rst, **kw):
    return render_text(rst, sphinx_compat=True, **kw)


# ── :pep: ─────────────────────────────────────────────────────────────────────

def test_pep_role_text_in_output(render_text):
    out = _render(render_text, "See :pep:`484`.")
    assert "PEP 484" in out


def test_pep_role_url_in_output(render_text):
    out = _render(render_text, "See :pep:`484`.")
    assert "peps.python.org" in out


def test_pep_role_zero_padded_url(render_text):
    out = _render(render_text, "See :pep:`8`.")
    assert "pep-0008" in out


# ── :rfc: ─────────────────────────────────────────────────────────────────────

def test_rfc_role_text_in_output(render_text):
    out = _render(render_text, "See :rfc:`2822`.")
    assert "RFC 2822" in out


def test_rfc_role_url_in_output(render_text):
    out = _render(render_text, "See :rfc:`2822`.")
    assert "datatracker.ietf.org" in out


# ── :command: / :program: ─────────────────────────────────────────────────────

def test_command_role_text_in_output(render_text):
    out = _render(render_text, "Run :command:`git status`.")
    assert "git status" in out


def test_program_role_text_in_output(render_text):
    out = _render(render_text, "Use :program:`python`.")
    assert "python" in out


# ── :dfn: ─────────────────────────────────────────────────────────────────────

def test_dfn_role_text_in_output(render_text):
    out = _render(render_text, "A :dfn:`widget` is an element.")
    assert "widget" in out


def test_dfn_role_produces_emphasis(make_visitor):
    rst = "A :dfn:`term` is defined here."
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    assert texts, "dfn role should produce text"
    t = texts[0]
    italic_spans = [s for s in t._spans if s.style.italic]
    assert italic_spans, ":dfn: should produce italic/emphasis"


# ── :abbr: ────────────────────────────────────────────────────────────────────

def test_abbr_role_shows_abbreviation(render_text):
    out = _render(render_text, "The :abbr:`API (Application Programming Interface)` is stable.")
    assert "API" in out


def test_abbr_role_with_explanation(render_text):
    out = _render(render_text, "Use :abbr:`RST (reStructuredText)` format.")
    assert "RST" in out


# ── :menuselection: ───────────────────────────────────────────────────────────

def test_menuselection_arrow_replaced(render_text):
    out = _render(render_text, "Go to :menuselection:`File --> Open`.")
    assert "▶" in out
    assert "-->" not in out


def test_menuselection_text_in_output(render_text):
    out = _render(render_text, "Select :menuselection:`Edit --> Paste`.")
    assert "Edit" in out
    assert "Paste" in out


# ── :samp: / :file: ───────────────────────────────────────────────────────────

def test_samp_role_strips_braces(render_text):
    out = _render(render_text, "Use :samp:`print({value})`.")
    assert "value" in out
    assert "{" not in out
    assert "}" not in out


def test_file_role_strips_braces(render_text):
    out = _render(render_text, "Edit :file:`/home/{user}/.bashrc`.")
    assert "user" in out
    assert "{" not in out


def test_file_role_text_in_output(render_text):
    out = _render(render_text, "See :file:`/etc/hosts`.")
    assert "/etc/hosts" in out


# ── :envvar: ─────────────────────────────────────────────────────────────────

def test_envvar_renders_as_code(render_text):
    out = _render(render_text, "Set :envvar:`HOME` variable.")
    assert "HOME" in out


def test_envvar_no_crash(make_visitor):
    rst = "Set :envvar:`PATH` in your shell."
    visitor = make_visitor(rst)
    assert visitor.renderables


# ── :kbd: ─────────────────────────────────────────────────────────────────────

def test_kbd_renders_as_code(render_text):
    out = _render(render_text, "Press :kbd:`Ctrl+C`.")
    assert "Ctrl+C" in out


# ── :guilabel: ───────────────────────────────────────────────────────────────

def test_guilabel_renders_as_code(render_text):
    out = _render(render_text, "Click :guilabel:`OK`.")
    assert "OK" in out


# ── :term: / :ref: / :doc: / :any: ───────────────────────────────────────────

def test_term_role_in_output(render_text):
    out = _render(render_text, "See :term:`glossary term`.")
    assert "glossary term" in out


def test_ref_role_in_output(render_text):
    out = _render(render_text, "See :ref:`my-section`.")
    assert "my-section" in out


def test_doc_role_in_output(render_text):
    out = _render(render_text, "See :doc:`installation`.")
    assert "installation" in out


def test_any_role_in_output(render_text):
    out = _render(render_text, "See :any:`something`.")
    assert "something" in out


# ── C/C++/JS domain roles ────────────────────────────────────────────────────

def test_c_func_renders_as_code(render_text):
    out = _render(render_text, "Call :c:func:`malloc`.")
    assert "malloc" in out


def test_cpp_class_renders_as_code(render_text):
    out = _render(render_text, "Use :cpp:class:`std::vector`.")
    assert "std::vector" in out


def test_js_func_renders_as_code(render_text):
    out = _render(render_text, "Call :js:func:`document.getElementById`.")
    assert "document.getElementById" in out


def test_c_func_no_crash(make_visitor):
    rst = "Call :c:func:`malloc` to allocate."
    visitor = make_visitor(rst)
    assert visitor.renderables


def test_cpp_type_no_crash(make_visitor):
    rst = "Use :cpp:type:`size_t` for sizes."
    visitor = make_visitor(rst)
    assert visitor.renderables
