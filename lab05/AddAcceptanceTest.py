import unittest

# users = [{'username':'Joe', 'password':'1234', 'current':False, 'wishlist':[]},
#         {'username':'Sarah', 'password':'abcd', 'current':False, 'wishlist':[]},
#         {'username':'Joe', 'password':'dogg', 'current':False, 'wishlist':[]}]

usernames_list = []
users = []

# before adding
print(users)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_user(self):
        new_user = {}
        new_user['username'] = self.username
        new_user['password'] = self.password
        users.append(new_user)


class AddUserTests(unittest.TestCase):

    def test_add(self):
        user_input = input("\nType add <username> <password>\n")
        user_input_list = user_input.split(" ")
        print(user_input_list)

        user = User(user_input_list[1], user_input_list[2])
        user.add_user()
        print(users)