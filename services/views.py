
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def woodwork(request):
    return render(request, 'woodwork.html')

def woodsales(request):
    if request.method == "POST":
        form = WoodSalesForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            woodsalesforms = form.save(commit=False)
            purchase_quantity = form.cleaned_data["quantity"]
            woodsalesforms.log.quantity = woodsalesforms.log.quantity - purchase_quantity
            woodsalesforms.total_price = purchase_quantity * woodsalesforms.log.unit_price
            woodsalesforms.save()
            woodsalesforms.log.save()
            messages.success(request, "Sales Complete")
        else:
            messages.warning(request, "form data error, please try again")
    else:
        form = WoodSalesForms()
    
    return render(request, "post/woodsalesforms.html", {"form":form})

        
    
