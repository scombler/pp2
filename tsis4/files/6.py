import os
path = os.getcwd()

for i in range(65, 91):
    open(chr(i) + ".txt", "w")