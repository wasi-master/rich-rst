"""Compatibility imports for Rich / fast-rich backends."""

from __future__ import annotations

import os

_BACKEND_SETTING = os.getenv("RICH_RST_USE_FAST_RICH", "auto").strip().lower()
_FAST_RICH_ALLOWED = _BACKEND_SETTING not in {"0", "false", "no", "off"}

USING_FAST_RICH = False

if _FAST_RICH_ALLOWED:
    try:
        import fast_rich as _rich_backend  # type: ignore[import-not-found]
    except ImportError:
        _rich_backend = None
    else:
        USING_FAST_RICH = True
else:
    _rich_backend = None

if _rich_backend is None:
    import rich as _rich_backend

if USING_FAST_RICH:
    from rich import box
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

    from fast_rich.align import Align  # type: ignore[assignment]
    from fast_rich.cells import cell_len
else:
    from rich import box
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
