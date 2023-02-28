import re

x = input()

pattern = "[A-Z]{1}[a-z]+"

y = re.findall(pattern, x)

print(*y)
print(y)
