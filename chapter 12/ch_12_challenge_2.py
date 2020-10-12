import math


class Circle:

    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        return math.pi*((self.diameter/2)**2)


small_circle = Circle(3)

print(small_circle.area())
