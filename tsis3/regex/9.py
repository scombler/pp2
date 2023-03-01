# write a python program to insert spaces between words starting with capital letters.
# 1 :
import re

x = input()        # AdventureTime -> Adventure Time

pattern = "[A-Z]+[a-z]*"    

y = re.findall(pattern, x)

print(*y)

# 2 :

z = re.findall(pattern, x)

print(" ".join(z))