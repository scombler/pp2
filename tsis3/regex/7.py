# camel case string : myVariableName (each word, except the first, starts with a capital letter:)
# snake case string : my_variable_name (each word is separated by an underscore character)
# write a python program to convert snake case string to camel case string.
import re

def cvrt(x):
    return x.group("g1") + x.group("g3").upper()


txt = input()
pattern = "(?P<g1>[a-z])(?P<g2>[_])(?P<g3>[a-z])"

print(re.sub(pattern, cvrt, txt))