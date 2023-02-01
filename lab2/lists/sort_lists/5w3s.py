# customize sort function by using the keyword argument key = function:
def function(x):
    return abs(x - 50)

list = [26, 66, 19, 86, 200]
list.sort(key = function)
print(list)

# x = 26 -> abs(26 - 50) = 24
# x = 666 -> abs(66 - 50) = 16
# x = 19 -> abs(19 - 50) = 31
# x = 86 -> abs(86 - 50) = 36
# x = 200 -> abs(200 - 50) = 150

# in "close to 50" order: 66, 26, 19, 86, 200