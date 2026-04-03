import argparse
import sys
from rich.console import Console
from rich_rst import RestructuredText
from rich.terminal_theme import TerminalTheme
from rich.traceback import install

def rgb(r, g, b):
    """
    Function to represent color in RGB format.

    Parameters
    ----------
    r : int
        Red color value.
    g : int
        Green color value.
    b : int
        Blue color value.

    Returns
    -------
    tuple
        A tuple representing the RGB color.
    """
    return (r, g, b)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Render reStructuredText to the console with rich-rst")
    parser.add_argument("path", metavar="PATH", help="path to file, or - for stdin")
    parser.add_argument("-c", "--force-color", dest="force_color", action="store_true", default=None, help="force color for non-terminals")
    parser.add_argument("-e", "--encoding", dest="encoding", type=str, default="utf-8", help="encoding for file (default: utf-8)")
    parser.add_argument("-w", "--width", type=int, dest="width", default=None, help="width of output (default will auto-detect)")
    parser.add_argument("-hw", "--html-width", type=str, dest="html_width", default="1675px", help="width of html output (default: 1675px)")
    parser.add_argument("-t", "--code-theme", dest="code_theme", type=str, default="monokai", help="pygments code theme")
    parser.add_argument("--show-line-numbers", action="store_true", dest="show_line_numbers", default=False, help="show line numbers for syntax-highlighted code blocks")
    parser.add_argument("-html", "--save-html", type=str, dest="html_filename", default=False, help="save to html")
    parser.add_argument("-r", "--wrap", dest="word_wrap", action="store_true", default=False, help="word wrap long lines")
    parser.add_argument("-s", "--soft-wrap", action="store_true", dest="soft_wrap", default=False, help="enable soft wrapping mode")
    parser.add_argument("-gl", "--guess-lexer", action="store_true", dest="guess_lexer", default=False, help="Whether to guess the lexer for code blocks without specified language")
    parser.add_argument("-dl", "--default-lexer", type=str, dest="default_lexer", default="python", help="The default lexer for code blocks without specified language if no lexer could be guessed or found")
    parser.add_argument("-se", "--show-errors", action="store_true", dest="show_errors", default=False, help="Whether to show errors or not")
    return parser.parse_args()

def main():
    """The main function."""
    args = parse_arguments()
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
    # NOTE: CSS braces must be doubled ({{ / }}) so that Rich's internal
    # code_format.format(...) call treats them as literal characters.
    # args.html_width is spliced in with a plain str.replace to avoid
    # adding a third round of brace escaping.
    CONSOLE_HTML_FORMAT = """\
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
        white-space: pre-wrap;       /* Since CSS 2.1 */
        white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
        white-space: -pre-wrap;      /* Opera 4-6 */
        white-space: -o-pre-wrap;    /* Opera 7 */
        word-wrap: break-word;       /* Internet Explorer 5.5+ */
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
    """.replace("HTML_WIDTH_PLACEHOLDER", args.html_width)
    console = Console(force_terminal=args.force_color, width=args.width, record=bool(args.html_filename))
    if args.path == "-":
        code = sys.stdin.read()
    else:
        with open(args.path, "rt", encoding=args.encoding) as file_handle:
            code = file_handle.read()
    rst = RestructuredText(
        code,
        code_theme=args.code_theme,
        show_line_numbers=args.show_line_numbers,
        guess_lexer=args.guess_lexer,
        default_lexer=args.default_lexer,
        show_errors=args.show_errors,
        filename=args.path if args.path != "-" else "<stdin>",
    )
    console.print(rst, soft_wrap=args.soft_wrap)
    if args.html_filename:
        console.save_html(args.html_filename, theme=DRACULA_TERMINAL_THEME, code_format=CONSOLE_HTML_FORMAT)

if __name__ == "__main__":
    install()
    main()
