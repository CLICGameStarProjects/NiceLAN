from django.db import models


class Partaker(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)


class Player(Partaker):
    discord = models.CharField(max_length=64, blank=True)
    Telegram = models.CharField(max_length=64, blank=True)


class Team(Partaker):
    leader = models.ForeignKey("self", on_delete=models.CASCADE)
    members = models.ManyToManyField("self")
