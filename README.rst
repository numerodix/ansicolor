ansicolor
=========

.. image:: https://pypip.in/v/ansicolor/badge.png
    :target: https://pypi.python.org/pypi/ansicolor/

.. image:: https://travis-ci.org/numerodix/ansicolor.png?branch=master
    :target: https://travis-ci.org/numerodix/ansicolor

.. image:: https://pypip.in/wheel/ansicolor/badge.png
    :target: https://pypi.python.org/pypi/ansicolor/

Python version support: CPython 2.6, 2.7, 3.2, 3.3 and PyPy.


Introduction
------------

``ansicolor`` is a library that makes it easy to use ansi color markup in command
line programs.


Installation
------------

.. code:: bash

    $ pip install ansicolor


Getting started
---------------

To highlight using colors:

.. code:: python

    from ansicolor import green
    from ansicolor import red
    from ansicolor import white

    print("Let's try two colors: %s and %s!" % (red("red"), green("green")))
    print("It's also easy to produce text in %s," % (red("bold", bold=True)))
    print("...%s," % (green("reverse", reverse=True)))
    print("...and %s." % (cyan("bold and reverse", bold=True, reverse=True)))


This will emit ansi escapes into the string: one when starting a color, another
to reset the color back to the default:

.. code:: python

    >>> from ansicolor import green

    >>> green("green")
    '\x1b[0;0;32mgreen\x1b[0;0m'


If I want to be able to pass a color as an argument I can also use the
``colorize`` function:

.. code:: python

    from ansicolor import Colors
    from ansicolor import colorize

    print(colorize("I'm blue", Colors.Blue))


I can also apply color on a portion of a string:

.. code:: python

    from ansicolor import Colors
    from ansicolor import wrap_string

    print(wrap_string("I'm blue, said the policeman.", 8, Colors.Blue))


Sometimes I may have a string that contains markup and I'll want to do something
with it that concerns only the text, so I can strip the markup:

.. code:: python

    >>> from ansicolor import red
    >>> from ansicolor import strip_escapes
    >>> from ansicolor import yellow

    >>> message = "My favorite colors are %s and %s" % (yellow("yellow"), red("red"))
    >>> print("The length of this string is not: %d" % len(message))
    The length of this string is not: 67
    >>> print("The length of this string is: %d" % len(strip_escapes(message)))
    The length of this string is: 37


Going further
-------------

Take a look at the ``demos`` to see what's possible.

.. code:: bash

    $ python -m ansicolor.demos --color
    $ python -m ansicolor.demos --highlight
    $ python -m ansicolor.demos --diff

Also see the `API documentation`_.


.. _`API documentation`: https://ansicolor.readthedocs.org/
