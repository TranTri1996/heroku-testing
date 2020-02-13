import jwt
import base64
import hashlib
from racing.base.base_views import PublicPostAPIView, PrivateGetAPIView
from racing.constants import BikerResponseMsg, Result
from racing.mangers import biker_manager
from racing.mangers.biker_manager import generate_biker_response
from racing.models import Biker
from racing.serializers import BikerLoginSerializer, BikerListSerializer, BikeRegisterSerializer, \
    BikerGetProfileSerializer, BikerLogoutSerializer
from vietnamracing import settings
from django.db.models import Q


class BikerRegisterView(PublicPostAPIView):
    def __init__(self):
        PublicPostAPIView.__init__(self)
        self.serializer_class = BikeRegisterSerializer

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
                self.response_json(BikerResponseMsg.ERROR_EMAIL_EXISTED, {})
            if biker.phone == data["phone"]:
                self.response_json(BikerResponseMsg.ERROR_PHONE_EXISTED, {})

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
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_LENGTH_IS_SMALLER_THAN_6, {})
        if not any(char.isdigit() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_NUMERAL, {})
        if not any(char.isupper() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_UPPER_CASE, {})
        if not any(char.islower() for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_LOWER_CASE, {})
        if not any(char in special_sym for char in password):
            self.response_json(BikerResponseMsg.ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_SPECIAL_SYMBOL, {})


class BikerLoginView(PublicPostAPIView):
    def __init__(self):
        PublicPostAPIView.__init__(self)
        self.serializer_class = BikerLoginSerializer

    def process(self, data):
        hashed_password = biker_manager.hash_password(data["password"])
        biker = Biker.objects.filter(email=data["email"], hashed_password=hashed_password).first()
        try:
            if biker:
                token = self.generate_token(biker)
                biker_info = biker_manager.generate_biker_response(biker)
                biker_info["token"] = token

                return Result.SUCCESS, biker_info

        except Exception as e:
            return Result.ERROR_SERVER, {"message {0}".format(e)}

    def generate_token(self, biker):
        payload = {
            'biker_id': biker.id
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return token


class BikerLogoutView(PublicPostAPIView):
    class_serializer = BikerLogoutSerializer

    def process(self, data):
        self.validate_data(data)
        return Result.SUCCESS, {}

    def validate_data(self, data):
        if not biker_manager.check_permission(data["biker_id"], data["token"]):
            self.response_json(BikerResponseMsg.ERROR_PERMISSION_DENIED, {})


class BikerGetProfileView(PrivateGetAPIView):
    def __init__(self):
        PrivateGetAPIView.__init__(self)
        self.serializer_class = BikerGetProfileSerializer

    def process(self, data):
        self.validate_data(data)
        biker = Biker.objects.filter(id=data["biker_id"]).first()
        if biker:
            return Result.SUCCESS, biker_manager.generate_biker_response(biker)

        return Result.ERROR_SERVER, {}

    def validate_data(self, data):
        pass


class BikerListAllView(PrivateGetAPIView):
    class_serializer = BikerListSerializer

    def process(self, data):
        bikers = Biker.objects.all()
        biker_serializers = []
        for biker in bikers:
            biker_serializers.append(generate_biker_response(biker))

        return Result.SUCCESS, biker_serializers
