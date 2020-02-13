import jwt
from rest_framework.views import APIView

from racing.base import encoders
from racing.constants import Result
from rest_framework.response import Response

from vietnamracing import settings


class BaseAPIVIew(APIView):
    def __init__(self):
        self.is_check_auth = None
        self.serializer_class = None

    def get(self, request):
        if not self.serializer_class(data=request.query_params).is_valid():
            self.response_json(Result.ERROR_PARAMS, {})

        return self.handle(request.META, request.query_params)

    def post(self, request):
        if not self.serializer_class(data=request.data).is_valid():
            self.response_json(Result.ERROR_PARAMS, {})

        return self.handle(request.META, request.data)

    def handle(self, request_meta, data):
        if self.is_check_auth:
            if not self.success_check_auth(request_meta):
                return self.response_json(Result.ERROR_ACCESS_TOKEN, {})

            if not self.success_check_permission(request_meta):
                return self.response_json(Result.ERROR_FORBIDDEN, {})

        result_code, reply = self.process(data)

        return self.response_json(result_code, reply)

    def success_check_auth(self, request_meta):
        jwt_access = request_meta.get("HTTP_AUTHORIZATION")
        if not jwt_access:
            return False

        return True

    def success_check_permission(self, request_meta):
        jwt_header, token = request_meta["HTTP_AUTHORIZATION"].split(" ")

        if jwt_header != settings.JWT_AUTH["JWT_AUTH_HEADER_PREFIX"]:
            return False

        decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # if decode_token["biker_id"] != request_meta.get["HTTP_BIKER_ID"]:
        #     return False

        return True

    def response_json(self, result_code, reply=None):
        return Response({"result": result_code, "reply": reply})


class PublicGetAPIView(BaseAPIVIew):
    def __init__(self):
        self.is_check_auth = False


class PublicPostAPIView(BaseAPIVIew):
    def __init__(self):
        self.is_check_auth = False


class PrivateGetAPIView(BaseAPIVIew):
    def __init__(self):
        self.is_check_auth = True


class PrivatePostAPIView(BaseAPIVIew):
    def __init__(self):
        self.is_check_auth = True
