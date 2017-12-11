from animal import Animal
#Reuse your Animal class
#Create a Farm class
#it has list of Animals
#it has slots which defines the number of free places for animals
#breed() -> creates a new animal if there's place for it
#slaughter() -> removes the least hungry animal

from animal import Animal

class Farm(object):
    def __init__(self, slots):
        self.animal = []
        self.slots = slots

    def add(self, animal):
        self.animal.append(animal)
        self.slots -= 1

    def breed(self):
        if self.slot > 0:
            new_animal = Animal()
            self.animal.append(new_animal)
            self.slots -= 1

    def slaughter(self):
        hunger = 0
        for i in range(len(self.animal)):
            if self.animal[i].hunger > hunger:
                hunger = self.animal[i].hunger
        for i in range(len(self.animal)):
            if self.animal[i].hunger == hunger:
                self.animal.remove(self.animal)
        self.slots += 1
