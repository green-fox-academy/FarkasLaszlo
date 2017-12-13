import unittest
from summa import summa


class TestSumma(unittest.TestCase):
    def test_summa(self):
        self.assertEqual(summa([]), 0)
        self.assertEqual(summa([1, 2, 3]), 6)
        self.assertEqual(summa([1]), 1)
        self.assertEqual(summa([0]), 0)


if __name__ == '__main__':
    unittest.main()