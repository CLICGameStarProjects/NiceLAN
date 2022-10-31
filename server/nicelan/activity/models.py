from django.db import models


OTH = "OTHER"
ACTIVITY_CATEGORIES = [
    (OTH, "Other"),
]


class Activity(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    category = models.CharField(max_length=8, choices=ACTIVITY_CATEGORIES, default=OTH)  # TODO why?
    start = models.DateTimeField()
    end = models.DateTimeField()
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
