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


# -- Project information -----------------------------------------------------


project = 'SCALE Manual'
copyright = '2020, SCALE developers'
author = 'SCALE developers'

pygments_style = "default"
highlight_language = "python"

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sys, os
sys.path.append(os.path.abspath('extensions'))

import sphinx_rtd_theme

extensions = ['sphinxcontrib.bibtex', "sphinx_rtd_theme", 'sphinxcontrib.rsvgconverter']


from SCALE_highlighting import ScaleLexer, ScaleStyle, set_pygments_style
from sphinx.highlighting import lexers
lexers['scale'] = ScaleLexer()
set_pygments_style("scale", ScaleStyle)
pygments_style = "scale"

numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Keno.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

def setup(app):
   app.add_stylesheet('css/custom.css')

from pygments.lexer import RegexLexer, bygroups, include, inherit, words
from pygments.style import Style
from pygments import token
################################################################################
def set_pygments_style(mod_name, cls):
    import sys
    import pygments.styles
    cls_name = cls.__name__
    mod = type(__import__("os"))(mod_name)
    setattr(mod, cls_name, cls)
    setattr(pygments.styles, mod_name, mod)
    sys.modules["pygments.styles." + mod_name] = mod
    from pygments.styles import STYLE_MAP
    STYLE_MAP[mod_name] = mod_name + "::" + cls_name
################################################################################
class ScaleStyle(Style):
    default_style = ""
    styles = {
        token.Comment: 'italic #008000',
        token.Number: 'bold #ff0000',
        token.Name: 'bold #0000FF',
        token.Name.Function: 'bold #000000',
        token.Text: 'bold #000000',
        token.String: 'italic #ff0000',
    }
################################################################################
class ScaleLexer(RegexLexer):
    name = 'Scale'
    aliases = ['scale']
    filenames = ['*.inp']

    tokens = {
        'root': [
            (r'^=.*\n', token.Name.Function),
            (r'^\'.*\n', token.Comment),
            (r'^\‘.*\n', token.Comment),
            (r'[ ]{1,}', token.Text),
            (r'\b(?i)(end([ ]{1,}|\n)end)\s\w+', token.Name,'block'),
            (r'\b(?i)(read|end)\s\w+', token.Name,'block'),
            (r'\b(?i)(end\s*$)', token.Name,'block'),
            (r'\b(?i)(location|cylgeometry|gridgeometry)\s', token.Name, 'block'),
            (r'\b(?i)(energybounds|timebounds)\s', token.Name, 'block'),
            (r'\b(?i)(response|distribution)\s', token.Name, 'block'),
            (r'\b(?i)(pointdetector|regiontally|meshtally)\s', token.Name, 'block'),
            (r'\b(?i)(src|meshsourcesaver)\s', token.Name, 'block'),
            (r'\b(?i)(importancemap|adjointsource|macromaterial)\s', token.Name, 'block'),
            (r'\b(?i)(fill)\s', token.Name, 'block'),
            (r'\b[0-9]+\s',token.Number),
            (r'([-+]?\d*\.?\d+)(?:[eE]([-+]?\d+))?\s',token.Number),
            (r'\"(.+?)\"', token.String),
            (r'\'(.+?)\'', token.String),
            (r'\”(.+?)\”', token.String),
            (r'\‘(.+?)\‘', token.String),
            (r'\“(.+?)\”', token.String),
            (r'\“(.+?)\"', token.String),
            (r'\”(.+?)\"', token.String),
            (r'\!.*\n', token.Comment),
            (r'(\w+|\n| )', token.Text),
            (r'(=|\-|\+|\%|\,|\‘|\$|\{|\}|\(|\)|\[|\]|\–|\_|\.|\…|\*|\,|\;|\:|\<|\>|\?|\/|\\)', token.Text),
            (r'\s+', token.Text),
            (r'.* ', token.Text)
        ],
        'block': [
            (r'(\n|[ ]{0,}\n)', token.Text,'#pop'),
            (r'[a-zA-Z]+\s', token.Name,'#pop'),
            (r'[0-9]+\s', token.Number,'#pop'),
            (r'\!.*\n', token.Comment,'#pop'),
            (r'.*\n', token.Text,'#pop'),
        ],
    }

################################################################################
def test():
    from pygments.styles import get_all_styles, STYLE_MAP
    styles = list(get_all_styles())
    print('style_maps: ', STYLE_MAP.keys())
    print('styles: ',styles)
################################################################################
if __name__ == "__main__":
    test()
################################################################################
