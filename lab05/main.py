import main_tests
import User


def main():

    # Should we check the Acceptance Tests?
    test = True
    # Stores user input
    user_input = [""]

    if test:
        main_tests.main_tests()

    while user_input[0] != "quit":
        user_input = input()
        user = User(user_input)
        user.command(user_input)


if __name__ == "__main__":
    main()
