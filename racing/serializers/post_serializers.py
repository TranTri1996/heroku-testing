from rest_framework import serializers


class PostListParamSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=False)
    post_id = serializers.IntegerField(required=False)


class CreatePostSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)
    status = serializers.CharField(required=True)
