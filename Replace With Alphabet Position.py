"""

Replace With Alphabet Position

Welcome.

In this kata you are required to, given a string, replace every letter
with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3
12 15 3 11" as a string.

"""


def alphabet_position(text):
    new_list = []
    iteration = 0
    string = ""
    for i in text:
        iteration += 1
        if ord(i.upper()) >= 65 and ord(i.upper()) <= 90:
            new_list.append(str(ord(i.upper()) - 64))

    return (" ".join(new_list))
