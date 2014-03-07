from setuptools import setup

import ansicolor


setup(
    name='ansicolor',
    version=ansicolor.__version__,
    description='A library to produce ansi color output and colored highlighting and diffing',
    author='Martin Matusiak',
    author_email='numerodix@gmail.com',
    url='https://github.com/numerodix/ansicolor',

    packages=[
        'ansicolor',
    ],

    # don't install as zipped egg
    zip_safe=False,
)
