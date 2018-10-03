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


class AddTest(unittest.TestCase):
    def test_add(self):

        # prompts for new user
        user_input_list = prompt()
        print("user_input_list = ", user_input_list)

        # adds the user into the dictionary
        user = User(user_input_list[1], user_input_list[2])
        user.add_user()
        print("users = ", users)

        add = "add"

        for each_user in users:
            # prints the input string
            print("\ninput is: ", add, each_user["username"], each_user["password"])
            self.assertEqual(command(add + each_user["username"] + each_user["password"]),
                             "User " + each_user["username"] + " added")
