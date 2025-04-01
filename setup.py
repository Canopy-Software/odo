#!/usr/bin/env python

"""
Setup module used to install the package
"""

from distutils.core import setup

from setuptools import find_packages, setup

setup(
    name="canopy_client",
    version="0.2",
    description="Client package for interacting with Canopy software",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    url="https://github.com/Canopy-Software/canopy-client",
    author="Felipe de Oliveira",
    author_email="felipe.oliveira@canopyco.io",
    # packages=["src"],
    license="All rights reserved to Canopy Sofware Company",
    packages=find_packages(),
)