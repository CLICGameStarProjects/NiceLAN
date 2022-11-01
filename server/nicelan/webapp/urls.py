from django.urls import path
from django.views.generic import RedirectView


from .views import dashboard


urlpatterns = [
    path("", RedirectView.as_view(url="d", permanent=False), name="index"),
    path("d/", dashboard, name="dashboard"),
]
