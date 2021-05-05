Release notes
=============


0.3.1
-----

- Updating changelog (belatedly).

0.3.0
-----

- Dropped support for Python 2.6.

0.2.6
-----

- New :func:`ansicolor.get_code_v2` which mirrors :func:`ansicolor.get_code` but also
  allows passing ``underline`` and ``blink``.
- New :func:`ansicolor.colorize_v2` which mirrors :func:`ansicolor.colorize` but also
  allows passing ``underline`` and ``blink``.

0.2.4
-----

- First version supporting Python 3.4!

0.2.3
-----

- :func:`ansicolor.highlight_string` accepts a new kwarg `colors`. `color` has been
  deprecated.

0.2.2
-----

- :func:`ansicolor.colorize` now accepts ``start`` and ``end`` kwargs.
  :func:`ansicolor.wrap_string` has been deprecated.
