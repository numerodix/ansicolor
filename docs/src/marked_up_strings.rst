Working with marked-up strings
==============================


Stripping markup
----------------

Sometimes I may have a string that contains markup and I'll want to do something
with it that concerns only the text, so I can strip the markup:

.. code:: python

    >>> from ansicolor import red
    >>> from ansicolor import strip_escapes
    >>> from ansicolor import yellow

    >>> message = "My favorite colors are %s and %s" % (yellow("yellow"), red("red"))
    >>> print("The length of this text is not: %d" % len(message))
    The length of this text is not: 67
    >>> print("The length of this text is: %d" % len(strip_escapes(message)))
    The length of this text is: 37


Producing output
----------------

Printing marked-up strings directly is not appropriate for all use cases. When
writing to a file it's generally not desirable to print ansi escapes meant
for a terminal. The two functions :data:`ansicolor.write_out` and
:data:`ansicolor.write_err` omit ansi escapes if the file being written to is
not a tty.

.. literalinclude:: ../snippets/marked_up_strings_1.py
