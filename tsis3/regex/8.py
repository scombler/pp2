import re

x = input()

pattern = "[A-Z]+[^A-Z]*"

y = re.findall(pattern, x)

print(*y)