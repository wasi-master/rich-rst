
"""
reStructuredText parser for rich

Initial few lines gotten from: https://github.com/willmcgugan/rich/discussions/1263#discussioncomment-808898
There are a lot of improvements are added by me
"""
import importlib.metadata

from rich_rst._directives import (  # noqa: F401
    _AutodocDirective,
    _AvailabilityDirective,
    _CenteredDirective,
    _CodeBlockDirective,
    _CurrentModuleDirective,
    _CustomBlockQuote,
    _DeprecatedRemovedDirective,
    _Epigraph,
    _flat_table_cspan,
    _flat_table_rspan,
    _FlatTableBuilder,
    _FlatTableDirective,
    _GlossaryDirective,
    _HighlightDirective,
    _Highlights,
    _HlistDirective,
    _ImplDetailDirective,
    _IncludeDirective,
    _LiteralIncludeDirective,
    _MathDirective,
    _OnlyDirective,
    _parse_toctree_numbered,
    _ParsedLiteralDirective,
    _ProductionListDirective,
    _PullQuote,
    _PyObjectDirective,
    _register_sphinx_directives,
    _SeeAlsoDirective,
    _SilentDirective,
    _SoftDeprecatedDirective,
    _sphinx_registration_guard,
    _ToctreeDirective,
    _VersionDirective,
)
from rich_rst._document import (  # noqa: F401
    RST,
    ReStructuredText,
    RestructuredText,
    reST,
    reStructuredText,
)
from rich_rst._nodes import (  # noqa: F401
    _colSpan,
    _rowSpan,
    availability,
    centered_block,
    glossary_block,
    hlist_block,
    impl_detail,
    literalinclude_stub,
    py_desc,
    seealso,
    soft_deprecated,
    toctree_stub,
    versionmodified,
)
from rich_rst._roles import _register_sphinx_roles  # noqa: F401
from rich_rst._utils import (  # noqa: F401
    MLStripper,
    _convert_math_to_unicode,
    _validate_default_lexer_name,
    strip_tags,
)
from rich_rst._visitor import RSTVisitor

__all__ = ("RST", "RSTVisitor", "ReStructuredText", "RestructuredText", "reStructuredText", "rich_rst")
__author__ = "Arian Mollik Wasi (aka. Wasi Master)"
__version__ = importlib.metadata.version(__package__ or __name__)
