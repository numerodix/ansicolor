from __future__ import absolute_import

from ansicolor.ansicolor import black
from ansicolor.ansicolor import blue
from ansicolor.ansicolor import cyan
from ansicolor.ansicolor import green
from ansicolor.ansicolor import magenta
from ansicolor.ansicolor import red
from ansicolor.ansicolor import white
from ansicolor.ansicolor import yellow

from ansicolor.ansicolor import colorize
from ansicolor.ansicolor import colorize_v2
from ansicolor.ansicolor import get_code
from ansicolor.ansicolor import get_code_v2
from ansicolor.ansicolor import wrap_string

from ansicolor.ansicolor import highlight_string
from ansicolor.ansicolor import get_highlighter

from ansicolor.ansicolor import strip_escapes
from ansicolor.ansicolor import justify_formatted

from ansicolor.ansicolor import colordiff
from ansicolor.ansicolor import set_term_title
from ansicolor.ansicolor import write_out
from ansicolor.ansicolor import write_err

from ansicolor.ansicolor import Colors


__all__ = [
    "black",
    "blue",
    "cyan",
    "green",
    "magenta",
    "red",
    "white",
    "yellow",
    "colorize",
    "colorize_v2",
    "get_code",
    "get_code_v2",
    "wrap_string",
    "highlight_string",
    "get_highlighter",
    "strip_escapes",
    "justify_formatted",
    "colordiff",
    "set_term_title",
    "write_out",
    "write_err",
    "Colors",
]

__major_version__ = "0.3"
__release__ = "3"
__version__ = "%s.%s" % (__major_version__, __release__)
