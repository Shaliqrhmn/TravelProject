from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Places, Team


# Create your views here.
def index(request):
    obj = Places.objects.all()
    obj_team = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team_obj': obj_team})

