from __future__ import absolute_import

from ansicolor.ansicolor import *  # noqa


__all__ = [
    'black',
    'blue',
    'cyan',
    'green',
    'magenta',
    'red',
    'white',
    'yellow',

    'colorize',
    'wrap_string',
    'get_code',

    'highlight_string',
    'get_highlighter',

    'strip_escapes',
    'justify_formatted',

    'colordiff',
    'set_term_title',
    'write_out',
    'write_err',

    'Colors',
]

__major_version__ = "0.2"
__release__ = "6"
__version__ = "%s.%s" % (__major_version__, __release__)
