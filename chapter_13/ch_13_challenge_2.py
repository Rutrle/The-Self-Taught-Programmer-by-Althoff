
class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter

    def change_size(self, increasement):
        self.side = self.side+increasement


my_square = Square(5)

print(
    f"Square perimeter is {my_square.calculate_perimeter()}")

my_square.change_size(5)

print(
    f"Changed square perimeter is {my_square.calculate_perimeter()}")
