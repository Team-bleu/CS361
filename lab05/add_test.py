import unittest
from User import User


def prompt():
    user_input = input("\nType add <username> <password>\n")
    return user_input


class AddTest(unittest.TestCase):
    def test_add(self):
        print("\nUser story: we just want to add a user.\n")

        user_input = ""
        user_input_list = [""]

        # prompts for add command
        print("\nAdd a user.\n")
        while user_input_list[0] != "add":
            # prompts for new user
            user_input = prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "add":
                print("You have to add a user and password")
        print("\nUser added is: " + user_input_list[1]
              + ", with the password: " + user_input_list[2])

        # user gets added into the dictionary
        user = User(user_input)
        self.assertEqual(user.command(user_input),
                         "User " + User.users[0].get("username") + " added")
