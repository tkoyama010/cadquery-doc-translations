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
import sys

from sphinx.util.osutil import fs_encoding

os.system("git submodule update --init --force --recursive cadquery")
os.system("cp -r ./cadquery/doc/ext .")

BASEDIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASEDIR, "cadquery/doc/conf.py"), "rb") as f:
    code = compile(f.read(), fs_encoding, "exec")
    exec(code, globals())

locale_dirs = [os.path.join(BASEDIR, "locale/")]


def setup(app):
    app.srcdir = os.path.join(BASEDIR, "cadquery/doc/")
    app.confdir = app.srcdir
