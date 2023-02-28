import re

def laps(x):
    return x.group("g1") + "_" + x.group("g2").lower()

txt = input()  # camel case  -> iSawUInMyDreams

pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"

print(re.sub(pattern, laps, txt))