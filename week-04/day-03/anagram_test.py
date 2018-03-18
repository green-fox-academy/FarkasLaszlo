import unittest
from anagram import anagram


class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        self.assertTrue(anagram('safetyrail', 'Fairytales'))

    def test_anagram_with_pause(self):
        self.assertTrue(anagram('safetyrail', 'Fairy tales'))

    def test_anagram_if_not(self):
        self.assertFalse(anagram('ssafetyrail', 'Fairytales'))


if __name__ == '__main__':
    unittest.main()
