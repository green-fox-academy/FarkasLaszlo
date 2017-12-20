import unittest
from Unique_Characters import unique_character


class Test_Unique_Character(unittest.TestCase):

    def test_unique_valami(self):
        self.assertEqual(unique_character("valami"), ["v", "l", "m", "i"])

    def test_unique_anagram(self):
        self.assertEqual(unique_character("anagram"), ["n", "g", "r", "m"])

    def test_unique_global(self):
        self.assertEqual(unique_character("Global World"), ["G", "b", "a", "W", "r", "d"])

    def test_unique_no_string(self):
        self.assertEqual(unique_character(""), [])

    def test_unique_all_same(self):
        self.assertEqual(unique_character("aaabbaabbaabb"), [])


if __name__ == '__main__':
    unittest.main()
