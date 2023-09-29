from django.db import models
from .managers import CustomerManager


class Customer(models.Model):
    """
    Класс Покупателя
    """
    username = models.CharField(
        max_length=20,
        verbose_name='имя заказчика'
    )

    objects = CustomerManager()

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return f'{self.username}'
