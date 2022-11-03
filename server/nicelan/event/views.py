from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView


from .forms import EventForm
from .models import Event


def event_list(request):
    events = Event.objects.all().order_by("-start_date", "-start_time")
    return render(request, "event/list.html", {"events": events})


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
