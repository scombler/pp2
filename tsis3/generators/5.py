def down():
    n = int(input())
    for x in range(n, 0 - 1, -1):
        yield x    # saves the previous values for x

print(*down())