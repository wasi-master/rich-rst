"""Tests for the register_visitor decorator form, unregister_visitor,
and list_registered_visitors (item 9d).
"""
import pytest

from rich.text import Text
from rich_rst import RSTVisitor
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core


# ── Decorator form ────────────────────────────────────────────────────────────

def test_register_visitor_decorator_form_visit_called(make_visitor):
    """@RSTVisitor.register_visitor(NodeClass) must register the decorated fn."""

    class _DecoratorNode(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    visited = []

    @RSTVisitor.register_visitor(_DecoratorNode)
    def visit_decorator_node(visitor, node):
        visited.append(node.__class__.__name__)
        raise docutils.nodes.SkipChildren()

    try:
        node = _DecoratorNode()
        visitor = make_visitor("")
        node.walkabout(visitor)
        assert "_DecoratorNode" in visited
    finally:
        RSTVisitor.unregister_visitor(_DecoratorNode)


def test_register_visitor_decorator_returns_original_function():
    """The decorator form must return the original (unwrapped) function."""

    class _ReturnNode(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    @RSTVisitor.register_visitor(_ReturnNode)
    def my_visit(visitor, node):
        raise docutils.nodes.SkipChildren()

    try:
        assert my_visit.__name__ == "my_visit"
    finally:
        RSTVisitor.unregister_visitor(_ReturnNode)


def test_register_visitor_decorator_produces_renderable(make_visitor):
    """Decorator form visit_fn can append renderables."""

    class _RenderNode(
        docutils.nodes.General,
        docutils.nodes.Body,
        docutils.nodes.Element,
    ):
        pass

    @RSTVisitor.register_visitor(_RenderNode)
    def visit_render_node(visitor, node):
        visitor.renderables.append(Text("from decorator"))
        raise docutils.nodes.SkipChildren()

    try:
        node = _RenderNode()
        visitor = make_visitor("")
        node.walkabout(visitor)
        texts = [r for r in visitor.renderables if isinstance(r, Text)]
        assert any("from decorator" in t.plain for t in texts)
    finally:
        RSTVisitor.unregister_visitor(_RenderNode)


# ── unregister_visitor ────────────────────────────────────────────────────────

def test_unregister_visitor_removes_registration(make_visitor):
    """After unregister, the node class must not be in the registry."""

    class _UnregNode(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    def dummy(v, n):
        raise docutils.nodes.SkipChildren()

    RSTVisitor.register_visitor(_UnregNode, visit_fn=dummy)
    assert _UnregNode in RSTVisitor.list_registered_visitors(), (
        "Node must be in the registry after registration"
    )

    RSTVisitor.unregister_visitor(_UnregNode)
    assert _UnregNode not in RSTVisitor.list_registered_visitors(), (
        "Node must not be in the registry after unregistration"
    )


def test_unregister_visitor_nonexistent_is_silent():
    """Unregistering a never-registered class must not raise."""

    class _NeverRegistered(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    # Should not raise
    RSTVisitor.unregister_visitor(_NeverRegistered)


# ── list_registered_visitors ──────────────────────────────────────────────────

def test_list_registered_visitors_returns_dict():
    result = RSTVisitor.list_registered_visitors()
    assert isinstance(result, dict)


def test_list_registered_visitors_includes_new_registration():
    class _ListNode(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    def dummy_visit(visitor, node):
        raise docutils.nodes.SkipChildren()

    RSTVisitor.register_visitor(_ListNode, visit_fn=dummy_visit)
    try:
        registry = RSTVisitor.list_registered_visitors()
        assert _ListNode in registry
        assert registry[_ListNode][0] is dummy_visit
    finally:
        RSTVisitor.unregister_visitor(_ListNode)


def test_list_registered_visitors_is_snapshot():
    """Modifying the returned dict must not affect the real registry."""

    class _SnapshotNode(
        docutils.nodes.General,
        docutils.nodes.Inline,
        docutils.nodes.Element,
    ):
        pass

    def dummy_visit(visitor, node):
        raise docutils.nodes.SkipChildren()

    RSTVisitor.register_visitor(_SnapshotNode, visit_fn=dummy_visit)
    try:
        snapshot = RSTVisitor.list_registered_visitors()
        snapshot.pop(_SnapshotNode, None)
        # Real registry must still have it
        assert _SnapshotNode in RSTVisitor.list_registered_visitors()
    finally:
        RSTVisitor.unregister_visitor(_SnapshotNode)
