from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


@login_required()
def dashboard(request):
    context = {"segment": "dashboard"}

    html_template = loader.get_template("webapp/dashboard.html")
    return HttpResponse(html_template.render(context, request))
