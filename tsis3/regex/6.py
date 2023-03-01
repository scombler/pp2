# write a python program to replace all occurrences of space, comma, or dot with a colon.
import re

x = input()

pattern = "[ |,|.]"  # | -. either or   # There should have been a time and a place, but this wasn't it.

print(re.sub(pattern, ":", x))