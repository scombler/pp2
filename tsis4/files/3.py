import os

path = input()  # C:\Users\admin\OneDrive\Документы\hehe

print("requested file/path exists :", os.path.exists(path)) 

if os.path.exists(path):
    print("directory :", os.path.dirname(path))
    print("file name :", os.path.basename(path))


# os.path.dirname() method is used to get the directory name from the specified path.
# os.path.basename() method is used to get the base name in specified path.