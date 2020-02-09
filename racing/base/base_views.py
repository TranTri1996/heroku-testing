from rest_framework.views import APIView
from racing.base import encoders
from racing.constants import Result
from rest_framework.response import Response

from racing.serializers import DumSerialize


class BaseView(APIView):

    def __init__(self, **kwargs):
        super(APIView, self).__init__(**kwargs)
        self._reply = None

    class __RespondJump(Exception):
        pass

    encoder_class = encoders.ExtendedJsonEncoder

    def get_serializer(self, *args, **kwargs):
        if 'request' in kwargs:
            request = kwargs.pop('request')
            if request.method.lower() == 'post':
                return self.class_serializer(data=request.data)
            if request.method.lower() == 'get':
                return self.class_serializer(data=request.query_params)
        return self.class_serializer(*args, **kwargs)

    def handle(self, request, data):
        try:
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
        return True


class GetAPIView(BaseView):
    class_serializer = DumSerialize

    def get(self, request):
        return self.handle(request, request.query_params)


class PostAPIView(BaseView):
    class_serializer = DumSerialize

    def post(self, request):
        return self.handle(request, request.data)
