# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="data-structures",
    description="A Python implementation of data structures.",
    version=0.1,
    author="David Banks, James Canning",
    author_email="crashtack@gmail.com, fake@fake..com",
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
