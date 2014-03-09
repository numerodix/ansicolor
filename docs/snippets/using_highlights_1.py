import re

from ansicolor import highlight_string

text = """
"What giants?" asked Sancho Panza.
"The ones you can see over there," answered his master, "with the huge arms, some of which are very nearly two leagues long."
"Now look, your grace," said Sancho, "what you see over there aren't giants, but windmills, and what seems to be arms are just their sails, that go around in the wind and turn the millstone."
"Obviously," replied Don Quijote, "you don't know much about adventures."
""".strip()

def get_line_indices(text):
    odds, evens = [], []
    for i, match in enumerate(re.finditer('(?m)^.*$', text)):
        start = match.start()
        end = match.end()
        if (i + 1) % 2 == 1:
            odds.append((start, end))
        else:
            evens.append((start, end))
    return odds, evens

def get_word_indices(regex, text):
    pairs = []
    for i, match in enumerate(re.finditer(regex, text)):
        start = match.start()
        end = match.end()
        pairs.append((start, end))
    return pairs

odds, evens = get_line_indices(text)
characters = get_word_indices('(?i)(don quijote|master|sancho panza|sancho)', text)

print(">> highlight only odds:")
print(highlight_string(text, odds))

print("\n>> highlight both:")
print(highlight_string(text, odds, evens))

print("\n>> highlight both + characters:")
print(highlight_string(text, odds, evens, characters))
