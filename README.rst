ansicolor
=========

.. image:: https://badge.fury.io/py/ansicolor.png
        :target: https://badge.fury.io/py/ansicolor

.. image:: https://travis-ci.org/numerodix/ansicolor.png?branch=master
    :target: https://travis-ci.org/numerodix/ansicolor

.. image:: https://pypip.in/wheel/ansicolor/badge.png
    :target: https://pypi.python.org/pypi/ansicolor/

.. image:: https://pypip.in/license/ansicolor/badge.png
        :target: https://pypi.python.org/pypi/ansicolor/

Python version support: CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy.


Introduction
------------

``ansicolor`` is a library that makes it easy to use ansi color markup in command
line programs.


Installation
------------

.. code:: bash

    $ pip install ansicolor


Documentation
-------------

Read the `documentation`_ on Read the Docs!


Going further
-------------

Take a look at the ``demos`` to see what's possible.

.. code:: bash

    $ python -m ansicolor.demos --color
    $ python -m ansicolor.demos --highlight
    $ python -m ansicolor.demos --diff


.. _`documentation`: https://ansicolor.readthedocs.org/



Maintenance tasks
-----------------


Setting up a development environment (Ubuntu)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    # if you don't have `mkvirtualenv` & `workon` functions in your shell
    $ sudo apt install virtualenvwrapper

    $ mkvirtualenv ansicolor
    (ansicolor) $ pip install -r dev-requirements.txt


Running tests
^^^^^^^^^^^^^

.. code:: bash

    $ py.test


Measuring code coverage
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ py.test --cov=ansicolor
    $ coverage html
    # open htmlcov/index.html in the browser