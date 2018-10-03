import unittest

users = [{"username": "Joe", "password": "1234", "current": "None"},
         {"username": "Sarah", "password": "abcd", "current": "None"}]

# prints the dictionary of users
print("dictionary of users are, ", users)


class LoginTest(unittest.TestCase):
    def test_login(self):
        login = "login"

        for each_user in users:
            self.assertEqual(command(login + each_user["username"] + each_user["password"]),
                             each_user["username"] + " logged in")
