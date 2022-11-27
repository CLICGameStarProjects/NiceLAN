from abc import ABC
import random


from django.db import models


from ..points.models import ActivityPoints, BracketPoints, BracketPointsMapping


# collection of BracketFights
class Bracket(models.Model, ABC):
    activity = models.ForeignKey("activity.Activity", on_delete=models.CASCADE)
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
        return self.bracket_partaker_set.all()

    def fights_for_step(self, step: int):
        return self.bracket_fight_set.filter(step=step)

    # generates the first BracketFights and all the BracketPartakers
    def _init(self):
        pass

    # generates all BracketFights for the current step
    def _generate_bracket_fights(self):
        pass

    # generates all BracketPoints for the current step, based on BracketFightPoints
    def _generate_bracket_points(self):
        pass

    # generates all ActivityPoints based on BracketPoints
    def _generate_activity_points(self):
        pass

    # concludes the current step and either generates the next step (`False`)
    # or terminates the bracket (`True`)
    def proceed(self):
        if self.step == 0:
            self._init()
            self.step = 1
            self.save()
            return False

        # generates BracketPoints from BracketFightPoints
        self._generate_bracket_points()

        # generates ActivityPoints from BracketPoints
        if self.step == self.max_step:
            self._generate_activity_points()
            return True

        # the bracket proceeds to the next step
        self.step += 1
        self.save()
        self._generate_bracket_fights()
        return False


class SimpleTreeBracket(Bracket):
    def _init(self):
        partakers = list(self.activity.partaker_set.all())
        if len(partakers) % 2 != 0:
            return

        random.shuffle(partakers)
        for a, b in zip(partakers[::2], partakers[1::2]):
            fight = BracketFight.objects.create(bracket=self, step=1)
            BracketPartaker.objects.create(bracket=self, bracket_fight=fight, partaker=a)
            BracketPartaker.objects.create(bracket=self, bracket_fight=fight, partaker=b)

        BracketPointsMapping.create_points_mappings_for(self)

    def _generate_bracket_fights(self):
        winners = []
        for fight in self.current_fights:
            results = fight.bracket_fight_points_set.all()
            if results[0].points > results[1].points:
                winners.append(results[0].bracket_partaker)
        for winner_1, winner_2 in zip(winners[::2], winners[1::2]):
            fight = BracketFight.objects.create(bracket=self, step=self.step)
            winner_1.update(bracket=self, bracket_fight=fight, partaker=winner_1)
            winner_2.update(bracket=self, bracket_fight=fight, partaker=winner_2)

    def _generate_bracket_points(self):
        for fight in self.current_fights:
            results = fight.bracket_fight_points_set.all()
            winner = None
            loser = None
            if results[0].points > results[1].points:
                winner = results[0].bracket_partaker
                loser = results[1].bracket_partaker
            elif results[0].points < results[1].points:
                winner = results[1].bracket_partaker
                loser = results[0].bracket_partaker
            else:
                random.shuffle(results)
                winner = results[0]
                loser = results[1]
            # BracketPoints for the loser BracketPartaker
            BracketPoints.objects.create(
                step=self.step, bracket=self, bracket_partaker=winner, points=self.points_map[0]
            )
            # BracketPoints for the loser BracketPartaker
            BracketPoints.objects.create(
                step=self.step, bracket=self, bracket_partaker=loser, points=self.points_map[1]
            )


class DoubleTreeBracket(Bracket):
    simple_tree = models.ForeignKey("SimpleTree", on_delete=models.CASCADE)

    def _init(self):
        self.simple_tree = SimpleTreeBracket.objects.create(
            activity=self.activity, step=1, max_step=self.max_step
        )

        BracketPointsMapping.create_points_mappings_for(self)
        BracketPointsMapping.create_points_mappings_for(self.simple_tree)

        partakers = list(self.activity.partaker_set.all())
        random.shuffle(partakers)

        for a, b in zip(partakers[::2], partakers[1::2]):
            fight = BracketFight.objects.create(bracket=self.simple_tree, step=1)
            BracketPartaker.objects.create(
                bracket=self.simple_tree, bracket_fight=fight, partaker=a
            )
            BracketPartaker.objects.create(
                bracket=self.simple_tree, bracket_fight=fight, partaker=b
            )

        self.save()

    def _generate_bracket_fights(self):
        pass

    def _generate_bracket_points(self):
        pass


class FFABracket(Bracket):
    def _init(self):
        partakers = self.activity.partaker_set.all()
        ffa_fight = BracketFight.objects.create(bracket=self, step=1)
        for partaker in partakers:
            BracketPartaker.objects.create(bracket=self, bracket_fight=ffa_fight, partaker=partaker)

        BracketPointsMapping.create_points_mappings_for(self)

    def _generate_bracket_fights(self):
        ffa_fight = BracketFight.objects.create(bracket=self, step=self.step)
        for bracket_partaker in self.bracket_partakers:
            bracket_partaker.update(
                bracket=self, partaker=bracket_partaker.partaker, bracket_fight=ffa_fight
            )
            bracket_partaker

    def _generate_bracket_points(self):
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

    def _generate_activity_points(self):
        all_bracket_points = self.bracket_points_set.all().order_by("points")
        for position, bracket_points in enumerate(all_bracket_points):
            ActivityPoints.objects.create(
                activity=self.activity,
                points=self.activity.points_map[position],
                partaker=bracket_points.bracket_partaker.partaker,
            )


class CustomBracket(Bracket):
    pass


# 2 to N BracketPartakers take part in a given BracketFight
class BracketFight(models.Model):
    bracket = models.ForeignKey("Bracket", on_delete=models.CASCADE)
    step = models.PositiveIntegerField()

    @property
    def bracket_partakers(self):
        return [
            bracket_fight_points.bracket_partaker
            for bracket_fight_points in self.bracket_fight_points_set.all()
        ]


# intermediate model to represent Partakers in a Bracket and its BracketFights
class BracketPartaker(models.Model):
    partaker = models.ForeignKey("partaker.Partaker", on_delete=models.CASCADE)
    bracket = models.ForeignKey("Bracket", on_delete=models.CASCADE)
    # !!! current !!! BracketFight
    bracket_fight = models.ForeignKey("BracketFight", on_delete=models.CASCADE)
