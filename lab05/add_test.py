import unittest
import User

def prompt():
    user_input = input("\nType add <username> <password>\n")
    user_input_parse = user_input.split(" ")
    return user_input_parse


class AddTest(unittest.TestCase):
    def test_add(self):
        user_input_list = [""]

        while user_input_list[0] != "add":
            # prompts for new user
            user_input_list = prompt()
            print("user_input_list = ", user_input_list)
            if user_input_list[0] != "add":
                print("You have to add a user and password")

        # adds the user into the dictionary
        user = User.User(user_input_list[1], user_input_list[2])
        user.add_user()
        print("users = ", user.get_users())

        print("\ninput is: add ", user.get_users()[0].get("username"), user.get_users()[0].get("password"))
        self.assertEqual(user.command("add " + user.get_users()[0].get("username") + " "
                                      + user.get_users()[0].get("password")),
                         "User " + user.get_users()[0].get("username") + " added")
