# write a python program to find sequences of lowercase letters joined with a underscore.
import re

x = input()  # aab_abbb -> aab_abbb

pattern = "[a-z]+_[a-z]+"   

y1 = re.match(pattern, x)
y2 = re.findall(pattern, x)

print(y1)
print(y2)