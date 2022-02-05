import argparse
import sys

from rich_rst import RestructuredText

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
args = parser.parse_args()

from rich.console import Console

console = Console(force_terminal=args.force_color, width=args.width)

if args.path == "-":
    code = sys.stdin.read()
    rst = RestructuredText(code)
else:
    with open(args.path, "rt", encoding=args.encoding) as code_file:
        code = code_file.read()
    rst = RestructuredText(code)
console.print(rst, soft_wrap=args.soft_wrap)
