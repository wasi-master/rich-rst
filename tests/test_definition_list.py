import docutils.core
from rich.console import Console
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
