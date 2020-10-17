

class Square:
    square_list = []

    def __init__(self, side):
        self.square_list.append(self)
        self.side = side

    def __repr__(self):

        return f"{self.side} by {self.side} by {self.side} by {self.side}"


obj_1 = Square(4)
obj_2 = obj_1
obj_3 = Square(4)

print(obj_1 is obj_2)
print(obj_1 is obj_3)
