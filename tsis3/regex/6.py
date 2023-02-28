import re

x = input()

pattern = "[ |,|.]"  # | -. either or

print(re.sub(pattern, ":", x))