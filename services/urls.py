from django.urls import path
from django.urls.resolvers import URLPattern
from services.models import MachineWork, Salary
from . import views
from accounts.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "services"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

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

    path('operator/add/', views.operator, name="operator"),
    path('operator/list/', views.operator_list, name="operator_list"),

    #path('furniture/add/', views.furniture, name="furniture"),
    #path('furniture/list/', views.furniture_list, name="furniture_list"),

    #path('sales/furniture/', views.furniture_sale, name="furniture"),

    path('staff/add/', register, name="register"),
    path('staff/list/', staff_list, name="staff_list"),
]
