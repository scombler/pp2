def squares(x, y):
    #for nums in range(len(x, y)):  
    for nums in range(x, y + 1):
        print(nums ** 2)

x, y = list(map(int, input().split()))

bb = squares(x, y)