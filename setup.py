#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup this package."""

from setuptools import find_packages, setup

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
    python_requires='>=3.6',
    setup_requires=[
        'pytest-runner',
        'setuptools-scm',
        'setuptools-pipfile',
    ],
    use_pipfile={
        'path': 'Pipfile',
        'extras': True,
    },
    # PyPI Metadata
    keywords=['pytest', 'yapf'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
