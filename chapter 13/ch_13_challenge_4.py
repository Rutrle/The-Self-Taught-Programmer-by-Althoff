class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


my_rider = Rider("Arthas")
my_horse = Horse("Invicible", "black", my_rider)

print(my_horse.rider.name)
