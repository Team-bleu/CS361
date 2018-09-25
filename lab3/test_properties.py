import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testAdd(unittest.TestCase):
    # THE TESTS BELOW TESTS THE PROPERTIES OF RATIONAL NUMBERS
    # Tests the Closure Property of Rational Numbers
    def test_closure(self):
        self.assertEqual(rational6, 1 / 3)

    # Tests the Commutative Property of Rational Numbers
    def test_commutative(self):
        self.assertEqual(rational1 + rational4, rational4 + rational1)

    # Tests the Associative Property of Rational Numbers
    def test_associative(self):
        self.assertEqual(rational1 + (rational2 + rational3), 9)

    # Tests the Additive Identity of Rational Numbers
    def test_additive(self):
        self.assertEqual(rational1 + Rational(0, 1), rational1)