class Shape:
    def __init__(self):
        self.area = 0

    def s_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length * length


form = Shape()
form.s_area()

subclass = Square(int(input()))
subclass.s_area()