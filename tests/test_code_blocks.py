"""Tests for code and data blocks.

Covers: literal blocks (plain ``::`` syntax and ``.. code-block::``),
doctest blocks, raw directives (HTML and other formats), and math
(inline role and block directive).

Formatting contract
-------------------
* **Literal / code blocks** are rendered as a ``Panel`` whose
  ``renderable`` is a ``rich.syntax.Syntax`` object.  The correct
  programming-language lexer is selected and exposed through
  ``Syntax.lexer.aliases``.
* **Doctest blocks** use the ``pycon`` lexer (``PythonConsoleLexer``) and
  have the panel title ``"doctest block"``.
* **Raw HTML** is stripped of tags and wrapped in a Panel titled
  ``"stripped raw html"``.
* **Raw (non-HTML)** content is wrapped in a Panel whose title contains
  the format name.
* **Math** content is rendered as plain text (the LaTeX source).
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
    assert isinstance(panels[0].renderable, Syntax), (
        "Literal block panel's renderable must be a Syntax object"
    )


def test_literal_block_default_lexer_is_python(make_visitor):
    visitor = make_visitor("Example::\n\n    x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert "python" in syn.lexer.aliases, (
        f"Default literal block lexer must be Python; aliases: {syn.lexer.aliases}"
    )


def test_literal_block_content_preserved(render_text):
    out = render_text("Example::\n\n    x = 1\n    y = 2\n")
    assert "x = 1" in out
    assert "y = 2" in out


def test_code_block_directive_with_python_language(make_visitor):
    rst = ".. code-block:: python\n\n   print('hello')\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. code-block:: must produce a Panel"
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert "python" in syn.lexer.aliases, (
        f".. code-block:: python must use Python lexer; aliases: {syn.lexer.aliases}"
    )


def test_code_block_directive_with_bash_language(make_visitor):
    rst = ".. code-block:: bash\n\n   echo hello\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert "bash" in syn.lexer.aliases, (
        f".. code-block:: bash must use Bash lexer; aliases: {syn.lexer.aliases}"
    )


def test_code_directive_alias_with_python(make_visitor):
    rst = ".. code:: python\n\n   x = 42\n"
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert "python" in syn.lexer.aliases


def test_code_block_directive_content_visible(render_text):
    rst = ".. code-block:: python\n\n   print('hello')\n"
    assert "print" in render_text(rst)


# ── Doctest blocks ────────────────────────────────────────────────────────────

def test_doctest_block_produces_panel(make_visitor):
    visitor = make_visitor(">>> print('hi')\nhi\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "A doctest block must produce a Panel renderable"


def test_doctest_block_panel_title_is_doctest_block(make_visitor):
    visitor = make_visitor(">>> x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "doctest block", (
        f"Doctest panel title must be 'doctest block', got {panels[0].title!r}"
    )


def test_doctest_block_uses_pycon_lexer(make_visitor):
    visitor = make_visitor(">>> x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert "pycon" in syn.lexer.aliases, (
        f"Doctest block must use the 'pycon' (PythonConsoleLexer) lexer; "
        f"aliases: {syn.lexer.aliases}"
    )


def test_doctest_block_content_visible(render_text):
    assert "x = 42" in render_text(">>> x = 42\n>>> print(x)\n42\n")


def test_doctest_block_output_line_visible(render_text):
    out = render_text(">>> 1 + 1\n2\n")
    assert "1 + 1" in out
    assert "2" in out


# ── Raw directives ────────────────────────────────────────────────────────────

def test_raw_html_produces_panel(make_visitor):
    visitor = make_visitor(".. raw:: html\n\n   <b>bold</b>\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. raw:: html must produce a Panel"


def test_raw_html_panel_title_is_stripped_raw_html(make_visitor):
    visitor = make_visitor(".. raw:: html\n\n   <b>bold</b>\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "stripped raw html", (
        f"Raw-HTML panel title must be 'stripped raw html', got {panels[0].title!r}"
    )


def test_raw_html_tags_stripped_content_visible(render_text):
    assert "Hello" in render_text(".. raw:: html\n\n   <p>Hello</p>\n")


def test_raw_latex_produces_panel(make_visitor):
    visitor = make_visitor(".. raw:: latex\n\n   \\textbf{bold}\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. raw:: latex must produce a Panel"


def test_raw_latex_panel_title_contains_format_name(make_visitor):
    visitor = make_visitor(".. raw:: latex\n\n   \\textbf{bold}\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert "latex" in panels[0].title.lower(), (
        f"Raw LaTeX panel title must mention 'latex', got {panels[0].title!r}"
    )


def test_raw_latex_content_visible(render_text):
    assert "textbf" in render_text(".. raw:: latex\n\n   \\textbf{bold}\n")


# ── Math ──────────────────────────────────────────────────────────────────────

def test_inline_math_role_content_visible(render_text):
    assert "E = mc^2" in render_text("The formula :math:`E = mc^2`.")


def test_math_block_directive_content_visible(render_text):
    assert "x^2 + y^2 = r^2" in render_text(".. math::\n\n   x^2 + y^2 = r^2\n")


def test_math_block_produces_text_renderable(make_visitor):
    visitor = make_visitor(".. math::\n\n   a^2 + b^2 = c^2\n")
    texts = [r for r in visitor.renderables if isinstance(r, Text)]
    combined = "".join(t.plain for t in texts)
    assert "a^2" in combined
