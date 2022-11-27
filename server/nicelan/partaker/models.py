from django.db import models


class Partaker(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    activities = models.ManyToManyField("activity.Activity")

    @property
    def is_player(self):
        return isinstance(self, Player)


class Player(Partaker):
    discord = models.CharField(max_length=64, blank=True)
    Telegram = models.CharField(max_length=64, blank=True)



class Team(Partaker):
    leader = models.ForeignKey("self", on_delete=models.CASCADE)
    members = models.ManyToManyField("self")


# sur-roles de player : PAS MTN
#class Manager(Player):
#    activity = models.ForeignKey("activity.Activity", on_delete=models.CASCADE)