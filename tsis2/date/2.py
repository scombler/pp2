import datetime

x = datetime.datetime.today()
y = datetime.datetime.today() - datetime.timedelta(days = 1)
z = datetime.datetime.today() + datetime.timedelta(days = 1)
w = datetime.datetime.today() + datetime.timedelta(days = 2)

print("today is ->", x)
print("yesterday was ->", y)
print("tomorrow will ->", z)
print("day after tomorrow will ->", w)