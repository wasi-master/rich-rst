import pytest
from rich_rst import RestructuredText
from pathlib import Path
from rich.console import Console
from rich.terminal_theme import TerminalTheme

test_vectors_path = Path("tests/test_vectors")
rst_paths = sorted(str(x) for x in test_vectors_path.glob("*.rst"))


def render_to_html(rst):
    DRACULA_TERMINAL_THEME = TerminalTheme(
        (40, 42, 54),
        (248, 248, 242),
        [
            (40, 42, 54),
            (255, 85, 85),
            (80, 250, 123),
            (241, 250, 140),
            (189, 147, 249),
            (255, 121, 198),
            (139, 233, 253),
            (255, 255, 255),
        ],
        [
            (40, 42, 54),
            (255, 85, 85),
            (80, 250, 123),
            (241, 250, 140),
            (189, 147, 249),
            (255, 121, 198),
            (139, 233, 253),
            (255, 255, 255),
        ],
    )
    console = Console(force_terminal=True, width=120, record=True)
    console.print(rst)
    return console.export_html(theme=DRACULA_TERMINAL_THEME)


@pytest.mark.parametrize("rst_path", rst_paths)
def test_main(rst_path):
    rst_path = Path(rst_path)
    actual_html_path = rst_path.parent / (rst_path.stem + "_actual.html")
    expected_html_path = rst_path.parent / (rst_path.stem + "_expected.html")

    rst = RestructuredText(rst_path.read_text(), show_errors=True)
    actual_html = render_to_html(rst)
    actual_html_path.write_text(actual_html)

    expected_html = expected_html_path.read_text()
    assert expected_html == actual_html
