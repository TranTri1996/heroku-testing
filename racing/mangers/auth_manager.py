import hashlib


def hash_password(password):
    salt = ""
    salted_password = hashlib.sha1((password + salt).encode('utf-8')).hexdigest()
    hashed_password = hashlib.sha256(
        (hashlib.sha256(salted_password.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()

    return hashed_password
