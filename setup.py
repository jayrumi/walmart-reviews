#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'walmart-reviews',
    version  = '0.1',
    packages = find_packages(),
    requires = ['python (>= 3.5)'],
    description  = 'Parsing reviews from Walmart.com without using API',
    long_description = 'A package for parsing reviews and all information about reviewers from walmart.com for specific item. For more information read README.rst', #open('README.rst').read(),
    author       = 'Yauheni Rumiantsau',
    author_email = 'jrumyantsev@gmail.com',
    url          = 'https://github.com/jayrumi/walmart-reviews',
    download_url = 'https://github.com/jayrumi/walmart-reviews',
    license      = 'MIT License',
    keywords     = 'walmart',
    classifiers  = [
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)