Sphinx Roles with Compatibility Mode
=====================================

This test demonstrates how rich-rst handles Sphinx-specific roles with
``sphinx_compat=True`` (the default behavior).

Common Sphinx Roles
-------------------

These roles are commonly used in Python docstrings and render as inline code:

- Function reference: :func:`os.path.join`
- Method reference: :meth:`str.format`
- Class reference: :class:`pathlib.Path`
- Module reference: :mod:`collections.abc`
- Attribute reference: :attr:`object.__name__`
- Object reference: :obj:`sys.stdout`
- Data reference: :data:`sys.maxsize`
- Exception reference: :exc:`ValueError`
- Type reference: :type:`int`

Python Domain Roles
-------------------

With explicit python domain prefix:

- :py:func:`open`
- :py:class:`dict`
- :py:meth:`list.append`
- :py:mod:`os.path`

Explicit Reference Text
-----------------------

When using explicit reference text (custom display text), only the display text
should be shown, not the full reference:

- :func:`custom name <os.path.join>` should show "custom name"
- :class:`MyPath <pathlib.Path>` should show "MyPath"
- :meth:`format method <str.format>` should show "format method"

Mixed Content
-------------

Sphinx roles work seamlessly with other RST markup:

This paragraph contains a :func:`function_call` and **bold text** and
``regular code`` all together. You can also have :class:`MyClass` in lists:

- Item with :meth:`method_name` reference
- Another :func:`function_ref` here
- Regular text without roles

Realistic Example
-----------------

Here's a realistic Python docstring example::

    def read_config(path, encoding='utf-8'):
        """
        Read configuration file from filesystem.

        Parameters
        ----------
        path : :class:`pathlib.Path` or str
            Path to configuration file
        encoding : str
            File encoding, see :func:`open` for details

        Returns
        -------
        :class:`dict`
            Parsed configuration dictionary

        See Also
        --------
        :func:`write_config` : Write configuration to file
        :meth:`dict.update` : Update configuration values
        """
        pass
