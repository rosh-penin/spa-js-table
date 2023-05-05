from django.db import models

from .constants import MAX_LENGTH


class TableRow(models.Model):
    """Simple test model with ordering by date."""
    date = models.DateField('Дата')
    name = models.CharField('Название', max_length=MAX_LENGTH)
    amount = models.IntegerField('Количество')
    distance = models.IntegerField('Расстояние')

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.name
