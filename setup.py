#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'django-cleanup',
    version  = '0.1',
    packages = find_packages(),
    requires = ['python (>= 3.5)'],
    description  = 'Deletes old files.',
    long_description = open('README.rst').read(),
    author       = 'Yauheni Rumiantsau',
    author_email = 'jrumyantsev@gmail.com',
    url          = 'https://github.com/jayrumi/walmart-reviews',
    download_url = 'https://github.com/jayrumi/walmart-reviews',
    license      = '',
    keywords     = 'walmart',
    classifiers  = [
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)