from path import Path
from paver.doctools import cog, html
from paver.easy import options
from paver.options import Bunch
from paver.setuputils import setup
from setuptools import find_packages

IMPORTS=[cog, html, setup]

options(
)

# get info from setup.py
setup_py = ''.join(
    [x for x in Path('setup.py').lines() if 'setuptools' not in x])
exec(setup_py)





