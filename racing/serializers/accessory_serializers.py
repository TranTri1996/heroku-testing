from rest_framework_mongoengine.serializers import DocumentSerializer

from racing.models.models import Accessory


class AccessorySerializer(DocumentSerializer):
    class Meta:
        model = Accessory
        depth = 2
        fields = '__all__'
