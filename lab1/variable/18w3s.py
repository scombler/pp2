x = "awesome"

def f():
    global x
    x = "fantastic"

f()

print("Python is " + x)