import unittest
from Counter import counter


class TestCounter(unittest.TestCase):

    def test_counter_valami(self):
        self.assertEqual(counter('valami'), {'v': 1, 'a': 2, 'l': 1, 'm': 1, 'i': 1})

    def test_counter_pause(self):
        self.assertEqual(counter('v v'), {' ': 1, 'v': 2})

    def test_counter_long(self):
        self.assertEqual(counter('a lot of words'), {'a': 1, ' ': 3, 'l': 1, 'o': 3, 't': 1, 'f': 1, 'w': 1, 'r': 1, 'd': 1, 's': 1})

    def test_counter_uppercase(self):
        self.assertEqual(counter('AaAaAaaaaAA'), {'A': 5, 'a': 6})


if __name__ == '__main__':
    unittest.main()
