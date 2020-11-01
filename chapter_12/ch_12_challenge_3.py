import math


class Triangle:

    def __init__(self, side_a, side_b, side_c):

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.diameter = side_a+side_b+side_c

    def area(self):
        s = self.diameter/2
        area_calc = (s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c))**(1/2)
        return area_calc


my_triangle = Triangle(1, 1, 1)

print(my_triangle.area())
