import datetime

import jwt
from django.db.models import Q
from racing.base.base_views import PublicPostAPIView, PrivatePostAPIView
from racing.constants import Result
from racing.mangers import biker_manager
from racing.mangers.biker_manager import generate_biker_response
from racing.models import Biker
from racing.serializers import RegisterSerializer, LoginSerializer, ForgotPasswordSerializer
from vietnamracing import settings


class RegisterView(PublicPostAPIView):
    def __init__(self):
        PublicPostAPIView.__init__(self)
        self.serializer_class = RegisterSerializer

    def process(self, data):
        self.validate_data(data)
        hashed_password = biker_manager.hash_password(data["password"])
        biker = Biker.objects.create(full_name=data["full_name"],
                                     user_name=data["user_name"],
                                     phone=data["phone"],
                                     email=data["email"],
                                     hashed_password=hashed_password,
                                     job=data.get("job", ""),
                                     gender=data.get("gender", 1),
                                     facebook=data.get("facebook", "")
                                     )

        return Result.SUCCESS, generate_biker_response(biker)

    def validate_data(self, data):
        biker = Biker.objects.filter(Q(email=data["email"]) | Q(phone=data["phone"])).first()
        if biker:
            if biker.email == data["email"]:
                return Result.ERROR_EMAIL_EXISTED
            if biker.phone == data["phone"]:
                return Result.ERROR_PHONE_EXISTED

        self.verify_password(data["password"])

    def verify_password(self, password):
        """Check if the password is valid.

            This function checks the following conditions
            if its length is greater than 6
            if it has at least one uppercase letter
            if it has at least one lowercase letter
            if it has at least one numeral
            if it has any of the required special symbols
            """
        sym = ['@', '#', '$', '&', '^', '*', '!', ',', '?', '.', '{', '}', '(', ')', '~', ';', ':', '/', '|', '\\']
        if len(password) < 6:
            return Result.ERROR_PASSWORD_LENGTH_IS_SMALLER_THAN_6
        if not any(char.isdigit() for char in password):
            return Result.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_NUMERAL
        if not any(char.isupper() for char in password):
            return Result.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_UPPER_CASE
        if not any(char.islower() for char in password):
            return Result.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_LOWER_CASE
        if not any(char in sym for char in password):
            return Result.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_SPECIAL_SYMBOL


class LoginView(PublicPostAPIView):
    def __init__(self):
        PublicPostAPIView.__init__(self)
        self.serializer_class = LoginSerializer

    def process(self, data):
        biker = Biker.objects.filter(email=data["email"]).first()

        if not biker:
            return Result.EMAIL_NOT_EXISTED, None

        hashed_password = biker_manager.hash_password(data["password"])
        if biker.hashed_password != hashed_password:
            return Result.ERROR_WRONG_PASSWORD, None

        if biker:
            access_token = self.generate_access_token(biker)
            biker_info = biker_manager.generate_biker_response(biker)
            biker_info["access_token"] = access_token

            return Result.SUCCESS, biker_info

    def generate_access_token(self, biker):
        payload = {
            'user_id': biker.id,
            'expired_time': str(datetime.datetime.now() + settings.JWT_AUTH["JWT_EXPIRATION_DELTA"])
        }

        access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_AUTH["ENCRYPT_ALGORITHM"])

        return access_token


class ForgotPasswordView(PublicPostAPIView):
    def __init__(self):
        PublicPostAPIView.__init__(self)

    def process(self):
        pass


class LogoutView(PrivatePostAPIView):
    def __init__(self):
        PrivatePostAPIView.__init__(self)

    def process(self, data):
        return Result.SUCCESS, {}
