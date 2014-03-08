ansicolor
=========

.. image:: https://pypip.in/v/ansicolor/badge.png
    :target: https://pypi.python.org/pypi/ansicolor/

.. image:: https://travis-ci.org/numerodix/ansicolor.png?branch=master
    :target: https://travis-ci.org/numerodix/ansicolor

.. image:: https://pypip.in/wheel/ansicolor/badge.png
    :target: https://pypi.python.org/pypi/ansicolor/

Supported platforms:

- CPython 2.6, 2.7, 3.2, 3.3
- PyPy


Introduction
------------

`ansicolor` is a library that makes it easy to use ansi color markup in command
line programs.


Installation
------------

.. code:: bash

    $ pip install ansicolor


Simple color markup
-------------------

.. code:: python

    from ansicolor import green
    from ansicolor import red
    from ansicolor import white

    print("Let's try two colors: %s and %s!" % (red("red"), green("green")))
    print("It's also easy to produce text in %s," % (red("bold", bold=True)))
    print("...%s," % (green("reverse", reverse=True)))
    print("...and %s." % (cyan("bold and reverse", bold=True, reverse=True)))
