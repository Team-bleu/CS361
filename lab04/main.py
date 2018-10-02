import unittest

from test_add import testAdd
from test_sb import testSub
from test_mul import testMul
from test_div import testDiv
from test_float import testFloat
from test_init import testInit
from test_properties import testProperties
from test_str import testStr

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(testAdd))
suite.addTest(unittest.makeSuite(testSub))
suite.addTest(unittest.makeSuite(testMul))
suite.addTest(unittest.makeSuite(testDiv))
suite.addTest(unittest.makeSuite(testFloat))
suite.addTest(unittest.makeSuite(testInit))
suite.addTest(unittest.makeSuite(testProperties))
suite.addTest(unittest.makeSuite(testStr))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
#print("*"*20)
#for i in res.failures: print(i[1])
