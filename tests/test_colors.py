from ansicolor import Colors
from ansicolor import colorize
from ansicolor import get_code
from ansicolor import get_highlighter
from ansicolor import wrap_string


def test_codes():
    # reset code
    assert '\033[0;0m' == get_code(None)

    # plain color codes
    assert '\033[0;0;30m' == get_code(Colors.Black)
    assert '\033[0;0;31m' == get_code(Colors.Red)
    assert '\033[0;0;32m' == get_code(Colors.Green)
    assert '\033[0;0;33m' == get_code(Colors.Yellow)
    assert '\033[0;0;34m' == get_code(Colors.Blue)
    assert '\033[0;0;35m' == get_code(Colors.Magenta)
    assert '\033[0;0;36m' == get_code(Colors.Cyan)
    assert '\033[0;0;37m' == get_code(Colors.White)

    # bold color
    assert '\033[0;1;31m' == get_code(Colors.Red, bold=True)

    # reverse color
    assert '\033[0;7;31m' == get_code(Colors.Red, reverse=True)

    # bold + reverse color
    assert '\033[1;7;31m' == get_code(Colors.Red, bold=True, reverse=True)


def test_highlights():
    # can I get a highlighter?
    assert Colors.Green == get_highlighter(0)
    assert Colors.Yellow == get_highlighter(1)


def test_colorize():
    assert (
        get_code(Colors.Red)
        + "Hi there"
        + get_code(None)
    ) == colorize("Hi there", Colors.Red)


def test_wrap_string():
    assert (
        get_code(Colors.Red)
        + "Hi "
        + get_code(None)
        + "there"
    ) == wrap_string("Hi there", 3, Colors.Red)
