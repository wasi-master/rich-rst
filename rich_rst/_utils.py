"""Small shared helpers: lexer validation, HTML stripping, LaTeX-to-Unicode."""
import re
from html.parser import HTMLParser
from io import StringIO
from typing import Optional

# Imports from the rich package for the printing
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

# Imports from rich_rst._vendor.docutils package for the parsing


def _validate_default_lexer_name(default_lexer: Optional[str]) -> Optional[str]:
    """Validate that ``default_lexer`` is a known Pygments lexer alias."""
    if default_lexer is None:
        return default_lexer
    try:
        get_lexer_by_name(default_lexer)
    except ClassNotFound as error:
        raise ValueError(f"Unknown Pygments lexer name: {default_lexer!r}") from error
    return default_lexer




class MLStripper(HTMLParser):
    """Utility class to strip out html for raw html source"""
    def __init__(self):
        super().__init__()
        self.reset()
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d: str) -> None:
        self.text.write(d)

    def get_data(self) -> str:
        return self.text.getvalue()


def strip_tags(html: str) -> str:
    s = MLStripper()
    try:
        s.feed(html)
        s.close()
    except Exception:
        return html
    return s.get_data()

# ---------------------------------------------------------------------------
# LaTeX-to-Unicode math conversion
# ---------------------------------------------------------------------------

_LATEX_TO_UNICODE = {
    # Greek lowercase
    r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ',
    r'\epsilon': 'ε', r'\varepsilon': 'ε', r'\zeta': 'ζ', r'\eta': 'η',
    r'\theta': 'θ', r'\vartheta': 'ϑ', r'\iota': 'ι', r'\kappa': 'κ',
    r'\lambda': 'λ', r'\mu': 'μ', r'\nu': 'ν', r'\xi': 'ξ',
    r'\pi': 'π', r'\varpi': 'ϖ', r'\rho': 'ρ', r'\varrho': 'ϱ',
    r'\sigma': 'σ', r'\varsigma': 'ς', r'\tau': 'τ', r'\upsilon': 'υ',
    r'\phi': 'φ', r'\varphi': 'φ', r'\chi': 'χ', r'\psi': 'ψ',
    r'\omega': 'ω',
    # Greek uppercase
    r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ',
    r'\Xi': 'Ξ', r'\Pi': 'Π', r'\Sigma': 'Σ', r'\Upsilon': 'Υ',
    r'\Phi': 'Φ', r'\Psi': 'Ψ', r'\Omega': 'Ω',
    # Operators and punctuation
    r'\times': '×', r'\div': '÷', r'\pm': '±', r'\mp': '∓',
    r'\cdot': '·', r'\ldots': '…', r'\cdots': '⋯',
    r'\vdots': '⋮', r'\ddots': '⋱',
    # Comparison
    r'\leq': '≤', r'\le': '≤', r'\geq': '≥', r'\ge': '≥',
    r'\neq': '≠', r'\ne': '≠', r'\approx': '≈', r'\equiv': '≡',
    r'\sim': '∼', r'\simeq': '≃', r'\cong': '≅', r'\propto': '∝',
    # Set operations
    r'\subset': '⊂', r'\supset': '⊃', r'\subseteq': '⊆', r'\supseteq': '⊇',
    r'\in': '∈', r'\notin': '∉', r'\cup': '∪', r'\cap': '∩',
    r'\emptyset': '∅', r'\varnothing': '∅',
    # Logic
    r'\neg': '¬', r'\wedge': '∧', r'\vee': '∨', r'\oplus': '⊕',
    r'\forall': '∀', r'\exists': '∃', r'\nexists': '∄',
    # Arrows
    r'\to': '→', r'\rightarrow': '→', r'\leftarrow': '←', r'\gets': '←',
    r'\leftrightarrow': '↔', r'\Rightarrow': '⇒', r'\Leftarrow': '⇐',
    r'\Leftrightarrow': '⇔', r'\uparrow': '↑', r'\downarrow': '↓',
    r'\updownarrow': '↕', r'\Uparrow': '⇑', r'\Downarrow': '⇓',
    r'\mapsto': '↦',
    # Miscellaneous
    r'\infty': '∞', r'\partial': '∂', r'\nabla': '∇',
    r'\sum': '∑', r'\prod': '∏', r'\int': '∫', r'\oint': '∮',
    r'\hbar': 'ℏ', r'\ell': 'ℓ', r'\wp': '℘', r'\Re': 'ℜ', r'\Im': 'ℑ',
    r'\aleph': 'ℵ', r'\angle': '∠', r'\perp': '⊥', r'\parallel': '∥',
    r'\prime': '′', r'\dagger': '†', r'\ddagger': '‡',
    r'\langle': '⟨', r'\rangle': '⟩',
    # Whitespace
    r'\quad': '  ', r'\qquad': '    ', r'\ ': ' ',
}

# Pre-sort substitutions once so repeated conversions avoid sorting overhead.
_LATEX_TO_UNICODE_SORTED = tuple(
    sorted(_LATEX_TO_UNICODE.items(), key=lambda item: -len(item[0]))
)


def _convert_math_to_unicode(text: str) -> str:
    """Convert common LaTeX math notation to Unicode approximations.

    Handles the most common cases (Greek letters, operators, arrows, etc.)
    for improved readability in the terminal.  Unknown commands are left as-is.
    """
    result = text

    # Strip \\left / \\right size modifiers (no terminal equivalent)
    result = re.sub(r'\\left\s*', '', result)
    result = re.sub(r'\\right\s*', '', result)

    # \\frac{a}{b} → (a/b)
    result = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1/\2)', result)

    # \\sqrt{x} → √(x)
    result = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', result)

    # ^{...} → keep exponent inline
    result = re.sub(r'\^\{([^{}]*)\}', r'^\1', result)

    # _{...} → keep subscript inline
    result = re.sub(r'_\{([^{}]*)\}', r'_\1', result)

    # Remove remaining braces
    result = result.replace('{', '').replace('}', '')

    # Apply symbol substitutions (longest first to avoid partial replacements)
    for latex, uni in _LATEX_TO_UNICODE_SORTED:
        result = result.replace(latex, uni)

    return result


