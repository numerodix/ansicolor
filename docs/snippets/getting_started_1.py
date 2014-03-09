from ansicolor import cyan
from ansicolor import green
from ansicolor import red
from ansicolor import white

print("Let's try two colors: %s and %s!" % (red("red"), green("green")))
print("It's also easy to produce text in %s," % (red("bold", bold=True)))
print("...%s," % (green("reverse", reverse=True)))
print("...and %s." % (cyan("bold and reverse", bold=True, reverse=True)))
