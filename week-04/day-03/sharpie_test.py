import unittest
from sharpie import Sharpie


class TestSharpie(unittest.TestCase):

    def test_Sharpie(self):
        sharpie1 = Sharpie("red", 2.5)
        self.assertEqual(sharpie1.ink_amount, 100)
        self.assertEqual(sharpie1.color, "red")
        self.assertEqual(sharpie1.width, 2.5)

    def test_Sharpie_use(self):
        sharpie1 = Sharpie("red", 2.5)
        sharpie1.use()
        self.assertEqual(sharpie1.ink_amount, 99)


if __name__ == '__main__':
    unittest.main()
