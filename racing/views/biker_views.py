from rest_framework.views import APIView

from racing.base.base_views import GetAPIView, PostAPIView
from racing.constants import BikerResponseMsg, Result
from racing.mangers.biker_manager import generate_biker_response
from racing.models.models import Biker
from racing.serializers.biker_serializers import BikerListSerializer, BikerCreateSerializer
import hashlib


class BikerListAllView(GetAPIView):
    class_serializer = BikerListSerializer

    def process(self, data):
        bikers = Biker.objects.all()
        biker_serializers = []
        for biker in bikers:
            biker_serializers.append(generate_biker_response(biker))

        return Result.SUCCESS, biker_serializers


class BikerCreateView(PostAPIView):
    class_serializer = BikerCreateSerializer

    def process(self, data):
        self.validate_data(data)
        hashed_password = self.hash_password(data["password"])
        biker = Biker.objects.create(full_name=data["full_name"],
                                     user_name=data["user_name"],
                                     phone=data["phone"],
                                     email=data["email"],
                                     hashed_password=hashed_password,
                                     gender=data.get("gender", 1),
                                     facebook=data.get("facebook", ""))

        return Result.SUCCESS, generate_biker_response(biker)

    def validate_data(self, data):
        if not data.get("full_name"):
            self.response_json(BikerResponseMsg.ERROR_REQUIRED_FULL_NAME)
        if not data.get("user_name"):
            self.response_json(BikerResponseMsg.ERROR_REQUIRED_USER_NAME)
        if not data.get("phone"):
            self.response_json(BikerResponseMsg.ERROR_REQUIRED_BIKER_PHONE)
        if not data.get("email"):
            self.response_json(BikerResponseMsg.ERROR_REQUIRED_BIKER_EMAIL)
        if not data.get("password"):
            self.response_json(BikerResponseMsg.ERROR_REQUIRED_PASSWORD)
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
        special_sym = ['$', '@', '#', '$', '&', '^', '*', '!', ',', '?', '.', '{', '}', '(', ')', '~']
        if len(password) < 6:
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_LENGTH_IS_SMALLER_THAN_6)
        if not any(char.isdigit() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_NUMERAL)
        if not any(char.isupper() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_UPPER_CASE)
        if not any(char.islower() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_LOWER_CASE)
        if not any(char in special_sym for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_SPECIAL_SYMBOL)

    def hash_password(self, password):
        salt = ""
        salted_password = hashlib.sha1((password + salt).encode('utf-8')).hexdigest()
        hashed_password = hashlib.sha256(
            (hashlib.sha256(salted_password.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()

        return hashed_password
