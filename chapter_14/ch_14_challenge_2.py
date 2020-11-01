

class Square:
    square_list = []

    def __init__(self, side):
        self.square_list.append(self)
        self.side = side

    def __repr__(self):

        return f"{self.side} by {self.side} by {self.side} by {self.side}"


my_square = Square(4)

print(my_square)
