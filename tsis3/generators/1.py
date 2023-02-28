def squares_of_numbers():
    n = int(input())
    for x in range(n + 1):
        yield x ** 2

for i in squares_of_numbers():
    print(i)

"""
if n = 5:
0^2 = 0
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
5^2 = 25
"""
