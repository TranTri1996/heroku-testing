from rest_framework import serializers


class BikerListSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=False)
    is_active = serializers.IntegerField(required=False)
    from_time = serializers.DateTimeField(required=False)
    to_time = serializers.DateTimeField(required=False)


class BikerCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50, required=True)
    user_name = serializers.CharField(max_length=50, required=True)
    phone = serializers.CharField(max_length=15, required=True)
    email = serializers.CharField(max_length=100, required=True)
    date_of_birth = serializers.DateTimeField(required=False)
    password = serializers.CharField(max_length=100, required=True)
    gender = serializers.IntegerField(required=True)
    facebook = serializers.CharField(max_length=100, required=False)
