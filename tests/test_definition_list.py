from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core
from rich.console import Console
from rich.theme import Theme
from rich.text import Text

from rich_rst import RSTVisitor


def test_plain_definition_list_uses_term_style_branch():
    document = docutils.core.publish_doctree("term\n    definition\n")
    visitor = RSTVisitor(
        document,
        console=Console(force_terminal=True, record=True),
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    assert len(visitor.renderables) == 1
    renderable = visitor.renderables[0]
    assert isinstance(renderable, Text)
    assert renderable.plain == "term\n    definition\n      "
    assert renderable.spans == []


def test_definition_list_term_uses_term_style_not_classifier_style():
    document = docutils.core.publish_doctree("term\n    definition\n")
    console = Console(
        force_terminal=True,
        record=True,
        theme=Theme(
            {
                "restructuredtext.term_style": "green",
                "restructuredtext.classifier_style": "red",
            }
        ),
    )
    visitor = RSTVisitor(
        document,
        console=console,
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    assert len(visitor.renderables) == 1
    renderable = visitor.renderables[0]
    assert isinstance(renderable, Text)

    for index in range(len("term")):
        style = renderable.get_style_at_offset(console, index)
        assert style.color is not None
        assert style.color.name == "green"


def test_definition_list_item_with_only_term_child_does_not_crash():
    document = docutils.core.publish_doctree("")
    definition_list = docutils.nodes.definition_list()
    definition_list_item = docutils.nodes.definition_list_item()
    definition_list_item += docutils.nodes.term(text="term-only")
    definition_list += definition_list_item
    document += definition_list

    visitor = RSTVisitor(
        document,
        console=Console(force_terminal=True, record=True),
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )

    document.walkabout(visitor)

    assert len(visitor.renderables) == 1
    renderable = visitor.renderables[0]
    assert isinstance(renderable, Text)
    assert renderable.plain == "term-only\n"
