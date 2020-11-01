

class Apple:

    def __init__(self, color, weight, worms, species):
        self.color = color
        self.weight = weight
        self.number_of_worms = worms
        self.species = species


my_apple = Apple('red', 10, 0, 'golden')

print(my_apple.species)
