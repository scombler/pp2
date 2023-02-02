# customize sort function by using the keyword argument key = function:
def function(x):
    return abs(x - 50)

list = [100, 50, 65, 82, 23]
list.sort(key = function)
print(list)

# x = 100 -> abs(100 - 50) = 50
# x = 50 -> abs(50 - 50) = 0
# x = 65 -> abs(65 - 50) = 15
# x = 82 -> abs(82 - 50) = 32
# x = 23 -> abs(23 - 50) = 27

# 100, 50, 65, 82, 23  ->  50, 65, 23, 82, 100  -> values
# 50,  0,  15, 32, 27  ->  0,  15, 27, 32, 50   -> keys