"""Custom docutils node classes produced by rich-rst directives."""

# Imports from the rich package for the printing


# Imports from rich_rst._vendor.docutils package for the parsing
import rich_rst._vendor.docutils.nodes  # noqa: F401
from rich_rst._vendor import docutils

# ── Custom nodes for Sphinx directives ───────────────────────────────────────

class versionmodified(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node produced by the versionadded, versionchanged, and deprecated directives."""
    pass


class seealso(docutils.nodes.Admonition, docutils.nodes.Element):  # type: ignore[misc]
    """Node produced by the seealso directive."""
    pass


class centered_block(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. centered:: directive."""
    pass


class py_desc(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for Python/C/C++/JS domain object-description directives."""
    pass


class toctree_stub(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. toctree:: directive."""
    pass


class literalinclude_stub(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. literalinclude:: directive."""
    pass


class glossary_block(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. glossary:: directive."""
    pass


class hlist_block(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node for .. hlist:: directive carrying column-count metadata."""
    pass


class availability(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node produced by the availability directive."""
    pass


class soft_deprecated(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node produced by the soft-deprecated directive."""
    pass


class impl_detail(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
    """Node produced by the impl-detail directive."""
    pass



class _rowSpan(docutils.nodes.General, docutils.nodes.Element):
    """Inline node carrying a row-span value for flat-table cells."""
    pass


class _colSpan(docutils.nodes.General, docutils.nodes.Element):
    """Inline node carrying a column-span value for flat-table cells."""
    pass

