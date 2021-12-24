from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "services"

urlpatterns = [
    path('', views.index, name='index'),
    path('woodworks/', views.woodwork, name='woodwork'),
    path('sales/wood/', views.woodsales, name="woodsales")
    
]
