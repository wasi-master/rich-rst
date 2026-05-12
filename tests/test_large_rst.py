from rich_rst import RestructuredText


def test_large_rst_document_renders_without_errors():
    section = """Section Title
=============

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

- Item one
- Item two
- Item three

.. code-block:: python

   def greet(name: str) -> str:
       return f"Hello, {name}!"

Reference to `Python <https://python.org>`_.
"""
    large_rst = "\n\n".join(section for _ in range(220))
    rendered = RestructuredText(large_rst).render_to_string(width=120)
    assert "Section Title" in rendered
    assert "Lorem ipsum" in rendered
    assert len(rendered) > 1000
