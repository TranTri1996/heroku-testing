from rest_framework.views import APIView

from racing import models
from racing.base import encoders
from racing.base.constant import AppType
from racing.constants import Result
from rest_framework.response import Response

from racing.serializers import DumSerialize


class BaseView(APIView):
    class __RespondJump(Exception):
        pass

    def __init__(self, **kwargs):
        super(APIView, self).__init__(**kwargs)
        self._reply = None

    encoder_class = encoders.ExtendedJsonEncoder

    def get_serializer(self, *args, **kwargs):
        if 'request' in kwargs:
            request = kwargs.pop('request')
            if request.method.lower() == 'post':
                return self.class_serializer(data=request.data)
            if request.method.lower() == 'get':
                return self.class_serializer(data=request.query_params)
        return self.class_serializer(*args, **kwargs)

    def handle(self, request, data, is_check_auth=False):
        try:
            self._app_type = 1 # request.META.get("RACING_APP_TYPE")
            if is_check_auth:
                self.check_authen(request)

            serializer = self.class_serializer(data=data)
            if not serializer.is_valid():
                self.response_json(Result.ERROR_PARAMS, serializer.errors)
            result_code, reply = self.process(serializer.data)
            self.response_json(result_code, reply)

        except self.__RespondJump:
            return self._reply

    def response_json(self, result_code, reply=None):
        self._reply = Response({"result": result_code, "reply": reply})
        raise self.__RespondJump

    def check_authen(self, request):
        headers = request.META
        token = headers.get("HTTP_AUTHORIZATION")
        if not token:
            self.response_json(Result.ERROR_FORBIDDEN, {})

        app_type = 1# AppType[self._app_type].value
        access_token = models.Token.objects.filter(token=token, app_type=app_type).first()
        if not access_token:
            self.response_json(Result.ERROR_ACCESS_TOKEN, {})


class GetAPIView(BaseView):
    class_serializer = DumSerialize

    def get(self, request):
        return self.handle(request, request.query_params, False)


class PostAPIView(BaseView):
    class_serializer = DumSerialize

    def post(self, request):
        return self.handle(request, request.data, True)


class AuthenticatedAPView(BaseView):
    serializer_class = DumSerialize

    def get(self, request):
        self._app_type = request.META.get("RACING_APP_TYPE")
        self.check_authen(request)

        try:
            serializer = self.serializer_class(data=request.query_params)
            if not serializer.is_valid():
                self.response_json(Result.ERROR_PARAMS, serializer.errors)

            return self.process(serializer.data)
        except self._BaseAPIView__RespondJump:
            return self._reply

    def post(self, request):
        self._app_type = request.META.get("RACING_APP_TYPE")
        self.check_authen(request)

        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.respond_json(Result.ERROR_PARAMS, serializer.errors)

            return self.process(serializer.data)
        except self._BaseAPIView__RespondJump:
            return self._reply


class PublicGetAPIView(BaseView):
    serializer_class = DumSerialize

    def get(self, request):
        return self.handle(request, request.query_params, False)


class PublicPostAPIView(BaseView):
    serializer_class = DumSerialize

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            self.respond_json(Result.ERROR_PARAMS, serializer.errors)

        return self.handle(request, request.data, False)
