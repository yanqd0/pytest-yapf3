#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup this package."""

from setuptools import find_packages, setup

_TEST_REQUIRES = [
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-docstyle',
    'pytest-flake8',
    'pytest-isort',
    'pytest-mock',
    'pytest-pep8',
    'pytest-pylint',
]

setup(
    use_scm_version=True,
    zip_safe=False,
    # Package modules and data
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # Entries
    entry_points={
        'pytest11': ('yapf = pytest_yapf3', ),
    },
    # Requires
    python_requires='>=3.4',
    install_requires=(
        'pytest>=3.1.1',
        'yapf>=0.16.2',
    ),
    setup_requires=[
        'pytest-runner',
        'setuptools-scm',
    ],
    tests_require=_TEST_REQUIRES,
    extras_require={
        'dev': _TEST_REQUIRES + [
            'flake8',
            'isort',
            'pylint',
        ],
    },
    # PyPI Metadata
    keywords=['pytest', 'yapf', 'sc'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
