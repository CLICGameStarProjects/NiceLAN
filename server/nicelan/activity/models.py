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
    description = models.TextField(max_length=1024)

    @property
    def points(self):
        return {
            activity_points.partaker.name: activity_points.points
            for activity_points in self.activity_points_set.all()
        }

    @property
    def points_map(self):
        return self.activity_points_mapping_set.all().order_by("position").asc()
