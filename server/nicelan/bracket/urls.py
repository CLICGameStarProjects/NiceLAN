from django.urls import path
import bracket.views

urlpatterns = [
    path("bracket_show_ffa/<int:activity_pk>/", bracket.views.bracket_show_ffa),
    path("bracket_show_simple_tree/<int:activity_pk>/", bracket.views.bracket_show_simple_tree),
    path("bracket_show_double_tree/<int:activity_pk>/", bracket.views.bracket_show_double_tree),

    path("bracket_create_ffa/<int:activity_pk>/", bracket.views.bracket_create_ffa),
    path("bracket_create_simple_tree/<int:activity_pk>/", bracket.views.bracket_create_simple_tree),
    path("bracket_create_double_tree/<int:activity_pk>/", bracket.views.bracket_create_double_tree),

    path("bracket_delete/<int:pk>", bracket.views.bracket_delete),
]

