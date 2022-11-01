from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView


from .models import Player


class PlayerCreateView(CreateView):
    model = Player
    fields = ["name", "discord", "name"]


@login_required()
def player_new(request):
    context = {"segment": "partaker"}

    html_template = loader.get_template("partaker/new.html")
    return HttpResponse(html_template.render(context, request))
