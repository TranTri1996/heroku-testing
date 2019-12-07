from rest_framework_mongoengine.serializers import DocumentSerializer

from racing.models.models import Biker, Address, Location
from racing.serializers.address_serializers import AddressSerializer
from racing.serializers.location_serializers import LocationSerializer


class BikerSerializer(DocumentSerializer):
    addresses = AddressSerializer(Address)
    locations = LocationSerializer(Location)

    class Meta:
        model = Biker
        depth = 2
        fields = '__all__'
