from django.urls import path


from .views import event_list, event_select, event_show, EventCreateView, EventDeleteView, EventUpdateView


urlpatterns = [
    path("", event_list, name="event_list"),
    path("new", EventCreateView.as_view(), name="event_new"),
    path("<pk>/", event_show, name="event_show"),
    path("<pk>/select", event_select, name="event_select"),
    path("<pk>/edit", EventUpdateView.as_view(), name="event_edit"),
    path("<pk>/delete", EventDeleteView.as_view(), name="event_delete"),
]
