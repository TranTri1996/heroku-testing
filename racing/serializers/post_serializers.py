from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    post_id = serializers.IntegerField(required=False)
    biker_id = serializers.IntegerField(required=False)


class PostCreateSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=255, required=False, default="")
    description = serializers.CharField(max_length=5000, required=False, default="")
    is_active = serializers.IntegerField(required=False, default=1)
