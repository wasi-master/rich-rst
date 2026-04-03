Styling
=======

rich-rst uses `Rich <https://rich.readthedocs.io/>`_'s powerful styling and theming system to customize the appearance of rendered reStructuredText documents. This page explains how to personalize the visual style of your RST output.

.. contents::
   :local:

Overview
--------

rich-rst renders RST elements (headings, admonitions, lists, etc.) using Rich renderables, each styled with a specific style name from the Rich console's theme. The default styles provide sensible colors and formatting, but you can override them to match your preferences or theme.

All style names used by rich-rst follow the ``restructuredtext.*`` naming convention, making them easy to identify and customize.

How Styling Works
------------------

When rich-rst renders a document, it retrieves styles for each element using the current Rich console's theme. If a style name is not defined in the theme, rich-rst uses a built-in default style, ensuring that output always looks reasonable.

This approach has several advantages:

- **Flexibility**: Styles are defined centrally in the console's theme, not hardcoded.
- **Consistency**: Your custom styles automatically apply to all RST documents rendered with the same console.
- **Fallback defaults**: Every style name has a sensible default, so rendering never fails even with incomplete theme definitions.

Customizing Styles
-------------------

There are several ways to customize rich-rst styles, depending on your use case.

Via Console Theme
~~~~~~~~~~~~~~~~~

The most straightforward way to customize styles is to create a Rich console with a custom theme and pass it to the rendering code. Here's an example:

.. code-block:: python

   from rich.console import Console
   from rich.theme import Theme
   from rich_rst import RestructuredText
   
   # Create a custom theme
   custom_theme = Theme({
       "restructuredtext.title.level.1": "bold magenta",
       "restructuredtext.title.level.2": "bold cyan",
       "restructuredtext.note": "bold green on blue",
       "restructuredtext.warning": "bold yellow on red",
       "restructuredtext.reference": "cyan underline",
   })
   
   # Create a Rich console with your custom theme
   console = Console(theme=custom_theme)
   
   rst_document = """
   Example Document
   ================
   
   This is a **note**:
   
   .. note::
   
      This is styled with your custom theme!
   
   Visit `this site <https://example.com>`_ for more info.
   """
   
   # Render using the console
   console.print(RestructuredText(rst_document))

Modifying Console Theme At Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have a console instance, you can modify its theme directly:

.. code-block:: python

   from rich.console import Console
   from rich_rst import RestructuredText
   
   console = Console()
   
   # Customize specific styles in the console's theme
   console.push_style("restructuredtext.title.level.1", "bold magenta")
   console.push_style("restructuredtext.note", "bold cyan on dark_blue")
   
   rst_document = """
   Heading
   =======
   
   .. note::
   
      This note uses the customized style.
   """
   
   console.print(RestructuredText(rst_document))

Using a Theme File
~~~~~~~~~~~~~~~~~~

Rich supports loading themes from JSON files. This is useful for sharing themes or organizing complex style definitions:

.. code-block:: json

   {
     "restructuredtext.title.level.1": "bold #ff00ff",
     "restructuredtext.title.level.2": "bold #00ffff",
     "restructuredtext.title.level.3": "bold underline #ffff00",
     "restructuredtext.note": "bold white on #0066ff",
     "restructuredtext.warning": "bold white on #ff3300",
     "restructuredtext.error": "bold white on #ff0000",
     "restructuredtext.admonition": "bold #00ff00",
     "restructuredtext.reference": "blue underline"
   }

Save this as ``my_theme.json``, then load it in your code:

.. code-block:: python

   from rich.console import Console
   from rich.theme import Theme
   from rich_rst import RestructuredText
   
   # Load the theme from a JSON file
   theme = Theme.read("my_theme.json")
   console = Console(theme=theme)
   
   rst_document = "Your RST content here..."
   console.print(RestructuredText(rst_document))

Customizable Style Names
------------------------

Below is a comprehensive list of all style names that rich-rst uses. You can customize any of these by defining them in your console's theme.

Headings
~~~~~~~~

Headings are organized by level, and rich-rst supports up to 6 levels:

.. code-block:: text

   restructuredtext.title.level.1  (default: "bold" with double-line box)
   restructuredtext.title.level.2  (default: "bold" with rounded box)
   restructuredtext.title.level.3  (default: "bold underline")
   restructuredtext.title.level.4  (default: "bold")
   restructuredtext.title.level.5  (default: "underline")
   restructuredtext.title.level.6  (default: "italic")

Example of customizing all heading levels:

.. code-block:: python

   from rich.theme import Theme
   
   custom_theme = Theme({
       "restructuredtext.title.level.1": "bold bright_magenta",
       "restructuredtext.title.level.2": "bold bright_cyan",
       "restructuredtext.title.level.3": "bold bright_green",
       "restructuredtext.title.level.4": "bold bright_yellow",
       "restructuredtext.title.level.5": "bright_blue",
       "restructuredtext.title.level.6": "italic bright_white",
   })

Admonitions
~~~~~~~~~~~

Admonitions are special note boxes for warnings, tips, and other important information:

.. code-block:: text

   restructuredtext.note       (default: "bold white")
   restructuredtext.warning    (default: "bold yellow")
   restructuredtext.error      (default: "bold red")
   restructuredtext.danger     (default: "bold white on red")
   restructuredtext.tip        (default: "bold green")
   restructuredtext.hint       (default: "yellow")
   restructuredtext.important  (default: "bold blue")
   restructuredtext.caution    (default: "red")
   restructuredtext.attention  (default: "bold black on yellow")
   restructuredtext.admonition (default: "bold white")

Example of customizing admonitions:

.. code-block:: python

   from rich.theme import Theme
   
   custom_theme = Theme({
       "restructuredtext.note": "bold cyan on dark_blue",
       "restructuredtext.warning": "bold yellow on dark_red",
       "restructuredtext.error": "bold white on red",
       "restructuredtext.tip": "bold green on dark_green",
       "restructuredtext.important": "bold bright_blue",
   })

Special Elements
~~~~~~~~~~~~~~~~

Styles for other special elements:

.. code-block:: text

   restructuredtext.reference            (default: "blue underline on default")
   restructuredtext.rubric               (default: "italic dim")
   restructuredtext.text                 (default: "default on default not underline")
   restructuredtext.seealso              (default: "bold white")
   restructuredtext.centered             (default: "bold")
   restructuredtext.py_desc              (default: "bold blue")
   restructuredtext.toctree              (default: "bold cyan")
   restructuredtext.bullet_list_marker   (default: "bold yellow")
   restructuredtext.literalinclude       (default: "grey58")
   restructuredtext.subscript            (default: "none")
   restructuredtext.superscript          (default: "none")

Full Customization Example
---------------------------

Here's a complete example that customizes multiple aspects of rich-rst styling:

.. code-block:: python

   from rich.console import Console
   from rich.theme import Theme
   from rich_rst import RestructuredText
   
   # Create a comprehensive custom theme
   dark_theme = Theme({
       # Headings - professional blue/purple gradient
       "restructuredtext.title.level.1": "bold bright_blue",
       "restructuredtext.title.level.2": "bold bright_cyan",
       "restructuredtext.title.level.3": "bold cyan",
       "restructuredtext.title.level.4": "cyan",
       "restructuredtext.title.level.5": "dim cyan",
       "restructuredtext.title.level.6": "italic dim cyan",
       
       # Admonitions - semantic colors
       "restructuredtext.note": "bold white on dark_blue",
       "restructuredtext.warning": "bold bright_yellow on dark_goldenrod",
       "restructuredtext.error": "bold bright_white on dark_red",
       "restructuredtext.tip": "bold bright_green on dark_green",
       "restructuredtext.important": "bold bright_magenta",
       "restructuredtext.danger": "bold bright_white on dark_red",
       
       # Links and references
       "restructuredtext.reference": "bright_cyan underline",
       "restructuredtext.toctree": "bright_cyan",
       
       # Lists
       "restructuredtext.bullet_list_marker": "bright_yellow",
       
       # Code and literals
       "restructuredtext.literalinclude": "grey66",
   })
   
   # Create console and render
   console = Console(theme=dark_theme)
   
   rst_content = """
   API Documentation
   =================
   
   Overview
   --------
   
   This is an important API.
   
   .. warning::
   
      Do not use this in production without testing!
   
   .. note::
   
      See the `official docs <https://example.com>`_ for more information.
   
   Features
   --------
   
   - Feature one
   - Feature two
   - Feature three
   
   .. tip::
   
      You can combine multiple features for powerful workflows.
   """
   
   console.print(RestructuredText(rst_content))

Tips for Effective Styling
---------------------------

1. **Use semantic colors**: Map admonitions to meaningful colors (red for danger, yellow for warnings, green for tips).

2. **Ensure contrast**: Make sure your chosen colors have sufficient contrast against your terminal background for easy reading.

3. **Be consistent**: Use a limited palette of related colors for visual coherence.

4. **Test in your environment**: Terminal color rendering varies across platforms and configurations, so test your theme in your actual terminal.

5. **Standard Rich color names**: Rich supports a wide variety of color names:
   
   - Basic: ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``magenta``, ``cyan``, ``white``
   - Bright: ``bright_red``, ``bright_green``, ``bright_blue``, etc.
   - Grayscale: ``grey0`` through ``grey100``
   - Named colors: ``dark_red``, ``navy_blue``, ``gold``, etc.
   - Hex colors: ``#ff0000``, ``#00ff00``, etc.

6. **Text attributes**: You can combine colors with attributes:
   
   - ``bold`` - bold/bright text
   - ``dim`` - dimmed/faint text
   - ``italic`` - italic text
   - ``underline`` - underlined text
   - ``blink`` - blinking text
   - ``reverse`` - reversed/inverted colors
   - ``conceal`` - hidden text
   - ``strike`` - strike-through text

See Also
--------

- `Rich documentation on styling <https://rich.readthedocs.io/en/latest/style.html>`__
- `Rich documentation on themes <https://rich.readthedocs.io/en/latest/themes.html>`__
- `reStructuredText reference <https://docutils.sourceforge.io/rst.html>`__
