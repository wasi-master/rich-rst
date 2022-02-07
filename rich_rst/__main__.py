import argparse
import sys

from rich_rst import RestructuredText
from rich.terminal_theme import TerminalTheme

parser = argparse.ArgumentParser(description="Render reStructuredText to the console with rich-rst")
parser.add_argument(
    "path",
    metavar="PATH",
    help="path to file, or - for stdin",
)
parser.add_argument(
    "-c",
    "--force-color",
    dest="force_color",
    action="store_true",
    default=None,
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
    "-t",
    "--code-theme",
    dest="code_theme",
    type=str,
    default="monokai",
    help="pygments code theme",
)
parser.add_argument(
    "-html",
    "--save-html",
    type=str,
    dest="html_filename",
    default=False,
    help="save to html",
)
parser.add_argument(
    "-r",
    "--wrap",
    dest="word_wrap",
    action="store_true",
    default=False,
    help="word wrap long lines",
)
parser.add_argument(
    "-s",
    "--soft-wrap",
    action="store_true",
    dest="soft_wrap",
    default=False,
    help="enable soft wrapping mode",
)
parser.add_argument(
    "-gl",
    "--guess-lexer",
    action="store_true",
    dest="guess_lexer",
    default=False,
    help="Whether to guess the lexer for code blocks without specified language",
)
parser.add_argument(
    "-dl",
    "--default-lexer",
    type=str,
    dest="default_lexer",
    default="python",
    help="The default lexer for code blocks without specified language if no lexer could be guessed or found",
)


rgb = lambda r,g,b: (r,g,b)

DRACULA_TERMINAL_THEME = TerminalTheme(
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

args = parser.parse_args()

from rich.console import Console

console = Console(force_terminal=args.force_color, width=args.width, record=bool(args.html_filename))

if args.path == "-":
    code = sys.stdin.read()
    rst = RestructuredText(code, code_theme=args.code_theme, guess_lexer=args.guess_lexer, default_lexer=args.default_lexer)
else:
    with open(args.path, "rt", encoding=args.encoding) as code_file:
        code = code_file.read()
    rst = RestructuredText(code, code_theme=args.code_theme, guess_lexer=args.guess_lexer, default_lexer=args.default_lexer)
console.print(rst, soft_wrap=args.soft_wrap)

if args.html_filename:
    console.save_html(args.html_filename, theme=DRACULA_TERMINAL_THEME)
