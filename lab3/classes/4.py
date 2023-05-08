from math import sqrt

class Point:
    def __init__(self):
        self.x1 = int(input("first x: "))
        self.y1 = int(input("first y: "))
    
    def show(self):
        print(self.x1, self.y1)
    
    def move(self):
        self.x2 = int(input("second x: "))
        self.y2 = int(input("second y: "))
    
    def dist(self):
        print(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))

p = Point()
p.move()
p.dist()