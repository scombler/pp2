x = "awesome" #global one

def f():
    x = "fantastic" #local one
    print("Python is " + x)

f()

print("Python is " + x)