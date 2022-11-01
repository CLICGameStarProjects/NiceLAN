from django.urls import path


from .views import player_new, PlayerCreateView


urlpatterns = [
    path("player/new", PlayerCreateView.as_view(), name="player_new"),
]
