import math


class Hexagon:

    def __init__(self, side):

        self.side = side

    def calculate_perimeter(self):
        return 6 * self.side


my_hexagon = Hexagon(3)

print(my_hexagon.calculate_perimeter())
