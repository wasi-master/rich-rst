# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import importlib.metadata

# -- Project information -----------------------------------------------------

project = 'rich-rst'
copyright = '2022, Wasi Master aka. Arian Mollik Wasi'
author = 'Wasi Master aka. Arian Mollik Wasi'

# The full version, including alpha/beta/rc tags
version = importlib.metadata.version('rich-rst')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

# Add the locations and names of other projects that should be linked to in this documentation.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'rich': ('https://rich.readthedocs.io/en/stable/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# For readthedocs
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# Modern Furo theme - clean, animated, dark/light mode toggle
html_theme = 'furo'

html_title = f'rich-rst'

html_theme_options = {
    # Light mode colour palette
    "light_css_variables": {
        "--color-brand-primary": "#5B4FE9",
        "--color-brand-content": "#5B4FE9",
        "--color-brand-visited": "#8B5CF6",
        "--font-stack": "'Google Sans', 'Inter', system-ui, sans-serif",
        "--font-stack--monospace": "'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace",
        "--color-admonition-background": "rgba(91, 79, 233, 0.05)",
        "--color-sidebar-background": "#f8f8fc",
        "--color-sidebar-background-border": "#e8e5f5",
        "--color-sidebar-brand-text": "#5B4FE9",
        "--color-sidebar-link-text--top-level": "#2d2d3f",
        "--color-sidebar-item-background--hover": "rgba(91, 79, 233, 0.08)",
        "--color-sidebar-item-expander-background--hover": "rgba(91, 79, 233, 0.08)",
        "--color-highlight-on-target": "rgba(91, 79, 233, 0.12)",
        "--color-api-name": "#5B4FE9",
        "--color-api-pre-name": "#8B5CF6",
        "--color-link": "#5B4FE9",
        "--color-link--hover": "#8B5CF6",
        "--color-link-underline": "rgba(91, 79, 233, 0.3)",
        "--color-link-underline--hover": "#8B5CF6",
    },
    # Dark mode colour palette
    "dark_css_variables": {
        "--color-brand-primary": "#A78BFA",
        "--color-brand-content": "#A78BFA",
        "--color-brand-visited": "#C4B5FD",
        "--font-stack": "'Google Sans', 'Inter', system-ui, sans-serif",
        "--font-stack--monospace": "'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace",
        "--color-admonition-background": "rgba(167, 139, 250, 0.08)",
        "--color-sidebar-background": "#12111a",
        "--color-sidebar-background-border": "#2a2738",
        "--color-sidebar-brand-text": "#A78BFA",
        "--color-sidebar-link-text--top-level": "#d4d0e8",
        "--color-sidebar-item-background--hover": "rgba(167, 139, 250, 0.1)",
        "--color-sidebar-item-expander-background--hover": "rgba(167, 139, 250, 0.1)",
        "--color-highlight-on-target": "rgba(167, 139, 250, 0.15)",
        "--color-api-name": "#A78BFA",
        "--color-api-pre-name": "#C4B5FD",
        "--color-link": "#A78BFA",
        "--color-link--hover": "#C4B5FD",
        "--color-link-underline": "rgba(167, 139, 250, 0.3)",
        "--color-link-underline--hover": "#C4B5FD",
        "--color-background-primary": "#0f0e17",
        "--color-background-secondary": "#12111a",
        "--color-background-hover": "rgba(167, 139, 250, 0.05)",
        "--color-background-border": "#2a2738",
        "--color-foreground-primary": "#e8e4f8",
        "--color-foreground-secondary": "#b8b4d4",
        "--color-foreground-muted": "#8884a8",
        "--color-foreground-border": "#3d3a5c",
        "--color-inline-code-background": "rgba(167, 139, 250, 0.1)",
    },
    # Navigation & UI options
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "source_repository": "https://github.com/wasi-master/rich-rst/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    # Footer social icons
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/wasi-master/rich-rst",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">'
                '<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59'
                ".4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23"
                "-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87"
                ".87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82"
                "-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 "
                "1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27"
                '.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 '
                '2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>'
            ),
            "class": "",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/rich-rst/",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24">'
                '<path d="M12.001 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm.483 4.5c1.72 0 3.1.28 '
                "3.93.77.81.48 1.26 1.14 1.26 2.03v4.5c0 .89-.47 1.66-1.27 2.12-.8.46-1.97.71"
                "-3.42.71H9.73c-.44 0-.8.36-.8.8v1.56c0 .44.36.8.8.8h2.54c.44 0 .8-.36.8-.8v"
                "-.73h.73c.44 0 .8.36.8.8v.93c0 .89-.47 1.65-1.27 2.1-.8.47-1.96.72-3.4.72-1"
                ".45 0-2.62-.25-3.43-.72-.8-.45-1.27-1.21-1.27-2.1v-4.5c0-.89.47-1.66 1.27-2"
                '.12.8-.46 1.97-.71 3.42-.71h3.27c.44 0 .8-.36.8-.8V7.3c0-.44-.36-.8-.8-.8H9'
                ".73c-.44 0-.8.36-.8.8v.73h-.73c-.44 0-.8-.36-.8-.8v-.93c0-.89.47-1.55 1.26-"
                '2.03.82-.49 2.2-.77 3.83-.77z"/></svg>'
            ),
            "class": "",
        },
    ],
}

# Add any paths that contain custom static files (style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# Add any files that contain extra static files that will be placed in the
# document root.
html_extra_path = ['_extra']
# Custom CSS files loaded after theme CSS
html_css_files = ["custom.css"]
# Custom JS for animations and interactivity
html_js_files = ["custom.js"]

html_context = {
    "github_user": "wasi-master",
    "github_repo": project,
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}
