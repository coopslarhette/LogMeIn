# prolly should use MySql
import sqlite3

credentials = {}

conn = sqlite3.connect('/Users/coopslarhette/PycharmProjects/LogMeIn')
curs = conn.cursor()


def has_user(user):
    return user in credentials


def create_new_account(user, password):
    while has_user(user):
        user = input("Please enter a new username, that one is taken.")
    credentials[user] = password
    print(credentials[user])


class LogMeIn():
    userInput = input("Please enter username, or enter 'new account' if you wish to register: ")
    loggedIn = False
    if userInput.lower() == "new account":
        userInput = input("Please enter a username: ")
        pw = input("Please enter a password: ")
        # creates account later to not get asked twice
    elif has_user(userInput):
        pw = input("Pleas enter the password for your account: ")
    else:
        print("Their is no such registered user, please come again.")
        exit(0)
    create_new_account(userInput, pw)
    i = 0
    while i < 4 and not loggedIn:
        if credentials[userInput] == pw:
            loggedIn = True
            print("Congrats you're logged in!")
        else:
            pw = input("Password inccorect, please enter a new password: ")
        i += 1
