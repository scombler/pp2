# write a python program to find the sequences of one upper case letter followed by lower case letters.
import re

x = input()   # MarkLee -> Mark Lee

pattern = "[A-Z]{1}[a-z]+"

y = re.findall(pattern, x)

print(*y)
print(y)
