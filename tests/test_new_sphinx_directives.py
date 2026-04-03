"""Tests for new Sphinx-specific block directives."""
import pytest
from rich.panel import Panel
from rich.align import Align

from rich_rst import _register_sphinx_directives, _register_sphinx_roles


@pytest.fixture(autouse=True)
def ensure_sphinx_compat():
    _register_sphinx_directives()
    _register_sphinx_roles()


def _panels(make_visitor, rst):
    visitor = make_visitor(rst)
    return [r for r in visitor.renderables if isinstance(r, Panel)]


def _first_panel(make_visitor, rst):
    panels = _panels(make_visitor, rst)
    assert panels, f"Must produce at least one Panel:\n{rst}"
    return panels[0]


def _render(render_text, rst, **kw):
    return render_text(rst, sphinx_compat=True, **kw)


# ── code-block ────────────────────────────────────────────────────────────────

def test_codeblock_with_language_produces_panel(make_visitor):
    rst = ".. code-block:: python\n\n   x = 1\n"
    assert _panels(make_visitor, rst), "code-block should produce a Panel"


def test_codeblock_language_in_panel_title(make_visitor):
    rst = ".. code-block:: python\n\n   x = 1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "python"


def test_codeblock_content_appears_in_output(render_text):
    rst = ".. code-block:: python\n\n   x = 42\n"
    assert "x = 42" in _render(render_text, rst)


def test_codeblock_without_language_renders(make_visitor):
    rst = ".. code-block::\n\n   some text\n"
    visitor = make_visitor(rst)
    assert visitor.renderables, "code-block without language should produce renderables"


def test_sourcecode_works_like_codeblock(render_text):
    rst = ".. sourcecode:: python\n\n   y = 2\n"
    assert "y = 2" in _render(render_text, rst)


def test_sourcecode_produces_panel(make_visitor):
    rst = ".. sourcecode:: python\n\n   z = 3\n"
    assert _panels(make_visitor, rst), "sourcecode should produce a Panel"


# ── highlight ─────────────────────────────────────────────────────────────────

def test_highlight_produces_no_output(make_visitor):
    rst = ".. highlight:: python\n"
    visitor = make_visitor(rst)
    panels = _panels(make_visitor, rst)
    assert not panels, "highlight should produce no Panel"


def test_highlight_no_crash(render_text):
    rst = ".. highlight:: python\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── index / tabularcolumns ────────────────────────────────────────────────────

def test_index_produces_no_output(make_visitor):
    rst = ".. index:: myterm\n"
    panels = _panels(make_visitor, rst)
    assert not panels, "index should produce no Panel"


def test_index_no_crash(render_text):
    rst = ".. index:: some term\n\nSome text.\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_tabularcolumns_produces_no_output(make_visitor):
    rst = ".. tabularcolumns:: |L|L|\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_tabularcolumns_no_crash(render_text):
    rst = ".. tabularcolumns:: |L|L|\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── currentmodule / py:currentmodule ─────────────────────────────────────────

def test_currentmodule_produces_no_output(make_visitor):
    rst = ".. currentmodule:: os.path\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_currentmodule_no_crash(render_text):
    rst = ".. currentmodule:: os.path\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_py_currentmodule_produces_no_output(make_visitor):
    rst = ".. py:currentmodule:: os.path\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_py_currentmodule_no_crash(render_text):
    rst = ".. py:currentmodule:: os.path\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


# ── only ──────────────────────────────────────────────────────────────────────

def test_only_always_renders_content(render_text):
    rst = ".. only:: html\n\n   This is html only content.\n"
    out = _render(render_text, rst)
    assert "This is html only content." in out


def test_only_with_latex_expression(render_text):
    rst = ".. only:: latex\n\n   LaTeX only text here.\n"
    out = _render(render_text, rst)
    assert "LaTeX only text here." in out


# ── centered ──────────────────────────────────────────────────────────────────

def test_centered_produces_output(render_text):
    rst = ".. centered:: My Centered Title\n"
    out = _render(render_text, rst)
    assert "My Centered Title" in out


def test_centered_produces_align(make_visitor):
    rst = ".. centered:: Center Me\n"
    visitor = make_visitor(rst)
    aligns = [r for r in visitor.renderables if isinstance(r, Align)]
    assert aligns, "centered should produce an Align renderable"


# ── hlist ─────────────────────────────────────────────────────────────────────

def test_hlist_content_appears_in_output(render_text):
    rst = ".. hlist::\n   :columns: 2\n\n   * Item one\n   * Item two\n"
    out = _render(render_text, rst)
    assert "Item one" in out
    assert "Item two" in out


def test_hlist_no_crash(make_visitor):
    rst = ".. hlist::\n\n   * Alpha\n   * Beta\n"
    visitor = make_visitor(rst)
    assert isinstance(visitor.renderables, list)


# ── toctree ───────────────────────────────────────────────────────────────────

def test_toctree_renders_as_panel(make_visitor):
    rst = ".. toctree::\n   :maxdepth: 2\n\n   intro\n   usage\n"
    panels = _panels(make_visitor, rst)
    assert panels, "toctree should produce a Panel"


def test_toctree_entries_visible(render_text):
    rst = ".. toctree::\n\n   intro\n   advanced\n"
    out = _render(render_text, rst)
    assert "intro" in out
    assert "advanced" in out


def test_toctree_caption_used(make_visitor):
    rst = ".. toctree::\n   :caption: My Table of Contents\n\n   page1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "My Table of Contents"


def test_toctree_default_caption(make_visitor):
    rst = ".. toctree::\n\n   page1\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "Contents"


# ── literalinclude ────────────────────────────────────────────────────────────

def test_literalinclude_renders_as_panel(make_visitor):
    rst = ".. literalinclude:: myfile.py\n"
    panels = _panels(make_visitor, rst)
    assert panels, "literalinclude should produce a Panel"


def test_literalinclude_filename_visible(render_text):
    rst = ".. literalinclude:: path/to/myfile.py\n"
    out = _render(render_text, rst)
    assert "path/to/myfile.py" in out


def test_literalinclude_panel_title(make_visitor):
    rst = ".. literalinclude:: example.py\n"
    panel = _first_panel(make_visitor, rst)
    assert panel.title == "literalinclude"


# ── productionlist ────────────────────────────────────────────────────────────

def test_productionlist_content_appears(render_text):
    rst = ".. productionlist::\n   statement: assignment\n   assignment: NAME '=' expr\n"
    out = _render(render_text, rst)
    assert "statement" in out


def test_productionlist_produces_panel(make_visitor):
    rst = ".. productionlist::\n   rule: token\n"
    panels = _panels(make_visitor, rst)
    assert panels, "productionlist should produce a Panel"


# ── glossary ──────────────────────────────────────────────────────────────────

def test_glossary_content_appears(render_text):
    rst = ".. glossary::\n\n   term1\n      Definition of term1.\n"
    out = _render(render_text, rst)
    assert "term1" in out


def test_glossary_no_crash(make_visitor):
    rst = ".. glossary::\n\n   myterm\n      The definition.\n"
    visitor = make_visitor(rst)
    assert isinstance(visitor.renderables, list)


# ── deprecated-removed ────────────────────────────────────────────────────────

def test_deprecated_removed_produces_panel(make_visitor):
    rst = ".. deprecated-removed:: 3.0 4.0\n"
    panels = _panels(make_visitor, rst)
    assert panels, "deprecated-removed should produce a Panel"


def test_deprecated_removed_both_versions_visible(render_text):
    rst = ".. deprecated-removed:: 3.0 4.0\n\n   Use the new API.\n"
    out = _render(render_text, rst)
    assert "3.0" in out
    assert "4.0" in out


def test_deprecated_removed_body_visible(render_text):
    rst = ".. deprecated-removed:: 3.0 4.0\n\n   Use the new API instead.\n"
    out = _render(render_text, rst)
    assert "Use the new API instead." in out


# ── Python domain directives ──────────────────────────────────────────────────

def test_py_function_produces_panel(make_visitor):
    rst = ".. py:function:: my_func(arg1, arg2)\n\n   Does something.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "py:function should produce a Panel"


def test_py_function_signature_visible(render_text):
    rst = ".. py:function:: compute(x, y)\n\n   Computes a value.\n"
    out = _render(render_text, rst)
    assert "compute(x, y)" in out


def test_py_class_produces_panel(make_visitor):
    rst = ".. py:class:: MyClass(base)\n\n   A class.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_py_method_produces_panel(make_visitor):
    rst = ".. py:method:: MyClass.my_method(self, arg)\n\n   A method.\n"
    panels = _panels(make_visitor, rst)
    assert panels


def test_py_attribute_produces_panel(make_visitor):
    rst = ".. py:attribute:: MyClass.attr\n\n   An attribute.\n"
    panels = _panels(make_visitor, rst)
    assert panels


# ── C domain directives ───────────────────────────────────────────────────────

def test_c_function_produces_panel(make_visitor):
    rst = ".. c:function:: int my_func(int x)\n\n   A C function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "c:function should produce a Panel"


def test_c_type_produces_panel(make_visitor):
    rst = ".. c:type:: my_type\n\n   A C type.\n"
    panels = _panels(make_visitor, rst)
    assert panels


# ── C++ domain directives ─────────────────────────────────────────────────────

def test_cpp_function_produces_panel(make_visitor):
    rst = ".. cpp:function:: void my_func(int x)\n\n   A C++ function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "cpp:function should produce a Panel"


def test_cpp_class_produces_panel(make_visitor):
    rst = ".. cpp:class:: MyClass\n\n   A C++ class.\n"
    panels = _panels(make_visitor, rst)
    assert panels


# ── JS domain directives ──────────────────────────────────────────────────────

def test_js_function_produces_panel(make_visitor):
    rst = ".. js:function:: myFunc(arg)\n\n   A JS function.\n"
    panels = _panels(make_visitor, rst)
    assert panels, "js:function should produce a Panel"


# ── autodoc directives ────────────────────────────────────────────────────────

def test_automodule_produces_no_output(make_visitor):
    rst = ".. automodule:: mymodule\n   :members:\n"
    panels = _panels(make_visitor, rst)
    assert not panels, "automodule should produce no Panel"


def test_automodule_no_crash(render_text):
    rst = ".. automodule:: mymodule\n   :members:\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)


def test_autoclass_produces_no_output(make_visitor):
    rst = ".. autoclass:: mymodule.MyClass\n"
    panels = _panels(make_visitor, rst)
    assert not panels


def test_autofunction_no_crash(render_text):
    rst = ".. autofunction:: mymodule.my_func\n"
    out = _render(render_text, rst)
    assert isinstance(out, str)
