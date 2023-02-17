from datetime import datetime

x = datetime.strptime("2023.02.17 -> 01:19:40", "%Y.%m.%d -> %H:%M:%S")   # datetime.datetime(2023, 2, 17, 1, 19, 40)  
y = datetime.now()
w = (y - x)

print("x ->", x)
print("y ->", datetime.now())
print("y - x =", w.seconds)