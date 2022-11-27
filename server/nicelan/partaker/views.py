from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Player


class PlayerCreateView(CreateView):
    model = Player
    fields = ["name", "event", "discord", "Telegram"] #comment faire pr qu'il affiche une liste d'events quand je veux créer / edit un player
    template_name = "partaker/player/edit.html"

    def get_success_url(self):
            return reverse_lazy("player_list")

class PlayerUpdateView(UpdateView):
    model = Player
    fields = ["name", "event", "discord", "Telegram"]
    template_name = "partaker/player/edit.html"

    def get_success_url(self):
        return reverse_lazy("player_list")


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "partaker/player/delete.html"

    def get_success_url(self):
        return reverse_lazy("player_list")


def player_list(request) :
    players = Player.objects.all()
    return render(
        request,
        "partaker/player/list.html",
        {"players" : players}

    )

def player_show(request, pk):
    player = get_object_or_404(Player, pk=pk)
    events = player.event # get the event's name i guess
    activities = player.activities
    return render(
        request, "partaker/player/show.html", {"player": player, "events" : events, "activities": activities}
    )


