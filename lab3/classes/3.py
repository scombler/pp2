class Shape:
    def __init__(self):
        self.area = 0

    def s_area(self):
        print(self.area)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width

form = Rectangle(int(input("length -> ")), int(input("width ->")))
form.s_area()