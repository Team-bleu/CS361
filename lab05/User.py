
users = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def command(self, user_input):
        pass

    def done(self):
        return True

    def get_users(self):
        return users

    def add_user(self):
        new_user = {}
        new_user['username'] = self.username
        new_user['password'] = self.password
        users.append(new_user)