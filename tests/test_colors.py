def test_importability():
    from ansicolor import black
    from ansicolor import blue
    from ansicolor import cyan
    from ansicolor import green
    from ansicolor import magenta
    from ansicolor import red
    from ansicolor import white
    from ansicolor import yellow

    from ansicolor import Colors
    Colors.Black
    Colors.Blue
    Colors.Cyan
    Colors.Green
    Colors.Magenta
    Colors.Red
    Colors.White
    Colors.Yellow

    from ansicolor import get_highlighter
    from ansicolor import get_code

    from ansicolor import colorize
    from ansicolor import wrap_string
    from ansicolor import highlight_string
    from ansicolor import colordiff
    from ansicolor import justify_formatted
    from ansicolor import strip_escapes
    from ansicolor import set_term_title

    from ansicolor import write_err
    from ansicolor import write_out
