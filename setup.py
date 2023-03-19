# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('f1/f1.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "f1",
    packages = ["f1"],
    entry_points = {
        "console_scripts": ['f1 = f1.f1:main']
    },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Renato Duarte",
    author_email = "rntdrt.s@gmail.com",
)
