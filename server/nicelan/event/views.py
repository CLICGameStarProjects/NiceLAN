from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView


from .forms import EventForm
from .models import Event


def event_select(request, pk):
    request.session["current_event"] = int(pk)
    return HttpResponseRedirect(reverse_lazy("event_list"))


def event_show(request, pk):
    event = get_object_or_404(Event, pk=pk)
    players = event.players
    activities = event.activity_set.all()
    return render(
        request, "event/show.html", {"event": event, "players": players, "activities": activities}
    )


def event_list(request):
    events = Event.objects.all().order_by("-start_date", "-start_time")
    return render(
        request,
        "event/list.html",
        {"events": events, "current_event": request.session.get("current_event", -1)},
    )


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "event/edit.html"

    def get_success_url(self):
        return reverse_lazy("event_list")


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "event/edit.html"

    def get_success_url(self):
        return reverse_lazy("event_list")


class EventDeleteView(DeleteView):
    model = Event
    template_name = "event/delete.html"

    def get_success_url(self):
        return reverse_lazy("event_list")
