# the extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.):
list = ["blue", "purple", "white"]
tuple = ("black", "silver", "lavender")
list.extend(tuple)
print(list)