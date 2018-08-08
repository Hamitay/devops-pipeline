import unittest
import calc

class TestCalcModule(unittest.TestCase):

    def test_soma(self):
        a = 3
        b = 10
        expected = 13

        self.assertEqual(calc.soma(a,b), expected)

    def test_sub(self):
        a = 3
        b = 10
        expected = -6

        self.assertEqual(calc.sub(a,b), expected)

    def test_div(self):
        a = 9
        b = 3
        expected = 3
        self.assertEqual(calc.div(a,b), expected)

        with self.assertRaises(Exception):
            calc.div(a, 0)

if __name__ == '__main__':
    unittest.main()