#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['readchar', 'blessings']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Lars Yencken",
    author_email='lars@yencken.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="A lightweight  Python interface for annotating things.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='questioner',
    name='questioner',
    packages=find_packages(include=['questioner']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/larsyencken/questioner',
    version='0.1.0',
    zip_safe=False,
)
