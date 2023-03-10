import os

f1 = open("5.txt", "w")
x = list(input().split())

f1.write('\n'.join(x))
f1.close()

#f2 = open("5.txt")
#print(f2.read())