import re

x = input()

pattern = "^[a-z_]+"    #pattern = "^[a-z]+_+[a-z]+"

y = re.findall(pattern, x)

print(*y)