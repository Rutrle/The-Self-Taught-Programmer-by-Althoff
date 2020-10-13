class Shape:
    def what_am_i(self):
        print("I'm a shape")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter

    def change_size(self, increasement):
        self.side = self.side+increasement


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2*self.length+2*self.width
        return perimeter


my_square = Square(5)
my_rectangle = Rectangle(5, 10)

my_square.what_am_i()
my_rectangle.what_am_i()
