from django.db import models


from ..points.models import ActivityPoints, BracketPoints


# collection of BracketFights
class Bracket(models.Model):
    activity = models.ForeignKey("Activity")
    step = models.PositiveIntegerField()
    max_step = models.PositiveIntegerField()

    @property
    def current_fights(self):
        return self.fights_for_step(self.step)

    @property
    def points_map(self):
        return [
            bracket_points_mapping.points
            for bracket_points_mapping in self.bracket_points_mapping_set.all()
            .order_by("position")
            .asc()
        ]

    @property
    def bracket_partakers(self):
        return self.bracket_partakers_set.all()

    def fights_for_step(self, step: int):
        return self.bracket_fight_set.filter(step=step)

    def generate_activity_points(self):
        all_bracket_points = self.bracket_points_set.all().order_by("points")
        for position, bracket_points in enumerate(all_bracket_points):
            ActivityPoints.objects.create(
                activity=self.activity,
                points=self.activity.points_map[position],
                partaker=bracket_points.bracket_partaker.partaker,
            )


class SimpleTreeBracket(Bracket):
    pass


class DoubleTreeBracket(Bracket):
    pass


class FFABracket(Bracket):
    # generates the BracketPartakers and the first BracketFight
    def init(self):
        partakers = self.activity.partaker_set.all()
        ffa_fight = BracketFight.objects.create(bracket=self, step=0)
        for partaker in partakers:
            BracketPartaker.objects.create(bracket=self, bracket_fight=ffa_fight, partaker=partaker)

    # generates the BracketPoints for the current step
    def generate_bracket_points(self):
        all_bracket_fight_points = (
            self.current_fights[0].bracket_fight_points_set.all().order_by("points")
        )
        for position, fight_points in enumerate(all_bracket_fight_points):
            BracketPoints.objects.create(
                points=self.points_map[position],
                bracket_partaker=fight_points.bracket_partaker,
                bracket=self,
                step=self.step,
            )

    # generates the single (FFA) BracketFight for the current step
    def generate_bracket_fights(self):
        ffa_fight = BracketFight.objects.create(bracket=self, step=self.step)
        for bracket_partaker in self.bracket_partakers:
            bracket_partaker.update(
                bracket=self, partaker=bracket_partaker.partaker, bracket_fight=ffa_fight
            )

    # concludes the current step and either generates the next step (False)
    # or terminates the bracket (True)
    def proceed(self):
        self.generate_bracket_points()

        if self.step == self.max_step:
            self.generate_activity_points()
            self.save()
            return True

        self.step += 1
        self.generate_bracket_fights()
        self.save()

        return False


class CustomBracket(Bracket):
    pass


# 2 to N BracketPartakers take part in a given BracketFight
class BracketFight(models.Model):
    bracket = models.ForeignKey("Bracket")
    step = models.PositiveIntegerField()

    @property
    def bracket_partakers(self):
        return [
            bracket_fight_points.bracket_partaker
            for bracket_fight_points in self.bracket_fight_points_set.all()
        ]


# intermediate model to represent Partakers in a Bracket and its BracketFights
class BracketPartaker(models.Model):
    partaker = models.ForeignKey("partaker.Partaker")
    bracket = models.ForeignKey("Bracket")
    # !!! current !!! BracketFight
    bracket_fight = models.ForeignKey("BracketFight")
