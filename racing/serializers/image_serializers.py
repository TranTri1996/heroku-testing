from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer

from racing.models.models import Image


class ImageSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Image
        depth = 2
        fields = '__all__'
