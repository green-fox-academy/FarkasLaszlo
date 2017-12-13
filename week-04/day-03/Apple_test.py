import unittest
from Apple import Apple


class TestApple(unittest.TestCase):

    def test_Apple(self):
        apple1 = Apple()
        self.assertEqual(apple1.get_apple("apple"), "apple")


    def test_Some_String(self):
        apple1 = Apple()
        self.assertEqual(apple1.get_apple("Some String"), "Some String")

    def test_extra_chars(self):
        apple1 = Apple()
        self.assertEqual(apple1.get_apple("+'!%/=())"), "+'!%/=())")


if __name__ == '__main__':
    unittest.main()