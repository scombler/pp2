def divisibleby():
    n = int(input())
    for x in range(0, n):
        if x % 3 == 0 and x % 4 == 0:
            yield x 

for i in divisibleby():
    print(i)