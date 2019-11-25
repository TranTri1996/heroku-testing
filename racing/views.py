from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from racing.models import Biker
from racing.serializers import BikerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class getAllBiker(APIView):

    def get(self, request):
        bikers = Biker.objects.all()
        serializer = BikerSerializer(bikers, many=True)

        return Response(serializer.data)


class getAllRacing(APIView):

    def get(self, request):
        bikers = Biker.objects.all()
        serializer = BikerSerializer(bikers, many=True)

        return Response(serializer.data)
