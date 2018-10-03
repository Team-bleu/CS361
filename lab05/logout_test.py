import unittest

users = [{"username": "Joe", "password": "1234", "current": True}]


class LoginTest(unittest.TestCase):
    def test_logout(self):
        command("logout")
        self.assertEqual(users[0].get("current"), "None")
