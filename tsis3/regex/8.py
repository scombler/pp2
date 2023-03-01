# write a python program to split a string at uppercase letters.
import re

x = input()

pattern = "[A-Z]+[^A-Z]*"   # AcceptAllCookiesPls -> Accept All Cookies Pls

y = re.findall(pattern, x)

print(*y)