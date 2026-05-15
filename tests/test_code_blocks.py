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
from rich.console import Console

from rich_rst import RSTVisitor
from rich_rst._vendor import docutils
import rich_rst._vendor.docutils.core
import pytest
from rich.rule import Rule
from rich.table import Table
import rich_rst
from rich_rst import RestructuredText, RSTVisitor
from rich_rst import RSTVisitor, RestructuredText


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


def test_literal_block_panel_title_marks_default_lexer(make_visitor):
    visitor = make_visitor("Example::\n\n    x = 1\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "python (default)", (
        f"Literal block without explicit language should show default label; got {panels[0].title!r}"
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


def test_code_block_directive_panel_title_stays_explicit(make_visitor):
    visitor = make_visitor(".. code-block:: python\n\n   print('hello')\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "python", (
        f"Explicit code-block language should stay unqualified; got {panels[0].title!r}"
    )


def test_literal_block_panel_title_marks_guessed_lexer(make_visitor, monkeypatch):
    monkeypatch.setattr(RSTVisitor, "_guess_lexer_name", lambda self, text: ("python", True))
    document = docutils.core.publish_doctree(
        "Example::\n\n    some code\n",
        settings_overrides={"report_level": 69, "halt_level": 69},
    )
    console = Console(force_terminal=True, width=120, record=True)
    visitor = RSTVisitor(
        document,
        console=console,
        code_theme="monokai",
        show_line_numbers=False,
        guess_lexer=True,
        default_lexer="python",
    )
    document.walkabout(visitor)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "python (guessed)", (
        f"Guessed language should be clearly labeled; got {panels[0].title!r}"
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


def test_raw_html_falls_back_when_tag_stripping_fails(render_text, monkeypatch):
    monkeypatch.setattr("rich_rst.MLStripper.feed", lambda self, html: (_ for _ in ()).throw(ValueError("boom")))

    out = render_text(".. raw:: html\n\n   <b>bold</b>\n")

    assert "stripped raw html" in out
    assert "<b>bold</b>" in out


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


def test_math_block_produces_math_panel(make_visitor):
    visitor = make_visitor(".. math::\n\n   a^2 + b^2 = c^2\n")
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, ".. math:: must produce a Panel"
    assert panels[0].title == "math"
    assert "a^2" in str(panels[0].renderable)


# ── Regression tests for code-block options ────────────────────────────────


def test_code_block_with_linenos_and_start(make_visitor):
    rst = """.. code-block:: python
       :linenos:
       :lineno-start: 10

       x = 1
       y = 2
    """
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "code-block must produce a Panel"
    syn = panels[0].renderable
    assert isinstance(syn, Syntax)
    assert syn.line_numbers is True
    assert syn.start_line == 10



def test_code_block_emphasize_lines_sets_highlight_and_shows_linenos(make_visitor):
    rst = """.. code-block:: python
       :emphasize-lines: 1,3-4

       a = 1
       b = 2
       c = 3
    """
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    assert syn.highlight_lines == {1, 3, 4}
    assert syn.line_numbers is True


def test_code_block_name_in_panel_title(make_visitor):
    rst = """.. code-block:: python
       :name: example-id

       x = 1
    """
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels[0].title == "python — example-id"


def test_code_block_dedent_option_applies(make_visitor):
    rst = """.. code-block:: python
       :dedent:

           def foo():
               return 1
    """
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    syn = panels[0].renderable
    # dedent should remove common leading indentation so code begins with 'def'
    assert syn.code.lstrip().startswith('def foo') or syn.code.startswith('def ')

def test_validate_default_lexer_name_accepts_none():
    assert rich_rst._validate_default_lexer_name(None) is None

def test_validate_default_lexer_name_rejects_unknown():
    with pytest.raises(ValueError):
        rich_rst._validate_default_lexer_name("definitely-not-a-lexer")

def test_guess_lexer_with_unknown_language(render_text):
    """Test guessing lexer for code that doesn't match any known patterns."""
    rst = """\
.. code-block::

   this is just some random text
   not any specific language
   maybe looks like something
"""
    out = render_text(rst, guess_lexer=False)
    assert "python" in out

def test_lexer_guess_fallback_to_default(render_text):
    """Test that when guess fails, it returns default lexer."""
    rst = """\
.. code-block::

   ξξξξξξ random unicode ξξξξξξ
"""
    out = render_text(rst, guess_lexer=True, default_lexer="python")
    assert "python" in out or "random unicode" in out

def test_code_block_with_explicit_format(render_text):
    """Test code block with explicit format specification."""
    rst = """\
.. code-block:: javascript

   console.log("hello world");
"""
    out = render_text(rst)
    assert "console.log" in out

def test_code_block_with_class_syntax(render_text):
    """Test code block using class syntax for language."""
    rst = """\
.. code-block::
   :class: language-rust

   fn main() {
       println!("Hello");
   }
"""
    out = render_text(rst)
    assert "fn main" in out

def test_lexer_with_aliases(make_visitor):
    """Test lexer that has aliases (normal case)."""
    rst = """\
.. code-block:: python3

   x = 1
"""
    visitor = make_visitor(rst)
    panels = [r for r in visitor.renderables if isinstance(r, Panel)]
    assert panels, "code-block must produce a Panel renderable"
    assert panels[0].title == "python3", (
        f"Panel title must be the lexer alias 'python3', got {panels[0].title!r}"
    )

def test_render_with_line_numbers(render_text):
    """Test rendering with line numbers enabled."""
    rst = """\
.. code-block:: python

   def hello():
       return "world"
"""
    out = render_text(rst, show_line_numbers=True)
    assert "python" in out, "Panel title must show the lexer name 'python'"
    assert "def hello" in out, "Code content must be visible in line-numbered output"
    assert "1" in out, "Line number '1' must appear when show_line_numbers=True"

def test_render_with_custom_code_theme(render_text):
    """Test rendering with different code theme — code content must still be visible."""
    rst = """\
.. code-block:: python

   x = 42
"""
    out = render_text(rst, code_theme="github-dark")
    assert "x = 42" in out, "Code content must be visible regardless of the chosen code_theme"
    assert "python" in out, "Lexer panel title must be visible with a custom code_theme"

def test_doctest_block(render_text):
    """Test doctest block rendering (inline >>> syntax)."""
    rst = """\
>>> x = 1 + 2
>>> print(x)
3
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert "x = 1 + 2" in out, "Doctest code content must be visible"

def test_doctest_multiple_examples(render_text):
    """Test multiple doctest examples."""
    rst = """\
>>> list(range(3))
[0, 1, 2]
>>> dict(a=1, b=2)
{'a': 1, 'b': 2}
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert "list(range(3))" in out, "Doctest code must be visible"

def test_doctest_standalone(render_text):
    """Test doctest directive standalone."""
    rst = """\
>>> print("test")
test
"""
    out = render_text(rst)
    assert "doctest block" in out, (
        "Doctest block must render as a Panel with title 'doctest block'"
    )
    assert 'print("test")' in out, "Doctest code must be visible"

def test_math_block_inline(render_text):
    """Test inline math rendering."""
    rst = """\
Some text :math:`E = mc^2` more text.
"""
    out = render_text(rst)
    assert "E = mc^2" in out, "Inline math formula content must be visible in the output"

def test_math_block_display(render_text):
    """Test display math block."""
    rst = """\
.. math::

   E = mc^2
"""
    out = render_text(rst)
    assert "E = mc^2" in out, "Display math formula content must be visible in the output"

def test_math_standalone(render_text):
    """Test math directive standalone — frac converts to Unicode (a/b)."""
    rst = """\
.. math::

   \\frac{a}{b}
"""
    out = render_text(rst)
    # \\frac{a}{b} is now converted to the Unicode approximation (a/b)
    assert "a/b" in out, "Math directive must render \\frac{a}{b} as (a/b)"
