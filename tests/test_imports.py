def test_importability():
    from ansicolor import black  # noqa
    from ansicolor import blue  # noqa
    from ansicolor import cyan  # noqa
    from ansicolor import green  # noqa
    from ansicolor import magenta  # noqa
    from ansicolor import red  # noqa
    from ansicolor import white  # noqa
    from ansicolor import yellow  # noqa

    from ansicolor import Colors  # noqa

    Colors.Black
    Colors.Blue
    Colors.Cyan
    Colors.Green
    Colors.Magenta
    Colors.Red
    Colors.White
    Colors.Yellow

    from ansicolor import get_highlighter  # noqa
    from ansicolor import get_code  # noqa

    from ansicolor import colorize  # noqa
    from ansicolor import wrap_string  # noqa
    from ansicolor import highlight_string  # noqa
    from ansicolor import colordiff  # noqa
    from ansicolor import justify_formatted  # noqa
    from ansicolor import strip_escapes  # noqa
    from ansicolor import set_term_title  # noqa

    from ansicolor import write_err  # noqa
    from ansicolor import write_out  # noqa
