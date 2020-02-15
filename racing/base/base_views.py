import datetime
import jwt

from rest_framework.views import APIView
from racing.constants import Result
from rest_framework.response import Response
from vietnamracing import settings


class BaseAPIVIew(APIView):
    def __init__(self, **kwargs):
        self.is_check_auth = None
        self.user_id = None
        self.serializer_class = None

    def get(self, request):
        try:
            if self.serializer_class is None:
                return self.handle(request.META, request.query_params)

            if not self.serializer_class(data=request.query_params).is_valid():
                return self.response_json(Result.ERROR_PARAMS, {})

            return self.handle(request.META, request.query_params)

        except Exception:
            return self.response_json(Result.ERROR_SERVER, {})

    def post(self, request):
        try:
            if self.serializer_class is None:
                return self.handle(request.META, request.data)

            if not self.serializer_class(data=request.data).is_valid():
                return self.response_json(Result.ERROR_PARAMS, {})

            return self.handle(request.META, request.data)

        except Exception:
            return self.response_json(Result.ERROR_SERVER, {})

    def handle(self, request_meta, data):
        if self.is_check_auth:
            self.check_auth(request_meta)
            self.check_permission(request_meta)

        result_code, reply = self.process(data)

        return self.response_json(result_code, reply)

    def check_auth(self, request_meta):
        try:
            jwt_prefix, jwt_token = request_meta["HTTP_AUTHORIZATION"].split(" ")
            if not jwt_prefix or not jwt_token:
                return self.response_json(Result.ERROR_ACCESS_TOKEN, {})

            if jwt_prefix != settings.JWT_AUTH["JWT_AUTH_HEADER_PREFIX"]:
                return self.response_json(Result.ERROR_ACCESS_TOKEN, {})

            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY,
                                       algorithms=settings.JWT_AUTH["ENCRYPT_ALGORITHM"])
            expired_time = datetime.datetime.strptime(decoded_token["expired_time"], '%Y-%m-%d %H:%M:%S.%f')
            if expired_time < datetime.datetime.now():
                return self.response_json(Result.ERROR_TOKEN_EXPIRED, {})

            self.set_user_id(decoded_token["user_id"])

        except Exception:
            return self.response_json(Result.ERROR_SERVER, {})

    def set_user_id(self, user_id=None):
        self.user_id = user_id

    def check_permission(self, request_meta):
        pass

    def response_json(self, result_code, reply=None):
        return Response({"result": result_code, "reply": reply})


class PublicGetAPIView(BaseAPIVIew):
    def __init__(self):
        self.is_check_auth = False


class PublicPostAPIView(BaseAPIVIew):
    def __init__(self):
        self.serializer_class = None
        self.is_check_auth = False


class PrivateGetAPIView(BaseAPIVIew):
    def __init__(self):
        self.serializer_class = None
        self.is_check_auth = True


class PrivatePostAPIView(BaseAPIVIew):
    def __init__(self):
        self.serializer_class = None
        self.is_check_auth = True
