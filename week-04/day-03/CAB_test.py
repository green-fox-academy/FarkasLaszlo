import unittest
from CAB_game import CAB


class TestCAB(unittest.TestCase):

    def test_CAB(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.game_state, "playing")
        self.assertEqual(cab1.counter, 0)

    def test_CAB_number1(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(1234), ["cow", "cow", "cow", "cow"])

    def test_CAB_number2(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(1235), ["cow", "cow", "cow", "bull"])

    def test_CAB_number3(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(1434), ["cow", "bull", "cow", "cow"])

    def test_CAB_number4(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(7234), ["bull", "cow", "cow", "cow"])

    def test_CAB_number5(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(1244), ["cow", "cow", "bull", "cow"])

    def test_CAB_number6(self):
        cab1 = CAB("playing", 0, 1234)
        self.assertEqual(cab1.guess(1444), ["cow", "bull", "bull", "cow"])

    def test_CAB_number7(self):
        cab1 = CAB("playing", 0, 4444)
        self.assertEqual(cab1.guess(4444), ["cow", "cow", "cow", "cow"])

    def test_CAB_finished(self):
        cab1 = CAB("playing", 0, 1234)
        cab1.guess(1234)
        self.assertEqual(cab1.game_state, "finished")

    def test_CAB_finished2(self):
        cab1 = CAB("playing", 0, 1234)
        cab1.guess(1134)
        self.assertEqual(cab1.game_state, "playing")
        cab1.guess(1244)
        self.assertEqual(cab1.game_state, "playing")
        cab1.guess(1234)
        self.assertEqual(cab1.game_state, "finished")

    def test_CAB_playing(self):
        cab1 = CAB("playing", 0, 1234)
        cab1.guess(1244)
        self.assertEqual(cab1.game_state, "playing")

    def test_CAB_counter(self):
        cab1 = CAB("playing", 0, 1234)
        cab1.guess(1244)
        cab1.guess(1244)
        cab1.guess(1244)
        cab1.guess(1244)
        cab1.guess(1244)
        self.assertEqual(cab1.counter, 5)


if __name__ == '__main__':
    unittest.main()
