import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testStr(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(rational2), "3/1")
        self.assertEqual(str(rational1), "2/1")
        self.assertEqual(str(rational3), "4/1")
        self.assertEqual(str(rational4), "1/3")
        self.assertEqual(str(rational5), "2/3")