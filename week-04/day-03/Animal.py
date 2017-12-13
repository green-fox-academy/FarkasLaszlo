class Animal():
    def __init__(self, name, hunger = 50, thirst = 50):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.thirst += 1
        self.hunger += 1