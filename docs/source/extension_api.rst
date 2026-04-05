Extension API
=============

This page explains how to make rich-rst render your own docutils node types.

If you have a custom directive/transform that creates custom nodes, this is
the API you use to tell rich-rst how those nodes should appear.

The entry point is :class:`rich_rst.RSTVisitor`.

When should I use this?
-----------------------

Use this API when all of the following are true:

- You already have (or will create) a custom docutils node class.
- You want rich-rst output to show that node in a custom way.
- Built-in rendering is not enough.

If you only use standard reStructuredText/Sphinx features, you usually do not
need this page.

Overview
--------

During rendering, rich-rst visits nodes in the parsed document tree.

For each node:

1. For each node, :class:`rich_rst.RSTVisitor` checks its custom registry.
2. If a handler is registered for that exact node class, the handler runs.
3. Otherwise, normal ``visit_*`` / ``depart_*`` method lookup is used.

Important: registration is by exact class match (not by subclass hierarchy).

The custom registry is class-level and stores:

.. code-block:: text

   {node_class: (visit_fn, depart_fn)}

Quick start (5 steps)
---------------------

1. Define (or import) your custom node class.
2. Write a visit handler with signature ``handler(visitor, node)``.
3. Register it with :meth:`rich_rst.RSTVisitor.register_visitor`.
4. Render your document normally.
5. Unregister when the handler should no longer be active.

Minimal pattern:

.. code-block:: python

   from rich_rst import RSTVisitor


   def visit_my_node(visitor, node):
       # Add any Rich renderable you want.
       visitor.renderables.append(...)


   RSTVisitor.register_visitor(MyNode, visit_fn=visit_my_node)
   try:
       ...  # render documents
   finally:
       RSTVisitor.unregister_visitor(MyNode)

Public methods
--------------

``RSTVisitor.register_visitor(node_class, visit_fn=None, depart_fn=None)``
   Register custom handlers for a node class.

   ``node_class`` is the docutils node class to handle.
   ``visit_fn`` runs when entering the node.
   ``depart_fn`` is optional and runs after children are visited.

   Direct form:

   .. code-block:: python

      RSTVisitor.register_visitor(MyNode, visit_fn=my_visit, depart_fn=my_depart)

   Decorator form (registers the function as ``visit_fn``):

   .. code-block:: python

      @RSTVisitor.register_visitor(MyNode)
      def my_visit(visitor, node):
          ...

``RSTVisitor.unregister_visitor(node_class)``
   Remove a registration. Calling this for a class that is not registered is
   safe and does nothing.

``RSTVisitor.list_registered_visitors()``
   Return a snapshot of the registry as a dict. Mutating the returned dict does
   not change the live registry.

Handler contract
----------------

Visit/depart handlers are called as ``handler(visitor, node)``.

Inside handlers:

- ``visitor`` is the active :class:`rich_rst.RSTVisitor` instance.
- ``node`` is the current docutils node instance.

Common patterns:

- Add Rich renderables through ``visitor.renderables.append(...)``.
- Raise ``docutils.nodes.SkipChildren`` from a visit handler when you fully
  handle a node and do not want child traversal.
- Use a depart handler when you need closing behavior after children are
  visited.

End-to-end example (node + directive + RST)
-------------------------------------------

This example shows the full flow most users need:

1. Define a custom node class.
2. Define a directive that emits that node.
3. Register a visitor handler for that node.
4. Render an RST document that uses the directive.

.. code-block:: python

   from rich import print
   from rich.panel import Panel
   from rich_rst import RestructuredText, RSTVisitor
   from rich_rst._vendor import docutils


   class MyNode(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
       pass


   class MyCalloutDirective(docutils.parsers.rst.Directive):
       has_content = True

       def run(self):
           node = MyNode()
           self.state.nested_parse(self.content, self.content_offset, node)
           return [node]


   def visit_my_node(visitor, node):
       # Render the node as a Rich panel and skip normal child traversal.
       visitor.renderables.append(Panel(node.astext(), title="my-callout", border_style="cyan"))
       raise docutils.nodes.SkipChildren()


   def enable_extensions():
       docutils.parsers.rst.directives.register_directive("my-callout", MyCalloutDirective)
       RSTVisitor.register_visitor(MyNode, visit_fn=visit_my_node)


   def disable_extensions():
       RSTVisitor.unregister_visitor(MyNode)


   enable_extensions()
   try:
       rst_source = (
           "Before.\n\n"
           ".. my-callout::\n\n"
           "   This text is parsed into MyNode and rendered by visit_my_node.\n\n"
           "After.\n"
       )
       print(RestructuredText(rst_source))
   finally:
       disable_extensions()

Notes:

- ``register_directive`` and ``register_visitor`` are both global registrations.
- In tests, prefer fixture-based setup/teardown to avoid cross-test leakage.
- The ``try/finally`` above ensures the visitor is always unregistered.

Example: decorator registration
-------------------------------

Use this form when you like declaration-style setup:

.. code-block:: python

   from rich.text import Text
   from rich_rst import RSTVisitor
   from rich_rst._vendor import docutils


   class DecoratedNode(docutils.nodes.General, docutils.nodes.Inline, docutils.nodes.Element):
       pass


   @RSTVisitor.register_visitor(DecoratedNode)
   def visit_decorated(visitor, node):
       visitor.renderables.append(Text("from decorator"))
       raise docutils.nodes.SkipChildren()


   # later, when no longer needed:
   RSTVisitor.unregister_visitor(DecoratedNode)

Subclass behavior
-----------------

Registrations on :class:`rich_rst.RSTVisitor` are global to that class and are
visible to all instances.

If you call ``register_visitor`` on a subclass of ``RSTVisitor``, that subclass
gets its own registry dictionary. This isolates subclass-specific extensions
from the base class and from sibling subclasses.

Troubleshooting
---------------

- Handler did not run:
  Confirm you registered the exact node class being produced.
- Custom output appears twice:
  If your visit handler fully handles content, raise
  ``docutils.nodes.SkipChildren``.
- Tests affect each other:
  Unregister handlers in test teardown/fixtures.
- Registry changes do not stick:
  ``list_registered_visitors()`` returns a snapshot copy, not a live dict.

Recommendations
---------------

- Register handlers at application startup, not per document.
- Unregister temporary handlers in tests or short-lived plugin scopes.
- Keep handlers narrow and side-effect free except for appending renderables.
