from django.urls import path


from .views import activity_list, activity_show, ActivityCreateView, ActivityDeleteView, ActivityUpdateView


urlpatterns = [
    path("<event_pk>", activity_list, name="activity_list"),
    path("<event_pk>/new/", ActivityCreateView.as_view(), name="activity_new"),
    path("<event_pk>/<pk>/", activity_show, name="activity_show"),
    path("<event_pk>/<pk>/edit", ActivityUpdateView.as_view(), name="activity_edit"),
    path("<event_pk>/<pk>/delete", ActivityDeleteView.as_view(), name="activity_delete"),
]
