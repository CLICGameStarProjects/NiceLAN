from django.urls import path


from .views import player_show, player_list, PlayerCreateView, PlayerUpdateView, PlayerDeleteView


urlpatterns = [
    path("player", player_list, name="player_list"),
    path("player/list", player_list, name="player_list"), # maybe inutile ?
    path("player/new", PlayerCreateView.as_view(), name="player_new"),
    path("player/<pk>/show", player_show, name="player_show"),
    #path("player/<pk>/select", player_select, name="player_select"), --> we don't select players lol
    path("player/<pk>/edit", PlayerUpdateView.as_view(), name="player_edit"),
    path("player/<pk>/delete", PlayerDeleteView.as_view(), name="player_delete"),
]
