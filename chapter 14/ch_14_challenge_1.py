

class Square:
    square_list = []

    def __init__(self, side):
        self.square_list.append(self)
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter


Square(4)
print(Square.square_list)
