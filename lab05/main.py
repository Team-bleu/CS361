import unittest

from add_test import AddTest
from login_test import LoginTest
from logout_test import LogoutTest
from add_login_logout_acceptance_test import AddLoginLogoutTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(AddTest))
suite.addTest(unittest.makeSuite(LoginTest))
suite.addTest(unittest.makeSuite(LogoutTest))
suite.addTest(unittest.makeSuite(AddLoginLogoutTest))
runner = unittest.TextTestRunner()
res = runner.run(suite)
print(res)
