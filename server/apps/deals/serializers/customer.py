from rest_framework import serializers
from ..models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Сериализатор Покупателя
    """
    spent_money = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        read_only=True,
    )

    gems = serializers.ListField(
        read_only=True,
    )

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')
