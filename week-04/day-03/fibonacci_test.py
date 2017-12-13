import unittest
from fibonacci import fibonacci


class TestSumma(unittest.TestCase):
    def test_ficonacci(self):
        self.assertEqual(fibonacci(0), 0)

    def test_ficonacci_4th_element(self):
        self.assertEqual(fibonacci(4), 3)



if __name__ == '__main__':
    unittest.main()