import math as m
x = list(map(int, input().split()))
print(m.prod(x))

# math.prod() -> calculate the product of all the elements in the input iterable.

# import operator 
# print(operator.mul(x, x))

y = input().replace(',', "*")
print(eval(y))

# replace() -> this method replaces a specified phrase with another specified phrase.