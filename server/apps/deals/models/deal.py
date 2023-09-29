from django.db import models
from django.core.validators import MinValueValidator
from .gem import Gem
from .customer import Customer


class Deal(models.Model):
    """
    Класс Сделки
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='deals',
    )
    item = models.ForeignKey(
        Gem,
        on_delete=models.CASCADE,
        related_name='deals',
    )
    total = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=(MinValueValidator(0),),
        verbose_name='сумма',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
    )
    date = models.DateTimeField(
        verbose_name='дата и время',
    )

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return f'{self.customer} {self.item}'
