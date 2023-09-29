from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from ..models import Deal, Customer, Gem


class DealCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор сделки для ее создания

    Важно! Сериализатор не проверяет наличие customer и item
    в соответствующих таблицах. Он предназначен только
    для валидации остальных полей.
    """
    customer = PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        required=False,
    )
    item = PrimaryKeyRelatedField(
        queryset=Gem.objects.all(),
        required=False,
    )

    class Meta:
        model = Deal
        fields = ('id', 'customer', 'item', 'total', 'quantity', 'date')

