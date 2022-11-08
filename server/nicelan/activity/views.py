from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView


from .forms import ActivityForm
from .models import Activity


def activity_show(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    players = activity.players
    return render(request, "activity/show.html", {"activity": activity, "players": players})


def activity_list(request, event_pk):
    activity = Activity.objects.all().order_by("-start_date", "-start_time")
    return render(request, "activity/list.html", {"activity": activity})


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "activity/edit.html"

    def get_success_url(self):
        return reverse_lazy("activity_list")


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = "activity/edit.html"

    def get_success_url(self):
        return reverse_lazy("activity_list")


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = "activity/delete.html"

    def get_success_url(self):
        return reverse_lazy("activity_list")
