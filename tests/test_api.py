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
    assert RestructuredText("text").log_errors is False


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
    assert rst.log_errors is False


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
