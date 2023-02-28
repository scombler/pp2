def even_numbers():
    n = int(input())
    for x in range(0, n):
        if (x % 2 == 0):
            yield x        

for i in even_numbers():
    print(i)

print(*even_numbers())