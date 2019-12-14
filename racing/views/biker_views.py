from rest_framework.views import APIView
from racing.models.models import Biker
from rest_framework.response import Response


class BikerListAllView(APIView):

    def get(self, request):
        pass
