"""
Shared pytest fixtures for the rich-rst test suite.

``make_visitor``
    Parses RST text via docutils (full transform pipeline) and returns a
    walked :class:`RSTVisitor`.  Use this for structural assertions
    (renderable types, panel titles, span counts, …).

``render_text``
    Renders RST markup through the public :class:`RestructuredText` API and
    returns the exported plain text.  Use this for content / output assertions.
"""
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core
import pytest
from rich.console import Console

from rich_rst import RestructuredText, RSTVisitor


@pytest.fixture
def make_visitor():
    """Factory fixture: parse RST and return a walked RSTVisitor."""
    def _make(rst_text, **kwargs):
        document = docutils.core.publish_doctree(
            rst_text,
            settings_overrides={"report_level": 69, "halt_level": 69},
        )
        console = Console(force_terminal=True, width=120, record=True)
        visitor = RSTVisitor(
            document,
            console=console,
            code_theme="monokai",
            show_line_numbers=False,
            guess_lexer=False,
            default_lexer="python",
            **kwargs,
        )
        document.walkabout(visitor)
        return visitor

    return _make


@pytest.fixture
def render_text():
    """Factory fixture: render RST markup and return plain text output."""
    def _render(markup, **kwargs):
        console = Console(force_terminal=True, width=120, record=True)
        console.print(RestructuredText(markup, **kwargs))
        return console.export_text()

    return _render
