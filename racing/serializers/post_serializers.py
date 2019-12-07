from rest_framework_mongoengine.serializers import DocumentSerializer
from racing.serializers.image_serializers import ImageSerializer
from racing.models.models import Post, Image


class PostSerializer(DocumentSerializer):
    images = ImageSerializer(Image)

    class Post:
        model = Post
        depth = 2
        fields = '__all__'
