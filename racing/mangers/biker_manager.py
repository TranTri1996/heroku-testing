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


