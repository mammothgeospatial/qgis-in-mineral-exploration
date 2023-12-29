# How to use this repository

## Windows

### Dependencies
- `git`
- `Python` and `pip`
- `virtualenv`
  - see [Windows virtualenv setup](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
  - you might need to add it to your path environment variable
- `make`
  - see [GNU Make for Windows](https://gnuwin32.sourceforge.net/packages/make.htm)
  - you might need to add it to your path environment variable

### Set up
- Clone the repository
- Set up a virtual environment in the repository root: `virtualenv venv`
- Activate your virtual environment: `.\venv\Scripts\activate`
- Install required Python modules into your virtual environment: `pip install -r requirements.txt`

### Build the docs
- Activate your virtual environment: `.\venv\Scripts\activate`
- In the `docs` directory: `make html` -> this builds the docs in `_build/html`
- Open `_build/html/docs/index.html` in a browser to preview

## Linux

```bash
# Install packages
sudo apt install texlive-latex-recommended texlive-fonts-recommended tex-gyre texlive-latex-extra latexmk

# Build html
make html

# Build pdf
make latexpdf
```
## More info
### reStructuredText basics

- [reStructuredText Quick Reference](https://docutils.sourceforge.io/docs/user/rst/quickref.html#section-structure)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

### QGIS Docs example

If you want to see how the QGIS docs use various features in reStructuredText, it's useful to flick between their docs packages:

[QGIS Docs - Browser Introduction](https://docs.qgis.org/3.28/en/docs/user_manual/introduction/browser.html)

and the GitHub repo so you can see the reStructuredText:

[QGIS Documentation GitHub Repo - Browser](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/introduction/browser.rst)
