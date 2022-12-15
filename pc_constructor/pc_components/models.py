from django.db import models


# Create your models here.

class MonitorModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    length_m = models.CharField(max_length=100)
    weigth = models.CharField(max_length=100)
    matrix = models.CharField(max_length=100)

    def __str__(self):
        return self.name
