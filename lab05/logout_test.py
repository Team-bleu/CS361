import unittest
import User


class LogoutTest(unittest.TestCase):
    def test_logout(self):
        users = [{"username": "Joe", "password": "1234", "current": True}]

        for each_user in users:
            user = User.User(each_user["username"], each_user["password"])
            user.add_user()

        user.command("logout")
        self.assertEqual(user.get_current(), "None")
