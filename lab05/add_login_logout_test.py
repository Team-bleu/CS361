import unittest
from User import User


def add_prompt():
    user_input = input("Type add <username> <password>\n")
    return user_input


def login_prompt():
    user_input = input("Type login <username> <password>\n")
    return user_input


def logout_prompt():
    user_input = input("Type logout\n")
    return user_input


class AddLoginLogoutTest(unittest.TestCase):
    def test_add_login_logout(self):
        print("\nUser story: we want to add a user, have them log in, then logged out.\n")

        user_input = ""
        user_input_list = [""]

        # prompts for add command
        print("\nAdd a user.\n")
        while user_input_list[0] != "add":
            # prompts for new user
            user_input = add_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "add":
                print("You have to add a user and password")
        print("\nUser added is: " + user_input_list[1]
              + ", with the password: " + user_input_list[2])

        # user gets added into the dictionary
        user = User(user_input)
        self.assertEqual(user.command(user_input),
                         "User " + User.users[0].get("username") + " added")

        # prompts for login command
        print("\nLogin the user.\n")
        while user_input_list[0] != "login":
            # prompts for new user
            user_input = login_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "login":
                print("You have to login a user and password")
        print("\nUser logged in: " + user_input_list[1])

        # logs in user
        self.assertEqual(user.command(user_input),
                         user.users[0].get("username") + " logged in")

        # prompts for logout command
        print("\nNow, logout the user.\n")
        while user_input_list[0] != "logout":
            # prompts for new user
            user_input = logout_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "logout":
                print("You have to logout")

        # logs out user
        self.assertTrue(user.users[0].get("current", True))

        user.command(user_input)
        self.assertEqual(user.current, "None")
