credentials = {}


def has_user(user):
    return user in credentials


def create_new_account(user, password):
    while has_user(user):
        user = input("Please enter a new username, that one is taken.")
    credentials[user] = password


def log_in(username, password):
    i = 0
    while i < 4 and not loggedIn:
        if credentials[username] == pw:
            loggedIn = True
            print("Congrats you're logged in!")
        else:
            pw = input("Password inccorect, please enter a new password: ")
        i += 1


class LogMeIn:
    username = ""
    userInput = input("Please enter username, or enter 'new account' if you wish to register: ")
    if userInput.lower() == "new account":
        userNameInput = input("Please enter a username: ")
        passInput = input("Please enter a password: ")
        create_new_account(userInput, passInput)
    if has_user(userInput):
        pw = input("Pleas enter the password for your account: ")
    else:
        print("Their is no such registered user, please come again.")
        exit(0)
