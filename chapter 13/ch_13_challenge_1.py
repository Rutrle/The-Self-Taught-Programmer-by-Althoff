

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2*self.length+2*self.width
        return perimeter


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter


my_rectangle = Rectangle(5, 10)
my_square = Square(5)

print(
    f"Square perimeter is {my_square.calculate_perimeter()}, Rectangle perimeter is {my_rectangle.calculate_perimeter()}")
