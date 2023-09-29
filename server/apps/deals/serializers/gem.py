from rest_framework import serializers
from ..models import Gem


class GemSerializer(serializers.ModelSerializer):
    """
    Сериализатор Камня
    """
    class Meta:
        model = Gem
        fields = ('id', 'name')
