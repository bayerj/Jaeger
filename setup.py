#! /usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Justin Bayer, bayer.justin@googlemail.com'


from setuptools import setup, find_packages


setup(
    name="jaeger",
    version="pre-0.1",
    license="BSD",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
)

