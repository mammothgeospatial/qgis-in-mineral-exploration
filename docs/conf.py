# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'QGIS in Mineral Exploration'
copyright = '2023, Grant Boxer'
author = 'Grant Boxer'
version = '1.0'
release = '1.0'

# master_doc = 'index'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Internationalisation ----------------------------------------------------

language = 'en'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo.png'
html_last_updated_fmt = '%d %b %Y, %H:%M %z'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = '_static/qgis_logo.ico'

html_theme_options = {
    'analytics_id': 'G-MX419S33H7',
    # 'analytics_anonymize_ip': False,
    # logo_only: Only display the logo image, do not display the project name at the top of the sidebar. Default: False,
    # 'logo_only': False,
    # display_version: If True, the version number is shown at the top of the sidebar. Default: True,
    # 'display_version': True,
    'prev_next_buttons_location': 'top',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
}

# Custom css
def setup(app):
   app.add_css_file('css/custom.css')

# -- Options for LaTeX output --------------------------------------------------

# latex_engine = 'xelatex'

latex_logo = '_static/logo.png'

# conf.py

# ...

latex_maketitle = f'''
  \\begin{{titlepage}}
    \\centering
    \\vspace*{{2cm}}
    \\sffamily
    \\Huge QGIS in \\par
    \\Huge Mineral Exploration \\par
    \\vspace{{2cm}}
    \\vspace{{2cm}}
    {{\\Large Version: {version} \\par }}
    {{\\large \\today \\par}}
    \\vspace{{1cm}}
    \\vspace*{{\\fill}}
  \\end{{titlepage}}
'''


latex_elements = {
    'papersize': 'a4paper',
    'preamble': r'''
      \usepackage[none]{hyphenat}
      \usepackage[document]{ragged2e}
      \usepackage[en-GB]{datetime2}
      \DTMlangsetup[en-GB]{abbr,monthdaysep={\space},dayofmonth=ordinal}
      \usepackage[titles]{tocloft}
      \usepackage{graphicx}
      # \setkeys{Gin}{width=0.8\textwidth}  % Set default width for all images
      \usepackage{microtype}
    ''',
    'extraclassoptions': 'openany,oneside',
    'fncychap': r'\usepackage[Glenn]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    # 'maketitle': latex_maketitle,
  }
