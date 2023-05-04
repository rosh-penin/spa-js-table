from django.db import models

MAX_LENGTH = 100


class TableRow(models.Model):
    date = models.DateField('Дата')
    name = models.CharField('Название', max_length=MAX_LENGTH)
    amount = models.IntegerField('Количество')
    distance = models.IntegerField('Расстояние')

    def __str__(self) -> str:
        return self.name
