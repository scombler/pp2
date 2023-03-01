# write a python program to find sequences of lowercase letters joined with a underscore.
import re

x = input()  # aab_Abbb -> aab_

pattern = "^[a-z_]+"    #pattern = "^[a-z]+_+[a-z]+"

y = re.findall(pattern, x)

print(*y)