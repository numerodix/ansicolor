ansicolor
=========

.. image:: https://badge.fury.io/py/ansicolor.png
        :target: https://badge.fury.io/py/ansicolor

.. image:: https://img.shields.io/pypi/wheel/ansicolor.svg
    :target: https://pypi.python.org/pypi/ansicolor/

.. image:: https://img.shields.io/pypi/l/ansicolor.svg
        :target: https://pypi.python.org/pypi/ansicolor/

Python version support: CPython 2.7, 3.2+.


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

    # creating the virtual env the first time
    $ mkvirtualenv ansicolor
    (ansicolor) $ pip install -r dev-requirements.txt

    # re-activating the virtual env next time
    $ workon ansicolor

All the steps below assume you have an activated virtual env (even though the
``(ansicolor)`` prompt is not shown).


Running unit tests
^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ py.test


Measuring code coverage
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ py.test --cov=ansicolor.ansicolor
    $ coverage html
    # open htmlcov/index.html in the browser


Running all possible tests under tox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use ``tox`` to run both the unit tests and the demos under several different
Python interpreter versions. Depending on which interpreters you have installed
(this is managed system-wide and not covered in this README) ``tox`` will most
likely give you a partial success.

.. code:: bash

    # to run against all interpreters
    $ tox

    # to run only against selected interpreters
    $ tox -e py27,py38


Checking code style
^^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ flake8 ansicolor


Re-formatting code
^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ black ansicolor tests
