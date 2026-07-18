"""The public RestructuredText renderable."""
from typing import Literal, Optional, Union

# Imports from the rich package for the printing
from rich import box
from rich.console import Console, ConsoleOptions, Group, NewLine, RenderResult
from rich.jupyter import JupyterMixin
from rich.panel import Panel
from rich.syntax import SyntaxTheme
from rich.terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme
from rich.text import Text

# Imports from rich_rst._vendor.docutils package for the parsing
import rich_rst._vendor.docutils.core
import rich_rst._vendor.docutils.parsers.rst.directives  # noqa: F401
from rich_rst._directives import _ParsedLiteralDirective, _register_sphinx_directives
from rich_rst._roles import _register_sphinx_roles
from rich_rst._utils import _validate_default_lexer_name
from rich_rst._vendor import docutils
from rich_rst._visitor import RSTVisitor


class RestructuredText(JupyterMixin):
    """A reStructuredText renderable for rich.

    Parameters
    ----------
    markup : str
        A string containing reStructuredText markup.
    code_theme : Optional[Union[str, SyntaxTheme]]
        Pygments theme for code blocks. Defaults to "monokai".
    show_line_numbers : Optional[bool]
        Whether to display line numbers for syntax-highlighted code blocks.
    show_errors : Optional[bool]
        Whether to show system_messages aka errors and warnings.
    guess_lexer : Optional[bool]
        Whether to guess lexers for code blocks without specified language.
    default_lexer : Optional[str]
        Which lexer to use if no lexer is guessed or found. Defaults to "python"
    sphinx_compat : Optional[bool]
        Enable compatibility with Sphinx roles (func, meth, class, etc.) commonly used in
        Python docstrings. When enabled, these roles render as inline code instead of errors.
        Defaults to True for better compatibility with Python documentation.
    filename : Optional[str]
        A file name to use for error messages, useful for debugging purposes. Defaults to "<rst-document>"
    admonition_style : str
        How admonition directives (``note``, ``warning``, ``versionadded``, etc.) render.
        ``"panel"`` (default) emits a bordered Rich :class:`~rich.panel.Panel` per directive.
        ``"compact"`` collapses each directive to a styled inline title prefix, making the
        output suitable for narrow contexts such as CLI ``--help`` panels.
    """

    def __init__(
        self,
        markup: str,
        code_theme: Optional[Union[str, SyntaxTheme]] = "monokai",
        show_line_numbers: Optional[bool] = False,
        show_errors: Optional[bool] = False,
        guess_lexer: Optional[bool] = False,
        default_lexer: Optional[str] = "python",
        sphinx_compat: Optional[bool] = True,
        filename: Optional[str] = "<rst-document>",
        admonition_style: Literal["panel", "compact"] = "panel",
    ) -> None:
        if admonition_style not in ("panel", "compact"):
            raise ValueError(
                f"admonition_style must be 'panel' or 'compact', got {admonition_style!r}"
            )
        self.markup: str = markup
        self.code_theme: Optional[Union[str, SyntaxTheme]] = code_theme
        self.show_line_numbers: Optional[bool] = show_line_numbers
        self.show_errors: Optional[bool] = show_errors
        self.guess_lexer: Optional[bool] = guess_lexer
        self.default_lexer: Optional[str] = _validate_default_lexer_name(default_lexer)
        self.sphinx_compat: Optional[bool] = sphinx_compat
        self.filename: Optional[str] = filename
        self.admonition_style: Literal["panel", "compact"] = admonition_style

    def render_to_string(self, width: Optional[int] = None, *, force_terminal: bool = False) -> str:
        """Render the RST markup to a plain string.

        This is a convenience wrapper around the full rich rendering pipeline.
        All options passed to the constructor (code theme, show_errors, etc.)
        are respected.

        Parameters
        ----------
        width : int, optional
            Output width in columns.  Defaults to 80 when not specified.
        force_terminal : bool, optional
            When ``True`` the console is created with ``force_terminal=True``,
            which enables ANSI styles in the exported text.  Defaults to
            ``False`` so that the plain-text output is style-free by default.

        Returns
        -------
        str
            The rendered markup as a plain string.
        """
        console = Console(
            width=width or 80,
            force_terminal=force_terminal,
            record=True,
        )
        console.print(self)
        return console.export_text()

    def render_to_html(
        self,
        width: Optional[int] = None,
        *,
        theme: Optional[TerminalTheme] = None,
    ) -> str:
        """Render the RST markup to an HTML string.

        Parameters
        ----------
        width : int, optional
            Output width in columns.  Defaults to 80.
        theme : rich.terminal_theme.TerminalTheme, optional
            The colour theme to use for the HTML export.  Defaults to
            ``DEFAULT_TERMINAL_THEME`` from :mod:`rich.terminal_theme`.

        Returns
        -------
        str
            A self-contained HTML document.
        """
        console = Console(width=width or 80, force_terminal=True, record=True)
        console.print(self)
        return console.export_html(theme=theme or DEFAULT_TERMINAL_THEME)

    def render_to_svg(
        self,
        width: Optional[int] = None,
        *,
        title: str = "",
    ) -> str:
        """Render the RST markup to an SVG string.

        Parameters
        ----------
        width : int, optional
            Output width in columns.  Defaults to 80.
        title : str, optional
            Title shown in the SVG image header.  Defaults to an empty string.

        Returns
        -------
        str
            An SVG document as a string.
        """
        console = Console(width=width or 80, force_terminal=True, record=True)
        console.print(self)
        return console.export_svg(title=title)

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        if self.sphinx_compat:
            _register_sphinx_roles()
            _register_sphinx_directives()

        docutils.parsers.rst.directives.register_directive('parsed-literal', _ParsedLiteralDirective)

        # Use the full docutils publish pipeline so that all standard transforms
        # (substitution resolution, hyperlink resolution, footnote numbering,
        # bibliographic-field promotion, …) are applied before we walk the tree.
        markup = self.markup
        if "|page|" in markup and ".. |page|" not in markup:
            markup += "\n\n.. |page| replace:: 1\n"

        document = docutils.core.publish_doctree(
            markup,
            source_path=self.filename,
            settings_overrides={"report_level": 69, "halt_level": 69},
        )

        # Render the RST `document` using Rich.
        visitor = RSTVisitor(
            document,
            console=console,
            code_theme=self.code_theme or "monokai",
            show_line_numbers=self.show_line_numbers,
            guess_lexer=self.guess_lexer,
            default_lexer=self.default_lexer,
            admonition_style=self.admonition_style,
        )
        document.walkabout(visitor)

        # Strip all trailing newlines and newline-like rich objects
        while visitor.renderables:
            if isinstance(visitor.renderables[-1], Text):
                visitor.renderables[-1].rstrip()
                visitor.renderables[-1].end = "\n"
                if visitor.renderables[-1]:  # The Text object still contains data.
                    break
                else:
                    visitor.renderables.pop()
            elif isinstance(visitor.renderables[-1], NewLine):
                visitor.renderables.pop()
            else:
                break

        for renderable in visitor.renderables:
            # Move trailing "\n"s from Text content into ``end``. Otherwise a
            # paragraph stored as ``Text("X\n\n", end="")`` renders to three
            # padded lines under ``options.justify == "left"`` — the content
            # plus two phantom blank-padded rows — and the trailing padded
            # blank fuses onto the next renderable's first row, breaking
            # callers like cyclopts' help-cell layout. Visible output is
            # identical when trailing newlines live in ``end`` instead.
            if isinstance(renderable, Text):
                plain = renderable.plain
                if plain.endswith("\n"):
                    stripped = plain.rstrip("\n")
                    trailing = plain[len(stripped):]
                    fixed = renderable.copy()
                    fixed.rstrip()
                    fixed.end = trailing + fixed.end
                    renderable = fixed
            yield from console.render(renderable, options)
        if self.show_errors and visitor.errors:
            for error in visitor.errors:
                yield from console.render(error, options)

        citation_style = console.get_style("restructuredtext.citation", default="none")
        citation_border_style = console.get_style("restructuredtext.citation_border", default="grey74")
        if visitor.citations:
            yield from console.render(
                Panel(Group(*visitor.citations), title="citation", box=box.SQUARE, border_style=citation_border_style, style=citation_style)
            )

        style = console.get_style("restructuredtext.footer", default="none")
        border_style = console.get_style("restructuredtext.footer_border", default="grey74")
        if visitor.footer:
            yield from console.render(
                Panel(Group(*visitor.footer), title="Footer", box=box.SQUARE, border_style=border_style, style=style)
            )


RST = reST = ReStructuredText = reStructuredText = RestructuredText
