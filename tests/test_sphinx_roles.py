"""Tests for Sphinx-specific interpreted-text roles.

rich-rst registers Sphinx roles (``func``, ``class``, ``meth``, etc.)
so that Python docstrings render cleanly instead of showing system-message
errors.  Each role is tested in isolation.

Formatting contract
-------------------
When a Sphinx role appears **in a sentence** (not as the only content of a
paragraph), the role text is rendered with a ``grey78-on-grey7`` span — the
same code/literal styling used for ``\`\`inline code\`\```.

When a Sphinx role appears standalone (the entire paragraph), the base
style of the ``Text`` object carries the grey78/grey7 colours.

When the ``display name <target>`` syntax is used, only the display name
appears; the target identifier is omitted from the output.
"""
import pytest
from rich.text import Text

from rich_rst import _register_sphinx_roles
from rich.console import Console
from rich_rst import _register_sphinx_directives, _register_sphinx_roles
from rich_rst import RestructuredText


@pytest.fixture(autouse=True)
def ensure_sphinx_roles():
    """Register Sphinx roles once before any test in this module runs."""
    _register_sphinx_roles()


def _get_text(make_visitor, rst, **kw):
    visitor = make_visitor(rst, **kw)
    return next(r for r in visitor.renderables if isinstance(r, Text))


def _code_spans(t):
    return [
        s for s in t._spans
        if s.style.color and s.style.color.name == "grey78"
        and s.style.bgcolor and s.style.bgcolor.name == "grey7"
    ]


# ── Sphinx role in-sentence produces grey78-on-grey7 span ────────────────────

def test_func_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Call :func:`os.path.join` to join paths.")
    spans = _code_spans(t)
    assert spans, ":func: in sentence must produce a grey78-on-grey7 span"
    assert t.plain[spans[0].start : spans[0].end] == "os.path.join"


def test_class_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Use :class:`pathlib.Path` for paths.")
    spans = _code_spans(t)
    assert spans, ":class: in sentence must produce a grey78-on-grey7 span"
    assert t.plain[spans[0].start : spans[0].end] == "pathlib.Path"


def test_meth_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Call :meth:`str.format` on strings.")
    spans = _code_spans(t)
    assert spans, ":meth: in sentence must produce a grey78-on-grey7 span"
    assert t.plain[spans[0].start : spans[0].end] == "str.format"


def test_mod_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Import :mod:`collections.abc` first.")
    spans = _code_spans(t)
    assert spans, ":mod: in sentence must produce a grey78-on-grey7 span"


def test_attr_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Access :attr:`object.__name__` for the name.")
    spans = _code_spans(t)
    assert spans, ":attr: in sentence must produce a grey78-on-grey7 span"


def test_exc_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Raises :exc:`ValueError` on bad input.")
    spans = _code_spans(t)
    assert spans, ":exc: in sentence must produce a grey78-on-grey7 span"


# ── Explicit-title (display-name) syntax ─────────────────────────────────────

def test_func_role_explicit_title_span_covers_display_name(make_visitor):
    t = _get_text(make_visitor, "Call :func:`custom name <os.path.join>` here.")
    spans = _code_spans(t)
    assert spans, "Explicit-title :func: must produce a code span"
    marked = t.plain[spans[0].start : spans[0].end]
    assert marked == "custom name", (
        f"Code span must cover the display name 'custom name', got {marked!r}"
    )


def test_func_role_explicit_title_target_not_in_plain(make_visitor):
    t = _get_text(make_visitor, "Call :func:`custom name <os.path.join>` here.")
    assert "os.path.join" not in t.plain, (
        "Target identifier must not appear in the plain text"
    )


def test_class_role_explicit_title_shows_display_name(make_visitor):
    t = _get_text(make_visitor, "Use :class:`MyPath <pathlib.Path>` here.")
    spans = _code_spans(t)
    assert spans
    assert t.plain[spans[0].start : spans[0].end] == "MyPath"
    assert "pathlib.Path" not in t.plain


def test_meth_role_explicit_title_shows_display_name(make_visitor):
    t = _get_text(make_visitor, "Call :meth:`format method <str.format>` here.")
    spans = _code_spans(t)
    assert spans
    assert t.plain[spans[0].start : spans[0].end] == "format method"
    assert "str.format" not in t.plain


# ── Core Sphinx domain roles produce the role text ────────────────────────────

def test_func_role_content_in_output(render_text):
    assert "os.path.join" in render_text(":func:`os.path.join`", sphinx_compat=True)

def test_meth_role_content_in_output(render_text):
    assert "str.format" in render_text(":meth:`str.format`", sphinx_compat=True)

def test_class_role_content_in_output(render_text):
    assert "pathlib.Path" in render_text(":class:`pathlib.Path`", sphinx_compat=True)

def test_mod_role_content_in_output(render_text):
    assert "collections.abc" in render_text(":mod:`collections.abc`", sphinx_compat=True)

def test_attr_role_content_in_output(render_text):
    assert "object.__name__" in render_text(":attr:`object.__name__`", sphinx_compat=True)

def test_obj_role_content_in_output(render_text):
    assert "sys.stdout" in render_text(":obj:`sys.stdout`", sphinx_compat=True)

def test_data_role_content_in_output(render_text):
    assert "sys.maxsize" in render_text(":data:`sys.maxsize`", sphinx_compat=True)

def test_exc_role_content_in_output(render_text):
    assert "ValueError" in render_text(":exc:`ValueError`", sphinx_compat=True)

def test_const_role_content_in_output(render_text):
    assert "MAX_SIZE" in render_text(":const:`MAX_SIZE`", sphinx_compat=True)

def test_var_role_content_in_output(render_text):
    assert "my_var" in render_text(":var:`my_var`", sphinx_compat=True)

def test_type_role_content_in_output(render_text):
    assert "int" in render_text(":type:`int`", sphinx_compat=True)


# ── Python domain prefix roles ────────────────────────────────────────────────

def test_py_func_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Use :py:func:`open` to read files.")
    spans = _code_spans(t)
    assert spans, ":py:func: in sentence must produce a code span"
    assert t.plain[spans[0].start : spans[0].end] == "open"


def test_py_class_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Return :py:class:`dict` value.")
    spans = _code_spans(t)
    assert spans
    assert t.plain[spans[0].start : spans[0].end] == "dict"


def test_py_meth_role_in_sentence_has_code_span(make_visitor):
    t = _get_text(make_visitor, "Call :py:meth:`list.append` method.")
    spans = _code_spans(t)
    assert spans
    assert t.plain[spans[0].start : spans[0].end] == "list.append"


def test_py_mod_role_content_in_output(render_text):
    assert "os.path" in render_text(":py:mod:`os.path`", sphinx_compat=True)

def test_py_exc_role_content_in_output(render_text):
    assert "KeyError" in render_text(":py:exc:`KeyError`", sphinx_compat=True)


# ── Mixed paragraph with Sphinx roles ─────────────────────────────────────────

def test_sphinx_roles_in_mixed_paragraph_all_styled(make_visitor):
    rst = (
        "This has :func:`function_call` and **bold text** "
        "and ``regular code`` together."
    )
    t = _get_text(make_visitor, rst)
    code_spans = _code_spans(t)
    bold_spans = [s for s in t._spans if s.style.bold]
    # The func role and ``regular code`` both produce code spans
    assert len(code_spans) >= 2, "Both :func: and ``code`` must produce code spans"
    assert bold_spans, "**bold text** must produce a bold span"
    # Verify content of the first code span (func role)
    func_span_texts = [t.plain[s.start:s.end] for s in code_spans]
    assert "function_call" in func_span_texts


# ── sphinx_compat=False behaviour ─────────────────────────────────────────────

def test_unknown_role_shows_system_message(render_text):
    out = render_text(
        ":my_completely_unknown_role_xyz:`text`",
        sphinx_compat=False,
        show_errors=True,
    )
    assert "System Message" in out


def test_unknown_role_no_crash_when_errors_hidden(render_text):
    out = render_text(
        ":my_completely_unknown_role_xyz:`text`",
        sphinx_compat=False,
        show_errors=False,
    )
    assert isinstance(out, str)

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


def test_pep_role_url_not_in_output(render_text):
    out = _render(render_text, "See :pep:`484`.")
    assert "peps.python.org" not in out


def test_pep_role_zero_padded_url_not_in_output(render_text):
    out = _render(render_text, "See :pep:`8`.")
    assert "pep-0008" not in out


# ── :rfc: ─────────────────────────────────────────────────────────────────────

def test_rfc_role_text_in_output(render_text):
    out = _render(render_text, "See :rfc:`2822`.")
    assert "RFC 2822" in out


def test_rfc_role_url_not_in_output(render_text):
    out = _render(render_text, "See :rfc:`2822`.")
    assert "datatracker.ietf.org" not in out


# ── :command: / :program: ─────────────────────────────────────────────────────

def test_command_role_text_in_output(render_text):
    out = _render(render_text, "Run :command:`git status`.")
    assert "git status" in out


def test_program_role_text_in_output(render_text):
    out = _render(render_text, "Use :program:`python`.")
    assert "python" in out


def test_program_role_does_not_bold_following_text():
    console = Console(force_terminal=True, width=120, record=True)
    console.print(RestructuredText(":program:`git` is a distributed version control system.", sphinx_compat=True))
    out = console.export_text(styles=True)
    assert "\x1b[1mgit\x1b[0m" in out
    assert "\x1b[1;39;49m is a distributed version control system." not in out


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


@pytest.mark.parametrize(
    "rst, token",
    [
        ("Call :c:function:`initialize_system` uses MAX_BUFFER_SIZE.", "initialize_system"),
        ("Use :cpp:function:`maximum` for std::uint64_t values.", "maximum"),
        ("Run :js:method:`Cache.set` then :js:method:`Cache.get`.", "Cache.set"),
        ("Module reference: :js:module:`analytics.core`", "analytics.core"),
        ("Function reference: :js:function:`calculateMean`", "calculateMean"),
        ("Method reference: :js:method:`UserManager.authenticate`", "UserManager.authenticate"),
        ("Attribute reference: :js:attribute:`UserManager.activeUser`", "UserManager.activeUser"),
    ],
)
def test_long_form_c_cpp_and_js_roles_render_as_inline_code(render_text, rst, token):
    out = _render(render_text, rst)
    assert token in out


def test_mixed_language_role_flow_renders_without_errors(render_text):
    rst = (
        "1. :js:function:`parseConfiguration`\n"
        "2. :c:function:`initialize_system`\n"
        "3. :cpp:function:`add`\n"
        "4. :c:function:`shutdown_system`\n"
    )
    out = _render(render_text, rst)
    assert "parseConfiguration" in out
    assert "initialize_system" in out
    assert "add" in out
    assert "shutdown_system" in out


def test_c_func_no_crash(make_visitor):
    rst = "Call :c:func:`malloc` to allocate."
    visitor = make_visitor(rst)
    assert visitor.renderables


def test_cpp_type_no_crash(make_visitor):
    rst = "Use :cpp:type:`size_t` for sizes."
    visitor = make_visitor(rst)
    assert visitor.renderables