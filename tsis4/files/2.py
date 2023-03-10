import os 

path = input()   # C:\Users\admin\OneDrive\Документы\hehe

print("requested file exists :", os.access(path, os.F_OK))
print("readable :", os.access(path, os.R_OK))
print("writable :", os.access(path, os.W_OK))
print("executable :", os.access(path, os.X_OK)) 


# os.access() method uses the real uid/gid to test for access to path (uid - user id, gid - group id)
# values to pass as the mode parameter of access() to test the existence, readability, writability and executability of path, respectively.

# x = os.listdir(path)
#fname = input()   # enter folder/file name