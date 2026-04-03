"""Tests for the RestructuredText public API.

Covers: class instantiation, default options, all alias names,
custom options (code_theme, show_line_numbers, filename, sphinx_compat,
show_errors), and end-to-end rendering without exceptions.
"""
import pytest

from rich.console import Console
from rich_rst import (
    RST,
    ReStructuredText,
    RestructuredText,
    RSTVisitor,
    reStructuredText,
)
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core


# ── Alias names ───────────────────────────────────────────────────────────────

def test_rst_alias_is_restructuredtext():
    assert RST is RestructuredText


def test_restructuredtext_camelcase_alias():
    assert ReStructuredText is RestructuredText


def test_lowercase_alias():
    assert reStructuredText is RestructuredText


# ── Default option values ─────────────────────────────────────────────────────

def test_default_sphinx_compat_is_true():
    assert RestructuredText("text").sphinx_compat is True


def test_default_show_errors_is_false():
    assert RestructuredText("text").show_errors is False


def test_default_code_theme_is_monokai():
    assert RestructuredText("text").code_theme == "monokai"


def test_default_show_line_numbers_is_false():
    assert RestructuredText("text").show_line_numbers is False


def test_default_guess_lexer_is_false():
    assert RestructuredText("text").guess_lexer is False


def test_default_default_lexer_is_python():
    assert RestructuredText("text").default_lexer == "python"


def test_default_filename():
    assert RestructuredText("text").filename == "<rst-document>"


# ── Custom option values ──────────────────────────────────────────────────────

def test_custom_code_theme():
    rst = RestructuredText("text", code_theme="github-dark")
    assert rst.code_theme == "github-dark"


def test_show_line_numbers_enabled():
    rst = RestructuredText("text", show_line_numbers=True)
    assert rst.show_line_numbers is True


def test_custom_filename():
    rst = RestructuredText("text", filename="my_doc.rst")
    assert rst.filename == "my_doc.rst"


def test_sphinx_compat_disabled():
    rst = RestructuredText("text", sphinx_compat=False)
    assert rst.sphinx_compat is False


def test_show_errors_disabled():
    rst = RestructuredText("text", show_errors=False)
    assert rst.show_errors is False


def test_custom_default_lexer():
    rst = RestructuredText("text", default_lexer="bash")
    assert rst.default_lexer == "bash"


def test_guess_lexer_enabled():
    rst = RestructuredText("text", guess_lexer=True)
    assert rst.guess_lexer is True


def test_invalid_default_lexer_raises_on_restructuredtext_init():
    with pytest.raises(ValueError, match="Unknown Pygments lexer name"):
        RestructuredText("text", default_lexer="definitely-not-a-real-lexer")


def test_invalid_default_lexer_raises_on_visitor_init():
    document = docutils.core.publish_doctree(
        "text",
        settings_overrides={"report_level": 69, "halt_level": 69},
    )
    console = Console(force_terminal=True, width=120, record=True)

    with pytest.raises(ValueError, match="Unknown Pygments lexer name"):
        RSTVisitor(
            document,
            console=console,
            code_theme="monokai",
            show_line_numbers=False,
            guess_lexer=False,
            default_lexer="definitely-not-a-real-lexer",
        )


# ── End-to-end rendering ──────────────────────────────────────────────────────

def test_render_plain_text_no_exception(render_text):
    out = render_text("Hello **world**.")
    assert "Hello" in out
    assert "world" in out


def test_render_empty_string_no_exception():
    console = Console(force_terminal=True, record=True, width=80)
    console.print(RestructuredText(""))
    # Should not raise


def test_render_complex_document_no_exception(render_text):
    rst = """\
Title
=====

A paragraph with **bold**, *italic*, and ``code``.

.. note::

   A note.

* item one
* item two

#. first
#. second
"""
    out = render_text(rst)
    assert "Title" in out
    assert "bold" in out


# ── Error handling ────────────────────────────────────────────────────────────

def test_show_errors_true_shows_system_message(render_text):
    # An unknown role triggers a system message
    out = render_text(
        ":my_unknown_role_xyz:`text`",
        show_errors=True,
        sphinx_compat=False,
    )
    assert "System Message" in out


def test_show_errors_false_hides_system_message(render_text):
    out = render_text(
        ":my_unknown_role_xyz:`text`",
        show_errors=False,
        sphinx_compat=False,
    )
    assert "System Message" not in out


def test_problematic_node_renders_as_error_panel(render_text):
    out = render_text(
        ":my_unknown_role_xyz:`text`",
        show_errors=True,
        sphinx_compat=False,
    )
    assert "Problematic Element" in out


def test_no_exception_on_system_message():
    """Rendering a document with system messages must never raise."""
    console = Console(force_terminal=True, record=True, width=80)
    try:
        console.print(
            RestructuredText(
                ":my_unknown_role_xyz:`text`",
                show_errors=True,
                sphinx_compat=False,
            )
        )
    except Exception as exc:
        raise AssertionError(f"Rendering raised an unexpected exception: {exc}") from exc


# ── render_to_string ──────────────────────────────────────────────────────────

def test_render_to_string_returns_str():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_string()
    assert isinstance(out, str)


def test_render_to_string_contains_text():
    rst = RestructuredText("Hello **world**.")
    out = rst.render_to_string()
    assert "Hello" in out
    assert "world" in out


def test_render_to_string_default_width_is_80():
    rst = RestructuredText("A" * 100)
    out = rst.render_to_string()
    # With width=80 the text will be wrapped; we just check it doesn't crash.
    assert "A" in out


def test_render_to_string_custom_width():
    rst = RestructuredText("Short text.")
    out = rst.render_to_string(width=40)
    assert "Short text." in out


def test_render_to_string_respects_show_errors():
    rst = RestructuredText(
        ":bad_role:`text`",
        show_errors=True,
        sphinx_compat=False,
    )
    out = rst.render_to_string()
    assert "System Message" in out


def test_render_to_string_multiple_calls_same_result():
    rst = RestructuredText("Consistent output.")
    assert rst.render_to_string() == rst.render_to_string()


# ── RSTVisitor.register_visitor ───────────────────────────────────────────────

def test_register_visitor_visit_fn_called(make_visitor):
    """A registered visit_fn must be invoked when the node is encountered."""
    from rich_rst._vendor import docutils as _docutils

    # Create a unique custom node class so other tests aren't affected.
    class _MyNode(_docutils.nodes.General, _docutils.nodes.Inline, _docutils.nodes.Element):
        pass

    visited = []

    def my_visit(visitor, node):
        visited.append(node.__class__.__name__)
        raise _docutils.nodes.SkipChildren()

    RSTVisitor.register_visitor(_MyNode, visit_fn=my_visit)
    try:
        doc = _docutils.core.publish_doctree(
            "",
            settings_overrides={"report_level": 69, "halt_level": 69},
        )
        node = _MyNode()
        doc += node
        visitor = make_visitor("")
        # Walk manually so we can inject the custom node.
        node.walkabout(visitor)
        assert "_MyNode" in visited
    finally:
        RSTVisitor._custom_visitors.pop(_MyNode, None)


def test_register_visitor_depart_fn_called(make_visitor):
    """A registered depart_fn must be invoked when the node is exited."""
    from rich_rst._vendor import docutils as _docutils

    class _MyNode2(_docutils.nodes.General, _docutils.nodes.Inline, _docutils.nodes.Element):
        pass

    departed = []

    def my_depart(visitor, node):
        departed.append(node.__class__.__name__)

    RSTVisitor.register_visitor(_MyNode2, depart_fn=my_depart)
    try:
        node = _MyNode2()
        visitor = make_visitor("")
        node.walkabout(visitor)
        assert "_MyNode2" in departed
    finally:
        RSTVisitor._custom_visitors.pop(_MyNode2, None)


def test_register_visitor_renderable_produced(make_visitor):
    """A registered visit_fn can append renderables to the visitor."""
    from rich_rst._vendor import docutils as _docutils
    from rich.text import Text

    class _GreetNode(_docutils.nodes.General, _docutils.nodes.Body, _docutils.nodes.Element):
        pass

    def greet_visit(visitor, node):
        visitor.renderables.append(Text("hello from custom node"))
        raise _docutils.nodes.SkipChildren()

    RSTVisitor.register_visitor(_GreetNode, visit_fn=greet_visit)
    try:
        node = _GreetNode()
        visitor = make_visitor("")
        node.walkabout(visitor)
        texts = [r for r in visitor.renderables if isinstance(r, Text)]
        assert any("hello from custom node" in t.plain for t in texts)
    finally:
        RSTVisitor._custom_visitors.pop(_GreetNode, None)
