from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    category = models.CharField(max_length=64)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    place = models.CharField(max_length=64)  # TODO Model for places choices?
    team = models.BooleanField(default=False)
    description = models.CharField(max_length=1024)


class Tournament(Activity):
    points_min = models.IntegerField(default=0)
    points_per_place = None  # TODO
    format = None  # TODO
    bracket = None  # TODO


class Animation(Activity):
    possible_points = models.IntegerField(default=0)  # TODO


class Other(Activity):
    pass
