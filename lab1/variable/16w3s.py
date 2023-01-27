x = "awesome"   #global variable

def f():
    x = "fantastic"   #local variable
    print("Python is " + x)

f()

print("Python is " + x)