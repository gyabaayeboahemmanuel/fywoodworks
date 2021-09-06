from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpattens = [
    path('machinework', views.machinework, name='machinework'),
]
