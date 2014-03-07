from setuptools import setup

import ansicolor


setup(
    name='ansicolor',
    version=ansicolor.__version__,
    description='Ansi color output library',
    author='Martin Matusiak',
    author_email='numerodix@gmail.com',

    packages=[
        'ansicolor',
    ],

    # don't install as zipped egg
    zip_safe=False,
)
