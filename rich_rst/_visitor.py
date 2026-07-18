"""The docutils node visitor that produces rich renderables."""
import re
import threading
from typing import Any, Callable, ClassVar, Dict, List, Literal, Optional, Tuple, Type, Union

# Imports from the rich package for the printing
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
from rich import box
from rich.align import Align
from rich.cells import cell_len
from rich.console import Console, Group, NewLine
from rich.panel import Panel
from rich.rule import Rule
from rich.segment import Segment
from rich.style import Style
from rich.styled import Styled
from rich.syntax import Syntax, SyntaxTheme
from rich.table import Table
from rich.text import Text

# Imports from rich_rst._vendor.docutils package for the parsing
import rich_rst._vendor.docutils.nodes
import rich_rst._vendor.docutils.utils  # noqa: F401
from rich_rst._nodes import py_desc
from rich_rst._utils import _convert_math_to_unicode, _validate_default_lexer_name, strip_tags
from rich_rst._vendor import docutils


# pylama:ignore=D,C0116
class RSTVisitor(docutils.nodes.SparseNodeVisitor):
    """A visitor that produces rich renderables.

    .. note:: The ``_SUPERSCRIPT`` and ``_SUBSCRIPT`` translation tables are
       class-level constants so they are computed once rather than per-instance.

    Custom visitors for third-party node types can be registered via
    :meth:`register_visitor`.  Registered functions take ``(visitor, node)``
    as arguments and should follow the same conventions as the built-in
    ``visit_*`` / ``depart_*`` methods (e.g. raise
    ``docutils.nodes.SkipChildren`` to suppress child processing).
    """

    # Class-level registry mapping node_class → (visit_fn, depart_fn).
    # Entries are consulted by dispatch_visit / dispatch_departure before
    # falling through to the normal method-name lookup.
    #
    # Design note: the base class owns an empty dict.  When register_visitor is
    # called on a *subclass*, the guard below ensures the subclass gets its own
    # dict so that base-class registrations are never accidentally polluted by
    # subclass registrations (and vice-versa).  Registrations on RSTVisitor
    # itself are truly global and apply to every instance.
    _custom_visitors: ClassVar[Dict[Type[docutils.nodes.Node], Tuple[Optional[Callable[..., Any]], Optional[Callable[..., Any]]]]] = {}
    _DISPATCH_CACHE_MISS: ClassVar[object] = object()

    _SUPERSCRIPT: ClassVar[Dict[int, int]] = str.maketrans(
        "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=+-*/×÷",
        "¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ⁼⁺⁻*/×÷",
    )
    _SUBSCRIPT: ClassVar[Dict[int, int]] = str.maketrans(
        "1234567890abcdefghijklmnopqrstuvwxyz=+-*/×÷", "₁₂₃₄₅₆₇₈₉₀abcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz₌₊₋*/×÷"
    )

    @classmethod
    def register_visitor(cls, node_class: Type[docutils.nodes.Node], visit_fn: Optional[Callable[..., Any]] = None, depart_fn: Optional[Callable[..., Any]] = None) -> Optional[Callable[..., Any]]:
        """Register custom visit/depart functions for *node_class*.

        The registration is class-wide: it applies to every instance of this
        class (and subclasses that do not provide their own registry).

        Can be used in two ways:

        **Direct form** (original API)::

            RSTVisitor.register_visitor(MyNode, visit_fn=my_visit)

        **Decorator form** (when ``visit_fn`` and ``depart_fn`` are both
        ``None``, a single-argument call returns a decorator that registers
        the decorated function as the visit handler)::

            @RSTVisitor.register_visitor(MyNode)
            def visit_my_node(visitor, node):
                visitor.renderables.append(Text(node.astext()))
                raise docutils.nodes.SkipChildren()

        Parameters
        ----------
        node_class : type
            The docutils node class to handle.
        visit_fn : callable or None
            Called as ``visit_fn(visitor, node)`` when the node is entered.
            May raise ``docutils.nodes.SkipChildren`` to suppress child
            traversal.  Pass ``None`` to use a no-op visit.
        depart_fn : callable or None
            Called as ``depart_fn(visitor, node)`` when the node is exited.
            Pass ``None`` to use a no-op departure.

        Returns
        -------
        callable or None
            When used as a decorator (no ``visit_fn`` / ``depart_fn``
            provided), returns a decorator.  Otherwise returns ``None``.
        """
        if visit_fn is None and depart_fn is None:
            # Decorator form: @RSTVisitor.register_visitor(MyNodeClass)
            def _decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
                cls.register_visitor(node_class, visit_fn=fn)
                return fn
            return _decorator

        if '_custom_visitors' not in cls.__dict__:
            # Give subclasses their own dict so parent registrations are not
            # accidentally modified.
            cls._custom_visitors = {}
        cls._custom_visitors[node_class] = (visit_fn, depart_fn)
        return None

    @classmethod
    def unregister_visitor(cls, node_class: Type[docutils.nodes.Node]) -> None:
        """Remove a previously registered custom visitor for *node_class*.

        If no registration exists for *node_class* the call is silently
        ignored.  Useful in test teardown to restore the original state.

        Parameters
        ----------
        node_class : type
            The docutils node class whose custom handlers should be removed.
        """
        if '_custom_visitors' in cls.__dict__:
            cls._custom_visitors.pop(node_class, None)

    @classmethod
    def list_registered_visitors(cls) -> Dict[Type[docutils.nodes.Node], Tuple[Optional[Callable[..., Any]], Optional[Callable[..., Any]]]]:
        """Return a snapshot of the current custom-visitor registry.

        Returns
        -------
        dict
            A ``{node_class: (visit_fn, depart_fn)}`` mapping.  The dict is
            a shallow copy; modifying it does not affect the registry.
        """
        return dict(cls._custom_visitors)

    def dispatch_visit(self, node: docutils.nodes.Node) -> None:
        entry = self._custom_visitors.get(type(node))
        if entry is not None:
            visit_fn, _ = entry
            if visit_fn is not None:
                return visit_fn(self, node)
            return None
        return self._resolve_visit_handler(type(node))(node)

    def dispatch_departure(self, node: docutils.nodes.Node) -> None:
        entry = self._custom_visitors.get(type(node))
        if entry is not None:
            _, depart_fn = entry
            if depart_fn is not None:
                return depart_fn(self, node)
            return None
        return self._resolve_depart_handler(type(node))(node)

    def __init__(
        self,
        document: docutils.nodes.document,
        console: Console,
        code_theme: Union[str, SyntaxTheme] = "monokai",
        show_line_numbers: Optional[bool] = False,
        guess_lexer: Optional[bool] = True,
        default_lexer: Optional[str] = "python",
        admonition_style: Literal["panel", "compact"] = "panel",
    ) -> None:
        super().__init__(document)
        if self.document is not None and getattr(self.document, "reporter", None) is None:
            class DummyReporter:
                def debug(self, *args, **kwargs): pass
                def info(self, *args, **kwargs): pass
                def warning(self, *args, **kwargs): pass
                def error(self, *args, **kwargs): pass
                def severe(self, *args, **kwargs): pass
            self.document.reporter = DummyReporter()  # type: ignore[assignment]
        self.console: Console = console
        self.code_theme: Union[str, SyntaxTheme] = code_theme
        self.show_line_numbers: Optional[bool] = show_line_numbers
        self.admonition_style: Literal["panel", "compact"] = admonition_style
        self.renderables: List[Any] = []
        self.errors: List[Panel] = []
        self.footer: List[Align] = []
        self.citations: List[Align] = []
        self.guess_lexer: Optional[bool] = guess_lexer
        self.default_lexer: Optional[str] = _validate_default_lexer_name(default_lexer)
        self.refname_to_renderable: Dict[str, Tuple[Text, int, int]] = {}
        self._in_docinfo = False
        # Tracks the most recent ``Text`` produced by ``depart_paragraph`` (i.e.
        # an actual prose paragraph in this visitor's scope), so that
        # ``_append_inline_to_prev_paragraph`` can distinguish a paragraph from
        # a ``Text`` emitted by some other path (admonition prefix line, body
        # paragraph from a sub-visitor, etc.) and avoid merging tags across
        # directive boundaries.
        self._last_paragraph_text: Optional[Text] = None
        # Cache node-type dispatch handlers to reduce per-node lookup cost
        # in large documents.
        self._visit_dispatch_cache: Dict[Type[docutils.nodes.Node], Callable[[docutils.nodes.Node], Any]] = {}
        self._depart_dispatch_cache: Dict[Type[docutils.nodes.Node], Callable[[docutils.nodes.Node], Any]] = {}
        self._dispatch_cache_lock = threading.Lock()

    def _resolve_visit_handler(self, node_type: Type[docutils.nodes.Node]) -> Callable[[docutils.nodes.Node], Any]:
        cached = self._visit_dispatch_cache.get(node_type)
        if cached is not None:
            return cached

        with self._dispatch_cache_lock:
            cached = self._visit_dispatch_cache.get(node_type)
            if cached is not None:
                return cached
            handler = getattr(self, f"visit_{node_type.__name__}", self.unknown_visit)
            self._visit_dispatch_cache[node_type] = handler
            return handler

    def _resolve_depart_handler(self, node_type: Type[docutils.nodes.Node]) -> Callable[[docutils.nodes.Node], Any]:
        cached = self._depart_dispatch_cache.get(node_type)
        if cached is not None:
            return cached

        with self._dispatch_cache_lock:
            cached = self._depart_dispatch_cache.get(node_type)
            if cached is not None:
                return cached
            handler = getattr(self, f"depart_{node_type.__name__}", self.unknown_departure)
            self._depart_dispatch_cache[node_type] = handler
            return handler

    def _translate_with_fallback(self, text: str, table: Dict[int, Any]) -> str:
        """Translate characters using `table` while preserving unmapped/deleted chars."""
        translated_chars: List[str] = []
        for ch in text:
            mapped = table.get(ord(ch), ch)
            # str.translate deletes chars when mapping value is None; keep original instead.
            if mapped is None:
                translated_chars.append(ch)
            elif isinstance(mapped, int):
                translated_chars.append(chr(mapped))
            else:
                translated_chars.append(mapped)
        return "".join(translated_chars)

    def _guess_lexer_name(self, text: str) -> Tuple[Optional[str], bool]:
        try:
            lexer = guess_lexer(text)
        except ClassNotFound:
            return self.default_lexer, False
        guessed = lexer.aliases[0] if lexer.aliases else None
        if guessed == "text" or guessed is None:
            return self.default_lexer, False
        return guessed, True

    def _find_lexer(self, node: docutils.nodes.Node) -> Tuple[Optional[str], str]:
        lexer = None
        if isinstance(node, docutils.nodes.Element):
            lexer = (
                node["classes"][1] if len(node.get("classes", [])) >= 2 else (node["format"] if node.get("format") else None)
            )
        if lexer is not None:
            return lexer, "explicit"
        if self.guess_lexer:
            guessed_lexer, was_guessed = self._guess_lexer_name(node.astext())
            return guessed_lexer, "guessed" if was_guessed else "default"
        return self.default_lexer, "default"

    def _section_level(self, node: docutils.nodes.Node) -> int:
        level = 0
        parent = getattr(node, "parent", None)
        while parent is not None:
            if isinstance(parent, docutils.nodes.section):
                level += 1
            parent = getattr(parent, "parent", None)
        return level

    def _render_heading(self, text: str, level: int) -> None:
        heading_levels = [
            ("restructuredtext.title.level.1", "bold", box.DOUBLE),
            ("restructuredtext.title.level.2", "bold", box.ROUNDED),
            ("restructuredtext.title.level.3", "bold underline", None),
            ("restructuredtext.title.level.4", "bold", None),
            ("restructuredtext.title.level.5", "underline", None),
            ("restructuredtext.title.level.6", "italic", None),
        ]
        index = min(level, len(heading_levels) - 1)
        style_name, default_style, panel_box = heading_levels[index]
        style = self.console.get_style(style_name, default=default_style)
        if panel_box is None:
            self.renderables.append(Align(Text(text, style=style), "center"))
            self.renderables.append(NewLine())
        else:
            self.renderables.append(Panel(Align(Text(text, style=style), "center"), box=panel_box, style=style, border_style=style))

    def _format_labelled_node(self, node: docutils.nodes.Node) -> str:
        """Return labelled nodes (footnotes/citations) as `label: body`."""
        label_node = next((child for child in node.children if isinstance(child, docutils.nodes.label)), None)
        label = ""
        if label_node is not None:
            label = label_node.astext().replace("\n", " ").strip()

        body_parts = []
        for child in node.children:
            if child is label_node:
                continue
            part = child.astext().replace("\n", " ").strip()
            if part:
                body_parts.append(part)
        body = " ".join(body_parts).strip()

        if label and body:
            return f"{label}: {body}"
        if label:
            return f"{label}:"
        return node.astext().replace("\n", " ").strip()

    def visit_reference(self, node: docutils.nodes.Node) -> None:
        assert isinstance(node, docutils.nodes.Element)
        if len(node.children) == 1 and isinstance(node.children[0], docutils.nodes.image):
            return
        refuri = node.attributes.get("refuri")
        style = self.console.get_style("restructuredtext.reference", default="blue underline on default")
        if refuri:
            style = style.update_link(refuri)
        renderable = Text(node.astext().replace("\n", " "), style=style, end="")
        if self.renderables and isinstance(self.renderables[-1], Text):
            renderable.end = " "
            start = len(self.renderables[-1])
            # Calculate end based on what we're appending to avoid stale counter after merge.
            # Account for both the renderable text and its trailing space character.
            end = start + len(renderable) + len(renderable.end)
            self.renderables[-1].append_text(renderable)
        else:
            start = 0
            # Account for the trailing space character in the renderable.
            end = len(renderable) + len(renderable.end)
            self.renderables.append(renderable)

        if not refuri:
            # We'll get the URL reference later in visit_target.
            refname = node.attributes.get("refname")
            if refname:
                self.refname_to_renderable[refname] = (self.renderables[-1], start, end)
        raise docutils.nodes.SkipChildren()

    def visit_target(self, node) -> None:
        uri = node.get("refuri")
        if uri:
            for name in node["names"]:
                try:
                    renderable, start, end = self.refname_to_renderable[name]
                except KeyError:
                    continue
                style = renderable.get_style_at_offset(self.console, start)
                style = style.update_link(uri)
                renderable.stylize(style, start, end)
        raise docutils.nodes.SkipChildren()

    def visit_paragraph(self, node) -> None:
        if hasattr(node, "parent") and isinstance(node.parent, docutils.nodes.system_message):
            self.visit_system_message(node.parent)
            raise docutils.nodes.SkipChildren()

    def depart_paragraph(self, node) -> None:  # pylint: disable=unused-argument
        if self.renderables and isinstance(self.renderables[-1], Text):
            if self.renderables[-1]:
                if isinstance(getattr(node, "parent", None), docutils.nodes.list_item):
                    self.renderables[-1].append("\n")
                else:
                    self.renderables[-1].append("\n\n")
                self._last_paragraph_text = self.renderables[-1]

    def visit_title(self, node) -> None:
        level = self._section_level(node)
        self._render_heading(node.astext(), level)
        raise docutils.nodes.SkipChildren()

    def visit_subtitle(self, node) -> None:
        """Render document subtitle with ROUNDED box styling."""
        style = self.console.get_style("restructuredtext.subtitle", default="bold")
        self.renderables.append(Panel(Align(node.astext(), "center"), box=box.ROUNDED, style=style, border_style=style))
        self.renderables.append(NewLine())
        raise docutils.nodes.SkipChildren()

    def visit_rubric(self, node) -> None:
        style = self.console.get_style("restructuredtext.rubric", default="italic dim")
        self.renderables.append(Panel(Align(node.astext(), "center"), box=box.ROUNDED, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_Text(self, node) -> None:
        style = self.console.get_style(
            "restructuredtext.text",
            default="default not bold not italic not underline",
        )
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(node.astext().replace("\n", " "), style=style, end=" "))
            return
        self.renderables.append(Text(node.astext().replace("\n", " "), end="", style=style))

    def visit_comment(self, node) -> None:
        raise docutils.nodes.SkipChildren()

    def visit_substitution_definition(self, node) -> None:
        raise docutils.nodes.SkipChildren()

    def visit_compound(self, node) -> None:
        pass  # transparent container; let the visitor descend into children

    def depart_compound(self, node) -> None:  # pylint: disable=unused-argument
        pass

    def visit_container(self, node) -> None:
        # Transparent container used by ``.. container::``; traverse children.
        pass

    def depart_container(self, node) -> None:  # pylint: disable=unused-argument
        pass

    def visit_inline(self, node) -> None:
        """Render a generic inline span, applying any ``classes`` as a style name."""
        classes = node.get('classes', [])
        style_name = (
            f"restructuredtext.inline.{classes[0]}" if classes else "restructuredtext.inline"
        )
        style = self.console.get_style(style_name, default="none")
        text = node.astext().replace("\n", " ")
        self._append_inline_text(text, style)
        raise docutils.nodes.SkipChildren()

    def _append_inline_text(self, text: str, style: Style) -> None:
        """Append styled *text* to the last renderable if it is a :class:`Text`, otherwise create a new one.

        When merging into an existing Text, uses ``end=" "`` to add word
        separation; standalone Text gets ``end=""`` so the caller controls
        whitespace.
        """
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append_text(Text(text, style=style, end=" "))
        else:
            self.renderables.append(Text(text, style=style, end=""))

    def _make_sub_visitor(self) -> "RSTVisitor":
        """Create a fresh sub-visitor that shares this visitor's configuration."""
        return RSTVisitor(
            self.document,
            console=self.console,
            code_theme=self.code_theme,
            show_line_numbers=self.show_line_numbers,
            guess_lexer=self.guess_lexer,
            default_lexer=self.default_lexer,
            admonition_style=self.admonition_style,
        )

    def _clean_body_for_panel(self, body: List[Any]) -> List[Any]:
        """Strip trailing newlines and NewLine objects from the end of a panel body."""
        while body:
            last = body[-1]
            if isinstance(last, Text):
                last.rstrip()
                if last:
                    break
                else:
                    body.pop()
            elif isinstance(last, NewLine):
                body.pop()
            else:
                break
        return body

    def _render_admonition_body(self, children: List[docutils.nodes.Node]) -> List[Any]:
        """Render admonition body children using a sub-visitor to preserve inline markup."""
        sub_visitor = self._make_sub_visitor()
        for child in children:
            child.walkabout(sub_visitor)
        return sub_visitor.renderables

    def _render_child_inline(self, child: docutils.nodes.Node) -> List[Any]:
        """Render a single child node using a sub-visitor to preserve inline markup.

        This is used for list items and other contexts where we want to preserve
        bold, italic, links, inline code, and other inline markup instead of
        stripping to plain text via astext().
        """
        sub_visitor = self._make_sub_visitor()
        child.walkabout(sub_visitor)
        return sub_visitor.renderables

    def _emit_admonition(
        self,
        *,
        title: str,
        glyph: str,
        style_name: str,
        default_style: str,
        body_children: List[docutils.nodes.Node],
    ) -> None:
        """Render an admonition in either ``panel`` or ``compact`` style.

        ``title`` is the bare label (e.g. ``"Note"``) — used directly as the
        panel title in panel mode and as the inline prefix label (followed by
        ``": "``) in compact mode.
        """
        style = self.console.get_style(style_name, default=default_style)
        if self.admonition_style == "compact":
            self._emit_compact_admonition(title=title, glyph=glyph, style=style, body_children=body_children)
        else:
            self._emit_panel_admonition(
                panel_title=title,
                style=style,
                body_children=body_children,
            )

    def _emit_panel_admonition(self, *, panel_title: str, style: Style, body_children: List[docutils.nodes.Node]) -> None:
        body = self._render_admonition_body(body_children)
        body = self._clean_body_for_panel(body)
        # Apply the background colour (if any) to the whole panel so that
        # admonitions like "attention" (on yellow) and "danger" (on red) fill
        # the panel body with the expected background, not the terminal default.
        panel_style = Style(bgcolor=style.bgcolor) if style.bgcolor else Style.null()
        self.renderables.append(
            Panel(Group(*body) if body else "", title=panel_title, style=panel_style, border_style=style)
        )

    def _emit_compact_admonition(self, *, title: str, glyph: str, style: Style, body_children: List[docutils.nodes.Node]) -> None:
        prefix = Text(f"{glyph}{title}: ", style=style, end="")
        body = self._render_admonition_body(body_children)
        self._prepend_styled_prefix(prefix, body)

    def _append_inline_to_prev_paragraph(self, tag: Text) -> None:
        """Inline ``tag`` onto the trailing paragraph, space-separated.

        Used by compact-mode version directives so that short tags like
        ``[Added in v0.47]`` share a line with the paragraph they follow,
        instead of being forced onto their own line by ``depart_paragraph``'s
        trailing ``"\\n\\n"``. Only merges when ``self.renderables[-1]`` is the
        ``Text`` most recently emitted by ``depart_paragraph`` in this
        visitor's scope (tracked via ``_last_paragraph_text``); otherwise
        falls back to emitting ``tag`` as its own paragraph. This guard
        prevents the tag from leaking onto a preceding admonition's prefix
        line or onto an admonition body paragraph appended via
        ``_prepend_styled_prefix``.
        """
        prev = self._last_paragraph_text
        if prev is not None and self.renderables and self.renderables[-1] is prev:
            prev.rstrip()
            merged = Text.assemble(prev, Text(" "), tag, end="")
            merged.append("\n\n")
            self.renderables[-1] = merged
            # Keep chained inlining working: a second version tag immediately
            # following should still be able to merge onto this same line.
            self._last_paragraph_text = merged
        else:
            tag.append("\n\n")
            self.renderables.append(tag)

    def _prepend_styled_prefix(self, prefix: Text, body: List[Any]) -> None:
        """Append ``prefix`` followed by ``body`` to ``self.renderables``.

        When the first body renderable is a :class:`Text` (the common case —
        a paragraph), the prefix is merged into it via :meth:`Text.assemble`
        so the prefix and first paragraph share a wrapped line. Otherwise
        the prefix is emitted on its own line above the body. ``prefix`` is
        expected to have ``end=""`` so paragraph spacing is governed by the
        ``"\\n\\n"`` already baked into paragraph Texts by ``depart_paragraph``.
        """
        if not body:
            prefix.append("\n\n")
            self.renderables.append(prefix)
            return
        first = body[0]
        if isinstance(first, Text):
            merged = Text.assemble(prefix, first, end=first.end)
            self.renderables.append(merged)
            self.renderables.extend(body[1:])
        else:
            self.renderables.append(prefix)
            self.renderables.extend(body)

    def _emit_version_directive(self, type_: str, version: str, body_children: List[docutils.nodes.Node]) -> None:
        style_map = {
            "versionadded": ("restructuredtext.versionadded", "bold green"),
            "versionchanged": ("restructuredtext.versionchanged", "bold cyan"),
            "deprecated": ("restructuredtext.deprecated", "bold yellow"),
            "deprecated-removed": ("restructuredtext.deprecated_removed", "bold red"),
            "availability": ("restructuredtext.availability", "bold blue"),
            "soft-deprecated": ("restructuredtext.soft_deprecated", "bold bright_yellow"),
        }
        panel_title_map = {
            "versionadded": f"New in version {version}",
            "versionchanged": f"Changed in version {version}",
            "deprecated": f"Deprecated since version {version}",
            "deprecated-removed": f"Deprecated since version {version}",
            "availability": f"Available since version {version}",
            "soft-deprecated": f"Soft Deprecated since version {version}",
        }
        # ``deprecated-removed`` relies on _DeprecatedRemovedDirective.run embedding
        # "(removed in <removed>)" into the version string, so this map produces
        # tags like ``[Deprecated in v0.9 (removed in 2.0)]``. Keep the formats
        # in sync if that directive's version-string format ever changes.
        short_title_map = {
            "versionadded": f"Added in v{version}",
            "versionchanged": f"Changed in v{version}",
            "deprecated": f"Deprecated in v{version}",
            "deprecated-removed": f"Deprecated in v{version}",
            "availability": f"Available in v{version}",
            "soft-deprecated": f"Soft Deprecated in v{version}",
        }
        # Severity glyphs match the admonition convention: ⚠ for warning-tone
        # (deprecated/soft-deprecated → yellow), ✖ for danger-tone
        # (deprecated-removed → bold red). versionadded/versionchanged/availability
        # stay glyphless.
        glyph_map = {
            "deprecated": "⚠ ",
            "deprecated-removed": "✖ ",
            "soft-deprecated": "⚠ ",
        }
        style_name, default_style = style_map.get(type_, ("restructuredtext.versionadded", "bold green"))
        style = self.console.get_style(style_name, default=default_style)

        if self.admonition_style == "panel":
            panel_title = panel_title_map.get(type_, f"{type_} {version}")
            body = self._render_admonition_body(body_children)
            body = self._clean_body_for_panel(body)
            self.renderables.append(
                Panel(Group(*body) if body else "", title=panel_title, border_style=style)
            )
            return

        short_title = short_title_map.get(type_, f"{type_} {version}")
        glyph = glyph_map.get(type_, "")
        body = self._render_admonition_body(body_children)
        if not body:
            tag = Text(f"{glyph}[{short_title}]", style=style, end="")
            self._append_inline_to_prev_paragraph(tag)
            return
        # Bracket-collapse only when the body is a single paragraph. Adjacent
        # paragraphs are coalesced into one trailing Text by visit_Text/depart_paragraph,
        # so detect multi-paragraph bodies by checking for an internal "\n\n".
        if len(body) == 1 and isinstance(body[0], Text):
            inner = body[0].copy()
            inner.rstrip()
            if "\n\n" not in inner.plain:
                bracketed = Text.assemble(
                    Text(f"{glyph}[{short_title}: ", style=style),
                    inner,
                    Text("]", style=style),
                    end="",
                )
                self._append_inline_to_prev_paragraph(bracketed)
                return
        # Multi-paragraph or structural body: fall back to title-prefix shape (no brackets).
        prefix = Text(f"{glyph}{short_title}: ", style=style, end="")
        self._prepend_styled_prefix(prefix, body)

    def visit_admonition(self, node) -> None:
        # Generic admonition: first child is the user-supplied title node
        if node.children and isinstance(node.children[0], docutils.nodes.title):
            user_title = node.children[0].astext()
            body_children = node.children[1:]
        else:
            user_title = "Admonition"
            body_children = node.children
        self._emit_admonition(
            title=user_title,
            glyph="",
            style_name="restructuredtext.admonition",
            default_style="bold white",
            body_children=body_children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_attention(self, node) -> None:
        self._emit_admonition(
            title="Attention",
            glyph="⚠ ",
            style_name="restructuredtext.attention",
            default_style="bold black on yellow",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_caution(self, node) -> None:
        self._emit_admonition(
            title="Caution",
            glyph="⚠ ",
            style_name="restructuredtext.caution",
            default_style="red",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_danger(self, node) -> None:
        self._emit_admonition(
            title="DANGER",
            glyph="✖ ",
            style_name="restructuredtext.danger",
            default_style="bold white on red",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_error(self, node) -> None:
        self._emit_admonition(
            title="ERROR",
            glyph="✖ ",
            style_name="restructuredtext.error",
            default_style="bold red",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_hint(self, node) -> None:
        self._emit_admonition(
            title="Hint",
            glyph="",
            style_name="restructuredtext.hint",
            default_style="yellow",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_important(self, node) -> None:
        self._emit_admonition(
            title="IMPORTANT",
            glyph="",
            style_name="restructuredtext.important",
            default_style="bold blue",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_note(self, node) -> None:
        self._emit_admonition(
            title="Note",
            glyph="",
            style_name="restructuredtext.note",
            default_style="bold white",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_tip(self, node) -> None:
        self._emit_admonition(
            title="Tip",
            glyph="",
            style_name="restructuredtext.tip",
            default_style="bold green",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_warning(self, node) -> None:
        self._emit_admonition(
            title="Warning",
            glyph="⚠ ",
            style_name="restructuredtext.warning",
            default_style="bold yellow",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def visit_versionmodified(self, node) -> None:
        type_ = node.get("type", "versionadded")
        version = node.get("version", "")
        self._emit_version_directive(type_, version, node.children)
        raise docutils.nodes.SkipChildren()

    def depart_versionmodified(self, node) -> None:
        pass

    def visit_seealso(self, node) -> None:
        self._emit_admonition(
            title="See Also",
            glyph="",
            style_name="restructuredtext.seealso",
            default_style="bold white",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def depart_seealso(self, node) -> None:
        pass

    def visit_availability(self, node) -> None:
        version = node.get("version", "")
        if version:
            self._emit_version_directive("availability", version, node.children)
        else:
            # Defensive: the directive requires a version arg, but if missing
            # we degrade to a plain admonition rather than rendering "v".
            self._emit_admonition(
                title="Availability",
                glyph="",
                style_name="restructuredtext.availability",
                default_style="bold blue",
                body_children=node.children,
            )
        raise docutils.nodes.SkipChildren()

    def depart_availability(self, node) -> None:
        pass

    def visit_soft_deprecated(self, node) -> None:
        version = node.get("version", "")
        if version:
            self._emit_version_directive("soft-deprecated", version, node.children)
        else:
            self._emit_admonition(
                title="Soft Deprecated",
                glyph="⚠ ",
                style_name="restructuredtext.soft_deprecated",
                default_style="bold bright_yellow",
                body_children=node.children,
            )
        raise docutils.nodes.SkipChildren()

    def depart_soft_deprecated(self, node) -> None:
        pass

    def visit_impl_detail(self, node) -> None:
        self._emit_admonition(
            title="Implementation Detail",
            glyph="",
            style_name="restructuredtext.impl_detail",
            default_style="bold magenta",
            body_children=node.children,
        )
        raise docutils.nodes.SkipChildren()

    def depart_impl_detail(self, node) -> None:
        pass

    def visit_centered_block(self, node) -> None:
        style = self.console.get_style("restructuredtext.centered", default="bold")
        text = node.get('text', '')
        self.renderables.append(Align(Text(text, style=style), "center"))
        raise docutils.nodes.SkipChildren()

    def depart_centered_block(self, node) -> None:
        pass

    @staticmethod
    def _parse_py_field_name(field_name: str) -> Tuple[str, str]:
        """Classify a Python-domain field-list name.

        Returns a tuple ``(kind, arg)`` where ``kind`` is one of:
        ``param``, ``type``, ``returns``, ``rtype``, ``raises``, ``unknown``.
        """
        name = field_name.strip()
        lowered = name.lower()

        if lowered in ("returns", "return"):
            return "returns", ""
        if lowered == "rtype":
            return "rtype", ""

        for prefix in ("param", "parameter", "arg", "argument"):
            token = prefix + " "
            if lowered.startswith(token):
                return "param", name[len(token):].strip()

        if lowered.startswith("type "):
            return "type", name[5:].strip()

        for prefix in ("raises", "raise", "except", "exception"):
            token = prefix + " "
            if lowered.startswith(token):
                return "raises", name[len(token):].strip()

        return "unknown", name

    def _render_py_field_list(self, field_list_node: docutils.nodes.field_list) -> List[Any]:
        """Render a Sphinx-style Python field list as API sections."""
        params = {}
        param_order = []
        returns_desc = ""
        returns_type = ""
        raises_items = []
        unknown_items = []

        for field in field_list_node.children:
            if len(field.children) < 2:
                continue
            raw_name = field.children[0].astext().strip()
            raw_value = field.children[1].astext().replace("\n", " ").strip()
            kind, arg = self._parse_py_field_name(raw_name)

            if kind == "param":
                param_name = arg or "<unnamed>"
                if param_name not in params:
                    params[param_name] = {"type": "", "desc": ""}
                    param_order.append(param_name)
                params[param_name]["desc"] = raw_value
            elif kind == "type":
                param_name = arg or "<unnamed>"
                if param_name not in params:
                    params[param_name] = {"type": "", "desc": ""}
                    param_order.append(param_name)
                params[param_name]["type"] = raw_value
            elif kind == "returns":
                returns_desc = raw_value
            elif kind == "rtype":
                returns_type = raw_value
            elif kind == "raises":
                raises_items.append((arg or "Exception", raw_value))
            else:
                unknown_items.append((raw_name, raw_value))

        if not (param_order or returns_desc or returns_type or raises_items or unknown_items):
            return self._render_admonition_body([field_list_node])

        section_style = self.console.get_style("restructuredtext.py_desc.section", default="bold")
        param_name_style = self.console.get_style("restructuredtext.py_desc.param_name", default="bold")
        param_type_style = self.console.get_style("restructuredtext.py_desc.param_type", default="cyan")
        return_style = self.console.get_style("restructuredtext.py_desc.returns", default="none")

        renderables: List[Any] = []

        if param_order:
            renderables.append(Text("Parameters", style=section_style))
            for param_name in param_order:
                entry = params[param_name]
                line = Text("  ")
                line.append(param_name, style=param_name_style)
                if entry["type"]:
                    line.append(": ")
                    line.append(entry["type"], style=param_type_style)
                renderables.append(line)
                if entry["desc"]:
                    renderables.append(Text(f"    {entry['desc']}"))
            renderables.append(NewLine())

        if returns_desc or returns_type:
            renderables.append(Text("Returns", style=section_style))
            if returns_type and returns_desc:
                returns_text = f"{returns_type}: {returns_desc}"
            else:
                returns_text = returns_type or returns_desc
            renderables.append(Text(f"  {returns_text}", style=return_style))
            renderables.append(NewLine())

        if raises_items:
            renderables.append(Text("Raises", style=section_style))
            for exc_name, exc_desc in raises_items:
                line = Text("  ")
                line.append(exc_name, style=param_name_style)
                if exc_desc:
                    line.append(": ")
                    line.append(exc_desc)
                renderables.append(line)
            renderables.append(NewLine())

        if unknown_items:
            renderables.append(Text("Other", style=section_style))
            for key, value in unknown_items:
                line = Text("  ")
                line.append(key, style=param_name_style)
                if value:
                    line.append(": ")
                    line.append(value)
                renderables.append(line)
            renderables.append(NewLine())

        return renderables

    def _render_py_desc_options(self, node: docutils.nodes.Node) -> List[Any]:
        """Render ``py:*`` directive options as structured metadata."""
        assert isinstance(node, docutils.nodes.Element)
        options = node.get('options', {}) or {}
        objtype = str(node.get("objtype", "") or "").strip().lower()
        domain = str(node.get("domain", "py") or "").strip().lower()
        if not options:
            return []

        label_map = {
            'value': 'Value',
            'type': 'Type',
            'module': 'Module',
            'annotation': 'Annotation',
            'canonical': 'Canonical',
            'platform': 'Platform',
            'synopsis': 'Synopsis',
        }
        flag_order = (
            'async', 'classmethod', 'staticmethod', 'abstract',
            'final', 'deprecated', 'noindex', 'no-index',
        )

        rows = []
        for key, label in label_map.items():
            if domain in {"py", "js"} and objtype in {"attribute", "property", "data", "variable"} and key in {"type", "value"}:
                continue
            value = options.get(key)
            if value is not None and value != '':
                rows.append((label, str(value)))

        flags = []
        for key in flag_order:
            if key in options:
                flags.append(key.replace('-', ' '))
        if flags:
            rows.append(('Flags', ', '.join(flags)))

        if not rows:
            return []

        section_style = self.console.get_style("restructuredtext.py_desc.section", default="bold")
        meta_name_style = self.console.get_style("restructuredtext.py_desc.meta_name", default="bold")
        meta_value_style = self.console.get_style("restructuredtext.py_desc.meta_value", default="none")

        renderables: List[Any] = [Text("Details", style=section_style)]
        for property_name, property_value in rows:
            line = Text("  ")
            line.append(property_name, style=meta_name_style)
            line.append(": ")
            line.append(property_value, style=meta_value_style)
            renderables.append(line)
        renderables.append(NewLine())
        return renderables

    def _py_desc_panel_style(self, objtype: str, domain: str = "py") -> Style:
        """Return panel style based on object type and domain."""
        normalized_domain = (domain or "py").strip().lower()
        normalized = (objtype or "").lower().strip()
        if not normalized:
            normalized = "object"
        style_name = f"restructuredtext.{normalized_domain}_desc.{normalized}"
        if normalized_domain == "py":
            if normalized in {"class", "exception"}:
                default_style = "bold green"
            elif normalized in {"method", "classmethod", "staticmethod", "coroutinemethod", "abstractmethod"}:
                default_style = "bold cyan"
            elif normalized in {"function", "decorator", "decoratorfunction", "coroutinefunction"}:
                default_style = "bold magenta"
            elif normalized in {"attribute", "property", "data", "variable", "envvar", "option"}:
                default_style = "bold yellow"
            elif normalized in {"module", "type", "typevar", "typealias", "opcode", "describe"}:
                default_style = "bold blue"
            else:
                default_style = "bold white"
        elif normalized_domain == "c":
            if normalized in {"struct", "union", "type"}:
                default_style = "bold green"
            elif normalized in {"function", "macro"}:
                default_style = "bold magenta"
            elif normalized in {"enum", "enumerator"}:
                default_style = "bold yellow"
            elif normalized in {"member", "var"}:
                default_style = "bold cyan"
            else:
                default_style = "bold white"
        elif normalized_domain == "cpp":
            if normalized in {"class", "struct", "union", "type"}:
                default_style = "bold green"
            elif normalized in {"function", "concept"}:
                default_style = "bold magenta"
            elif normalized in {"enum", "enumerator"}:
                default_style = "bold yellow"
            elif normalized in {"member", "var"}:
                default_style = "bold cyan"
            elif normalized in {"alias"}:
                default_style = "bold blue"
            else:
                default_style = "bold white"
        elif normalized_domain == "js":
            if normalized in {"class", "module"}:
                default_style = "bold green"
            elif normalized in {"function", "method"}:
                default_style = "bold magenta"
            elif normalized in {"attribute", "data"}:
                default_style = "bold yellow"
            else:
                default_style = "bold white"
        else:
            default_style = "bold white"
        return self.console.get_style(style_name, default=default_style)

    def _highlight_c_cpp_signature(self, domain: str, objtype: str, signature: str) -> Text:
        """Apply custom syntax highlighting to C/C++ domain signatures."""
        rendered = Text(signature)
        if not signature:
            return rendered

        c_keywords = frozenset({
            "auto", "char", "const", "double", "enum", "extern", "float", "inline",
            "int", "long", "register", "restrict", "short", "signed", "static",
            "struct", "typedef", "union", "unsigned", "void", "volatile", "_Atomic",
            "_Bool", "_Complex", "_Imaginary",
        })
        cpp_keywords = frozenset({
            "bool", "char", "char8_t", "char16_t", "char32_t", "class", "concept",
            "const", "consteval", "constexpr", "constinit", "decltype", "double",
            "enum", "explicit", "export", "final", "float", "friend", "inline",
            "int", "long", "mutable", "namespace", "noexcept", "override", "private",
            "protected", "public", "short", "signed", "static", "struct", "template",
            "typename", "union", "unsigned", "using", "virtual", "void", "volatile",
            "wchar_t", "nullptr", "auto",
        })

        normalized_domain = (domain or "c").strip().lower()
        normalized_objtype = (objtype or "").strip().lower()
        type_style = self.console.get_style(f"restructuredtext.{normalized_domain}_desc.signature.type", default="bright_cyan")
        name_style = self.console.get_style(f"restructuredtext.{normalized_domain}_desc.signature.name", default="bold")
        namespace_style = self.console.get_style(f"restructuredtext.{normalized_domain}_desc.signature.namespace", default="magenta")
        operator_style = self.console.get_style(f"restructuredtext.{normalized_domain}_desc.signature.operator", default="bold yellow")
        number_style = self.console.get_style(f"restructuredtext.{normalized_domain}_desc.signature.number", default="green")

        keywords = c_keywords if normalized_domain == "c" else (c_keywords | cpp_keywords)
        keyword_pattern = r"\b(?:{})\b".format("|".join(sorted(re.escape(keyword) for keyword in keywords)))
        for match in re.finditer(keyword_pattern, signature):
            rendered.stylize(type_style, match.start(), match.end())

        for match in re.finditer(r"\b\d+(?:\.\d+)?\b", signature):
            rendered.stylize(number_style, match.start(), match.end())

        for match in re.finditer(r"::|->|=", signature):
            rendered.stylize(operator_style, match.start(), match.end())

        for match in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)::", signature):
            rendered.stylize(namespace_style, match.start(1), match.end(1))

        if normalized_objtype == "alias":
            alias_match = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\b\s*=", signature)
            if alias_match is not None:
                rendered.stylize(name_style, alias_match.start(1), alias_match.end(1))
        elif normalized_objtype == "function":
            name_match = None
            # Signatures may include qualified names (e.g. ``ns::Class::method(...)``);
            # the last identifier before ``(`` is the callable name to emphasize.
            for match in re.finditer(r"(~?[A-Za-z_][A-Za-z0-9_]*)\s*(?=\()", signature):
                name_match = match
            if name_match is not None:
                rendered.stylize(name_style, name_match.start(1), name_match.end(1))
        elif normalized_objtype in {"class", "struct", "union", "enum", "concept", "type"}:
            head_match = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b", signature)
            if head_match is not None:
                leaf = head_match.group(1).split("::")[-1]
                leaf_start = head_match.end(1) - len(leaf)
                rendered.stylize(name_style, leaf_start, head_match.end(1))
        elif normalized_objtype in {"member", "var", "enumerator"}:
            rightmost_identifier = None
            for match in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\b", signature):
                token = match.group(1)
                if token not in keywords:
                    rightmost_identifier = match
            if rightmost_identifier is not None:
                rendered.stylize(name_style, rightmost_identifier.start(1), rightmost_identifier.end(1))

        return rendered

    def _highlight_js_signature(self, objtype: str, signature: str) -> Text:
        """Apply custom syntax highlighting to JavaScript-domain signatures."""
        rendered = Text(signature)
        if not signature:
            return rendered

        js_keywords = frozenset({
            "async", "await", "break", "case", "catch", "class", "const", "continue",
            "debugger", "default", "delete", "do", "else", "export", "extends",
            "false", "finally", "for", "function", "if", "import", "in", "instanceof",
            "let", "new", "null", "return", "super", "switch", "this", "throw", "true",
            "try", "typeof", "var", "void", "while", "with", "yield",
        })

        normalized_objtype = (objtype or "").strip().lower()
        keyword_style = self.console.get_style("restructuredtext.js_desc.signature.keyword", default="bright_cyan")
        name_style = self.console.get_style("restructuredtext.js_desc.signature.name", default="bold")
        namespace_style = self.console.get_style("restructuredtext.js_desc.signature.namespace", default="magenta")
        operator_style = self.console.get_style("restructuredtext.js_desc.signature.operator", default="bold yellow")
        number_style = self.console.get_style("restructuredtext.js_desc.signature.number", default="green")

        keyword_pattern = r"\b(?:{})\b".format("|".join(sorted(re.escape(keyword) for keyword in js_keywords)))
        for match in re.finditer(keyword_pattern, signature):
            rendered.stylize(keyword_style, match.start(), match.end())

        for match in re.finditer(r"\b\d+(?:\.\d+)?\b", signature):
            rendered.stylize(number_style, match.start(), match.end())

        for match in re.finditer(r"=>|=|\.", signature):
            rendered.stylize(operator_style, match.start(), match.end())

        if normalized_objtype in {"function", "method"}:
            name_match = None
            for match in re.finditer(r"([A-Za-z_$][A-Za-z0-9_$]*)\s*(?=\()", signature):
                name_match = match
            if name_match is not None:
                rendered.stylize(name_style, name_match.start(1), name_match.end(1))
        elif normalized_objtype == "class":
            class_match = re.search(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\b", signature)
            if class_match is not None:
                rendered.stylize(name_style, class_match.start(1), class_match.end(1))
        elif normalized_objtype == "module":
            for match in re.finditer(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\.", signature):
                rendered.stylize(namespace_style, match.start(1), match.end(1))
            leaf_match = re.search(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\b$", signature)
            if leaf_match is not None:
                rendered.stylize(name_style, leaf_match.start(1), leaf_match.end(1))
        elif normalized_objtype == "attribute":
            attribute_match = re.search(r"([A-Za-z_$][A-Za-z0-9_$]*)\s*(?::|=|$)", signature)
            if attribute_match is not None:
                rendered.stylize(name_style, attribute_match.start(1), attribute_match.end(1))
        elif normalized_objtype == "data":
            data_match = re.search(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\b", signature)
            if data_match is not None:
                rendered.stylize(name_style, data_match.start(1), data_match.end(1))

        return rendered

    def _highlight_py_signature(self, objtype: str, signature: str) -> Text:
        """Apply custom syntax highlighting to Python-domain signatures."""
        rendered = Text(signature)
        if not signature:
            return rendered

        self_and_cls_style = self.console.get_style("restructuredtext.py_desc.signature.self_and_cls", default="bright_magenta")
        arrow_style = self.console.get_style("restructuredtext.py_desc.signature.arrow", default="bold yellow")
        type_style = self.console.get_style("restructuredtext.py_desc.signature.type", default="cyan")
        name_style = self.console.get_style("restructuredtext.py_desc.signature.name", default="bold")
        bool_style = self.console.get_style("restructuredtext.py_desc.signature.bool", default="magenta")
        int_style = self.console.get_style("restructuredtext.py_desc.signature.int", default="green")

        if objtype in {
            "function", "method", "classmethod", "staticmethod",
            "decorator", "decoratorfunction", "coroutinefunction",
            "coroutinemethod", "abstractmethod",
        }:
            name_match = None
            # Signatures may include dotted names (e.g. ``Class.method(...)``);
            # the last match before ``(`` is the callable's display name.
            for match in re.finditer(r"([A-Za-z_][A-Za-z0-9_]*)\s*(?=\()", signature):
                name_match = match
            if name_match is not None:
                rendered.stylize(name_style, name_match.start(1), name_match.end(1))

        for match in re.finditer(r"\b(self|cls)\b", signature):
            rendered.stylize(self_and_cls_style, match.start(1), match.end(1))

        for match in re.finditer(r"->", signature):
            rendered.stylize(arrow_style, match.start(), match.end())

        # Highlight return types, but be bracket-aware so generics like
        # ``-> dict[str, int]`` aren't cut off at internal commas.
        for arrow_match in re.finditer(r"->", signature):
            # start scanning after the arrow, skipping whitespace
            i = arrow_match.end()
            signature_length = len(signature)
            while i < signature_length and signature[i].isspace():
                i += 1
            # scan until we hit a delimiter at bracket depth 0
            depth = 0
            j = i
            while j < signature_length:
                ch = signature[j]
                if ch in "([{":
                    depth += 1
                elif ch in ")]}":
                    if depth > 0:
                        depth -= 1
                    else:
                        # unmatched closing - treat as delimiter
                        break
                # stop at comma, closing paren or equals only if not inside brackets
                if depth == 0 and ch in ",)=":
                    break
                j += 1
            # trim whitespace from ends
            type_start = i
            type_end = j
            while type_start < type_end and signature[type_start].isspace():
                type_start += 1
            while type_end > type_start and signature[type_end - 1].isspace():
                type_end -= 1
            if type_end > type_start:
                rendered.stylize(type_style, type_start, type_end)

        # Highlight parameter annotation types, bracket-aware so
        # ``param: dict[str, int]`` doesn't stop at the inner comma.
        for colon_match in re.finditer(r":\s*", signature):
            # start scanning at first non-space after ':'
            i = colon_match.end()
            signature_length = len(signature)
            while i < signature_length and signature[i].isspace():
                i += 1
            # if next char is ')' or ',' or end, nothing to do
            if i >= signature_length or signature[i] in ",)":
                continue
            depth = 0
            j = i
            while j < signature_length:
                ch = signature[j]
                if ch in "([{":
                    depth += 1
                elif ch in ")]}":
                    if depth > 0:
                        depth -= 1
                    else:
                        break
                # stop at comma, closing paren or equals only if not inside brackets
                if depth == 0 and ch in ",)=":
                    break
                j += 1
            type_start = i
            type_end = j
            while type_start < type_end and signature[type_start].isspace():
                type_start += 1
            while type_end > type_start and signature[type_end - 1].isspace():
                type_end -= 1
            if type_end > type_start:
                rendered.stylize(type_style, type_start, type_end)

        for match in re.finditer(r"\b(?:True|False)\b", signature):
            rendered.stylize(bool_style, match.start(), match.end())

        for match in re.finditer(r"\b\d+\b", signature):
            rendered.stylize(int_style, match.start(), match.end())

        return rendered

    def _render_py_desc_title(self, domain: str, objtype: str, signature: str) -> Text:
        """Render a styled panel title for Python/C/C++/JS domain objects."""
        prefix_style = self.console.get_style("restructuredtext.py_desc.title_prefix", default="bold")
        title = Text(f"[{objtype}] ", style=prefix_style)
        normalized_domain = (domain or "py").strip().lower()
        if normalized_domain in {"c", "cpp"}:
            title.append_text(self._highlight_c_cpp_signature(domain=domain, objtype=objtype, signature=signature))
        elif normalized_domain == "js":
            title.append_text(self._highlight_js_signature(objtype=objtype, signature=signature))
        else:
            title.append_text(self._highlight_py_signature(objtype=objtype, signature=signature))
        return title

    @staticmethod
    def _split_py_attribute_signature(signature: str) -> Tuple[str, str]:
        """Split ``name[: type]`` style signatures into name/type parts."""
        cleaned = signature.strip()
        if ":" in cleaned:
            name_part, _, type_part = cleaned.partition(":")
            parsed_type = type_part.strip()
        else:
            name_part = cleaned
            parsed_type = ""
        normalized_name = name_part.strip()
        # Some malformed/empty signatures can yield no usable attribute name.
        # Use a stable placeholder instead of emitting an empty attribute label.
        # Signatures may be qualified (``Class.attr``); render the leaf attribute name.
        leaf_name = normalized_name.rsplit(".", 1)[-1] if normalized_name else ""
        parsed_name = leaf_name or "<attribute>"
        return parsed_name, parsed_type

    def _collect_typed_class_attributes(self, class_node: docutils.nodes.Node) -> Tuple[List[Tuple[str, str, str]], List[docutils.nodes.Node]]:
        """Collect typed ``py:attribute`` style children under a class description."""
        attributes: List[Tuple[str, str, str]] = []
        remaining_children: List[docutils.nodes.Node] = []
        attribute_types = {"attribute", "property", "data", "variable"}

        for child in class_node.children:
            if isinstance(child, py_desc) and child.get("objtype", "").lower() in attribute_types:
                child_options = child.get("options", {}) or {}
                attr_name, sig_type = self._split_py_attribute_signature(child.get("sig", ""))
                raw_type = child_options.get("type")
                if raw_type in (None, ""):
                    raw_type = sig_type
                attr_type = str(raw_type).strip() if raw_type is not None else ""
                if attr_type:
                    description_parts = []
                    for grandchild in child.children:
                        # Field lists are rendered separately by _render_py_field_list
                        # and should not be duplicated in attribute descriptions.
                        if isinstance(grandchild, docutils.nodes.field_list):
                            continue
                        piece = grandchild.astext().replace("\n", " ").strip()
                        if piece:
                            description_parts.append(piece)
                    attributes.append((attr_name, attr_type, " ".join(description_parts).strip()))
                    continue
            remaining_children.append(child)

        return attributes, remaining_children

    def _render_py_class_attribute_table(self, rows: List[Tuple[str, str, str]]) -> List[Any]:
        """Render typed class attributes as an indented list."""
        section_style = self.console.get_style("restructuredtext.py_desc.section", default="bold")
        name_style = self.console.get_style("restructuredtext.py_desc.param_name", default="bold")
        type_style = self.console.get_style("restructuredtext.py_desc.param_type", default="cyan")
        value_style = self.console.get_style("restructuredtext.py_desc.meta_value", default="none")

        renderables: List[Any] = [Text("Attributes", style=section_style)]
        for attr_name, attr_type, attr_description in rows:
            attr_text = Text(attr_name, style=name_style)
            attr_text.append(": ")
            attr_text.append(attr_type, style=type_style)
            line = Text("  ")
            line.append_text(attr_text)
            renderables.append(line)
            if attr_description:
                renderables.append(Text(f"    {attr_description}", style=value_style))
        renderables.append(NewLine())
        return renderables

    def visit_py_desc(self, node) -> None:
        domain = node.get('domain', 'py')
        objtype = node.get('objtype', 'object')
        sig = node.get('sig', '')

        sig_for_title = sig
        if domain in {"py", "js"} and objtype in {"attribute", "property", "data", "variable"}:
            options = node.get('options', {}) or {}
            attr_type = options.get('type')
            attr_value = options.get('value')
            if attr_type:
                sig_for_title += f": {attr_type}"
            if attr_value is not None and attr_value != '':
                sig_for_title += f" = {attr_value}"

        style = self._py_desc_panel_style(objtype, domain=domain)
        title = self._render_py_desc_title(domain=domain, objtype=objtype, signature=sig_for_title)
        body = []
        body_children: List[docutils.nodes.Node]

        if domain == "py" and objtype in {"class", "exception"}:
            typed_attributes, body_children = self._collect_typed_class_attributes(node)
            if typed_attributes:
                body.extend(self._render_py_class_attribute_table(typed_attributes))
        else:
            body_children = list(node.children)

        body.extend(self._render_py_desc_options(node))
        for child in body_children:
            if isinstance(child, docutils.nodes.field_list):
                body.extend(self._render_py_field_list(child))
            else:
                body.extend(self._render_admonition_body([child]))
        body = self._clean_body_for_panel(body)
        self.renderables.append(
            Panel(Group(*body) if body else "", title=title,
                  style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_py_desc(self, node) -> None:
        pass

    def visit_toctree_stub(self, node) -> None:
        style = self.console.get_style("restructuredtext.toctree", default="bold cyan")
        caption = node.get('caption', 'Contents')
        entries = list(node.get('entries', []))
        maxdepth = node.get('maxdepth', 0)  # 0 means unlimited
        reversed_entries = node.get('reversed', False)
        numbered_enabled = node.get('numbered_enabled', False)
        numbered_depth = node.get('numbered', 0)
        marker_style = self.console.get_style("restructuredtext.bullet_list_marker", default="bold yellow")

        if reversed_entries:
            entries.reverse()

        renderables = []
        counters: List[int] = []
        for entry in entries:
            if not entry:
                continue
            # Parse the optional "Display Title <docname>" format.
            if entry.endswith('>') and '<' in entry:
                display = entry[:entry.rfind('<')].strip()
                docname = entry[entry.rfind('<') + 1:-1].strip()
            else:
                display = entry
                docname = entry

            # Derive visual depth from the number of '/' separators in the
            # document name so that entries like "guide/installation" appear
            # indented under their parent path group.
            depth = docname.count('/')
            if maxdepth > 0 and depth >= maxdepth:
                continue  # Omit entries beyond the configured maxdepth.

            if numbered_enabled:
                if depth >= len(counters):
                    counters.extend([0] * (depth + 1 - len(counters)))
                else:
                    counters = counters[:depth + 1]
                counters[depth] += 1

            if numbered_enabled and (numbered_depth == 0 or depth < numbered_depth):
                number_label = ".".join(str(value) for value in counters[:depth + 1])
                marker = "  " * depth + f"{number_label}. "
            else:
                markers = [" • ", " ∘ ", " ▪ "]
                marker = "  " * depth + markers[min(depth, len(markers) - 1)]
            renderables.append(Text(marker + display, style=marker_style))

        self.renderables.append(
            Panel(Group(*renderables) if renderables else "", title=caption,
                  style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_toctree_stub(self, node) -> None:
        pass

    def visit_literalinclude_stub(self, node) -> None:
        style = self.console.get_style("restructuredtext.literalinclude", default="grey58")
        filename = node.get('filename', '<unknown file>')
        content = node.get('content', None)

        if content is not None:
            # File was successfully read by the directive — render as a syntax-
            # highlighted code block with the filename as the panel title.
            language = node.get('language') or self.default_lexer
            linenos = node.get('linenos', self.show_line_numbers)
            self.renderables.append(
                Panel(
                    Syntax(content, language, theme=self.code_theme, line_numbers=linenos),
                    title=filename,
                    border_style=style,
                    box=box.SQUARE,
                )
            )
        else:
            # File was not available (wrong path, no source file, …): show a
            # placeholder panel so the document still renders without crashing.
            self.renderables.append(
                Panel(Text(filename), title="literalinclude", border_style=style)
            )
        raise docutils.nodes.SkipChildren()

    def depart_literalinclude_stub(self, node) -> None:
        pass

    def visit_glossary_block(self, node) -> None:
        style = self.console.get_style("restructuredtext.glossary", default="bold")
        body = self._render_admonition_body(node.children)
        body = self._clean_body_for_panel(body)
        self.renderables.append(
            Panel(Group(*body) if body else "", title="Glossary", style=style, border_style=style)
        )
        raise docutils.nodes.SkipChildren()

    def depart_glossary_block(self, node) -> None:
        pass

    def visit_hlist_block(self, node) -> None:
        """Render an hlist node as a borderless multi-column table."""
        columns = node.get('columns', 2) or 2

        # Collect all list items from the nested bullet_list
        items: List[Any] = []
        for child in node.children:
            if isinstance(child, docutils.nodes.bullet_list):
                for item in child.children:
                    item_renderables = self._render_admonition_body(item.children)
                    if not item_renderables:
                        items.append(Text(""))
                    elif len(item_renderables) == 1:
                        items.append(item_renderables[0])
                    else:
                        items.append(Group(*item_renderables))

        if not items:
            raise docutils.nodes.SkipChildren()

        hlist_table = Table(show_header=False, box=None, padding=(0, 1))
        for _ in range(columns):
            hlist_table.add_column("")

        # Distribute items row-major
        for row_start in range(0, len(items), columns):
            row = list(items[row_start:row_start + columns])
            while len(row) < columns:
                row.append(Text(""))
            hlist_table.add_row(*row)

        self.renderables.append(hlist_table)
        raise docutils.nodes.SkipChildren()

    def depart_hlist_block(self, node) -> None:
        pass

    def visit_subscript(self, node) -> None:
        style = self.console.get_style("restructuredtext.subscript", default="none")
        translated = self._translate_with_fallback(node.astext(), self._SUBSCRIPT)
        self._append_inline_text(translated, style)
        raise docutils.nodes.SkipChildren()

    def visit_superscript(self, node) -> None:
        style = self.console.get_style("restructuredtext.superscript", default="none")
        translated = self._translate_with_fallback(node.astext(), self._SUPERSCRIPT)
        self._append_inline_text(translated, style)
        raise docutils.nodes.SkipChildren()

    def visit_emphasis(self, node) -> None:
        style = self.console.get_style("restructuredtext.emphasis", default="italic")
        self._append_inline_text(node.astext().replace("\n", " "), style)
        raise docutils.nodes.SkipChildren()

    def visit_strong(self, node) -> None:
        style = self.console.get_style("restructuredtext.strong", default="bold")
        self._append_inline_text(node.astext().replace("\n", " "), style)
        raise docutils.nodes.SkipChildren()

    def _make_image_text(self, node: docutils.nodes.image, link_override: Optional[str] = None) -> Text:
        alt, target = None, None
        if ":target:" in node.rawsource:
            target = node.rawsource.split(":target:")[-1].strip()
        if ":alt:" in node.rawsource:
            alt = node.rawsource.split(":alt:")[-1].strip()
        link = link_override or node.get("target", target or "Image") or node.get("uri")
        return Text("🌆 ") + Text(
            node.get("alt", alt or "Image"),
            style=Style(link=link, color="#6088ff"),
        )

    def _render_inline_with_explanation(self, node: docutils.nodes.Node, style_name: str) -> None:
        assert isinstance(node, docutils.nodes.Element)
        style = self.console.get_style(style_name, default="underline")
        explanation = node.get("explanation", "")
        text = node.astext().replace("\n", " ")
        if explanation:
            text = f"{text} ({explanation})"
        self._append_inline_text(text, style)
        raise docutils.nodes.SkipChildren()

    def visit_abbreviation(self, node) -> None:
        self._render_inline_with_explanation(node, "restructuredtext.abbreviation")

    def visit_acronym(self, node) -> None:
        self._render_inline_with_explanation(node, "restructuredtext.acronym")

    def visit_image(self, node) -> None:
        self.renderables.append(self._make_image_text(node))
        raise docutils.nodes.SkipChildren()

    def visit_figure(self, node) -> None:
        # When :target: is given, docutils wraps the image in a reference node
        ref_node = next((c for c in node.children if isinstance(c, docutils.nodes.reference)), None)
        image_node = next((c for c in node.children if isinstance(c, docutils.nodes.image)), None)
        if image_node is None and ref_node is not None:
            image_node = next((c for c in ref_node.children if isinstance(c, docutils.nodes.image)), None)
        caption_node = next((c for c in node.children if isinstance(c, docutils.nodes.caption)), None)
        legend_node = next((c for c in node.children if isinstance(c, docutils.nodes.legend)), None)

        if image_node is not None:
            link_override = ref_node.get("refuri") if ref_node is not None else None
            image_text = self._make_image_text(image_node, link_override=link_override)
        else:
            image_text = Text("🌆 Image")
        caption = caption_node.astext() if caption_node is not None else None
        legend_text = legend_node.astext().replace("\n", " ") if legend_node is not None else None

        border_style = self.console.get_style("restructuredtext.figure_border", default="blue")
        legend_style = self.console.get_style("restructuredtext.figure_legend", default="dim")
        body_renderable = (
            Group(image_text, Text(legend_text, style=legend_style))
            if legend_text is not None
            else image_text
        )
        # Render legend inside the body so it can wrap naturally instead of
        # being cropped in a one-line subtitle slot.
        self.renderables.append(Panel(body_renderable, title=caption, border_style=border_style, expand=False))
        raise docutils.nodes.SkipChildren()

    _BULLET_LIST_MARKERS = [" • ", " ∘ ", " ▪ "]

    @staticmethod
    def _merge_bullet_markers_with_text(renderables: List[Any]) -> List[Any]:
        """Merge marker-only bullet Text nodes with their following Text node.

        List rendering emits the marker and item body as separate Text
        renderables. In contexts that prefix each renderable line-by-line
        (e.g. block quotes), that separation can visually split bullets from
        their text. This helper keeps marker and first text fragment together.
        """
        merged = []
        i = 0
        bullet_markers = {"•", "∘", "▪"}
        while i < len(renderables):
            current = renderables[i]
            if (
                isinstance(current, Text)
                and current.plain.strip() in bullet_markers
                and i + 1 < len(renderables)
                and isinstance(renderables[i + 1], Text)
            ):
                combined = Text()
                combined.append_text(current)
                combined.append_text(renderables[i + 1])
                merged.append(combined)
                i += 2
                continue

            merged.append(current)
            i += 1

        return merged

    def _render_bullet_list(self, node: docutils.nodes.bullet_list, level: int = 0) -> None:
        """Recursively render a bullet list with support for unlimited nesting and any child elements."""
        marker_style = self.console.get_style("restructuredtext.bullet_list_marker", default="bold yellow")
        text_style = self.console.get_style("restructuredtext.bullet_list_text", default="none")
        indent = "  " * level
        marker = self._BULLET_LIST_MARKERS[min(level, len(self._BULLET_LIST_MARKERS) - 1)]
        for list_item in node.children:
            first_content = True
            for child in list_item.children:
                if isinstance(child, docutils.nodes.bullet_list):
                    self._render_bullet_list(child, level + 1)
                elif isinstance(child, docutils.nodes.enumerated_list):
                    self._render_enumerated_list(child, level + 1)
                elif isinstance(child, docutils.nodes.literal_block):
                    if first_content:
                        self.renderables.append(Text(indent + marker, end="", style=marker_style))
                        first_content = False
                    try:
                        self.visit_literal_block(child)
                    except docutils.nodes.SkipChildren:
                        pass
                else:
                    # Use sub-visitor to preserve inline markup (bold, italic, links, etc.)
                    child_renderables = self._render_child_inline(child)
                    if first_content:
                        # Prepend the marker directly onto the first Text
                        # renderable so they form a single unit.  When rendered
                        # inside a Table.grid() cell, separate renderables are
                        # laid out independently, which would put the marker
                        # and its text on different lines.
                        if child_renderables and isinstance(child_renderables[0], Text):
                            combined = Text(indent + marker, end="", style=marker_style)
                            combined.append_text(child_renderables[0])
                            child_renderables[0] = combined
                            self.renderables.extend(child_renderables)
                        else:
                            self.renderables.append(Text(indent + marker, end="", style=marker_style))
                            self.renderables.extend(child_renderables)
                        first_content = False
                    else:
                        # Prepend continuation indent to first renderable if it's text
                        if child_renderables:
                            if isinstance(child_renderables[0], Text):
                                child_renderables[0].stylize(text_style)
                            self.renderables.extend(child_renderables)

    def visit_bullet_list(self, node) -> None:
        self._render_bullet_list(node, level=0)
        is_toc = False
        parent = getattr(node, "parent", None)
        while parent is not None:
            if isinstance(parent, docutils.nodes.topic) and "contents" in parent.get("classes", []):
                is_toc = True
                break
            parent = getattr(parent, "parent", None)
        if not is_toc:
            self.renderables.append(NewLine())
        raise docutils.nodes.SkipChildren()

    @staticmethod
    def _make_enum_marker(enumtype: str, i: int) -> str:
        """Convert an integer *i* to the appropriate enumeration label."""
        from rich_rst._vendor.docutils.utils._roman_numerals import RomanNumeral
        if enumtype == "loweralpha":
            return chr(ord("a") + i - 1)
        elif enumtype == "upperalpha":
            return chr(ord("A") + i - 1)
        elif enumtype == "lowerroman":
            return str(RomanNumeral(i)).lower()
        elif enumtype == "upperroman":
            return str(RomanNumeral(i))
        else:  # arabic (default)
            return str(i)

    def _render_enumerated_list(self, node: docutils.nodes.enumerated_list, level: int = 0) -> None:
        """Recursively render an enumerated list with support for unlimited nesting and any child elements."""
        marker_style = self.console.get_style("restructuredtext.enumerated_list_marker", default="bold yellow")
        text_style = self.console.get_style("restructuredtext.enumerated_text", default="none")
        indent = "  " * level
        enumtype = node.get("enumtype", "arabic")
        prefix = node.get("prefix", "")
        suffix = node.get("suffix", ".")
        start = node.get("start", 1)
        for idx, list_item in enumerate(node.children):
            i = start + idx
            marker = f"{indent} {prefix}{self._make_enum_marker(enumtype, i)}{suffix}"
            first_content = True
            for child in list_item.children:
                if isinstance(child, docutils.nodes.bullet_list):
                    self._render_bullet_list(child, level + 1)
                elif isinstance(child, docutils.nodes.enumerated_list):
                    self._render_enumerated_list(child, level + 1)
                elif isinstance(child, docutils.nodes.literal_block):
                    if first_content:
                        self.renderables.append(Text(marker, end=" ", style=marker_style))
                        first_content = False
                    try:
                        self.visit_literal_block(child)
                    except docutils.nodes.SkipChildren:
                        pass
                else:
                    # Use sub-visitor to preserve inline markup (bold, italic, links, etc.)
                    child_renderables = self._render_child_inline(child)
                    if first_content:
                        self.renderables.append(Text(marker, end=" ", style=marker_style))
                        self.renderables.extend(child_renderables)
                        first_content = False
                    else:
                        # Prepend continuation indent to first renderable if it's text
                        if child_renderables:
                            if isinstance(child_renderables[0], Text):
                                child_renderables[0].stylize(text_style)
                            self.renderables.extend(child_renderables)

    def visit_enumerated_list(self, node) -> None:
        self._render_enumerated_list(node, level=0)
        is_toc = False
        parent = getattr(node, "parent", None)
        while parent is not None:
            if isinstance(parent, docutils.nodes.topic) and "contents" in parent.get("classes", []):
                is_toc = True
                break
            parent = getattr(parent, "parent", None)
        if not is_toc:
            self.renderables.append(NewLine())
        raise docutils.nodes.SkipChildren()

    def visit_literal(self, node) -> None:
        style = self.console.get_style("restructuredtext.inline_codeblock", default="grey78 on grey7")
        self._append_inline_text(node.astext().replace("\n", " "), style)
        raise docutils.nodes.SkipChildren()

    def visit_title_reference(self, node) -> None:
        style = self.console.get_style("restructuredtext.title_reference", default="italic")
        self._append_inline_text(node.astext().replace("\n", " "), style)
        raise docutils.nodes.SkipChildren()

    def _render_parsed_literal_node(self, node: docutils.nodes.Node, parent_style: Optional[Style] = None) -> Text:
        from rich_rst._vendor.docutils import nodes

        if isinstance(node, nodes.Text):
            return Text(node.astext(), style=parent_style)

        result = Text()
        style = parent_style or Style()
        if isinstance(node, nodes.emphasis):
            style = style + self.console.get_style("restructuredtext.emphasis", default="italic")
        elif isinstance(node, nodes.strong):
            style = style + self.console.get_style("restructuredtext.strong", default="bold")
        elif isinstance(node, nodes.literal):
            style = style + self.console.get_style("restructuredtext.inline_codeblock", default="grey78 on grey7")
        elif isinstance(node, nodes.title_reference):
            style = style + self.console.get_style("restructuredtext.title_reference", default="italic")
        elif isinstance(node, nodes.reference):
            uri = node.get("refuri", "")
            if uri:
                style = style + Style(link=uri, color="#6088ff", underline=True)
            else:
                style = style + Style(color="#6088ff", underline=True)
        elif isinstance(node, nodes.inline):
            classes = node.get('classes', [])
            style_name = f"restructuredtext.inline.{classes[0]}" if classes else "restructuredtext.inline"
            style = style + self.console.get_style(style_name, default="none")

        for child in node.children:
            result.append_text(self._render_parsed_literal_node(child, parent_style=style))

        return result

    def visit_literal_block(self, node) -> None:
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].rstrip()
            self.renderables[-1].append_text(Text("\n"))

        if "parsed-literal" in node.get("classes", []):
            content = self._render_parsed_literal_node(node)
            title = "parsed-literal"
            names = node.get('names', [])
            name = node.get('name') or (names[0] if names else None)
            if name:
                title = f"{title} — {name}"

            from rich.syntax import Syntax as RichSyntax
            try:
                theme = RichSyntax.get_theme(self.code_theme or "monokai")
                bg_style = theme.get_background_style()
            except Exception:
                bg_style = Style()

            self.renderables.append(
                Panel(
                    content,
                    style=bg_style,
                    border_style=style,
                    box=box.SQUARE,
                    title=title,
                )
            )
            raise docutils.nodes.SkipChildren()

        lexer, lexer_source = self._find_lexer(node)
        title = lexer if lexer_source == "explicit" else f"{lexer} ({lexer_source})"
        # If the directive supplied a :name: option, include it in the
        # panel title alongside the language identifier.
        names = node.get('names', [])
        name = node.get('name') or (names[0] if names else None)
        if name:
            title = f"{title} — {name}"

        # Determine whether to show line numbers. We show them when:
        # - the directive explicitly requested `:linenos:`, or
        # - there are highlighted lines, or
        # - the global `show_line_numbers` is enabled.
        has_highlight = bool(node.get('highlight_lines'))
        explicit_linenos = bool(node.get('linenos', False))
        show_linenos = bool(explicit_linenos or has_highlight or self.show_line_numbers)

        start_line = int(node.get('start_line', 1))

        self.renderables.append(
            Panel(
                Syntax(
                    node.astext(),
                    lexer,
                    theme=self.code_theme,
                    line_numbers=show_linenos,
                    start_line=start_line,
                    highlight_lines=node.get('highlight_lines'),
                ),
                border_style=style,
                box=box.SQUARE,
                title=title,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_system_message(self, node) -> None:
        self.errors.append(
            Panel(
                Text(node.astext()),
                title=f"System Message: {node.attributes.get('type', '?')}/{node.attributes.get('level', '?')} ({node.attributes.get('source', '?')}, line {node.attributes.get('line', '?')});",
                border_style={None: "none", "INFO": "bold cyan", "WARNING": "bold yellow", "ERROR": "bold red", "SEVERE": "bold magenta", "DEBUG": "bold white"}.get(
                    node.attributes.get("type"), "bold red"
                )
            ),
        )

        # Preserve the offending source snippet in normal output so invalid
        # markup does not silently disappear when show_errors=False.
        # Skip snippets for title formatting errors where the title was already parsed correctly.
        message_text = node.astext().lower()
        is_title_error = any(keyword in message_text for keyword in ("title", "overline", "underline"))

        if not is_title_error:
            for child in node.children:
                if isinstance(child, docutils.nodes.literal_block):
                    snippet = child.astext().replace("\n", " ")
                    if snippet:
                        if self.renderables and isinstance(self.renderables[-1], Text):
                            self.renderables[-1].append_text(Text(snippet, end=" "))
                        else:
                            self.renderables.append(Text(snippet, end=""))
        raise docutils.nodes.SkipChildren()

    def _render_docinfo_value(self, node: docutils.nodes.Node) -> Any:
        has_block_element = any(
            not isinstance(child, (docutils.nodes.Inline, docutils.nodes.Text))
            for child in node.children
        )
        if has_block_element:
            body_renderables = self._render_admonition_body(node.children)
            body_renderables = self._clean_body_for_panel(body_renderables)
            for r in body_renderables:
                if isinstance(r, Text):
                    r.rstrip()
                    r.end = "\n"
            if len(body_renderables) == 1:
                return body_renderables[0]
            elif len(body_renderables) > 1:
                return Group(*body_renderables)
            return ""

        parts = []
        for child in node.children:
            parts.extend(self._render_child_inline(child))

        combined = Text()
        for part in parts:
            if isinstance(part, Text):
                combined.append_text(part)
            else:
                combined.append(str(part))
        return combined

    def _add_to_field_table(self, field_name: str, field_value: Any) -> None:
        """Add a row to the shared field table, creating it if necessary."""
        field_name_style = self.console.get_style("restructuredtext.field_name", default="bold")
        field_value_style = self.console.get_style("restructuredtext.field_value", default="none")
        if isinstance(field_value, str):
            val = Text(field_value, style=field_value_style)
        else:
            val = field_value
        if self.renderables and isinstance(self.renderables[-1], Table):
            possible_table = self.renderables[-1]
            if (possible_table.columns[0].header == "Field Name") and (possible_table.columns[1].header == "Field Value"):
                possible_table.add_row(Text(field_name, style=field_name_style), val)
                return
        table = Table("Field Name", "Field Value", show_lines=True)
        if getattr(self, "_in_docinfo", False):
            docinfo_title_style = self.console.get_style("restructuredtext.docinfo_title", default="bold")
            table.title = Text("Document Information", style=docinfo_title_style)
        table.add_row(Text(field_name, style=field_name_style), val)
        self.renderables.append(table)

    def visit_field(self, node) -> None:
        self._add_to_field_table(node.children[0].astext(), self._render_docinfo_value(node.children[1]))
        raise docutils.nodes.SkipChildren()

    def visit_docinfo(self, node) -> None:
        self._in_docinfo = True

    def depart_docinfo(self, node) -> None:
        self._in_docinfo = False

    def visit_author(self, node) -> None:
        self._add_to_field_table("Author", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_authors(self, node) -> None:
        author_texts = []
        for author in node.children:
            author_texts.append(self._render_docinfo_value(author))
        combined_text = Text("\n").join(author_texts)
        self._add_to_field_table("Authors", combined_text)
        raise docutils.nodes.SkipChildren()

    def visit_organization(self, node) -> None:
        self._add_to_field_table("Organization", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_address(self, node) -> None:
        self._add_to_field_table("Address", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_contact(self, node) -> None:
        self._add_to_field_table("Contact", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_version(self, node) -> None:
        self._add_to_field_table("Version", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_revision(self, node) -> None:
        self._add_to_field_table("Revision", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_status(self, node) -> None:
        self._add_to_field_table("Status", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_date(self, node) -> None:
        self._add_to_field_table("Date", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_copyright(self, node) -> None:
        self._add_to_field_table("Copyright", self._render_docinfo_value(node))
        raise docutils.nodes.SkipChildren()

    def visit_definition_list(self, node) -> None:
        term_style = self.console.get_style("restructuredtext.term_style", default="none")
        classifier_style = self.console.get_style("restructuredtext.classifier_style", default="cyan")
        definitions_style = self.console.get_style("restructuredtext.definitions_style", default="none")
        for child in node.children:
            child_children = child.children
            if not child_children:
                continue

            if len(child_children) == 3:
                # term + one classifier + definition
                term, classifier, definitions = child_children[:3]
                header = (
                    Text(term.astext(), style=term_style, end="")
                    + Text(" : ", end="")
                    + Text(classifier.astext(), style=classifier_style)
                )
                self.renderables.append(header)
                self.renderables.append(Text("\n    ", end=""))
                # Use a sub-visitor so inline markup inside the definition body
                # (bold, italic, links, etc.) is preserved rather than flattened.
                def_renderables = self._render_admonition_body(
                    definitions.children if hasattr(definitions, 'children') else []
                )
                self.renderables.extend(def_renderables)
                self.renderables.append(Text("\n", end=""))
            elif len(child_children) >= 2:
                term = child_children[0]
                # The last child is always the definition; everything between
                # term and definition are additional classifiers.
                definition = child_children[-1]
                if len(child_children) > 2:
                    # Render the first classifier (child_children[1]) as part of
                    # the term header, and handle any extra classifiers plus the
                    # definition body.
                    first_classifier = child_children[1]
                    header = (
                        Text(term.astext(), style=term_style, end="")
                        + Text(" : ", end="")
                        + Text(first_classifier.astext(), style=classifier_style)
                    )
                    self.renderables.append(header)
                    for ch in child_children[2:]:
                        if isinstance(ch, docutils.nodes.classifier):
                            self.renderables.append(
                                Text(" : " + ch.astext(), style=classifier_style)
                            )
                        elif isinstance(ch, docutils.nodes.definition):
                            self.renderables.append(Text("\n    ", end=""))
                            def_renderables = self._render_admonition_body(ch.children)
                            self.renderables.extend(def_renderables)
                            self.renderables.append(Text("\n", end=""))
                        elif isinstance(ch, docutils.nodes.paragraph):
                            self.renderables.append(Text("\n    ", end=""))
                            self.renderables.extend(self._render_child_inline(ch))
                            self.renderables.append(Text("\n", end=""))
                        elif isinstance(ch, docutils.nodes.bullet_list):
                            try:
                                self.visit_bullet_list(ch)
                            except docutils.nodes.SkipChildren:
                                pass
                        elif isinstance(ch, docutils.nodes.enumerated_list):
                            try:
                                self.visit_enumerated_list(ch)
                            except docutils.nodes.SkipChildren:
                                pass
                        elif isinstance(ch, docutils.nodes.literal_block):
                            try:
                                self.visit_literal_block(ch)
                            except docutils.nodes.SkipChildren:
                                pass
                        elif isinstance(ch, docutils.nodes.literal):
                            try:
                                self.visit_literal(ch)
                            except docutils.nodes.SkipChildren:
                                pass
                        elif isinstance(ch, docutils.nodes.block_quote):
                            try:
                                self.visit_block_quote(ch)
                            except docutils.nodes.SkipChildren:
                                pass
                else:
                    # len == 2: term + definition (no classifier).
                    # Rename clarity: `definition` is child_children[1], NOT a
                    # classifier — the old variable name was misleading.
                    self.renderables.append(
                        Text(term.astext(), style=term_style)
                        + Text("\n    ", end="")
                        + Text(definition.astext().replace("\n", " "), style=definitions_style)
                        + Text("\n      ", end="")
                    )
            else:
                term = child_children[0]
                self.renderables.append(Text(term.astext(), style=term_style) + Text("\n", end=""))
        raise docutils.nodes.SkipChildren()

    def visit_option_list(self, node) -> None:
        option_string_style = self.console.get_style("restructuredtext.option_string", default="none")
        option_argument_style = self.console.get_style("restructuredtext.option_argument", default="none")
        option_child_text_separator_style = self.console.get_style(
            "restructuredtext.option_child_text_separator", default="none"
        )
        option_description_style = self.console.get_style("restructuredtext.option_description", default="none")
        for option_list_item in node.children:
            option_group, description = option_list_item.children
            # option_group.child_text_separator.join(map(lambda x: x.astext(), option_group.children)))
            option_text = Text(end="")
            for option in option_group.children:
                try:
                    option_string, option_argument = option.children
                except ValueError:
                    option_string, option_argument = option.children[0], None
                option_text += (
                    Text(option_string.astext(), style=option_string_style)
                    + (Text(option_argument.astext(), style=option_argument_style) if option_argument else Text())
                    + (
                        Text(option_group.child_text_separator, style=option_child_text_separator_style)
                        if len(option_group.children) > 1
                        else Text()
                    )
                )
            if description:
                option_text += Text("\n    ")
                option_text += Text(description.astext(), style=option_description_style)
            self.renderables.append(option_text + Text("\n"))
        raise docutils.nodes.SkipChildren()

    def visit_doctest_block(self, node) -> None:
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        self.renderables.append(
            Panel(
                Syntax(node.astext(), "pycon", theme=self.code_theme, line_numbers=bool(self.show_line_numbers)),
                border_style=style,
                box=box.SQUARE,
                title="doctest block",
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_block_quote(self, node) -> None:
        text_style = self.console.get_style("restructuredtext.blockquote_text", default="white")
        marker_style = self.console.get_style(
            "restructuredtext.blockquote_attribution_marker", default="bright_magenta"
        )
        author_style = self.console.get_style("restructuredtext.blockquote_attribution_text", default="grey89")
        children = list(node.children)
        attribution = children[-1] if children and isinstance(children[-1], docutils.nodes.attribution) else None
        paragraphs = children[:-1] if attribution else children

        for index, paragraph in enumerate(paragraphs):
            if index:
                self.renderables.append(Text("▌", style=marker_style))
            # Use a sub-visitor so inline markup (bold, italic, links, …)
            # inside the paragraph is preserved instead of being flattened by
            # astext().
            para_renderables = self._render_child_inline(paragraph)
            para_renderables = self._merge_bullet_markers_with_text(para_renderables)
            if para_renderables and isinstance(para_renderables[0], Text):
                first = para_renderables[0]
                first.rstrip()
                # Apply the block-quote body style so tests that check for a
                # white span still find one.
                first.stylize(text_style, 0, len(first))
                combined = Text("▌ ", style=marker_style)
                combined.append_text(first)
                self.renderables.append(combined)
                # Prepend the same `▌ ` marker to every subsequent Text so
                # that deeply nested block quotes accumulate the correct number
                # of markers at every nesting level.
                for r in para_renderables[1:]:
                    if isinstance(r, Text):
                        combined_r = Text("▌ ", style=marker_style)
                        combined_r.append_text(r)
                        self.renderables.append(combined_r)
                    else:
                        self.renderables.append(r)
            else:
                self.renderables.append(Text("▌ ", style=marker_style))
                self.renderables.extend(para_renderables)

        if attribution:
            self.renderables.append(NewLine())
            self.renderables.append(
                Text("  \u2014 " + attribution.astext(), style=author_style)
            )
        else:
            self.renderables.append(NewLine())

        raise docutils.nodes.SkipChildren()

    def _render_line_block(self, node: docutils.nodes.line_block, indent: int = 0) -> None:
        """Recursively render a line_block node, preserving nested indentation."""
        prefix = "    " * indent
        for child in node.children:
            if isinstance(child, docutils.nodes.line_block):
                self._render_line_block(child, indent + 1)
            elif isinstance(child, docutils.nodes.line):
                self.renderables.append(Text(prefix + child.astext()))

    def visit_line_block(self, node) -> None:
        self._render_line_block(node)
        raise docutils.nodes.SkipChildren()

    def _collect_body_renderables(self, children: List[docutils.nodes.Node]) -> List[Any]:
        """Render a list of body nodes into renderables, returning the collected list.

        Uses a sub-visitor for each child so that inline markup (bold, italic,
        links, inline code, etc.) is preserved throughout.
        """
        result = []
        for child in children:
            result.extend(self._render_child_inline(child))
        return result

    def visit_topic(self, node) -> None:
        style = self.console.get_style("restructuredtext.topic", default="bold cyan")
        children = list(node.children)
        title = ""
        body_start = 0
        if children and isinstance(children[0], docutils.nodes.title):
            title = children[0].astext()
            body_start = 1

        body_renderables = self._collect_body_renderables(children[body_start:])
        body_renderables = self._clean_body_for_panel(body_renderables)

        if body_renderables:
            self.renderables.append(
                Panel(Group(*body_renderables), title=title, style=style, border_style=style)
            )
        else:
            self.renderables.append(Panel("", title=title, style=style, border_style=style))
        raise docutils.nodes.SkipChildren()

    def visit_sidebar(self, node) -> None:
        children = list(node.children)
        title = ""
        body_children = children

        if body_children and isinstance(body_children[0], docutils.nodes.title):
            title = body_children[0].astext()
            body_children = body_children[1:]

        subtitle = ""
        if body_children and isinstance(body_children[0], docutils.nodes.subtitle):
            subtitle = body_children[0].astext()
            body_children = body_children[1:]

        if body_children and isinstance(body_children[0], docutils.nodes.field_list):
            field_list = body_children[0]
            for field in field_list.children:
                if len(field.children) >= 2:
                    field_name = field.children[0].astext().strip().lower()
                    field_body = field.children[1]
                    if field_name == "subtitle":
                        subtitle = field_body.astext().strip()
            body_children = body_children[1:]

        # Use _collect_body_renderables so inline markup in the sidebar body is
        # preserved instead of being flattened by astext().
        body_renderables = self._collect_body_renderables(body_children)
        body_renderables = self._clean_body_for_panel(body_renderables)
        content = Group(*body_renderables) if body_renderables else ""
        self.renderables.append(Panel(content, title=title, subtitle=subtitle, expand=False))

        raise docutils.nodes.SkipChildren()

    def visit_transition(self, node) -> None:
        style = self.console.get_style("restructuredtext.hr", default="yellow")
        self.renderables.append(Rule(style=style))

    def visit_math_block(self, node) -> None:
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].rstrip()
            self.renderables[-1].append_text(Text("\n"))
        converted = _convert_math_to_unicode(node.astext())
        label = node.get("label")
        title = f"math - {label}" if label else "math"
        self.renderables.append(
            Panel(
                Text(converted),
                border_style=style,
                box=box.SQUARE,
                title=title,
            )
        )
        raise docutils.nodes.SkipChildren()

    def visit_math(self, node) -> None:
        """Render inline math with Unicode approximations where possible."""
        style = self.console.get_style("restructuredtext.math", default="italic")
        converted = _convert_math_to_unicode(node.astext().replace("\n", " "))
        self._append_inline_text(converted, style)
        raise docutils.nodes.SkipChildren()

    def visit_citation(self, node) -> None:
        self.citations.append(Align(self._format_labelled_node(node), "left"))
        raise docutils.nodes.SkipChildren()

    def visit_citation_reference(self, node) -> None:
        style = self.console.get_style("restructuredtext.citation_reference", default="grey74")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(node.astext().replace("\n", " "), style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(node.astext().replace("\n", " "), style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_header(self, node) -> None:
        style = self.console.get_style("restructuredtext.caption", default="bold")
        body = self._render_admonition_body(node.children)
        body = self._clean_body_for_panel(body)
        content = Group(*body) if body else ""
        self.renderables.insert(0, Panel(Align(content, "center"), title="caption", box=box.DOUBLE, style=style))
        raise docutils.nodes.SkipChildren()

    def visit_footer(self, node) -> None:
        body = self._render_admonition_body(node.children)
        body = self._clean_body_for_panel(body)
        for r in body:
            self.footer.append(Align(r, "center"))
        raise docutils.nodes.SkipChildren()

    def visit_footnote_reference(self, node) -> None:
        style = self.console.get_style("restructuredtext.footnote_reference", default="grey74")
        newline = '\n'
        text = f"[{node.astext().replace(newline, ' ')}]"
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(text, style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(text, style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_substitution_reference(self, node) -> None:
        style = self.console.get_style("restructuredtext.substitution_reference", default="none")
        text = node.astext().replace("\n", " ")
        if self.renderables and isinstance(self.renderables[-1], Text):
            self.renderables[-1].append(text, style=style)
            raise docutils.nodes.SkipChildren()
        self.renderables.append(Text(text, style=style, end=""))
        raise docutils.nodes.SkipChildren()

    def visit_footnote(self, node) -> None:
        self.footer.append(Align(self._format_labelled_node(node), "left"))
        raise docutils.nodes.SkipChildren()

    def visit_generated(self, node) -> None:
        self.footer.append(Align(node.astext(), "left"))
        raise docutils.nodes.SkipChildren()

    def visit_pending(self, node) -> None:
        raise docutils.nodes.SkipChildren()

    def visit__colSpan(self, node) -> None:
        raise docutils.nodes.SkipNode()

    def visit__rowSpan(self, node) -> None:
        raise docutils.nodes.SkipNode()

    def visit_problematic(self, node) -> None:
        # Keep problematic inline source visible in the main render output.
        problematic_style = self.console.get_style("restructuredtext.problematic", default="none")
        problematic_text = node.astext().replace("\n", " ")
        if problematic_text:
            if self.renderables and isinstance(self.renderables[-1], Text):
                self.renderables[-1].append(problematic_text, style=problematic_style)
            else:
                self.renderables.append(Text(problematic_text, style=problematic_style, end=""))

        self.errors.append(
            Panel(
                Syntax(node.astext(), lexer="rst", theme=self.code_theme),
                title="System Message: Problematic Element",
                border_style="bold red",
            ),
        )
        raise docutils.nodes.SkipChildren()

    def visit_raw(self, node) -> None:
        style = self.console.get_style("restructuredtext.literal_block_border", default="grey58")
        lexer, _ = self._find_lexer(node)
        text = node.astext()
        title = "stripped raw html" if lexer == "html" else ("raw " + lexer if lexer is not None else "raw")

        if lexer == "html":
            text = strip_tags(text)
            # Stripping HTML tags leaves behind plain text
            lexer = None

        self.renderables.append(
            Panel(
                Syntax(text, lexer, theme=self.code_theme, line_numbers=bool(self.show_line_numbers)),
                border_style=style,
                box=box.SQUARE,
                title=title,
            )
        )
        raise docutils.nodes.SkipChildren()

    # ── spanning table renderer ───────────────────────────────────────────────

    @staticmethod
    def _spanning_table(
        grid: List[List[Any]],
        col_widths: List[int],
        header_rows: int,
        title: Optional[str],
        header_style: Any,
        cell_style: Any,
        console: Console,
    ) -> "Group":
        """Build a Rich Group that renders a table with proper cspan/rspan merging.

        *grid[r][c]* is either ``(renderable, cspan, rspan)`` for a real cell or
        ``None`` for a placeholder occupied by a span from another cell.
        *col_widths[c]* is the inner character width of column *c* (excluding borders).
        """
        nrows = len(grid)
        ncols = len(col_widths)
        lines: List[Text] = []

        # ── box chars ──────────────────────────────────────────────────────
        # Top border (heavy)
        TL, TH, TM, TR = "┏", "━", "┳", "┓"
        # Head/body separator
        SL, SH, SM, SR = "┡", "━", "╇", "┩"
        # Body row separator
        ML, MH, MM, MR = "├", "─", "┼", "┤"
        # Bottom border
        BL, BH, BM, BR = "└", "─", "┴", "┘"
        # Vertical content borders: header uses heavy ┃, body uses light │
        VH, VB = "┃", "│"

        # ── helpers ────────────────────────────────────────────────────────
        origin_cache: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}

        def _origin(r: int, c: int) -> Optional[Tuple[int, int]]:
            """Return (origin_row, origin_col) for the real cell covering (r, c)."""
            key = (r, c)
            cached = origin_cache.get(key, None)
            if cached is not None or key in origin_cache:
                return cached

            for rr in range(r, -1, -1):
                for cc in range(c, -1, -1):
                    cell = grid[rr][cc]
                    if cell is None:
                        continue
                    _, csp, rsp = cell
                    if rr <= r <= rr + rsp and cc <= c <= cc + csp:
                        origin_cache[key] = (rr, cc)
                        return (rr, cc)

            origin_cache[key] = None
            return None

        def _rspan_continues(row_above: int, c: int) -> bool:
            """True if a cell covering (row_above, c) extends to the next row."""
            if row_above < 0 or row_above + 1 >= nrows:
                return False
            for rr in range(row_above, -1, -1):
                for cc in range(c, -1, -1):
                    cell = grid[rr][cc]
                    if cell is None:
                        continue
                    _, csp, rsp = cell
                    if cc <= c <= cc + csp and rr <= row_above <= rr + rsp:
                        return row_above < rr + rsp
            return False

        def _cspan_continues(r: int, c: int) -> bool:
            """True if column c is a cspan continuation of the cell to its left in row r."""
            left_origin = _origin(r, c - 1)
            here_origin = _origin(r, c)
            return left_origin is not None and left_origin == here_origin

        def _is_header(r: int) -> bool:
            return r < header_rows

        def _has_vborder(r: int, c: int) -> bool:
            """True iff row *r* has a vertical separator between column *c* and *c+1*."""
            return _origin(r, c) != _origin(r, c + 1)

        def _segments_to_lines(line_segments: List[Segment]) -> List[Text]:
            lines: List[Text] = [Text()]
            for seg in line_segments:
                if seg.control or not seg.text:
                    continue
                parts = seg.text.split("\n")
                for index, part in enumerate(parts):
                    if part:
                        lines[-1].append(part, seg.style)
                    if index < len(parts) - 1:
                        lines.append(Text())
            return lines

        def _row_style(r: int) -> Any:
            return header_style if _is_header(r) else cell_style

        cell_render_cache: Dict[Tuple[int, int], List[Text]] = {}

        def _render_cell_lines(r: int, c: int) -> List[Text]:
            """Render cell content into styled lines sized to its spanned width."""
            key = (r, c)
            if key in cell_render_cache:
                return cell_render_cache[key]

            cell = grid[r][c]
            if cell is None:
                cell_render_cache[key] = []
                return []

            content, csp, _ = cell
            avail = sum(col_widths[c:c + csp + 1]) + 3 * csp
            style = _row_style(r)
            if avail <= 0:
                cell_render_cache[key] = [Text("")]
                return cell_render_cache[key]

            options = console.options.update(width=avail, max_width=avail)
            render_target = Styled(content, style) if style else (content if content is not None else Text(""))
            rendered_lines = console.render_lines(
                render_target,
                options=options,
                style=None,
                pad=True,
                new_lines=False,
            )

            lines: List[Text] = []
            for rendered in rendered_lines:
                lines.extend(_segments_to_lines(rendered))
            if not lines:
                lines = [Text(" " * avail, style=style)]
            normalized: List[Text] = []
            for line in lines:
                current_width = cell_len(line.plain)
                if current_width > avail:
                    line.truncate(avail, overflow="crop", pad=False)
                elif current_width < avail:
                    line.append(" " * (avail - current_width), style=style)
                normalized.append(line)

            cell_render_cache[key] = normalized
            return normalized

        # ── separator line ─────────────────────────────────────────────────

        def _sep(above: Optional[int], below: Optional[int]) -> Text:
            """Horizontal rule between rows *above* and *below* (None = table edge)."""
            is_top = above is None
            is_bot = below is None
            is_head_sep = (
                above is not None
                and below is not None
                and above == header_rows - 1
                and below == header_rows
            )
            # Separator between two header rows (not the final header→body boundary).
            is_inner_header_sep = (
                above is not None
                and below is not None
                and _is_header(above)
                and _is_header(below)
            )
            if is_top:
                L, H, _M, R = TL, TH, TM, TR
            elif is_bot:
                L, H, _M, R = BL, BH, BM, BR
            elif is_head_sep:
                L, H, _M, R = SL, SH, SM, SR
            elif is_inner_header_sep:
                L, H, _M, R = "┣", "━", "╋", "┫"
            else:
                L, H, _M, R = ML, MH, MM, MR

            # Left border: use heavy ┃ inside header, light │ in body, for rspan continuations
            rc0 = _rspan_continues(above, 0) if above is not None and not is_top else False
            V_sep = VH if is_inner_header_sep else VB
            if rc0 and not is_top and not is_bot:
                s = V_sep
            else:
                s = L
            for c in range(ncols):
                rc = _rspan_continues(above, c) if above is not None and not is_top else False
                if rc:
                    s += " " * (col_widths[c] + 2)
                else:
                    s += H * (col_widths[c] + 2)

                if c < ncols - 1:
                    lrc = rc
                    rrc = (_rspan_continues(above, c + 1) if above is not None and not is_top else False)
                    if lrc and rrc:
                        same_origin = (
                            above is not None
                            and _origin(above, c) is not None
                            and _origin(above, c) == _origin(above, c + 1)
                        )
                        # When both columns continue the same merged rowspan cell,
                        # there is no interior boundary at this separator.
                        s += " " if same_origin else V_sep
                    elif lrc or rrc:
                        if is_inner_header_sep:
                            s += "┣" if lrc else "┫"
                        else:
                            s += "├" if lrc else "┤"
                    else:
                        has_up = above is not None and not is_top and _has_vborder(above, c)
                        has_dn = below is not None and _has_vborder(below, c)
                        if has_up and has_dn:
                            if is_head_sep:
                                s += SM
                            elif is_inner_header_sep:
                                s += "╋"
                            else:
                                s += MM
                        elif has_up:
                            # ┻ = heavy horizontal + upward arm (head sep and inner header)
                            s += "┻" if (is_head_sep or is_inner_header_sep) else BM
                        elif has_dn:
                            # ┯/┳ = heavy horizontal + downward arm
                            if is_top:
                                s += TM
                            elif is_head_sep:
                                s += "┯"
                            elif is_inner_header_sep:
                                s += "┳"
                            else:
                                s += "┬"
                        else:
                            s += H  # no junction — just continue horizontal line
            # Right border
            rcN = _rspan_continues(above, ncols - 1) if above is not None and not is_top else False
            if rcN and not is_top and not is_bot:
                s += V_sep
            else:
                s += R
            return Text(s)

        # ── content line ───────────────────────────────────────────────────

        def _row_height(r: int) -> int:
            """Physical line count for a logical row after rendering cell content."""
            height = 1
            c = 0
            while c < ncols:
                cell = grid[r][c]
                if cell is None:
                    c += 1
                    continue
                _, csp, _ = cell
                height = max(height, len(_render_cell_lines(r, c)))
                c += 1 + csp
            return height

        def _content(r: int, line_no: int) -> Text:
            """One physical content line for logical row *r*."""
            is_hdr = _is_header(r)
            V = VH if is_hdr else VB
            style = _row_style(r)
            line = Text(V)
            c = 0
            while c < ncols:
                cell = grid[r][c]
                if cell is not None:
                    _, csp, _ = cell
                    avail = sum(col_widths[c:c + csp + 1]) + 3 * csp
                    rendered = _render_cell_lines(r, c)
                    inner = rendered[line_no] if line_no < len(rendered) else Text(" " * avail, style=style)
                    line.append(" ", style=style)
                    line.append_text(inner)
                    line.append(" ", style=style)
                    if c + csp < ncols - 1:
                        line.append(V)
                    c += 1 + csp  # jump past all placeholder columns
                else:
                    # Placeholder covered by a rowspan from an origin above.
                    # If this column is the first covered column for that origin
                    # in this row, render the full merged placeholder width.
                    origin = _origin(r, c)
                    if origin is not None and origin[1] == c:
                        span_end = c
                        while span_end + 1 < ncols and _origin(r, span_end + 1) == origin:
                            span_end += 1
                        csp = span_end - c
                        avail = sum(col_widths[c:span_end + 1]) + 3 * csp
                        line.append(" " * (avail + 2), style=style)
                        if span_end < ncols - 1:
                            line.append(V)
                        c = span_end + 1
                    else:
                        line.append(" " * (col_widths[c] + 2), style=style)
                        if c < ncols - 1 and not _cspan_continues(r, c + 1):
                            line.append(V)
                        c += 1
            line.append(V)
            return line

        def _is_placeholder_row(r: int) -> bool:
            """True when a row is fully covered by rowspans from above."""
            c = 0
            while c < ncols:
                if grid[r][c] is not None:
                    return False
                if _origin(r, c) is None:
                    return False
                c += 1
            return True

        # ── assemble lines ─────────────────────────────────────────────────

        if title:
            total = cell_len(_sep(None, 0).plain) if nrows else (sum(col_widths) + 3 * ncols + 1)
            lines.append(Text(title.center(total), style="italic"))

        for r in range(nrows):
            above = r - 1 if r > 0 else None
            is_placeholder = _is_placeholder_row(r)
            sep_line = _sep(above, r)
            if not (is_placeholder and all(ch in f" {VB}{VH}" for ch in sep_line.plain)):
                lines.append(sep_line)
            if is_placeholder:
                continue
            for line_no in range(_row_height(r)):
                lines.append(_content(r, line_no))

        lines.append(_sep(nrows - 1, None))
        return Group(*lines)

    # ── table visitor ─────────────────────────────────────────────────────

    def visit_table(self, node) -> None:
        header_style = self.console.get_style("restructuredtext.table_header", default="bold")
        cell_style = self.console.get_style("restructuredtext.table_cell", default="none")

        # Extract optional caption/title and the tgroup
        title = None
        tgroup = None
        for child in node.children:
            if isinstance(child, (docutils.nodes.title, docutils.nodes.caption)):
                title = child.astext()
            elif isinstance(child, docutils.nodes.tgroup):
                tgroup = child

        if tgroup is None:
            raise docutils.nodes.SkipChildren()

        # Count total columns from colspec elements (authoritative column count)
        num_cols = sum(1 for c in tgroup.children if isinstance(c, docutils.nodes.colspec))

        # Find thead and tbody within tgroup
        thead = None
        tbody = None
        for child in tgroup.children:
            if isinstance(child, docutils.nodes.thead):
                thead = child
            elif isinstance(child, docutils.nodes.tbody):
                tbody = child

        if tbody is None:
            raise docutils.nodes.SkipChildren()

        # Fallback column count when colspec elements are absent
        if num_cols == 0:
            if thead is not None and thead.children:
                num_cols = sum(1 + e.get("morecols", 0) for e in thead.children[0].children)
            elif tbody.children:
                num_cols = sum(1 + e.get("morecols", 0) for e in tbody.children[0].children)

        def _render_entry_content(entry: docutils.nodes.Node) -> Any:
            """Render an entry node with a sub-visitor to preserve inline RST markup."""
            sub_visitor = self._make_sub_visitor()
            for child in entry.children:
                child.walkabout(sub_visitor)
            renderables = sub_visitor.renderables
            if not renderables:
                return Text("", style=cell_style)
            has_list = any(
                isinstance(child, (docutils.nodes.bullet_list, docutils.nodes.enumerated_list))
                for child in entry.children
            )
            if has_list:
                # Table cells should keep list items compact: one visible line
                # per item without paragraph/list trailing blank lines.
                renderables = self._merge_bullet_markers_with_text(renderables)
                renderables = [r for r in renderables if not isinstance(r, NewLine)]
                if not renderables:
                    return Text("", style=cell_style)
                rendered_lines = self.console.render_lines(
                    Group(*renderables),
                    options=self.console.options.update(width=2048, max_width=2048),
                    pad=False,
                    new_lines=False,
                )
                compact_lines: List[Text] = []
                for line in rendered_lines:
                    line_text = Text.assemble(
                        *[(seg.text, seg.style or Style()) for seg in line if not seg.control]
                    )
                    line_text.rstrip()
                    if line_text.plain.strip():
                        compact_lines.append(line_text)
                if not compact_lines:
                    return Text("", style=cell_style)
                if len(compact_lines) == 1:
                    return compact_lines[0]
                return Group(*compact_lines)
            # depart_paragraph appends "\n\n" to trailing Text renderables; strip
            # it so cells don't carry extra vertical whitespace.  Also strip any
            # leading whitespace left over after span-role nodes (:cspan:/:rspan:)
            # are removed (the space between the role and the following text is
            # preserved as a leading space in the text node).
            for i, r in enumerate(renderables):
                if isinstance(r, Text):
                    r.rstrip()
                    leading = len(r.plain) - len(r.plain.lstrip())
                    if leading:
                        trimmed = r[leading:]
                        trimmed.end = r.end
                        renderables[i] = trimmed
            if len(renderables) == 1:
                return renderables[0]
            return Group(*renderables)

        def _build_row_cells(row: docutils.nodes.Node, occupied_cols: set) -> Tuple[List[Any], Dict[int, int]]:
            """Build cell renderables for one body row.

            Accounts for columns already occupied by rowspans from earlier rows
            and for cells that span multiple columns (morecols).  Returns a tuple
            of (cells, new_rowspans) where new_rowspans maps col_idx to the
            morerows value for any spanning cells introduced by this row.
            """
            cells = []
            new_rowspans = {}
            col_idx = 0
            entry_iter = iter(row.children)

            while col_idx < num_cols:
                if col_idx in occupied_cols:
                    # Column is covered by a rowspan from a previous row
                    cells.append(Text("", style=cell_style))
                    col_idx += 1
                    continue

                entry = next(entry_iter, None)
                if entry is None:
                    # All entries for this row have been consumed; pad remaining
                    # columns with empty cells (can happen with complex spanning).
                    cells.append(Text("", style=cell_style))
                    col_idx += 1
                    continue

                morecols = entry.get("morecols", 0)
                morerows = entry.get("morerows", 0)

                cells.append(_render_entry_content(entry))

                # Record any new rowspan introduced by this cell
                if morerows > 0:
                    for span_col in range(col_idx, col_idx + 1 + morecols):
                        new_rowspans[span_col] = morerows

                # Pad empty cells for additional spanned columns (colspan)
                for _ in range(morecols):
                    cells.append(Text("", style=cell_style))

                col_idx += 1 + morecols

            return cells, new_rowspans

        # ── detect whether any cell carries a span ────────────────────────────
        def _any_spans(section: docutils.nodes.Node) -> bool:
            for row in section.children:
                for e in row.children:
                    if e.get("morecols", 0) or e.get("morerows", 0):
                        return True
            return False

        has_spans = _any_spans(tbody) or (thead is not None and _any_spans(thead))

        if has_spans:
            # ── build a logical grid for the spanning renderer ────────────────
            num_header_rows = len(thead.children) if thead else 0
            grid: List[List[Any]] = []
            # rspan_active[col] = remaining body rows this col is still occupied
            rspan_active: Dict[int, int] = {}

            all_rows: List[Tuple[docutils.nodes.Node, bool]] = []
            if thead:
                for row in thead.children:
                    all_rows.append((row, True))
            for row in tbody.children:
                all_rows.append((row, False))

            for row_node, _ in all_rows:
                grid_row: List[Any] = [None] * num_cols
                col = 0
                entry_iter = iter(row_node.children)
                while col < num_cols:
                    if col in rspan_active:
                        rspan_active[col] -= 1
                        if rspan_active[col] <= 0:
                            del rspan_active[col]
                        col += 1
                        continue
                    entry = next(entry_iter, None)
                    if entry is None:
                        col += 1
                        continue
                    mc = entry.get("morecols", 0)
                    mr = entry.get("morerows", 0)
                    content = _render_entry_content(entry)
                    grid_row[col] = (content, mc, mr)
                    if mr > 0:
                        for span_c in range(col, col + mc + 1):
                            rspan_active[span_c] = mr
                    col += 1 + mc
                grid.append(grid_row)

            # ── calculate column widths from non-spanning cells ───────────────
            # Per-table-call cache; dropped after this visit_table invocation.
            # Keep identity pairs instead of id(...) keys so reuse of object ids
            # can never return stale data.
            rendered_plain_lines_cache: List[Tuple[Any, List[str]]] = []

            def _rendered_plain_lines(renderable: Any) -> List[str]:
                if renderable is None:
                    return []
                for cached_renderable, cached_lines in rendered_plain_lines_cache:
                    if cached_renderable is renderable:
                        return cached_lines
                lines = self.console.render_lines(
                    renderable,
                    options=self.console.options.update(width=2048, max_width=2048),
                    pad=False,
                    new_lines=False,
                )
                plain_lines: List[str] = []
                for line in lines:
                    plain = "".join(seg.text for seg in line if not seg.control)
                    plain_lines.append(plain)
                rendered_plain_lines_cache.append((renderable, plain_lines))
                return plain_lines

            def _plain_w(renderable: Any) -> int:
                lines = _rendered_plain_lines(renderable)
                return max((cell_len(line) for line in lines), default=0)

            def _min_token_w(renderable: Any) -> int:
                lines = _rendered_plain_lines(renderable)
                widest = 1
                for line in lines:
                    for token in line.split():
                        widest = max(widest, cell_len(token))
                return min(20, widest)

            col_widths = [1] * num_cols
            col_min_widths = [1] * num_cols
            for grid_row in grid:
                for c, cell in enumerate(grid_row):
                    if cell is None:
                        continue
                    content, mc, mr = cell
                    if mc == 0:
                        col_widths[c] = max(col_widths[c], _plain_w(content))
                        col_min_widths[c] = max(col_min_widths[c], _min_token_w(content))

            # Widen for spanning cells that need more space
            for grid_row in grid:
                for c, cell in enumerate(grid_row):
                    if cell is None:
                        continue
                    content, mc, mr = cell
                    if mc > 0:
                        available = sum(col_widths[c:c + mc + 1]) + 3 * mc
                        needed = _plain_w(content)
                        if needed > available:
                            col_widths[c + mc] += needed - available

            # Clamp spanning-table width to the available console width so long
            # text wraps inside cells instead of producing overflow and broken
            # visual alignment in narrow terminals.
            max_total_width = max(1, self.console.options.max_width)

            def _table_width(widths: List[int]) -> int:
                return sum(widths) + 3 * len(widths) + 1

            overflow = _table_width(col_widths) - max_total_width

            def _shrink_to_floor(floors: List[int], remaining: int) -> int:
                while remaining > 0:
                    reducible = [i for i, w in enumerate(col_widths) if w > floors[i]]
                    if not reducible:
                        break
                    reducible.sort(key=lambda i: col_widths[i], reverse=True)
                    per_col_cut = max(1, remaining // len(reducible))
                    changed = 0
                    for idx in reducible:
                        if remaining <= 0:
                            break
                        max_cut = col_widths[idx] - floors[idx]
                        cut = min(max_cut, per_col_cut, remaining)
                        if cut <= 0:
                            continue
                        col_widths[idx] -= cut
                        remaining -= cut
                        changed += cut
                    if changed == 0:
                        break
                return remaining

            # Prefer preserving enough width to avoid one-character vertical
            # stacks in key columns, then fall back to absolute minimum when
            # terminal width is very constrained.
            overflow = _shrink_to_floor(col_min_widths, overflow)
            if overflow > 0:
                overflow = _shrink_to_floor([1] * num_cols, overflow)

            self.renderables.append(
                self._spanning_table(
                    grid, col_widths, num_header_rows,
                    title, header_style, cell_style,
                    self.console,
                )
            )
            raise docutils.nodes.SkipChildren()

        # ── no spans: use Rich Table for best formatting ──────────────────────
        has_header = thead is not None and bool(thead.children)
        rich_table = Table(
            show_header=has_header,
            title=title,
            header_style=header_style,
            show_lines=True,
        )

        if thead is not None and thead.children:
            header_row = thead.children[0]
            col_idx = 0
            for entry in header_row.children:
                morecols = entry.get("morecols", 0)
                rich_table.add_column(entry.astext().replace("\n", " ").strip(), style=cell_style)
                for _ in range(morecols):
                    rich_table.add_column("", style=cell_style)
                col_idx += 1 + morecols
            while col_idx < num_cols:
                rich_table.add_column("", style=cell_style)
                col_idx += 1
        else:
            for _ in range(num_cols):
                rich_table.add_column("", style=cell_style)

        rowspan_remaining: Dict[int, int] = {}
        for row in tbody.children:
            occupied = {col for col, rem in rowspan_remaining.items() if rem > 0}
            cells, new_rowspans = _build_row_cells(row, occupied)
            for col in list(occupied):
                rowspan_remaining[col] -= 1
                if rowspan_remaining[col] <= 0:
                    del rowspan_remaining[col]
            rowspan_remaining.update(new_rowspans)
            rich_table.add_row(*cells)

        self.renderables.append(rich_table)
        raise docutils.nodes.SkipChildren()

