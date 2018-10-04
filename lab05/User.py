
class User:
    users = []
    current = "None"

    def __init__(self, user_input):
        self.user_input = user_input

    def command(self, user_input):

        # parses the string and stores it as an array of strings
        user_input = user_input.split(" ")

        # commands are stored in cmd variable
        cmd = user_input[0]

        # add command
        if cmd == "add":

            # checks dictionary if user already exists, if they do fails to add user
            for each_user in self.users:
                if each_user.get("username") == user_input[1]:
                    return "Failed. User exists."

            # creates new user and adds them into the users dictionary
            new_user = {"username": user_input[1], "password": user_input[2], "wishlist": []}
            self.users.append(new_user)
            return "User " + user_input[1] + " added"

        # login command
        elif cmd == "login":

            # checks if user is logged in, then logs them in
            for each_user in self.users:
                if each_user.get("username") == user_input[1] and each_user.get("password") == user_input[2]:
                    return user_input[1] + " logged in"

            # if user is already logged in, fails
            return "Failed. Username or password invalid."

        # logout command
        elif cmd == "logout":

            # current logged in user is logged out
            current = "None"
            return current

        # append command
        elif cmd == "append":
            pass

        # remove command
        elif cmd == "remove":
            pass

        # show command
        elif cmd == "show":
            pass

        # share command
        elif cmd == "share":
            pass

        # revoke command
        elif cmd == "revoke":
            pass

        # quit command
        elif cmd == "quit":
            pass

    def done(self):
        pass
