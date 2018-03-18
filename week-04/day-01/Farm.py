from animal import Animal
#Reuse your Animal class
#Create a Farm class
#it has list of Animals
#it has slots which defines the number of free places for animals
#breed() -> creates a new animal if there's place for it
#slaughter() -> removes the least hungry animal

from animal import Animal

class Farm():
    def __init__(self, slots):
        self.animal = []
        self.slots = slots

    def add(self, animal):
        if self.slots > 0:
            self.animal.append(animal)
            self.slots -= 1

    def breed(self, name, hunger = 50, thirst = 50):
        if self.slots > 0:
            new_animal = Animal(name,hunger,thirst)
            self.animal.append(new_animal)
            self.slots -= 1

    def slaughter(self):
        self.animal.sort(key = lambda x: x.hunger, reverse = False)
        del(self.animal[0])
            self.slots += 1

    def __str__(self):
        result = ''
        for i in range(0, len(self.animal)):
            result += str(i + 1) + '. ' + self.animal[i].__str__() + '\n'
        return result


