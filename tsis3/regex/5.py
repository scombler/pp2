# write a python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

x = input()  # asdfb -> asdfb

pattern = "^a.*b$"

print(re.match(pattern, x))