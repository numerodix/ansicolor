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

You can also download `tarballs from Github`_.


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

The tests expect the environment variable ``TERM`` to be set, and to a value
that is not ``dumb``. If this is not the case tests will fail.

The canonical setting is ``TERM=xterm`` to signal that a terminal supports
ANSI control codes just like ``xterm`` does.

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


Release a new version
^^^^^^^^^^^^^^^^^^^^^

1. Before starting work on a change/fix/whatever, make sure there is no
   unfinished work on ``develop`` and merge ``master`` into ``develop``.
2. Make all the changes on ``develop``.

Quality assurance (see steps above for how to):

1. Make sure all tests are passing.
2. Make sure test coverage has not declined.
3. Make sure ``tox`` run succeeds on all (installed) interpreters.
4. Make sure ``flake8`` checker passes.
5. Make sure ``black`` formatter has no changes to make.

Doc updates:

1. Update ``docs/src/changes.rst``.

Doing a release:

1. Bump version in ``ansicolor/__init__.py``.
2. Git tag the new version and push the tag. This allows users/packagers to
   download an auto-generated zip/tarball of the tagged release from Github.
3. ``python setup.py sdist``
4. ``python setup.py bdist_wheel``
5. ``twine upload dist/*``

Finally:

1. Merge ``develop`` into ``master``.

Post-release verification:

1. ``pip install -U ansicolor`` from PyPI and use a tool that uses it.


.. _`documentation`: https://ansicolor.readthedocs.org/
.. _`tarballs from Github`: https://github.com/numerodix/ansicolor/tags
