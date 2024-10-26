from django.shortcuts import render
from .models import Games
from .databse import DataBase

# Create your views here.
def main(request):
    db = DataBase()
    return render(request, 'main/main.html', {'games':games})