from django.db import models

class WaterData(models.Model):
    date = models.DateField()
    BOD = models.FloatField()

    class Meta:
        ordering = ('date',)


class WaterData2(models.Model):
    BOD = models.FloatField()
    COD = models.FloatField()
    month = models.IntegerField()

    class Metata:
        ordering = ('month')