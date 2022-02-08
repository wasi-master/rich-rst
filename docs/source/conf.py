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

import re

# -- Project information -----------------------------------------------------

project = 'rich-rst'
copyright = '2022, Wasi Master aka. Arian Mollik Wasi'
author = 'Wasi Master aka. Arian Mollik Wasi'

# The full version, including alpha/beta/rc tags
version = ''
with open('../../rich_rst/__init__.py', encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

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
intersphinx_mapping = {'python': ('https://docs.python.org/3', None), 'rich': ('https://rich.readthedocs.io/en/stable/', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# For readthedocs
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinxawesome_theme'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# Add any files that contain extra static files that will be placed in the
# document root. They are copied after the builtin static files and will
# overwrite the builtin files
html_extra_path = ['_extra']
# Add any files that contain extra custom css
html_css_files = ["custom.css"]

# Config for sphinxawesome_theme
# html_permalinks_icon = '<span>#</span>'
# html_collapsible_definitions = True
# html_theme_options = {
#     "show_prev_next": True,
#     "show_scrolltop": True,
#     "extra_header_links": {
#         "Docs": "./docs",
#         "Demo": "./demo",
#     }
# }

html_theme_options = {
    'display_version': True,
}
html_context = {
  "display_github": True, # Add 'Edit on Github' link instead of 'View page source'
  "github_user": "wasi-master",
  "github_repo": project,
  "github_version": "main",
  "conf_py_path": "/docs/source/",
}