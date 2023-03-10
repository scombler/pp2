import os

path = input() # C:\Users\admin\OneDrive\Документы\pp2\tsis4\files\8.txt

if os.path.exists(path):
    os.remove(path)
else:
    print("requested file/path doesn't exist")