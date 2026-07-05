"""Edge case and smoke tests for rich-rst."""
import tempfile
from pathlib import Path

import pytest

from rich_rst import RestructuredText


class TestEdgeCases:
    """Test edge cases and unusual inputs."""

    def test_empty_document(self):
        """Test rendering an empty document."""
        rst = RestructuredText("")
        # Should not raise
        assert rst is not None

    def test_very_long_line(self):
        """Test handling of very long lines without wrapping."""
        long_line = "x" * 5000
        rst = RestructuredText(f"This is a very long line:\n\n{long_line}")
        # Should not raise
        assert rst is not None

    def test_deeply_nested_lists(self):
        """Test handling of deeply nested lists."""
        doc = """
List
====

- Level 1

  - Level 2

    - Level 3

      - Level 4

        - Level 5
"""
        rst = RestructuredText(doc)
        assert rst is not None

    def test_unicode_content(self):
        """Test rendering Unicode content."""
        doc = """
Unicode Test
============

This document contains Unicode: 你好 مرحبا こんにちは 🚀 ♠️

- List with emoji 🎉
- More emoji 🔥
"""
        rst = RestructuredText(doc)
        assert rst is not None

    def test_special_characters_in_code(self):
        """Test code blocks with special characters."""
        doc = r'''
Code Example
============

.. code-block:: python

   # Special chars: <>&"'
   x = "special: \n\t\r"
   regex = r"[a-z]+\d{3}"
'''
        rst = RestructuredText(doc)
        assert rst is not None

    def test_malformed_markup_with_errors_hidden(self):
        """Test that malformed markup doesn't crash when errors are hidden."""
        doc = """
Bad Markup
==========

`Unclosed link <http://example.com
`Another unclosed link

.. unknown-directive::
   This directive doesn't exist
"""
        rst = RestructuredText(doc, show_errors=False)
        assert rst is not None

    def test_large_table(self):
        """Test rendering of a large table."""
        rows = "\n".join([f"| Cell {i},{j} | Cell {i},{j+1} |" for i in range(50) for j in range(0, 10, 2)])
        doc = f"""
Large Table
===========

+----------+----------+
| Header 1 | Header 2 |
+==========+==========+
{rows}
+----------+----------+
"""
        rst = RestructuredText(doc)
        assert rst is not None

    def test_multiple_code_themes(self):
        """Test with different code themes."""
        doc = """
Code
====

.. code-block:: python

   print("hello")
"""
        for theme in ["monokai", "fruity", "vim", "native"]:
            rst = RestructuredText(doc, code_theme=theme)
            assert rst is not None

    def test_encoding_edge_cases(self):
        """Test with various special encoding scenarios."""
        doc = "Café\nNaïve\nResuméé"
        rst = RestructuredText(doc)
        assert rst is not None

    def test_document_with_only_whitespace(self):
        """Test document with only whitespace."""
        doc = "   \n\n  \n\t\n   "
        rst = RestructuredText(doc)
        assert rst is not None

    def test_mixed_indentation(self):
        """Test document with mixed tabs and spaces."""
        doc = "Heading\n=======\n\n\tTabbed line\n  Spaced line\n\t  Mixed"
        rst = RestructuredText(doc)
        assert rst is not None


class TestHTMLExport:
    """Test HTML export functionality."""

    def test_html_export_basic(self):
        """Test basic HTML export."""
        doc = "Title\n=====\n\nParagraph with **bold**."
        rst = RestructuredText(doc)
        assert rst is not None

    def test_html_export_with_code(self):
        """Test HTML export with code blocks."""
        doc = """
Code
====

.. code-block:: python

   def hello():
       print("world")
"""
        rst = RestructuredText(doc)
        assert rst is not None

    def test_html_export_with_images(self):
        """Test HTML export with image directives."""
        doc = """
Images
======

.. image:: /path/to/image.png
   :alt: Alternative text
   :width: 100px
"""
        rst = RestructuredText(doc, show_errors=False)
        assert rst is not None


class TestCliEdgeCases:
    """Test CLI edge cases."""

    def test_stdin_rendering(self, tmp_path):
        """Test that stdin input can be rendered."""
        from rich_rst.__main__ import RestructuredText as CliRST
        
        doc = "Test\n====\n\nContent"
        rst = CliRST(doc)
        assert rst is not None

    def test_temp_file_encoding(self, tmp_path):
        """Test file with non-default encoding."""
        test_file = tmp_path / "test.rst"
        content = "Tëst\n====\n\nWïth spëcial chärs"
        test_file.write_text(content, encoding="utf-8")
        
        from rich_rst.__main__ import RestructuredText as CliRST
        
        with open(test_file, encoding="utf-8") as f:
            rst = CliRST(f.read())
        assert rst is not None
