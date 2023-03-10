import os 

path = input()  # C:\Users\admin\OneDrive\Документы\hehe

direct = os.listdir(path)
d = list()   # for directories
f = list()   # for files

for i in direct:
    if os.path.isdir(f"{path}/{i}"):
        d.append(i)
print("all directories:", d)

for i in direct:
    if os.path.isfile(f"{path}/{i}"):
        f.append(i)
print("all files:", f)


# the method listdir() returns a list containing the names of the entries in the directory given by path.
# os.path.isfile() method is used to check whether the specified path is an existing regular file or not.
# os.path.isdir() method is used to check whether the specified path is an existing directory or not. 


#path = os.getcwd()  ->  yhe method getcwd() returns current working directory of a process.