from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    description = models.CharField(max_length=1024, blank=True)
