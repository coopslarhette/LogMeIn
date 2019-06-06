import hashlib
import uuid

lineIndex = 0


# TODO: can probably implement a better search here...
def has_user(username, user_fpath):
    global lineIndex
    with open(user_fpath, "r") as file:
        for line in file.readlines():
            if username + "\n" == line:
                return True
            lineIndex += 1
        return False


def check_password(password, pass_fpath):
    global lineIndex
    with open(pass_fpath, "r+") as file:
        lines = file.readlines()
        temp_pass = lines[lineIndex]
        salty_hashed_pass, salt = temp_pass.split(':')
        salt = salt[:-1] # chops newline character
        given_salty_hashed_pass = hashlib.sha512(password.encode() + salt.encode()).hexdigest()
        return salty_hashed_pass == given_salty_hashed_pass


def register(username, password, user_fpath, pass_fpath):  # TODO: implement hash + salt here?
    with open(user_fpath, "a") as file:
        file.write(username + "\n")
    with open(pass_fpath, "a") as file:
        salt = uuid.uuid4().hex
        hash_pass = hashlib.sha512(password.encode() + salt.encode()).hexdigest() + ':' + salt
        file.write(hash_pass + "\n")
    return


class LogMeIn:
    global lineIndex
    username = ""
    while username != "logout":
        lineIndex = 0
        username = input(
            "Hello, to log in please enter your username or 'register' if you wish to create a new account: ")
        if username == "register":
            username = input("Please enter a username of your choice: ")
            password = input("Please enter the password of your choice: ")
            register(username, password, "data/user.txt", "data/pass.txt")
        elif has_user(username, "data/user.txt"):
            password = input("Please enter your password: ")
            print("everything worked, you're in") if check_password(password, "data/pass.txt") else print(
                "incorrect password")
        else:
            print("Please enter either 'register', to create a new account, or an already register username.")