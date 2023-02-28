import re

x = input()

pattern = "^a*b"

print(re.match(pattern, x))
print(bool(re.match(pattern, x)))
