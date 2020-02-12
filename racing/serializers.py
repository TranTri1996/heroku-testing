from rest_framework import serializers


# BASE SERIALIZER
class DumSerialize(serializers.Serializer):
    pass


# BIKER SERIALIZER
class BikeRegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50, required=False)
    user_name = serializers.CharField(max_length=50, required=True)
    phone = serializers.CharField(max_length=15, required=True)
    email = serializers.CharField(max_length=100, required=True)
    date_of_birth = serializers.DateTimeField(required=False)
    password = serializers.CharField(max_length=100, required=True)
    gender = serializers.IntegerField(required=True)
    job = serializers.CharField(max_length=255, required=False)
    facebook = serializers.CharField(max_length=100, required=False)


class BikerLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)


class BikerLogoutSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)
    token = serializers.CharField(required=True)


class BikerListSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=False)
    is_active = serializers.IntegerField(required=False)
    from_time = serializers.DateTimeField(required=False)
    to_time = serializers.DateTimeField(required=False)


class BikerGetProfileSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)


# POST SERIALIZER
class PostListSerializer(serializers.Serializer):
    post_id = serializers.IntegerField(required=False)
    biker_id = serializers.IntegerField(required=False)


class PostCreateSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=255, required=False, default="")
    description = serializers.CharField(max_length=5000, required=False, default="")
    is_active = serializers.IntegerField(required=False, default=1)
