"""Compatibility imports for Rich / fast-rich backends."""

from __future__ import annotations

import os
from typing import Any, Iterable

_BACKEND_SETTING = os.getenv("RICH_RST_USE_FAST_RICH", "auto").strip().lower()
_FAST_RICH_ALLOWED = _BACKEND_SETTING not in {"0", "false", "no", "off"}

USING_FAST_RICH = False

if _FAST_RICH_ALLOWED:
    try:
        import fast_rich as _rich_backend  # type: ignore[import-not-found]
    except Exception:
        _rich_backend = None
    else:
        USING_FAST_RICH = True
else:
    _rich_backend = None

if _rich_backend is None:
    import rich as _rich_backend

box = _rich_backend.box

if USING_FAST_RICH:
    from fast_rich.align import Align
    from fast_rich.cells import cell_len
    from fast_rich.console import Console
    from fast_rich.console_options import ConsoleOptions
    from fast_rich.jupyter import JupyterMixin
    from fast_rich.panel import Panel
    from fast_rich.rule import Rule
    from fast_rich.segment import Segment
    from fast_rich.style import Style
    from fast_rich.styled import Styled
    from fast_rich.syntax import Syntax
    from fast_rich.table import Table
    from fast_rich.terminal_theme import DIMMED_MONOKAI, MONOKAI, NIGHT_OWLISH, TerminalTheme
    from fast_rich.text import Text
    from fast_rich.theme import Theme

    RenderResult = Iterable[Any]
    SyntaxTheme = Any

    class Group:
        """Rich-compatible fallback Group implementation for fast-rich."""

        def __init__(self, *renderables: Any) -> None:
            self.renderables = renderables

        def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
            yield from self.renderables

    class NewLine:
        """Rich-compatible newline renderable."""

        def __init__(self, count: int = 1) -> None:
            self.count = count

        def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
            for _ in range(self.count):
                yield Text("\n")

    DEFAULT_TERMINAL_THEME = MONOKAI
else:
    from rich.align import Align
    from rich.cells import cell_len
    from rich.console import Console, ConsoleOptions, Group, NewLine, RenderResult
    from rich.jupyter import JupyterMixin
    from rich.panel import Panel
    from rich.rule import Rule
    from rich.segment import Segment
    from rich.style import Style
    from rich.styled import Styled
    from rich.syntax import Syntax, SyntaxTheme
    from rich.table import Table
    from rich.terminal_theme import DIMMED_MONOKAI, MONOKAI, NIGHT_OWLISH, DEFAULT_TERMINAL_THEME, TerminalTheme
    from rich.text import Text
    from rich.theme import Theme

__all__ = (
    "Align",
    "Console",
    "ConsoleOptions",
    "DEFAULT_TERMINAL_THEME",
    "DIMMED_MONOKAI",
    "Group",
    "JupyterMixin",
    "MONOKAI",
    "NIGHT_OWLISH",
    "NewLine",
    "Panel",
    "RenderResult",
    "Rule",
    "Segment",
    "Styled",
    "Style",
    "Syntax",
    "SyntaxTheme",
    "Table",
    "TerminalTheme",
    "Text",
    "Theme",
    "USING_FAST_RICH",
    "box",
    "cell_len",
)
