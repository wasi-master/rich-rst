Extension API
=============

rich-rst exposes a small extension surface for handling custom docutils node
types during rendering. The entry point is :class:`rich_rst.RSTVisitor`.

Overview
--------

The visitor dispatch flow is:

1. For each node, :class:`rich_rst.RSTVisitor` checks its custom registry.
2. If a handler is registered for that exact node class, the handler runs.
3. Otherwise, normal ``visit_*`` / ``depart_*`` method lookup is used.

The custom registry is class-level and stores:

.. code-block:: text

   {node_class: (visit_fn, depart_fn)}

Public methods
--------------

``RSTVisitor.register_visitor(node_class, visit_fn=None, depart_fn=None)``
   Register custom handlers for a node class.

   - Direct form:

     .. code-block:: python

        RSTVisitor.register_visitor(MyNode, visit_fn=my_visit, depart_fn=my_depart)

   - Decorator form (registers the function as ``visit_fn``):

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

Common patterns:

- Add Rich renderables through ``visitor.renderables.append(...)``.
- Raise ``docutils.nodes.SkipChildren`` from a visit handler when you fully
  handle a node and do not want child traversal.
- Use a depart handler when you need closing behavior after children are
  visited.

Example: direct registration
----------------------------

.. code-block:: python

   from rich import print
   from rich.text import Text
   from rich_rst import RestructuredText, RSTVisitor
   from rich_rst._vendor import docutils


   class MyNode(docutils.nodes.General, docutils.nodes.Body, docutils.nodes.Element):
       pass


   def visit_my_node(visitor, node):
       visitor.renderables.append(Text("[custom node rendered]", style="bold green"))
       raise docutils.nodes.SkipChildren()


   RSTVisitor.register_visitor(MyNode, visit_fn=visit_my_node)
   try:
       # In real integrations, MyNode usually comes from your own directive/transform.
       print(RestructuredText("Hello"))
   finally:
       RSTVisitor.unregister_visitor(MyNode)

Example: decorator registration
-------------------------------

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

Recommendations
---------------

- Register handlers at application startup, not per document.
- Unregister temporary handlers in tests or short-lived plugin scopes.
- Keep handlers narrow and side-effect free except for appending renderables.
