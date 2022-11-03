from django.urls import path
from django.views.generic import RedirectView


from .views import event_list, EventCreateView, EventDeleteView, EventUpdateView


urlpatterns = [
    path("", RedirectView.as_view(url="list", permanent=False)),
    path("new", EventCreateView.as_view(), name="event_new"),
    path("<pk>/edit", EventUpdateView.as_view(), name="event_edit"),
    path("<pk>/delete", EventDeleteView.as_view(), name="event_delete"),
    path("list", event_list, name="event_list"),
]
