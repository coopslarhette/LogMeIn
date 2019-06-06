import hashlib
import uuid


def write_user_and_pass():
    path = "data/user.txt"
    with open(path, "a") as file:
        for i in range(1000):
            file.write(str(i) + "\n")
    with open("data/pass.txt", "a") as file:
        for i in range(1000):
            salt = uuid.uuid4().hex
            hash_pass = hashlib.sha512('i'.encode() + salt.encode()).hexdigest() + ':' + salt
            file.write(hash_pass + "\n")


write_user_and_pass()
