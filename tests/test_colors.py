import contextlib

from ansicolor import Colors
from ansicolor import blue
from ansicolor import colordiff
from ansicolor import colorize
from ansicolor import colorize_v2
from ansicolor import get_code
from ansicolor import get_code_v2
from ansicolor import get_highlighter
from ansicolor import highlight_string
from ansicolor import justify_formatted
from ansicolor import red
from ansicolor import set_term_title
from ansicolor import strip_escapes
from ansicolor import wrap_string
from ansicolor import write_err
from ansicolor import write_out
import ansicolor


@contextlib.contextmanager
def disabled_state():
    ansicolor.ansicolor._disabled = True

    try:
        # run the test with colors disabled
        yield

    finally:
        ansicolor.ansicolor._disabled = False


def test_codes():
    # reset code
    assert "\033[0;0m" == get_code(None)

    # plain color codes
    assert "\033[0;0;30m" == get_code(Colors.Black)
    assert "\033[0;0;31m" == get_code(Colors.Red)
    assert "\033[0;0;32m" == get_code(Colors.Green)
    assert "\033[0;0;33m" == get_code(Colors.Yellow)
    assert "\033[0;0;34m" == get_code(Colors.Blue)
    assert "\033[0;0;35m" == get_code(Colors.Magenta)
    assert "\033[0;0;36m" == get_code(Colors.Cyan)
    assert "\033[0;0;37m" == get_code(Colors.White)

    # bold color
    assert "\033[0;1;31m" == get_code(Colors.Red, bold=True)

    # reverse color
    assert "\033[0;7;31m" == get_code(Colors.Red, reverse=True)

    # bold + reverse color
    assert "\033[1;7;31m" == get_code(Colors.Red, bold=True, reverse=True)


def test_codes_disabled():
    with disabled_state():
        assert "" == get_code(Colors.Black)


def test_codes_v2():
    # reset code
    assert "\033[0m" == get_code_v2(None)

    # plain color codes
    assert "\033[0;30m" == get_code_v2(Colors.Black)
    assert "\033[0;31m" == get_code_v2(Colors.Red)
    assert "\033[0;32m" == get_code_v2(Colors.Green)
    assert "\033[0;33m" == get_code_v2(Colors.Yellow)
    assert "\033[0;34m" == get_code_v2(Colors.Blue)
    assert "\033[0;35m" == get_code_v2(Colors.Magenta)
    assert "\033[0;36m" == get_code_v2(Colors.Cyan)
    assert "\033[0;37m" == get_code_v2(Colors.White)

    # bold, underline, blink, reverse color
    assert "\033[1;31m" == get_code_v2(Colors.Red, bold=True)
    assert "\033[4;31m" == get_code_v2(Colors.Red, underline=True)
    assert "\033[5;31m" == get_code_v2(Colors.Red, blink=True)
    assert "\033[7;31m" == get_code_v2(Colors.Red, reverse=True)

    # mixed color
    assert "\033[1;4;31m" == get_code_v2(Colors.Red, bold=True, underline=True)
    assert "\033[1;5;31m" == get_code_v2(Colors.Red, bold=True, blink=True)
    assert "\033[1;7;31m" == get_code_v2(Colors.Red, bold=True, reverse=True)

    assert "\033[4;5;31m" == get_code_v2(Colors.Red, underline=True, blink=True)
    assert "\033[4;7;31m" == get_code_v2(Colors.Red, underline=True, reverse=True)

    assert "\033[5;7;31m" == get_code_v2(Colors.Red, blink=True, reverse=True)

    assert "\033[1;4;5;31m" == get_code_v2(
        Colors.Red, bold=True, underline=True, blink=True
    )
    assert "\033[1;4;7;31m" == get_code_v2(
        Colors.Red, bold=True, underline=True, reverse=True
    )
    assert "\033[1;5;7;31m" == get_code_v2(
        Colors.Red, bold=True, blink=True, reverse=True
    )
    assert "\033[1;4;5;7;31m" == get_code_v2(
        Colors.Red, bold=True, underline=True, blink=True, reverse=True
    )


def test_codes_v2_disabled():
    with disabled_state():
        assert "" == get_code_v2(Colors.Black)


def test_coloring():
    assert "\033[0;0;31m" + "hi" + "\033[0;0m" == red("hi")


def test_get_hightlighter():
    # can I get a highlighter?
    assert Colors.Green == get_highlighter(0)
    assert Colors.Yellow == get_highlighter(1)


def test_highlight_string_one_layer():
    text = "aaabbbaaa"
    spanlists = [
        [(3, 6)],
    ]

    assert (
        "aaa" + get_code(Colors.Green) + "bbb" + get_code(None) + "aaa"
    ) == highlight_string(text, *spanlists)


def test_highlight_string_one_color_chosen():
    text = "aaabbbaaa"
    spanlists = [
        [(3, 6)],
    ]

    assert (
        "aaa" + get_code(Colors.Cyan) + "bbb" + get_code(None) + "aaa"
    ) == highlight_string(text, *spanlists, color=Colors.Cyan)


def test_highlight_string_nocolor():
    text = "aaabbbaaa"
    spanlists = [
        [(3, 6)],
    ]

    assert (
        "aaa" + get_code(None) + "bbb" + get_code(None) + "aaa"
    ) == highlight_string(text, *spanlists, nocolor=True)


def test_highlight_string_four_layers_inside_out():
    text = "aaabbbcccdddeeefffeeedddcccbbbaaa"
    spanlists = [
        [(3, 30)],
        [(6, 27)],
        [(9, 24)],
        [(12, 21)],
    ]
    colors = [
        Colors.Green,
        Colors.Yellow,
        Colors.Cyan,
        Colors.Blue,
    ]

    assert (
        "aaa"
        + get_code(Colors.Green)
        + "bbb"
        + get_code(Colors.Yellow, bold=True)
        + "ccc"
        + get_code(Colors.Cyan, reverse=True)
        + "ddd"
        + get_code(Colors.Blue, bold=True, reverse=True)
        + "eeefffeee"
        + get_code(Colors.Cyan, reverse=True)
        + "ddd"
        + get_code(Colors.Yellow, bold=True)
        + "ccc"
        + get_code(Colors.Green)
        + "bbb"
        + get_code(None)
        + "aaa"
    ) == highlight_string(text, *spanlists, colors=colors)


def test_highlight_string_four_layers_outside_in():
    text = "fffeeedddcccbbbaaabbbcccdddeeefff"
    spanlists = [[(12, 21)], [(9, 24)], [(6, 27)], [(3, 30)]]
    colors = [
        Colors.Green,
        Colors.Yellow,
        Colors.Cyan,
        Colors.Blue,
    ]

    assert (
        "fff"
        + get_code(Colors.Blue)
        + "eee"
        + get_code(Colors.Blue, bold=True)
        + "ddd"
        + get_code(Colors.Blue, reverse=True)
        + "ccc"
        + get_code(Colors.Blue, bold=True, reverse=True)
        + "bbbaaabbb"
        + get_code(Colors.Blue, reverse=True)
        + "ccc"
        + get_code(Colors.Blue, bold=True)
        + "ddd"
        + get_code(Colors.Blue)
        + "eee"
        + get_code(None)
        + "fff"
    ) == highlight_string(text, *spanlists, colors=colors)


def test_colorize():
    assert (get_code(Colors.Red) + "Hi there" + get_code(None)) == colorize(
        "Hi there", Colors.Red
    )


def test_colorize_with_start_end():
    assert ("H" + get_code(Colors.Red) + "i ther" + get_code(None) + "e") == colorize(
        "Hi there", Colors.Red, start=1, end=7
    )


def test_colorize_v2():
    assert (get_code_v2(Colors.Red) + "Hi there" + get_code_v2(None)) == colorize_v2(
        "Hi there", Colors.Red
    )

    assert (
        "H" + get_code_v2(Colors.Red) + "i ther" + get_code_v2(None) + "e"
    ) == colorize_v2("Hi there", Colors.Red, start=1, end=7)


def test_wrap_string():
    assert (get_code(Colors.Red) + "Hi " + get_code(None) + "there") == wrap_string(
        "Hi there", 3, Colors.Red
    )


def test_wrap_string_disabled():
    with disabled_state():
        assert "Hi|there" == wrap_string("Hi there", 3, Colors.Red)
        assert "|i there" == wrap_string("Hi there", 0, Colors.Red)


def test_strip_escapes():
    assert "Hi there" == strip_escapes(colorize("Hi there", Colors.Red, start=3))

    assert (
        strip_escapes(
            colorize("Hi", None, bold=True)
            + " there, "
            + colorize("stranger", Colors.Green, bold=True)
        )
        == "Hi there, stranger"
    )


def test_colordiff_different():
    x, y = colordiff("hi bob", "hi there", color_x=Colors.Red, color_y=Colors.Blue)

    def fx(s):
        return red(s, reverse=True)

    def fy(s):
        return blue(s, reverse=True)

    assert x == "hi " + fx("b") + fx("o") + fx("b")
    assert y == "hi " + fy("t") + fy("h") + fy("e") + fy("r") + fy("e")


def test_colordiff_edited():
    x, y = colordiff("hi bobby", "hi bob", color_x=Colors.Red, color_y=Colors.Blue)

    def fx(s):
        return red(s, reverse=True)

    assert x == "hi bob" + fx("b") + fx("y")
    assert y == "hi bob"


def test_justify_formatted():
    def rjust(s, width):
        return s.rjust(width)

    assert justify_formatted(red("hi"), rjust, 10) == "        " + red("hi")


def test_set_term_title(capsys):
    set_term_title("ansicolor demo")

    captured = capsys.readouterr()
    assert "\033]2;ansicolor demo\007" == captured.out


def test_write_out(capfd):
    text = colorize("Hi there", Colors.Red, start=3, end=6)

    # escapes will be stripped since we rely on capfd and os.isatty detects a
    # tty device on the other end
    write_out(text)

    captured = capfd.readouterr()
    assert "Hi there" == captured.out


def test_write_err(capfd):
    text = colorize("Hi there", Colors.Red, start=3, end=6)

    # escapes will be stripped since we rely on capfd and os.isatty detects a
    # tty device on the other end
    write_err(text)

    captured = capfd.readouterr()
    assert "Hi there" == captured.err
