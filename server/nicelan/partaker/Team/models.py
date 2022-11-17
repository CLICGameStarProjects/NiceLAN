from django import models

class Team(Partaker):
    leader = models.ForeignKey("self", on_delete=models.CASCADE)
    members = models.ManyToManyField("self")


