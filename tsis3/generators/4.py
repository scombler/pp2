def squares(x, y):
    for nums in range(x, y + 1):
        yield nums ** 2

#x, y = map(int, input().split())
#print(*squares(x, y))
x = int(input())
y = int(input())

for i in squares(x, y):
    print(i)