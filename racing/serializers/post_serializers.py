from rest_framework import serializers

from racing.models.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField()
    status = serializers.CharField()
