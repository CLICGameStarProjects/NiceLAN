from django.shortcuts import render


def event_new(request):
    pass


def event_list(request):
    return render(request, "event/list.html")
