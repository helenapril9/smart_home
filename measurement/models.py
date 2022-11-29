# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.db import models

class Sensor(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=30)
    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='Датчик')
    temperature = models.IntegerField()
    date = models.DateTimeField(verbose_name='Дата измерения')











