import re

x = input()

pattern = "^ab{2,3}"

print(re.search(pattern, x))    #abbbb -> span=(0, 4), match = "abbb"
print(re.findall(pattern, x))   #abbbb -> ["abbb"]
print(bool(re.search(pattern, x))) 
