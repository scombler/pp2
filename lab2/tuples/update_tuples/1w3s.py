# change tuple values:
x = ("python", "c++", "java")
y = list(x)
y[1] = "html"   # перезаписывает значение для элменета под индексом 0
x = tuple(y)

print(x)

