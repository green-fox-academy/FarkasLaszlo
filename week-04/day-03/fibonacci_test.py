import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_4th_element(self):
        self.assertEqual(fibonacci(4), 3)


if __name__ == '__main__':
    unittest.main()
