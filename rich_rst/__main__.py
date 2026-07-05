import argparse
import logging
import sys
from typing import Tuple

from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import (
    DIMMED_MONOKAI,
    DEFAULT_TERMINAL_THEME,
    MONOKAI,
    NIGHT_OWLISH,
    TerminalTheme,
)
from rich.text import Text
from rich.traceback import install

from rich_rst import RestructuredText, __version__

log = logging.getLogger(__name__)


def rgb(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """Represent color in RGB format."""
    return (r, g, b)


_DRACULA_TERMINAL_THEME = TerminalTheme(
    rgb(40, 42, 54),
    rgb(248, 248, 242),
    [
        rgb(40, 42, 54),
        rgb(255, 85, 85),
        rgb(80, 250, 123),
        rgb(241, 250, 140),
        rgb(189, 147, 249),
        rgb(255, 121, 198),
        rgb(139, 233, 253),
        rgb(255, 255, 255),
    ],
    [
        rgb(40, 42, 54),
        rgb(255, 85, 85),
        rgb(80, 250, 123),
        rgb(241, 250, 140),
        rgb(189, 147, 249),
        rgb(255, 121, 198),
        rgb(139, 233, 253),
        rgb(255, 255, 255),
    ],
)

_HTML_THEMES = {
    "dracula": _DRACULA_TERMINAL_THEME,
    "monokai": MONOKAI,
    "night-owl": NIGHT_OWLISH,
    "dimmed-monokai": DIMMED_MONOKAI,
    "default": DEFAULT_TERMINAL_THEME,
}


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Render reStructuredText to the console with rich-rst"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "path",
        metavar="PATH",
        nargs="?",
        default=None,
        help="path to file, or - for stdin",
    )
    parser.add_argument(
        "-c",
        "--force-color",
        dest="force_color",
        action="store_true",
        help="force color for non-terminals",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        dest="encoding",
        type=str,
        default="utf-8",
        help="encoding for file (default: utf-8)",
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        dest="width",
        default=None,
        help="width of output (default will auto-detect)",
    )
    parser.add_argument(
        "-hw",
        "--html-width",
        type=str,
        dest="html_width",
        default="1675px",
        help="width of html output (default: 1675px)",
    )
    parser.add_argument(
        "-t",
        "--code-theme",
        dest="code_theme",
        type=str,
        default="monokai",
        help="pygments code theme (default: monokai)",
    )
    parser.add_argument(
        "--show-line-numbers",
        action="store_true",
        dest="show_line_numbers",
        help="show line numbers in code blocks",
    )
    parser.add_argument(
        "-S",
        "--save-html",
        type=str,
        dest="html_filename",
        default=None,
        help="export rendered output to HTML file",
    )
    parser.add_argument(
        "-r",
        "--wrap",
        dest="word_wrap",
        action="store_true",
        help="enable word wrapping for long lines",
    )
    parser.add_argument(
        "-s",
        "--soft-wrap",
        action="store_true",
        dest="soft_wrap",
        help="enable soft wrapping mode",
    )
    parser.add_argument(
        "-gl",
        "--guess-lexer",
        action="store_true",
        dest="guess_lexer",
        help="guess lexer for code blocks without language",
    )
    parser.add_argument(
        "-dl",
        "--default-lexer",
        type=str,
        dest="default_lexer",
        default="python",
        help="default lexer if no lexer found (default: python)",
    )
    parser.add_argument(
        "-se",
        "--show-errors",
        action="store_true",
        dest="show_errors",
        help="display reStructuredText parsing errors",
    )
    parser.add_argument(
        "--admonition-style",
        dest="admonition_style",
        type=str,
        default="panel",
        choices=["panel", "compact"],
        help="rendering style for admonitions (default: panel)",
    )
    parser.add_argument(
        "--html-theme",
        dest="html_theme",
        type=str,
        default="dracula",
        choices=list(_HTML_THEMES),
        help="color theme for HTML export (default: dracula)",
    )
    parser.add_argument(
        "--list-html-themes",
        action="store_true",
        dest="list_html_themes",
        help="list available HTML export themes and exit",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=str,
        default=None,
        help="write plain-text output to FILE instead of stdout",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        help="enable debug logging",
    )

    args = parser.parse_args()

    if not args.list_html_themes and args.path is None:
        parser.error("the following arguments are required: PATH")

    return args


def main() -> int:
    """Main entry point."""
    args = parse_arguments()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        log.debug("Debug mode enabled")

    if args.list_html_themes:
        for name in sorted(_HTML_THEMES):
            print(name)
        return 0

    html_format = (
        """\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{stylesheet}
body {{
    color: {foreground};
    background-color: {background};
    max-width: HTML_WIDTH_PLACEHOLDER
}}
pre {{
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
}}
::-moz-selection {{
  background: #44475a;
}}
::selection {{
  background: #44475a;
}}
</style>
</head>
<body>
    <pre style="font-family:ui-monospace,'Fira Code',Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code>{code}</code></pre>
</body>
</html>
"""
    ).replace("HTML_WIDTH_PLACEHOLDER", args.html_width)

    record = bool(args.html_filename) or bool(args.output)
    console = Console(force_terminal=args.force_color, width=args.width, record=record)

    try:
        if args.path == "-":
            log.debug("Reading from stdin")
            code = sys.stdin.read()
        else:
            log.debug(f"Reading file: {args.path}")
            with open(args.path, "rt", encoding=args.encoding) as file_handle:
                code = file_handle.read()
    except OSError as e:
        console.print(
            Panel(
                Text(
                    f"[bold red]Error reading file[/bold red]\n\n"
                    f"Path: {args.path!r}\n"
                    f"Reason: {e.strerror}\n\n"
                    "Check that the file exists and you have read permission."
                ),
                title="[bold]File Error[/bold]",
                style="red",
            )
        )
        if args.debug:
            log.exception("File read error")
        return 1

    try:
        log.debug("Parsing reStructuredText")
        rst = RestructuredText(
            code,
            code_theme=args.code_theme,
            show_line_numbers=args.show_line_numbers,
            guess_lexer=args.guess_lexer,
            default_lexer=args.default_lexer,
            show_errors=args.show_errors,
            filename=args.path if args.path != "-" else "<stdin>",
            admonition_style=args.admonition_style,
        )
    except Exception as e:
        console.print(
            Panel(
                Text(
                    f"[bold red]Error parsing reStructuredText[/bold red]\n\n"
                    f"[yellow]{type(e).__name__}[/yellow]: {e}"
                ),
                title="[bold]Parse Error[/bold]",
                style="red",
            )
        )
        if args.debug:
            log.exception("Parse error")
        return 1

    try:
        if args.output:
            log.debug(f"Writing output to: {args.output}")
            console.print(rst, soft_wrap=args.soft_wrap)
            text_output = console.export_text()
            with open(args.output, "w", encoding="utf-8") as out_fh:
                out_fh.write(text_output)
        else:
            console.print(rst, soft_wrap=args.soft_wrap)

        if args.html_filename:
            log.debug(f"Exporting HTML to: {args.html_filename}")
            html_theme = _HTML_THEMES.get(args.html_theme, _DRACULA_TERMINAL_THEME)
            console.save_html(
                args.html_filename, theme=html_theme, code_format=html_format
            )
    except OSError as e:
        console.print(
            Panel(
                Text(
                    f"[bold red]Error writing output[/bold red]\n\n"
                    f"Path: {args.output or args.html_filename!r}\n"
                    f"Reason: {e.strerror}"
                ),
                title="[bold]Output Error[/bold]",
                style="red",
            )
        )
        if args.debug:
            log.exception("Output write error")
        return 1
    except Exception as e:
        console.print(
            Panel(
                Text(
                    f"[bold red]Error during export[/bold red]\n\n"
                    f"[yellow]{type(e).__name__}[/yellow]: {e}"
                ),
                title="[bold]Export Error[/bold]",
                style="red",
            )
        )
        if args.debug:
            log.exception("Export error")
        return 1

    return 0


if __name__ == "__main__":
    install()
    sys.exit(main())
