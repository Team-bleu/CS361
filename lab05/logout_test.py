import unittest
from User import User


def prompt():
    user_input = input("Type logout\n")
    return user_input


class LogoutTest(unittest.TestCase):
    def test_logout(self):
        print("\nUser story: we want to log out the current user.\n")

        user_input = ""
        user_input_list = [""]
        users = [{"username": "Joe", "password": "1234", "current": True}]

        # adds users
        for each_user in users:
            user_input = "add " + each_user["username"] + " " + each_user["password"]
            user = User(user_input)
            user.command(user_input)

        # logs users in
        for each_user in users:
            user_input = "login " + each_user["username"] + " " + each_user["password"]
            user = User(user_input)
            user.command(user_input)

        # prompts for logout command
        print("\nNow, logout the user.\n")
        while user_input_list[0] != "logout":
            # prompts for new user
            user_input = prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "logout":
                print("You have to logout")

        # logs out user
        self.assertTrue(user.users[0].get("current", True))

        user.command(user_input)
        self.assertEqual(user.current, "None")
