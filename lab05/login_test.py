import unittest
import User


class LoginTest(unittest.TestCase):
    def test_login(self):
        users = [{"username": "Joe", "password": "1234", "current": False},
                 {"username": "Sarah", "password": "abcd", "current": False}]

        # prints the dictionary of users
        print("\ndictionary of users are, ", users)

        for each_user in users:
            user = User.User(each_user["username"], each_user["password"])
            user.add_user()

        self.assertEqual(user.command("login " + users[0].get("username") + " " + users[0].get("password")),
                         users[0].get("username") + " logged in")
