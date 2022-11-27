from django.db import models


class PointsMapping(models.Model):
    position = models.PositiveIntegerField()
    points = models.PositiveIntegerField()


# points mapping for a given Activity
# i.e. what reward do Partakers get once the Bracket terminates
class ActivityPointsMapping(PointsMapping):
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)


# points mapping for a given Bracket
# i.e. what reward do BracketPartakers get once a BracketFight terminates
class BracketPointsMapping(PointsMapping):
    bracket = models.ForeignKey("Bracket", on_delete=models.CASCADE)

    # creates the default points mapping for the given bracket
    @staticmethod
    def create_points_mappings_for(bracket):
        nb_partakers = len(bracket.activity.partaker_set.all())
        for position in range(nb_partakers):
            BracketPointsMapping.objects.create(
                position=position, points=nb_partakers - position, bracket=bracket
            )


class Points(models.Model):
    points = models.PositiveIntegerField()


# final points of a given Partaker in a given Activity
class ActivityPoints(Points):
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    partaker = models.ForeignKey("partaker.Partaker", on_delete=models.CASCADE)


# points of a given BracketPartaker in a given Bracket at given bracket step
class BracketPoints(Points):
    step = models.PositiveIntegerField()
    bracket = models.ForeignKey("Bracket", on_delete=models.CASCADE)
    bracket_partaker = models.ForeignKey("BracketPartaker", on_delete=models.CASCADE)


# points of a given BracketPartaker in a given BracketFight
# i.e. how did Partakers perform in the BracketFight
class BracketFightPoints(Points):
    bracket_fight = models.ForeignKey("BracketFight", on_delete=models.CASCADE)
    bracket_partaker = models.ForeignKey("BracketPartaker", on_delete=models.CASCADE)
