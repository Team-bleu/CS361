import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(rational2 - rational1, 1)
        self.assertEqual(rational3 - rational1, 2)
        self.assertEqual(rational5 - rational4, 1 / 3)