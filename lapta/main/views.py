from django.shortcuts import render
from .models import Games
from .databse import DataBase

# Create your views here.
def home(request):
    db = DataBase()
    return render(request, 'main/home.html')

def teams(request):
    db = DataBase()
    return render(request, 'main/teams.html')

def matches(request):
    db = DataBase()
    return render(request, 'main/matches.html')

def seasons(request):
    db = DataBase()
    return render(request, 'main/seasons.html')

def about(request):
    db = DataBase()
    return render(request, 'main/about.html')