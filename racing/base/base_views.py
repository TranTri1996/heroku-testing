import datetime
import types

import jwt

from rest_framework.views import APIView
from racing.constants import Result
from rest_framework.response import Response
from vietnamracing import settings


class BaseAPIVIew(APIView):
    serializer_class = None
    is_check_auth = False

    def get(self, request):
        try:
            if self.serializer_class is None:
                return self.handle(request.META, request.query_params)

            if not self.serializer_class(data=request.query_params).is_valid():
                return self.response_json(Result.ERROR_PARAMS)

            return self.handle(request.META, request.query_params)

        except Exception as e:
            print(str(e))
            return self.response_json(Result.ERROR_SERVER)

    def post(self, request):
        try:
            if self.serializer_class is None:
                return self.handle(request.META, request.data)

            if not self.serializer_class(data=request.data).is_valid():
                return self.response_json(Result.ERROR_PARAMS)

            return self.handle(request.META, request.data)

        except Exception as e:
            print(str(e))
            return self.response_json(Result.ERROR_SERVER)

    def handle(self, request_meta, data):
        if self.is_check_auth:
            error_auth = self.check_auth(request_meta)
            if error_auth:
                return self.response_json(error_auth, None)
            self.check_permission(request_meta)
        result_code, reply = self.process(data)

        return self.response_json(result_code, reply)

    def check_auth(self, request_meta):
        try:
            if not request_meta.get("HTTP_AUTHORIZATION"):
                return Result.ERROR_ACCESS_TOKEN

            jwt_prefix, jwt_token = request_meta["HTTP_AUTHORIZATION"].split(" ")
            if not jwt_prefix or not jwt_token:
                return Result.ERROR_ACCESS_TOKEN

            if jwt_prefix != settings.JWT_AUTH["JWT_AUTH_HEADER_PREFIX"]:
                return Result.ERROR_ACCESS_TOKEN

            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY,
                                       algorithms=settings.JWT_AUTH["ENCRYPT_ALGORITHM"])
            expired_time = datetime.datetime.strptime(decoded_token["expired_time"], '%Y-%m-%d %H:%M:%S.%f')
            if expired_time < datetime.datetime.now():
                return Result.ERROR_TOKEN_EXPIRED

            self.user_id = decoded_token["user_id"]

            return None

        except Exception as e:
            print(str(e))
            return Result.ERROR_SERVER

    def check_permission(self, request_meta):
        pass

    def response_json(self, result_code, reply=None):
        return Response({"result": result_code, "reply": reply})


class PublicGetAPIView(BaseAPIVIew):
    is_check_auth = False


class PublicPostAPIView(BaseAPIVIew):
    is_check_auth = False


class PrivateGetAPIView(BaseAPIVIew):
    is_check_auth = True


class PrivatePostAPIView(BaseAPIVIew):
    is_check_auth = True
