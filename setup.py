#!/usr/bin/env python

from distutils.core import setup
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='stanford_parser',
    version='1.0',
    description='Stanford parser python wrapper',
    author='Wenhu Chen, Stefanie Tellex',
    author_email='hustchenwenhu@gmail.com',
    url='http://projects.csail.mit.edu/spatial/Stanford_Parser',
    packages=['stanford_parser', 'test', '3rdParty'],
    license = "BSD",
    keywords = "Stanford Parser Python wrapper",
    long_description=read('README.md')
    )
