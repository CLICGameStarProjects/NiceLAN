from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from activity.models import Activity

from .forms import BracketFightForm, FFABracketForm
from .models import Bracket, FFABracket, SimpleTreeBracket, DoubleTreeBracket, BracketFight


def bracket_show_ffa(request, pk):
    bracket = get_object_or_404(Bracket, pk)
    return render(request, "bracket/show_ffa.html", {"bracket": bracket, "activity": bracket.activity})


def bracket_show_simple_tree(request, pk):
    pass


def bracket_show_double_tree(request, pk):
    pass


def bracket_create_ffa(request, activity_pk):
    activity = get_object_or_404(Activity, activity_pk)
    
    if request.method == "POST":
        form = FFABracketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.activity = activity
            instance.save()
    else:
        form = FFABracketForm()

    return render(request, "bracket/create_ffa.html", {"form": form, "activity": activity})


def bracket_create_simple_tree(request, activity_pk):
    pass


def bracket_create_double_tree(request, activity_pk):
    pass


def bracket_delete(request, pk):
    bracket = get_object_or_404(Bracket, pk)
    back_url = reverse("activity_show", args=[bracket.activity.pk])
    
    if request.method == "POST":
        bracket.delete()
        redirect(back_url)
    
    return render(request, "bracket/delete.html", {"activity": bracket.activity})

