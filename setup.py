#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='coincappy',
    version='0.1.0',
    description="Simple Python wrapper around CoinMarketCap free endpoints",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kiwioverseas/coincappy',
    keywords=['crypto', 'cryptocurrency', 'coinmarketcap'],
    license='MIT',
    packages=['coincappy'],
    python_requires='>=3.6',
    install_requires=['requests'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
)