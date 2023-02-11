import datetime

x = datetime.datetime.today() - datetime.timedelta(days = 5)

print("5 days ago was ->", x)   # it was 06.02.2023 -> 23:12

# syntax : datetime.timedelta(days = 0, seconds = 0, microseconds = 0, milliseconds = 0, minutes = 0, hours = 0, weeks = 0).

# timedelta() is one of the easiest ways to perform date manipulations, function().