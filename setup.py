#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'walmart-reviews',
    version  = '0.1',
    packages = find_packages(),
    requires = ['python (>= 3.5)'],
    description  = 'Deletes old files.',
    long_description = open('README.rst').read(),
    author       = 'Yauheni Rumiantsau',
    author_email = 'jrumyantsev@gmail.com',
    url          = 'https://github.com/jayrumi/walmart-reviews',
    download_url = 'https://github.com/jayrumi/walmart-reviews/blob/master/',
    license      = 'Apache 2.0',
    keywords     = 'walmart',
    classifiers  = [
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)