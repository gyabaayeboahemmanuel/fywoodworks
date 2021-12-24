from django.urls import path
from django.urls.resolvers import URLPattern

from services.models import MachineWork, Salary
from . import views

app_name = "services"

urlpatterns = [
    path('', views.index, name='index'),
    path('woodworks/', views.woodwork, name='woodwork'),
    path('sales/wood/', views.woodsales, name="woodsales"),

    path('salary/pay/', views.salary, name = "salary"),
    path('salary/list/', views.salary_list, name = "salary_list"),

    path('generalexpenses/add/', views.generalexpense, name="generalexpenses"),
    path('generalexpenses/list/', views.general_expenses_list, name="general_expenses_list"),

    path('machinework/add/', views.machinework, name="machinework"),
    path('machinework/list/', views.machine_work_list, name="machine_work_list"),

    path('woodfrombush/add/', views.woodfrombush, name="woodfrombush"),
    path('woodfrombush/list/', views.wood_from_bush_list, name="wood_from_bush_list"),
]
