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

    path('salary/pay/', views.salary, name = "salary"),
    path('salary/list/', views.salary_list, name = "salary_list"),
    path('salary/<int:id>/delete/', views.delete_salary, name='delete_salary'),

    path('generalexpenses/add/', views.generalexpense, name="generalexpenses"),
    path('generalexpenses/edit/<int:pk>/', views.edit_expense, name="edit_expense"),
    path('generalexpenses/<int:id>/delete/',  views.delete_exepenses_view, name= "delete_exepenses_view"),
    path('generalexpenses/list/', views.general_expenses_list, name="general_expenses_list"),

    path('machinework/add/', views.machinework, name="machinework"),
    path('machinework/list/', views.machine_work_list, name="machine_work_list"),
    path('machinework/<int:id>/delete/', views.delete_machine_work, name = "delete_machine_work"),

    path('woodfrombush/add/', views.woodfrombush, name="woodfrombush"),
    path('woodfrombush/list/', views.wood_from_bush_list, name="wood_from_bush_list"),
    path('woodfrombush/<int:id>/delete/', views.delete_wood_from_bush, name = "delete_wood_from_bush"),
    path('add-woodpurchase', views.woodsales, name="woodsales"),

    path('operator/add/', views.operator, name="operator"),
    path('operator/list/', views.operator_list, name="operator_list"),
    path('operator/<int:id>/delete/', views.delete_operator, name = "delete_operator"),

    path('furnitureinventory/add/', views.furniture_inventory, name="furniture_inventory"),
    path('furniture/list/', views.furniture_list, name="furniture_list"),
    path('furniture/<int:id>/delete/', views.delete_furniture_view, name = "delete_furniture_view"),
    path('add-purchase/', views.add_furniture_purchase, name="add_furniture_purchase"),
    path('add-supply/', views.add_supply, name="add_supply"),

    path('staff/add/', register, name="register"),
    path('staff/<int:id>/delete/', delete_staff, name="delete_staff"),
    path('staff/<int:id>/detail/', staff_detail, name="staff_detail"),
    path('staff/list/', staff_list, name="staff_list"),

    path('summary/', views.Summary, name="summary")
]
