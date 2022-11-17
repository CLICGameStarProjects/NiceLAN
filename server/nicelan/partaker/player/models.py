from django import models

class Player(Partaker):
    discord = models.CharField(max_length=64, blank=True)
    Telegram = models.CharField(max_length=64, blank=True)

    @property
    def players(self):
        return [partaker for partaker in self.partaker_set.all() if partaker.is_player;

class Manager(Player):
    activity = leader = models.ForeignKey("activity.", on_delete=models.CASCADE)

    @property
    def add_player(Partaker partaker):
        # TODO

    @property
    def delete_player(Partaker partaker) :
        # TODO

class SuperManager(Player):
    # idk comment faire le type[Activity] thingie

    @property
    def create_activity(Activity activity):

