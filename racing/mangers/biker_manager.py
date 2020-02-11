import hashlib


def generate_biker_response(biker):
    return {
        "id": biker.id,
        "full_name": biker.full_name,
        "user_name": biker.user_name,
        "phone": biker.phone,
        "email": biker.email,
        "facebook": biker.facebook,
        "gender": biker.gender,
        "like_number": biker.like_number,
        "date_of_birth": biker.date_of_birth,
        "job": biker.job,
        "created_time": biker.created_time,
        "updated_time": biker.updated_time
    }


def hash_password(password):
    salt = ""
    salted_password = hashlib.sha1((password + salt).encode('utf-8')).hexdigest()
    hashed_password = hashlib.sha256(
        (hashlib.sha256(salted_password.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()

    return hashed_password
