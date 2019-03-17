"""

Disemvowel Trolls

Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels
from the trolls' comments, neutralizing the threat. Your task is to write
a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become
"Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

"""


def disemvowel(string):
    return "".join([i for i in string if i.lower() != 'a' and i.lower() != 'e'
                    and i.lower() != 'i' and i.lower() != 'o' and i.lower() != 'u'])


"""
Another improvement would be to put all of the 'and' cases into 1
ie:
def disemvowel(string):
  return "".join(i for i in string if i.lower() not in "aeiou")
"""
