import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,0)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(rational2 / rational1, 3 / 2)
        self.assertEqual(rational3 / rational1, 2)

    # Cannot divide by zero
    def test_div_zero(self):
        self.assertRaise(rational3, ZeroDivisionError)