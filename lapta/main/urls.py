from django.urls import path
from .views import main

urlpatterns = [
    path('', views.main, name='main'),
]
