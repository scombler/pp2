import math
n = float(input()) # input number of sides: 4
l = float(input()) # input the length of a side: 25
p = n * l # perimeter
a = l / 2 * math.tan(math.radians(180/n))
s = (p * a) / 2
print("the area of regular polygon is", round(s))   # the area of the polygon is: 625


# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wikihow.com%2FFind-the-Area-of-Regular-Polygons&psig=AOvVaw3yEoM74RcdfGX07Rfq8NfH&ust=1676223609117000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMiz29eBjv0CFQAAAAAdAAAAABAJ