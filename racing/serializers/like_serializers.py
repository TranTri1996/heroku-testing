from rest_framework_mongoengine.serializers import DocumentSerializer

from racing.models.models import Like


class LikeSerializer(DocumentSerializer):
    class Meta:
        model = Like
        depth = 2
        fields = '__all__'
