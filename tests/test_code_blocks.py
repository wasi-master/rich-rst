"""Tests for code and data blocks.

Covers: literal blocks (plain ``::`` syntax and ``.. code-block::``),
doctest blocks, raw directives (HTML and other formats), and math
(inline role and block directive).
"""
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text


# ── Literal blocks ────────────────────────────────────────────────────────────

def test_literal_block_produces_panel(make_visitor):
    visitor = make_visitor("Example::\n\n    code here\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "A '::' literal block must produce a Panel renderable"


def test_literal_block_panel_contains_syntax_object(make_visitor):
    visitor = make_visitor("Example::\n\n    code here\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert isinstance(panels[0].renderable, Syntax)


def test_literal_block_content_preserved(render_text):
    out = render_text("Example::\n\n    x = 1\n    y = 2\n")
    assert "x = 1" in out
    assert "y = 2" in out


def test_code_block_directive_with_python_language(make_visitor):
    rst = ".. code-block:: python\n\n   print('hello')\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_code_block_directive_content_visible(render_text):
    rst = ".. code-block:: python\n\n   print('hello')\n"
    assert "print" in render_text(rst)


def test_code_block_directive_with_shell_language(render_text):
    rst = ".. code-block:: bash\n\n   echo hello\n"
    assert "echo" in render_text(rst)


def test_literal_block_with_explicit_language_class(render_text):
    # The '.. code::' directive also works
    rst = ".. code:: python\n\n   x = 42\n"
    assert "x = 42" in render_text(rst)


# ── Doctest blocks ────────────────────────────────────────────────────────────

def test_doctest_block_produces_panel(make_visitor):
    visitor = make_visitor(">>> print('hi')\nhi\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "A doctest block must produce a Panel renderable"


def test_doctest_block_panel_title(make_visitor):
    visitor = make_visitor(">>> x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "doctest block"


def test_doctest_block_uses_pycon_lexer(make_visitor):
    visitor = make_visitor(">>> x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert syn.lexer == "pycon"


def test_doctest_block_content_visible(render_text):
    out = render_text(">>> x = 42\n>>> print(x)\n42\n")
    assert "x = 42" in out


def test_doctest_block_output_line_visible(render_text):
    out = render_text(">>> 1 + 1\n2\n")
    assert "1 + 1" in out
    assert "2" in out


# ── Raw directives ────────────────────────────────────────────────────────────

def test_raw_html_produces_panel(make_visitor):
    rst = ".. raw:: html\n\n   <b>bold</b>\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. raw:: html must produce a Panel"


def test_raw_html_panel_title_indicates_stripped(make_visitor):
    rst = ".. raw:: html\n\n   <b>bold</b>\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "stripped raw html"


def test_raw_html_tags_stripped_from_output(render_text):
    rst = ".. raw:: html\n\n   <p>Hello</p>\n"
    assert "Hello" in render_text(rst)


def test_raw_latex_produces_panel(make_visitor):
    rst = ".. raw:: latex\n\n   \\textbf{bold}\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels


def test_raw_latex_panel_title(make_visitor):
    rst = ".. raw:: latex\n\n   \\textbf{bold}\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert "latex" in panels[0].title.lower()


def test_raw_latex_content_visible(render_text):
    rst = ".. raw:: latex\n\n   \\textbf{bold}\n"
    assert "textbf" in render_text(rst)


# ── Math ──────────────────────────────────────────────────────────────────────

def test_inline_math_role_content_visible(render_text):
    # Inline math renders the LaTeX source as plain text
    assert "E = mc^2" in render_text("The formula :math:`E = mc^2`.")


def test_math_block_directive_content_visible(render_text):
    rst = ".. math::\n\n   x^2 + y^2 = r^2\n"
    assert "x^2 + y^2 = r^2" in render_text(rst)


def test_math_block_produces_text_renderable(make_visitor):
    rst = ".. math::\n\n   a^2 + b^2 = c^2\n"
    visitor = make_visitor(rst)
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "a^2" in combined
