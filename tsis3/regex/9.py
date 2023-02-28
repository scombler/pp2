# 1 :
import re

x = input()

pattern = "[A-Z]+[a-z]*"

y = re.findall(pattern, x)

print(*y)

# 2 :

z = re.findall(pattern, x)

print(" ".join(z))