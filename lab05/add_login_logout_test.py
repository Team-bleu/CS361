import unittest

users = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_user(self):
        new_user = {}
        new_user['username'] = self.username
        new_user['password'] = self.password
        users.append(new_user)


def prompt():
    user_input = input("\nType add <username> <password>\n")
    user_input_parse = user_input.split(" ")
    return user_input_parse


class AddLoginLogoutTest(unittest.TestCase):
    def test_add(self):
        user_input_list = [""]

        while user_input_list[0] != "add":
            # prompts for new user
            user_input_list = prompt()
            print("user_input_list = ", user_input_list)

        # adds the user into the dictionary
        user = User(user_input_list[1], user_input_list[2])
        user.add_user()
        print("users = ", users)

        add = "add"

        print("\ninput is: ", add, users[0].get("username"), users[0].get("password"))
        self.assertEqual(command("add" + users[0].get("username") + users[0].get("password")),
                         "User " + users[0].get("username") + " added")

        self.assertEqual(command("login" + users[0].get("username") + users[0].get("password")),
                         users[0].get("username") + " logged in")
        self.assertTrue(users[0].get("current", True))

        command("logout")
        self.assertEqual(users[0].get("current"), "None")
