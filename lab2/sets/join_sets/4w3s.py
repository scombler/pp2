# the symmetric_difference_update() method will keep only the elements that are NOT present in both sets:
set1 = {"blue", "purple", "white", "black"}
set2 = {"purple", "silver", "lavender", "white"}
set1.symmetric_difference_update(set2)
print(set1)

# the symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets:
set1 = {"blue", "purple", "white", "black"}
set2 = {"purple", "silver", "lavender", "white"}
set3 = set1.symmetric_difference(set2)
print(set3)