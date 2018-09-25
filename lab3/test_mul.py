import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testAdd(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(rational1 * rational2, 6)
        self.assertEqual(rational1 * rational3, 8)
        self.assertEqual(rational2 * rational3, 12)
        self.assertEqual(rational4 * rational5, 2 / 9)