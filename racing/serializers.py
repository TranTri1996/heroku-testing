from rest_framework import serializers

from .models import Biker, Post


class BikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biker
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
