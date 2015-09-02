#!/usr/bin/env python

import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload --sign')
    sys.exit()

packages = [
    'slugid',
]

version = ''
with open('slugid/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='slugid',
    version=version,
    description='Base64 encoded uuid v4 slugs',
    author='Pete Moore',
    author_email='pmoore@mozilla.com',
    url='http://taskcluster.github.io/slugid.py',
    packages=packages,
    package_data={'': ['LICENSE', 'README.md']},
    license='MPL 2.0',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ),
)
