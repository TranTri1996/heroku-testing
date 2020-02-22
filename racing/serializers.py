from rest_framework import serializers


# BIKER SERIALIZER
class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50, required=False)
    user_name = serializers.CharField(max_length=50, required=True)
    phone = serializers.CharField(max_length=15, required=True)
    email = serializers.CharField(max_length=100, required=True)
    date_of_birth = serializers.DateTimeField(required=False)
    password = serializers.CharField(max_length=100, required=True)
    gender = serializers.IntegerField(required=True)
    job = serializers.CharField(max_length=255, required=False)
    facebook = serializers.CharField(max_length=100, required=False)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)


# PRODUCT_SERIALIZER
class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=5000, required=False)
    province_id = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=3)
    accessory_id = serializers.IntegerField(required=True)


class GetPersonalProductListSerializer(serializers.Serializer):
    pass


# POST SERIALIZER
class PostListSerializer(serializers.Serializer):
    post_id = serializers.IntegerField(required=False)
    biker_id = serializers.IntegerField(required=False)


class PostCreateSerializer(serializers.Serializer):
    biker_id = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=255, required=False, default="")
    description = serializers.CharField(max_length=5000, required=False)
    is_active = serializers.IntegerField(required=False, default=1)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=100, required=True)
    new_password = serializers.CharField(max_length=100, required=True)
    repeat_new_password = serializers.CharField(max_length=100, required=True)
