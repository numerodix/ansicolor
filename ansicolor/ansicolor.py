# Author: Martin Matusiak <numerodix@gmail.com>

import difflib
import os
import re
import sys
import warnings


__all__ = [  # noqa
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
    "wrap_string",
    "get_code",
    "get_code_v2",
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


# Don't write escapes to dumb terminals
_disabled = (not os.environ.get("TERM")) or (os.environ.get("TERM") == "dumb")


class Colors(object):
    """Container class for colors"""

    @classmethod
    def new(cls, colorname):
        try:
            cls._colorlist
        except AttributeError:
            cls._colorlist = []

        newcls = type.__new__(type, colorname, (object,), {})
        newcls.id = len(cls._colorlist)

        cls._colorlist.append(newcls)
        setattr(cls, colorname, newcls)

    @classmethod
    def iter(cls):
        for color in cls._colorlist:
            yield color


# Define Colors members
Colors.new("Black")
Colors.new("Red")
Colors.new("Green")
Colors.new("Yellow")
Colors.new("Blue")
Colors.new("Magenta")
Colors.new("Cyan")
Colors.new("White")


# Define coloring shorthands
def make_func(color):
    def f(s, bold=False, reverse=False):
        return colorize(s, color, bold=bold, reverse=reverse)

    f.__doc__ = (
        """
    Colorize string in %s

    :param string s: The string to colorize.
    :param bool bold: Whether to mark up in bold.
    :param bool reverse: Whether to mark up in reverse video.
    :rtype: string
    """
        % color.__name__.lower()
    )
    return f


for color in Colors.iter():
    globals()[color.__name__.lower()] = make_func(color)


# Define highlighting colors
highlights = [
    Colors.Green,
    Colors.Yellow,
    Colors.Cyan,
    Colors.Blue,
    Colors.Magenta,
    Colors.Red,
]

highlight_map = {}
for (n, h) in enumerate(highlights):
    highlight_map[n] = [color for color in Colors.iter() if h == color].pop()


# Coloring functions
def get_highlighter(colorid):
    """
    Map a color index to a highlighting color.

    :param int colorid: The index.
    :rtype: :class:`Colors`
    """

    return highlight_map[colorid % len(highlights)]


def get_code(color, bold=False, reverse=False):
    """
    Returns the escape code for styling with the given color,
    in bold and/or reverse.

    :param color: The color to use.
    :type color: :class:`Colors` class
    :param bool bold: Whether to mark up in bold.
    :param bool reverse: Whether to mark up in reverse video.
    :rtype: string
    """

    if _disabled:
        return ""

    fmt = "0;0"
    if bold and reverse:
        fmt = "1;7"
    elif reverse:
        fmt = "0;7"
    elif bold:
        fmt = "0;1"
    color = (color is not None) and ";3%s" % color.id or ""

    return "\033[" + fmt + color + "m"


def get_code_v2(color, bold=False, reverse=False, underline=False, blink=False):
    """
    Returns the escape code for styling with the given color,
    in bold and/or reverse.

    :param color: The color to use.
    :type color: :class:`Colors` class
    :param bool bold: Whether to mark up in bold.
    :param bool underline: Whether to mark up in underline.
    :param bool blink: Whether to mark up in blink.
    :param bool reverse: Whether to mark up in reverse video.
    :rtype: string
    """

    if _disabled:
        return ""

    fmt = "0"
    items = []
    if bold:
        items.append("1")
    if underline:
        items.append("4")
    if blink:
        items.append("5")
    if reverse:
        items.append("7")
    if len(items) != 0:
        fmt = ";".join(items)

    color = (color is not None) and ";3%s" % color.id or ""

    return "\033[" + fmt + color + "m"


def colorize(s, color, bold=False, reverse=False, start=None, end=None):
    """
    Colorize a string with the color given.

    :param string s: The string to colorize.
    :param color: The color to use.
    :type color: :class:`Colors` class
    :param bool bold: Whether to mark up in bold.
    :param bool reverse: Whether to mark up in reverse video.
    :param int start: Index at which to start coloring.
    :param int end: Index at which to end coloring.
    :rtype: string
    """

    start = start if start else 0
    end = end if end else len(s)

    before = s[:start]
    between = s[start:end]
    after = s[end:]

    return "%s%s%s%s%s" % (
        before,
        get_code(color, bold=bold, reverse=reverse),
        between,
        get_code(None),
        after,
    )


def colorize_v2(
    s,
    color,
    bold=False,
    reverse=False,
    underline=False,
    blink=False,
    start=None,
    end=None,
):
    """
    Colorize a string with the color given.

    :param string s: The string to colorize.
    :param color: The color to use.
    :type color: :class:`Colors` class
    :param bool bold: Whether to mark up in bold.
    :param bool reverse: Whether to mark up in reverse video.
    :param bool blink: Whether to mark up in blink.
    :param bool reverse: Whether to mark up in reverse video.
    :param int start: Index at which to start coloring.
    :param int end: Index at which to end coloring.
    :rtype: string
    """

    start = start if start else 0
    end = end if end else len(s)

    before = s[:start]
    between = s[start:end]
    after = s[end:]

    return "%s%s%s%s%s" % (
        before,
        get_code_v2(
            color, bold=bold, underline=underline, blink=blink, reverse=reverse
        ),
        between,
        get_code_v2(None),
        after,
    )


def wrap_string(s, pos, color, bold=False, reverse=False):
    """
    Colorize the string up to a position.

    :param string s: The string to colorize.
    :param int pos: The position at which to stop.
    :param color: The color to use.
    :type color: :class:`Colors` class
    :param bool bold: Whether to mark up in bold.
    :param bool reverse: Whether to mark up in reverse video.
    :rtype: string

    .. deprecated:: 0.2.2
       This function has been deprecated in favor of :func:`colorize`.
    """

    warnings.warn("wrap_string is deprecated", DeprecationWarning, 2)

    if _disabled:
        if pos == 0:
            pos = 1
        return s[: pos - 1] + "|" + s[pos:]

    return "%s%s%s%s" % (
        get_code(color, bold=bold, reverse=reverse),
        s[:pos],
        get_code(None),
        s[pos:],
    )


def highlight_string(s, *spanlists, **kw):
    """
    Highlight spans in a string using a list of (begin, end) pairs. Each
    list is treated as a layer of highlighting. Up to four layers of
    highlighting are supported.

    :param string s: The string to highlight
    :param list spanlists: A list of tuples on the form ``[(begin, end)*]*``
    :param kw: May include: `bold`, `reverse`, `color`, `colors` and `nocolor`
    :rtype: string

    .. deprecated:: 0.2.3
       The `color` parameter has been deprecated in favor of `colors`.
    """

    colors = kw.get("colors", [])

    # pair span with color and id of the list -> (span, color, list_id)
    tuples = []
    for id, spanlist in enumerate(spanlists):
        try:
            color = colors[id]
        except IndexError:
            color = get_highlighter(id)

        tuples.extend([(span, color, id) for span in spanlist])

    # produce list of (pos,color,start_end,list_id) pairs
    # (begin, Red, True, list_id)   # start new color
    # (end, Red, False, list_id)    # end current color
    markers = []
    for i in tuples:
        (begin, end), color, list_id = i
        markers.append((begin, color, True, list_id))
        markers.append((end, color, False, list_id))

    def get_key(tup):
        pos, color, start_end, list_id = tup
        return pos

    markers.sort(key=get_key)

    # produce list of (pos, color, layer) pairs
    codes = []
    stack = []
    for (pos, color, start_end, list_id) in markers:
        # stack invariant :  list_id1 < list_id2   =>   i1 < i2
        if start_end:
            inserted = False
            for (i, (c, id)) in enumerate(stack):
                if list_id < id:
                    stack.insert(i, (color, list_id))
                    inserted = True
                    break
            if not inserted:
                stack.append((color, list_id))
        else:
            stack.remove((color, list_id))

        cur_color = None
        if len(stack) > 0:
            (cur_color, _) = stack[-1]

        codes.append((pos, cur_color, len(stack)))

    # apply codes to the string
    cursor = 0
    segments = []
    for (pos, color, layer) in codes:
        bold = False
        reverse = False

        # allow bold/reverse/nocolor styling as parameters
        if color:
            if kw.get("color"):
                color = kw.get("color")
                warnings.warn("color is deprecated", DeprecationWarning, 2)
            elif kw.get("nocolor"):
                color = None
            bold = kw.get("bold") or bold
            reverse = kw.get("reverse") or reverse

        if layer == 2:
            bold = True
        if layer == 3:
            reverse = True
        if layer >= 4:
            bold = True
            reverse = True

        segments.append(s[cursor:pos])
        segments.append(get_code(color, bold=bold, reverse=reverse))

        cursor = pos
    segments.append(s[cursor:])

    return "".join(segments)


def colordiff(x, y, color_x=Colors.Cyan, color_y=Colors.Green, debug=False):
    """
    Formats a diff of two strings using the longest common subsequence by
    highlighting characters that differ between the strings.

    Returns the strings `x` and `y` with highlighting.

    :param string x: The first string.
    :param string y: The second string.
    :param color_x: The color to use for the first string.
    :type color_x: :class:`Colors` class
    :param color_y: The color to use for the second string.
    :type color_y: :class:`Colors` class
    :param bool debug: Whether to print debug output underway.
    :rtype: tuple
    """

    def compute_seq(x, y):
        """SequenceMatcher computes the longest common contiguous subsequence
        rather than the longest common subsequence, but this just causes the
        diff to show more changed characters, the result is still correct"""
        sm = difflib.SequenceMatcher(None, x, y)
        seq = ""
        for match in sm.get_matching_blocks():
            seq += x[match.a : match.a + match.size]
        return seq

    def make_generator(it):
        g = ((i, e) for (i, e) in enumerate(it))

        def f():
            try:
                return next(g)
            except StopIteration:
                return (-1, None)

        return f

    def log(s):
        if debug:
            print(s)  # pragma: no cover

    seq = compute_seq(x, y)
    log(">>>  %s , %s  -> %s" % (x, y, seq))

    it_seq = make_generator(seq)
    it_x = make_generator(x)
    it_y = make_generator(y)

    (sid, s) = it_seq()
    (aid, a) = it_x()
    (bid, b) = it_y()

    x_spans = []
    y_spans = []

    while True:
        if not any([s, a, b]):
            break

        # character the same in all sets
        #   -> unchanged
        if s == a == b:
            log(" %s" % s)
            (sid, s) = it_seq()
            (aid, a) = it_x()
            (bid, b) = it_y()
        # character the same in orig and common
        #   -> added in new
        elif s == a:
            log("+%s" % b)
            y_spans.append((bid, bid + 1))
            (bid, b) = it_y()
        # character the same in new and common
        #   -> removed in orig
        elif s == b:
            log("-%s" % a)
            x_spans.append((aid, aid + 1))
            (aid, a) = it_x()
        # character not the same (eg. case change)
        #   -> removed in orig and added in new
        elif a != b:
            if a:
                log("-%s" % a)
                x_spans.append((aid, aid + 1))
                (aid, a) = it_x()
            if b:
                log("+%s" % b)
                y_spans.append((bid, bid + 1))
                (bid, b) = it_y()

    x_fmt = highlight_string(x, x_spans, reverse=True, colors=[color_x])
    y_fmt = highlight_string(y, y_spans, reverse=True, colors=[color_y])

    return x_fmt, y_fmt


def justify_formatted(s, justify_func, width):
    """
    Justify a formatted string to a width using a function
    (eg. ``string.ljust``).

    :param string s: The formatted string.
    :param justify_func: The justify function.
    :param int width: The width at which to justify.
    :rtype: string
    """
    dx = len(s) - len(strip_escapes(s))
    return justify_func(s, width + dx)


def strip_escapes(s):
    """
    Strips escapes from the string.

    :param string s: The string.
    :rtype: string
    """

    return re.sub(r"\033\[(?:(?:[0-9]*;)*)(?:[0-9]*m)", "", s)


# Output functions
def set_term_title(s):
    """
    Set the title of a terminal window.

    :param string s: The title.
    """

    if not _disabled:
        sys.stdout.write("\033]2;%s\007" % s)


def write_to(target, s):
    # assuming we have escapes in the string
    if not _disabled:
        if not os.isatty(target.fileno()):
            s = strip_escapes(s)
    target.write(s)
    target.flush()


def write_out(s):
    """
    Write a string to ``sys.stdout``, strip escapes if output is a pipe.

    :param string s: The title.
    """

    write_to(sys.stdout, s)


def write_err(s):
    """
    Write a string to ``sys.stderr``, strip escapes if output is a pipe.

    :param string s: The title.
    """

    write_to(sys.stderr, s)
