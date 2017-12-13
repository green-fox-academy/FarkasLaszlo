import unittest
from Animal import Animal


class TestAnimal(unittest.TestCase):

    def test_Animal_name(self):
        animal1 = Animal("dog")
        self.assertEqual(animal1.name,"dog")

    def test_Animal_hunger(self):
        animal1 = Animal("dog")
        self.assertEqual(animal1.hunger,50)

    def test_Animal_thirst(self):
        animal1 = Animal("dog")
        self.assertEqual(animal1.thirst,50)

    def test_Animal_eat(self):
        animal1 = Animal("dog")
        animal1.eat()
        self.assertEqual(animal1.hunger, 49)

    def test_Animal_drink(self):
        animal1 = Animal("dog")
        animal1.drink()
        self.assertEqual(animal1.thirst, 49)

    def test_Animal_play(self):
        animal1 = Animal("dog")
        animal1.play()
        self.assertEqual(animal1.thirst, 51)
        self.assertEqual(animal1.hunger, 51)


if __name__ == '__main__':
    unittest.main()