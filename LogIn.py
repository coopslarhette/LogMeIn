credentials = {}
usernames = open("user.txt", "r+")
passwords = open("pass.txt", "r+")
lineIndex = 0


# TODO: can probably implement a better search here...
def has_user(username):
    search_lines = usernames.readlines()
    for line in search_lines:
        if line.find(username):
            return True
    return False


# TODO: can probably implement a better search here...
def check_password(password):
    search_lines = passwords.readlines()
    for line in search_lines:
        print(line)


def register(username, password):  # TODO: implement hash + salt here?
    global lineIndex
    usernames.write(username + "\n")
    passwords.write(password + "\n")
    lineIndex += 1


class LogMeIn:
    username = ""
    while username != "logout":
        searchUser = usernames.readlines()
        for line in searchUser:
            print("line: " + line)
        username = input(
            "Hello, to log in please enter your username or 'register' if you wish to create a new account: ")
        if username == "register":
            username = input("Please enter a username of your choice: ")
            password = input("Please enter the password of your choice")
            register(username, password)
        elif has_user(username):
            password = input("Please enter your password: ")
            check_password(password)
        print("Please enter either 'register', to create a new account, or an already register username.")