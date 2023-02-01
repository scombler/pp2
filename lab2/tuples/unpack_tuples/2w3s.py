# if the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
space = ("universe", "galaxy", "solar system", "stars", "planets")
(dark, white, *silver) = space
print(dark)
print(white)
print(silver)