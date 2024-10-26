from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('matches/', views.matches, name='matches'),
    path('seasons/', views.seasons, name='seasons'),
    path('about/', views.about, name='about'),
]
