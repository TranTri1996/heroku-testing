from rest_framework.views import APIView
from racing.models.models import Biker
from racing.serializers.biker_serializers import BikerSerializer
from rest_framework.response import Response


class BikerListAllView(APIView):

    def get(self, request):
        bikers = Biker.objects.all()
        serializer = BikerSerializer(bikers, many=True)

        return Response(serializer.data)
