import unittest

from Rational import Rational

rational0 = Rational(0,0)
rational1 = Rational(2,1)
rational2 = Rational(3,1)
rational3 = Rational(4,1)
rational4 = Rational(1,3)
rational5 = Rational(2,3)

#print(rational1.__dict__)
#print(rational2.__dict__)

class MainTests(unittest.TestCase):
  def test_init(self):

    self.assertEqual(rational3, 4/1)
    self.assertEqual(rational2, 3/1)
    self.assertEqual(rational4, 1/3)

  def test_add(self):
  
    self.assertEqual(rational1 + rational2, 5)
    self.assertEqual(rational1 + rational3, 6)
    self.assertEqual(rational4 + rational5, 1)
  
  def test_sub(self):
    
    self.assertEqual(rational2 - rational1, 1)
    self.assertEqual(rational3 - rational1, 2)
    self.assertEqual(rational5 - rational4, 1/3)
 
  def test_mul(self):
    
    self.assertEqual(rational1 * rational2, 6)
    self.assertEqual(rational1 * rational3, 8)
    self.assertEqual(rational2 * rational3, 12)
    self.assertEqual(rational4 * rational5, 2/9)
    
  def test_div(self):
    
    self.assertEqual(rational2 / rational1, 3/2)
    self.assertEqual(rational3 / rational1, 2)
  
  # Cannot divide by zero                   
  def test_div_zero(self):

    self.assertEqual(rational3 / rational0, ZeroDivisionError)
                     
  def test_str(self):
    
    self.assertEqual(str(rational2), "3/1")
    self.assertEqual(str(rational1), "2/1")
    self.assertEqual(str(rational3), "4/1")
    self.assertEqual(str(rational4), "1/3")
    self.assertEqual(str(rational5), "2/3")

  def test_float(self):
    
    self.assertEqual(float(rational1), 2.0)
    self.assertEqual(float(rational2), 3.0)
    self.assertEqual(float(rational3), 4.0)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(MainTests))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
