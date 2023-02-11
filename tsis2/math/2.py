""" def area():
    a = float(input())   # base, first value: 5
    b = float(input())   # base, second value: 6
    h = float(input())   # height: 5
    s = (a + b) * h / 2
    print("the area of a trapezoid is", s)   # expected output: 27.5

area() """

import math
a = float(input())   # base, first value: 5
b = float(input())   # base, second value: 6
h = float(input())   # height: 5
s = (a + b) * h / 2
print("the area of a trapezoid is", s)   # expected output: 27.5