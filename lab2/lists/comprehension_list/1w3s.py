# without list comprehension:
list = ["universe", "galaxy", "solar system", "stars", "planets", "moons"]
newlist = []

for x in list:
    if "a" in x:
        newlist.append(x)

print(newlist)


# with list comprehension:
list = ["universe", "galaxy", "solar system", "stars", "planets", "moons"]
newlist = [x for x in list if "a" in x]
print(newlist)