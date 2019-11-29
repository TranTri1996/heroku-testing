from rest_framework import serializers

from racing.models.models import Biker


class BikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biker
        fields = '__all__'
