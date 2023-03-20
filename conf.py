# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os.path

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'NeuroPoly Internal Wiki'
copyright = '2021, NeuroPoly'
author = 'NeuroPoly'


# -- General configuration ---------------------------------------------------

root_doc = 'README'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence"]

# enable #section links: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 4

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '.venv', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["theme.css"]

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "gtranslate.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}

html_favicon = "_static/logo.png"
panels_add_bootstrap_css = False

html_sourcelink_suffix = ".md" # our sources are in markdown; but this only has an effect if "use_download_button": True

html_theme_options = {
    "logo": {
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
        "text": "NeuroPoly Lab Manual",
    },
    "toc_title": "Page Contents",
    "search_bar_text": "Search...",

    "use_fullscreen_button": False,
    "use_edit_page_button": True,
    "use_download_button": False,
}

html_context = {
    "default_mode": "light",
    "github_user": "neuropoly",
    "github_repo": "intranet.neuro.polymtl.ca",
    "github_version": "master",
    "doc_path": "",
}


# On Github's UI, README.{md,txt,rst} are treated as front pages
# On every other web site, index.{html,php,py,....} are.
# To make both renders work, glue these two together by symlinks _build/html/**/index.html -> README.html
#
# Doing this here, in conf.py, is hacky, but it's what we've got for now.
# TODO: an even better solution would be to find/write a sphinx extension
#       that internally renamed README -> index during the writing, but only internally.
#       but unless we special-cased something hat would break the edit_page_button.
# TODO: Another solution is to host on that lets us use .htaccess files to choose README.md as index pages
# TODO: Another solution is to decide not to care about auto-rendering index pages on github.
for dir, dirs, fnames in os.walk("."): #XXX "." is possibly buggy? This isn't necessarily running from the source dir.
    dirs[:] = [d for d in dirs if d not in exclude_patterns] # prune the search
    for fname in fnames:
        if os.path.splitext(fname)[0] == "README":
            z = os.path.join("_build", "html", dir, "index.html")
            #html_extra_path.append(z)
            os.makedirs(os.path.dirname(z), exist_ok=True)
            if os.path.lexists(z):
                os.unlink(z)
            if not os.path.exists(
                     os.path.join(os.path.dirname(z),
                                  "README.html")): # don't create dangling symlinks;
                                                   # it annoyes Github Pages.
                os.symlink("README.html", z)
