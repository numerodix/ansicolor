from ansicolor import Colors
from ansicolor import colordiff

statement = "All towles must be folded an stowed away neatly inthe closet."
reviewed = "All towels must be folded and stowed neatly in the closet!"

first, second = colordiff(statement, reviewed,
                          color_x=Colors.Cyan, color_y=Colors.Green)

print(first)
print(second)
