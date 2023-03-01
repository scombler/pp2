def even_numbers():
    n = int(input())
    for x in range(0, n + 1):   # range(0, n + 1, 2)
        if (x % 2 == 0):
            yield x        

#for i in even_numbers():
#    print(i)

print(*even_numbers(), sep = ", ")