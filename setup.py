from setuptools import setup

import ansicolor


setup(
    name="ansicolor",
    version=ansicolor.__version__,
    description=(
        "A library to produce ansi color output and colored highlighting and diffing"
    ),
    author="Martin Matusiak",
    author_email="numerodix@gmail.com",
    url="https://github.com/numerodix/ansicolor",
    packages=[
        "ansicolor",
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    # don't install as zipped egg
    zip_safe=False,
)
