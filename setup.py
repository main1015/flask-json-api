#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
import flask_json_api

setup(
    name='Flask-json-api',
    version=flask_json_api.__version__,
    url='https://github.com/anjianshi/flask-json-api',
    license='MIT',
    author='anjianshi',
    author_email='anjianshi@gmail.com',
    description='Flask REST API extension',
    packages=['flask_json_api'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=0.8'],
    keywords=['flask', 'python', 'rest', 'api'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)