from django import forms
from django.db.models import fields
from .models import *

class WoodSalesForms(forms.ModelForm):
    class Meta:
        model = WoodSale
        fields = ("log", "quantity",)

class SalaryForms(forms.ModelForm):
    class Meta: 
        model = Salary
        fields = ("staff", "amount_paid",)

class GeneralExpenseForms(forms.ModelForm):
    class Meta: 
        model = GeneralExpence
        fields = ("description", "amount",)
class MachineWorkForms(forms.ModelForm):
    class Meta: 
        model = MachineWork
        fields = ("machine_work_type", "description", "amount",)


class WoodFromBushForms(forms.ModelForm):
    class Meta: 
        model = WoodFromBush
        fields = ("operator", "woodtype", "quantity", "price", "processed", )