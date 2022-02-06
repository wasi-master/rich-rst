"""
reStructuredText parser for rich

Initial few lines gotten from: https://github.com/willmcgugan/rich/discussions/1263#discussioncomment-808898
There are a lot of improvements are added by me
"""

# Imports from docutils package for the parsing
from typing import Optional, Union
import docutils.io
import docutils.nodes
import docutils.parsers.rst
import docutils.utils

# Imports from the rich package for the printing
import rich
from rich import box
from rich.align import Align
from rich.console import Console, ConsoleOptions, RenderResult
from rich.jupyter import JupyterMixin
from rich.panel import Panel
from rich.style import Style
from rich.syntax import Syntax, SyntaxTheme
from rich.text import Text
from rich.traceback import install
from rich.rule import Rule

__all__ = ("RST", "ReStructuredText", "reStructuredText", "RestructuredText")
__author__ = "Arian Mollik Wasi (aka. Wasi Master)"
__version__ = "0.2.5"

install(show_locals=True)

# pylama:ignore=D,C0116
class RSTVisitor(docutils.nodes.SparseNodeVisitor):
    """A visitor that produces rich renderables"""

    def __init__(
        self,
        document: docutils.nodes.document,
        console: Console,
        code_theme: Union[str, SyntaxTheme] = "monokai",
    ) -> None:
        super().__init__(document)
        self.console = console
        self.code_theme = code_theme
        self.renderables = []
        self.supercript = str.maketrans("1234567890", "¹²³⁴⁵⁶⁷⁸⁹⁰")
        self.subscript = str.maketrans("1234567890", "₁₂₃₄₅₆₇₈₉₀")
        self.errors = []

    def visit_paragraph(self, node):
        if hasattr(node, "parent") and isinstance(node.parent, docutils.nodes.system_message):
            self.visit_system_message(node.parent)

    def depart_paragraph(self, node):  # pylint: disable=unused-argument
        self.renderables.append(Text("\n"))

    def visit_title(self, node):
        style = self.console.get_style("restructuredtext.title", default="bold")
        self.renderables.append(Panel(Align(node.astext(), "center"), box=box.DOUBLE, style=style))
        raise docutils.nodes.SkipChildren()

    def visit_Text(self, node):
        style = self.console.get_style("restructuredtext.text", default="none")
        self.renderables.append(Text(node.astext(), end="", style=style))

    def visit_comment(self, node):
        raise docutils.nodes.SkipChildren()

    def visit_admonition(self, node):
        style = self.console.get_style("restructuredtext.admonition", default="bold white")
        self.renderables.append(Text("Attention: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_attention(self, node):
        style = self.console.get_style("restructuredtext.attention", default="bold black on yellow")
        self.renderables.append(Text("Attention: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_caution(self, node):
        style = self.console.get_style("restructuredtext.caution", default="white on red")
        self.renderables.append(Text("Caution: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_danger(self, node):
        style = self.console.get_style("restructuredtext.danger", default="bold white on red")
        self.renderables.append(Text("DANGER: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_error(self, node):
        style = self.console.get_style("restructuredtext.error", default="bold red")
        self.renderables.append(Text("ERROR: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_hint(self, node):
        style = self.console.get_style("restructuredtext.hint", default="yellow")
        self.renderables.append(Text("Hint: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_important(self, node):
        style = self.console.get_style("restructuredtext.important", default="bold blue")
        self.renderables.append(Text("IMPORTANT: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_note(self, node):
        style = self.console.get_style("restructuredtext.note", default="bold white")
        self.renderables.append(Text("Note: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_tip(self, node):
        style = self.console.get_style("restructuredtext.tip", default="bold green")
        self.renderables.append(Text("Tip: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_warning(self, node):
        style = self.console.get_style("restructuredtext.warning", default="bold yellow")
        self.renderables.append(Text("Warning: " + node.rawsource.strip(), style=style))
        raise docutils.nodes.SkipChildren()

    def visit_subscript(self, node):
        style = self.console.get_style("restructuredtext.subscript", default="none")
        self.renderables.append(Text(node.astext().translate(self.subscript), end="", style=style))
        raise docutils.nodes.SkipChildren()

    def visit_superscript(self, node):
        style = self.console.get_style("restructuredtext.superscript", default="none")
        self.renderables.append(Text(node.astext().translate(self.supercript), end="", style=style))
        raise docutils.nodes.SkipChildren()

    def visit_emphasis(self, node):
        style = self.console.get_style("restructuredtext.emphasis", default="italic")
        self.renderables.append(Text(node.astext(), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_strong(self, node):
        style = self.console.get_style("restructuredtext.strong", default="bold")
        self.renderables.append(Text(node.astext(), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_image(self, node):
        alt, target = None, None
        if ":target:" in node.rawsource:
            target = node.rawsource.split(":target:")[-1].strip()
        if ":alt:" in node.rawsource:
            alt = node.rawsource.split(":alt:")[-1].strip()
        self.renderables.append(
            Text("🌆 ")
            + Text(
                node.get("alt", alt or "Image"),
                style=Style(
                    link=node.get("target", target or "Image") or node.get("uri"),
                    color="#6088ff",
                ),
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_bullet_list(self, node):
        # Currently as it stands, this isn't gonna work with more than 3 nested levels
        # TODO: I need to figure out some way to handle nested lists recursively
        marker_style = self.console.get_style("restructuredtext.bullet_list_marker", default="bold yellow")
        text_style = self.console.get_style("restructuredtext.bullet_list_text", default="none")
        for list_item in node.children:
            nested_list = [i for i in list_item.children if isinstance(i, docutils.nodes.bullet_list)]
            if nested_list:
                for list_item in list_item.children:
                    self.renderables.append(Text("  ", end="") + Text(" ∘ ", end="", style=marker_style))
                    self.renderables.append(Text(list_item.astext(), style=text_style))
                    if isinstance(list_item, docutils.nodes.bullet_list):
                        for list_item in list_item.children:
                            self.renderables.append(Text("    ", end="") + Text(" ▪ ", end="", style=marker_style))
                            self.renderables.append(Text(list_item.astext(), style=text_style))
            self.renderables.append(Text(" • ", end="", style=marker_style))
            self.renderables.append(Text(list_item.astext(), style=text_style))
        self.renderables.append(Text())
        raise docutils.nodes.SkipChildren()

    def visit_enumerated_list(self, node):
        marker_style = self.console.get_style("restructuredtext.enumerated_list_marker", default="none")
        text_style = self.console.get_style("restructuredtext.enumerated_text", default="none")
        for i, list_item in enumerate(node.children, 1):
            self.renderables.append(Text(f" {i}.", end=" ", style=marker_style))
            self.renderables.append(Text(list_item.astext(), style=text_style))

        self.renderables.append(Text())
        raise docutils.nodes.SkipChildren()

    def visit_literal(self, node):
        style = self.console.get_style("restructuredtext.inline_codeblock", default="grey78 on grey7")
        self.renderables.append(Text(node.astext(), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_literal_block(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        lexer = node["classes"][1] if len(node["classes"]) >= 2 else "python"
        self.renderables.append(
            Panel(
                Syntax(node.astext(), lexer, theme=self.code_theme),
                border_style=style,
                box=box.SQUARE,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_system_message(self, node):
        self.errors.append(node.parent)
        raise docutils.nodes.SkipChildren()

    def visit_field(self, node):
        border_style = self.console.get_style("restructuredtext.field_border", default="grey74")
        text_style = self.console.get_style("restructuredtext.field_text", default="none")
        self.renderables.append(
            Panel(
                Text(node.children[1].astext(), style=text_style),
                title=node.children[0].astext(),
                expand=False,
                border_style=border_style,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_definition_list(self, node):
        term_style = self.console.get_style("restructuredtext.term_style", default="none")
        classifier_style = self.console.get_style("restructuredtext.classifier_style", default="cyan")
        definitions_style = self.console.get_style("restructuredtext.definitions_style", default="none")
        for child in node.children:
            rich.inspect(child)
            term, classifier, definitions = child.children
            self.renderables.append(
                Text(term.astext(), style=term_style, end="")
                + Text(" : ", end="")
                + Text(classifier.astext(), style=classifier_style)
                + Text("\n  ", end="")
                + Text(definitions.astext(), style=definitions_style)
                + Text("\n", end="")
            )
        raise docutils.nodes.SkipChildren()

    def visit_option_list(self, node):
        option_string_style = self.console.get_style("restructuredtext.option_string", default="none")
        option_argument_style = self.console.get_style("restructuredtext.option_argument", default="none")
        option_child_text_separator_style = self.console.get_style(
            "restructuredtext.option_child_text_separator", default="none"
        )
        option_description_style = self.console.get_style("restructuredtext.option_description", default="none")
        for option_list_item in node.children:
            option_group, description = option_list_item.children
            # option_group.child_text_separator.join(map(lambda x: x.astext(), option_group.children)))
            option_text = Text(end="")
            for option in option_group.children:
                try:
                    option_string, option_argument = option.children
                except ValueError:
                    option_string, option_argument = option.children[0], None
                option_text += (
                    Text(option_string.astext(), style=option_string_style)
                    + (Text(option_argument.astext(), style=option_argument_style) if option_argument else Text())
                    + (
                        Text(option_group.child_text_separator, style=option_child_text_separator_style)
                        if len(option_group.children) > 1
                        else ""
                    )
                )
            if description:
                option_text += Text("\n    ")
                option_text += Text(description.astext(), style=option_description_style)
            self.renderables.append(option_text + Text("\n"))
        raise docutils.nodes.SkipChildren()

    def visit_doctest_block(self, node):
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        self.renderables.append(
            Panel(
                Syntax(node.astext(), "python", theme=self.code_theme),
                border_style=style,
                box=box.SQUARE,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_block_quote(self, node):
        text_style = self.console.get_style("restructuredtext.blockquote_text", default="white")
        marker_style = self.console.get_style(
            "restructuredtext.blockquote_attribution_marker", default="bright_magenta"
        )
        author_style = self.console.get_style("restructuredtext.blockquote_attribution_text", default="grey89")
        paragraph, attribution = node.children
        self.renderables.append(
            Text("▌ ", style=marker_style)
            + Text(paragraph.astext(), style=text_style)
            + Text("\n")
            + Text("  - " + attribution.astext(), style=author_style)
        )
        raise docutils.nodes.SkipChildren()

    def visit_line_block(self, node):
        for line in node.children:
            self.renderables.append(Text(line.astext()))
        raise docutils.nodes.SkipChildren()

    def visit_sidebar(self, node):
        rich.inspect(node)
        if len(node.children) > 2:
            title, subtitle, paragraph = node.children
        else:
            title, subtitle, paragraph = node.children[0], "", node.children[1]

        self.renderables.append(
            Panel(paragraph.astext(), title=title.astext(), subtitle=subtitle.astext(), expand=False)
        )

        raise docutils.nodes.SkipChildren()

    def visit_transition(self, node):
        style = self.console.get_style("restructuredtext.hr", default="yellow")
        self.renderables.append(Rule(style=style))


class RestructuredText(JupyterMixin):
    """A reStructuredText renderable for rich."""

    def __init__(
        self,
        markup: str,
        code_theme: Optional[Union[str, SyntaxTheme]] = "monokai",
        show_errors: Optional[bool] =True,
    ) -> None:
        """A reStructuredText renderable for rich.

        Parameters
        ----------
        markup : str
            A string containing reStructuredText markup.
        code_theme : Optional[Union[str, SyntaxTheme]]
            Pygments theme for code blocks. Defaults to "monokai".
        show_errors : Optional[bool]
            Whether to show system_messages aka errors and warnings.
        """
        self.markup = markup
        self.code_theme = code_theme
        self.log_errors = show_errors

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        # Parse the `markup` into a RST `document`.
        option_parser = docutils.frontend.OptionParser(components=(docutils.parsers.rst.Parser,))
        settings = option_parser.get_default_values()
        source = docutils.io.StringInput(self.markup)
        document = docutils.utils.new_document(source.source_path, settings)
        rst_parser = docutils.parsers.rst.Parser()
        rst_parser.parse(source.read(), document)

        # Render the RST `document` using Rich.
        visitor = RSTVisitor(document, console=console, code_theme=self.code_theme)
        document.walkabout(visitor)

        for renderable in visitor.renderables:
            yield from console.render(renderable, options)
        if self.log_errors and visitor.errors:
            for error in visitor.errors:
                yield from console.render(
                    Panel(
                        console.render_str(error.astext()),
                        title=f"System Message: {error.attributes['type']}/{error.attributes['level']} ({error.attributes['source']}, line {error.attributes['line']});",
                        border_style={"INFO": "bold cyan", "WARNING": "bold yellow", "ERROR": "bold red"}[
                            error.attributes["type"]
                        ],
                    ),
                    options,
                )


RST = ReStructuredText = reStructuredText = RestructuredText
