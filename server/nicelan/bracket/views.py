from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView


from .forms import BracketFightForm, BracketForm
from .models import Bracket, BracketFight


def activity_show(request, pk):
    activity = get_object_or_404(Bracket, pk=pk)
    players = activity.players
    return render(request, "activity/show.html", {"activity": activity, "players": players})


def activity_list(request, event_pk):
    activity = Bracket.objects.all().order_by("-start_date", "-start_time")
    return render(request, "activity/list.html", {"activity": activity})


class BracketCreateView(CreateView):
    model = Bracket
    form_class = BracketForm
    template_name = "bracket/new.html"

    def get_success_url(self):
        return reverse_lazy("bracket_list")


class BracketDeleteView(DeleteView):
    model = Bracket
    template_name = "bracket/delete.html"

    def get_success_url(self):
        return reverse_lazy("bracket_list")
