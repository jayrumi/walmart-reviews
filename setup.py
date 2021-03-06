#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name     = 'walmart-reviews',
    version  = '1.2.0.dev1',
    packages = find_packages(),
    requires = ['python (>= 3.5)'],
    #install_requires = ['random', 'requests', 'lxml', 'datetime', 'time'],
    description  = 'Parsing reviews from Walmart.com without using API',
    long_description = long_description, #'A package for parsing reviews and all information about reviewers from walmart.com for specific item. For more information read README.rst', #open('README.rst').read(),
    author       = 'Yauheni Rumiantsau',
    author_email = 'jrumyantsev@gmail.com',
    url          = 'https://github.com/jayrumi/walmart-reviews',
    #download_url = '',
    license      = 'MIT License',
    keywords     = 'walmart parsing',
    classifiers  = [
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

