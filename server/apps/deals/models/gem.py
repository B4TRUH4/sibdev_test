from django.db import models


class Gem(models.Model):
    """
    Класс Камня
    """
    name = models.CharField(
        max_length=20,
        verbose_name='название',
    )

    class Meta:
        verbose_name = 'Камень'
        verbose_name_plural = 'Камни'

    def __str__(self):
        return f'{self.id}, {self.name}'
