import unittest
import Extension


class TestExtend(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(Extension.add(2, 3), 5)

    def test_add_3_and_3_is_6(self):
        self.assertEqual(Extension.add(3, 3), 6)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(Extension.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(Extension.max_of_three(5, 4, 3), 5)

    def test_max_of_three_second(self):
        self.assertEqual(Extension.max_of_three(4, 5, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(Extension.max_of_three(3, 4, 5), 5)

    def test_max_of_three_equal(self):
        self.assertEqual(Extension.max_of_three(5, 5, 3), 5)

    def test_median_four(self):
        self.assertEqual(Extension.median([7, 5, 3, 5]), 5)

    def test_median_five(self):
        self.assertEqual(Extension.median([1, 2, 3, 4, 5]), 3)

    def test_median_diff(self):
        self.assertEqual(Extension.median([2, 2, 5, 1, 0]), 2)

    def test_is_vovel_a(self):
        self.assertTrue(Extension.is_vovel('a'))

    def test_is_vovel_aejhj(self):
        self.assertFalse(Extension.is_vovel('aehjbsdgfsjg'))

    def test_is_vovel_b(self):
        self.assertFalse(Extension.is_vovel('b'))

    def test_is_vovel_char(self):
        self.assertFalse(Extension.is_vovel('%'))

    def test_is_vovel_A(self):
        self.assertTrue(Extension.is_vovel('A'))

    def test_is_vovel_u(self):
        self.assertTrue(Extension.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(Extension.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_emeletes_busz(self):
        self.assertEqual(Extension.translate('emeletes busz'), 'evemeveleveteves buvusz')

    def test_translate_uppercase(self):
        self.assertEqual(Extension.translate('Emeletes Busz'), 'Evemeveleveteves Buvusz')

    def test_translate_vowel(self):
        self.assertEqual(Extension.translate('ae'), 'avaeve')

    def test_translate_kolbice(self):
        self.assertEqual(Extension.translate('kolbice'), 'kovolbiviceve')

    def test_translate_empty(self):
        self.assertEqual(Extension.translate(''), '')


if __name__ == '__main__':
    unittest.main()
