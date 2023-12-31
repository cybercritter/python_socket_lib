# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
#import sphinx_bootstrap_theme


sys.path.insert(0, os.path.abspath(".."))

project = 'Python Socket Mock'
copyright = '2023, cybercritter'
author = 'cybercritter'
release = '0.0.1'

autodoc_default_options = {
    'members': True,
    #'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',

}
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = "traditional"
html_theme = "sphinx_documatt_theme"
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ['_static']
