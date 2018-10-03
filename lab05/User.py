

class User:
    users = []
    current = "None"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def command(self, user_input):
        user_input = user_input.split(" ")

        if user_input[0] == "add":
            user = User(user_input[1], user_input[2])
            user.add_user()
            return "User " + user_input[1] + " added"

        elif user_input[0] == "login":
            for each_user in self.users:
                if each_user.get("username") == user_input[1] and each_user.get("password") == user_input[2]:
                    return user_input[1] + " logged in"
            return "Failed. Username or password invalid."

        elif user_input[0] == "logout":
            current = "None"
            return current

    def done(self):
        return True

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def get_current(self):
        return self.current

    def add_user(self):
        new_user = {}
        new_user['username'] = self.username
        new_user['password'] = self.password
        self.users.append(new_user)
