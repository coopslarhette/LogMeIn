credentials = {}
usernames = open("data/user.txt", "r+")
passwords = open("data/pass.txt", "r+")
lineIndex = 0


# TODO: can probably implement a better search here...
def has_user(username, user_search):
    global lineIndex
    for line in user_search:
        if username + "\n" == line:
            return True
        lineIndex += 1
    return False


# TODO: can probably implement a better search here...
def check_password(password, pass_search):
    print(pass_search.pop(lineIndex))
    return pass_search.pop(lineIndex) == password


def register(username, password, usernames, passwords):  # TODO: implement hash + salt here?
    global lineIndex
    usernames.write(username)
    passwords.write(password)


class LogMeIn:
    username = ""
    while username != "logout":
        usernames = open("data/user.txt", "r+")
        passwords = open("data/pass.txt", "r+")
        search_user = usernames.readlines()
        username = input(
            "Hello, to log in please enter your username or 'register' if you wish to create a new account: ")
        if username == "register":
            username = input("Please enter a username of your choice: ")
            password = input("Please enter the password of your choice: ")
            register(username, password, usernames, passwords)
        elif has_user(username, search_user):
            search_pass = passwords.readlines()
            password = input("Please enter your password: ")
            print("everything worked, you're in") if check_password(password, search_pass) else print(
                "incorrect password")
        else:
            print("Please enter either 'register', to create a new account, or an already register username.")
        usernames.close()
        passwords.close()
