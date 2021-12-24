from django import forms
from django.db.models import fields
from .models import *

class WoodSalesForms(forms.ModelForm):
    class Meta:
        model = WoodSale
        fields = ("log", "quantity",)
