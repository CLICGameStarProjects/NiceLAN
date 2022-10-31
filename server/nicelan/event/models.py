from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=64)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1024)
