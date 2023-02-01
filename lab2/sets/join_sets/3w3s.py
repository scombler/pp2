# the intersection_update():
set1 = {"blue", "purple", "white", "black"}
set2 = {"purple", "silver", "lavender", "white"}
set1.intersection_update(set2)
print(set1)   # returns only common items


# the intersection():
set1 = {"blue", "purple", "white", "black"}
set2 = {"purple", "silver", "lavender", "white"}
set3 = set1.intersection(set2)
print(set3)   # returns only common items in a new set