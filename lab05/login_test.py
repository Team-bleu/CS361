import unittest
from User import User


def prompt():
    user_input = input("Type login <username> <password>\n")
    return user_input


class LoginTest(unittest.TestCase):
    def test_login(self):
        print("\nUser story: we want an added user to login.\n")

        user_input = ""
        user_input_list = [""]
        users = [{"username": "Joe", "password": "1234", "current": False},
                 {"username": "Sarah", "password": "abcd", "current": False}]

        # prints the dictionary of users
        print("\ndictionary of users are, ", users)

        # adds users
        for each_user in users:
            user_input = "add " + each_user["username"] + " " + each_user["password"]
            user = User(user_input)
            user.command(user_input)

        # prompts for login command
        print("\nLogin a user.\n")
        while user_input_list[0] != "login":
            # prompts for new user
            user_input = prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "login":
                print("You have to login a user and password")
        print("\nUser logged in: " + user_input_list[1])

        # logs in user
        self.assertEqual(user.command(user_input),
                         user.users[0].get("username") + " logged in")