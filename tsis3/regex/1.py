# write a python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

x = input()

pattern = "^ab*"

print(re.match(pattern, x))
print(bool(re.match(pattern, x)))
