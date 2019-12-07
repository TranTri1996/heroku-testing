from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer

from racing.models.models import Location


class LocationSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Location
        depth = 2
        fields = '__all__'
