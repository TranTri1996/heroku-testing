from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer

from racing.models.models import Address


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Address
        depth = 2
        fields = '__all__'
