# BASEDIR is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized CoFEA document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'CoFEA/docs/`.

"""
import os

from sphinx.util.pycompat import execfile_

os.system("git submodule update --init --force --recursive cadquery")
os.system("cp -r ./cadquery/doc/ext .")

BASEDIR = os.path.dirname(os.path.abspath(__file__))

execfile_(os.path.join(BASEDIR, "cadquery/doc/conf.py"), globals())

locale_dirs = [os.path.join(BASEDIR, "locale/")]


def setup(app):
    app.srcdir = os.path.join(BASEDIR, "cadquery/doc/")
    app.confdir = app.srcdir
