from . import views
from django.urls import path, include

path('', views.index, name='index')


