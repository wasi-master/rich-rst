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

    # The term + definition are both visible in the output.
    all_plain = "".join(
        r.plain for r in visitor.renderables if isinstance(r, Text)
    )
    assert "term" in all_plain
    assert "definition" in all_plain


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

    # Find the Text renderable that contains the term.
    term_texts = [r for r in visitor.renderables if isinstance(r, Text) and "term" in r.plain]
    assert term_texts, "A Text renderable containing 'term' must exist"

    renderable = term_texts[0]
    term_start = renderable.plain.index("term")
    for index in range(term_start, term_start + len("term")):
        style = renderable.get_style_at_offset(console, index)
        assert style.color is not None, f"Expected green at offset {index}"
        assert style.color.name == "green", f"Expected green at offset {index}, got {style.color.name}"


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

    term_texts = [r for r in visitor.renderables if isinstance(r, Text) and "term-only" in r.plain]
    assert term_texts, "A Text renderable containing the term must exist"


def test_definition_list_classifier_indentation(render_text):
    rst = """\
term : string
    A string-typed term.

count : int
    An integer count.
"""

    out = render_text(rst)
    non_empty_lines = [line.rstrip() for line in out.splitlines() if line.strip()]

    assert non_empty_lines[0] == "term : string"
    assert non_empty_lines[1] == "    A string-typed term."
    assert non_empty_lines[2] == "count : int"
    assert non_empty_lines[3] == "    An integer count."
