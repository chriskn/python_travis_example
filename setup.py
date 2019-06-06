# -*- coding: utf-8 -*-
# Ignore invalid names
# pylint: disable = C0103
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leaderboard",
    version="0.1.4",
    author="Christoph Knauf",
    author_email="knauf.christoph@gmail.com",
    description="Python CI/CD example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chriskn/python_travis_example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
