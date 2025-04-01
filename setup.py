#!/usr/bin/env python

"""
Setup module used to install the package
"""

from distutils.core import setup

from setuptools import find_packages, setup

setup(
    name="odo-canopy",
    version="0.2",
    description="Client package for interacting with odo",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    url="https://github.com/Canopy-Software/odo",
    author="Felipe de Oliveira",
    author_email="felipe.oliveira@canopyco.io",
    # packages=["src"],
    license="All rights reserved to Canopy Sofware Company",
    packages=find_packages(),
)