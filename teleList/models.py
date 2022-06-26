from django.conf import settings
from django.db import models
from django.utils import timezone

class TeleItem(models.Model):
    rk = models.CharField(max_length=10)
    appt = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    number = models.BigIntegerField()

    def __str__(self):
        return self.name