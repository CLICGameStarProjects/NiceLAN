from django.urls import path


from .views import event_list, event_new


urlpatterns = [
    path("new", event_new, name="event_new"),
    path("list", event_list, name="event_list"),
]
