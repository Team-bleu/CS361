import unittest

from Rational import Rational

rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)
rational6 = Rational(3,9)

class testAdd(unittest.TestCase):
    def test_init(self):
        self.assertEqual(rational3, 4 / 1)
        self.assertEqual(rational2, 3 / 1)
        self.assertEqual(rational4, 1 / 3)


        # THE TESTS BELOW TESTS THE INITIALIZATION OF RATIONALS
        # Tests the initialization of a zero denominator

    def test_init_zero_denom(self):
        with self.assertRaises(ZeroDivisionError):
            Rational(3, 0)

        # Tests the initialization of a negative denominator (e.g. 3/-5 == -3/5)

    def test_init_neg(self):
        self.assertEqual(Rational(3, -5), -3 / 5)

    def test_init_neg_rationals(self):
        self.assertEqual(Rational(4, -5), Rational(-4, 5))

        # Tests the initializatoin of numerators

    def test_init_num(self):
        self.assertEqual(rational1.n, 2)
        self.assertEqual(rational2.n, 3)

        # Tests the initialization of denominators

    def test_init_denom(self):
        self.assertEqual(rational1.d, 1)
        self.assertEqual(rational2.d, 1)

        # Tests the initialization of non-numeric numberators

    def test_init_num_symbol(self):
        with self.assertRaises(ValueError):
            Rational("a", 3)

        # Tests the initialization of non-numeric denominators

    def test_init_denom_symbol(self):
        with self.assertRaises(ValueError):
            Rational(2, "b")