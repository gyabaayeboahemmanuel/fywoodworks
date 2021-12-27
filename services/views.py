
from django.core import paginator
from django.db.models.fields import files
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def woodwork(request):
    return render(request, 'woodwork.html')

@login_required
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
            return redirect("/sales/wood")
        else:
            messages.warning(request, "form data error, please try again")
    else:
        form = WoodSalesForms()
    
    return render(request, "post/woodsalesforms.html", {"form":form})

@login_required
def salary(request):
    if request.method == "POST":
        form = SalaryForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            #salaryforms = form.save(commit=False)
            form.save()
            messages.success(request, "Payment Complete")
            return redirect("/salary/pay")
        else: 
            messages.warning(request, "form data error, please try again")
    else:
        form =SalaryForms()
    return render (request, "post/paysalaryform.html", {"form":form})

@login_required
def salary_list(request):
    salarys = Salary.objects.all()

    paginator = Paginator(salarys, 20)
    page = request.GET.get('page')
    paged_salarys = paginator.get_page(page)
    context = {
        "salarys": paged_salarys
    }
    return render(request, "lists/salary_list.html", context) 

@login_required
def generalexpense(request):
    if request.method == "POST":
        form = GeneralExpenseForms(data= request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Expenses Recorded")
            return redirect("/generalexpenses/add")
        else:
            messages.warning(request, "Form data error, check and try aagain")
    else: 
        form = GeneralExpenseForms()
    return render (request, "post/generalexpensesforms.html", { "form" : form})

@login_required
def general_expenses_list(request):
    generalexpenses = GeneralExpence.objects.all()

    paginator = Paginator(generalexpenses, 20)
    page = request.GET.get('page')
    paged_general_expenses = paginator.get_page(page)
    context = {
        "generalexpenses": paged_general_expenses
    }
    return render(request, "lists/general_expenses_list.html", context)
    
@login_required
def machinework(request): 
    if request.method == "POST":
        form = MachineWorkForms (data= request.POST, files=request.FILES)
        if form.is_valid ():
            form.save()
            messages.success(request, "Machine Work added")
            return redirect("machinework/add")
        else:
            messages.warning(request, "Form data error, check and try again")
    else: 
        form = MachineWorkForms()
    return render (request, "post/machineworkforms.html", {"form" : form})

@login_required
def machine_work_list(request):
    machine_works = MachineWork.objects.all()

    paginator = Paginator(machine_works, 20)
    page = request.GET.get('page')
    paged_machine_work = paginator.get_page(page)
    context = {
        "machine_works": paged_machine_work
    }
    return render(request, "lists/machine_work_list.html", context)



@login_required
def woodfrombush (request): 
    if request.method == "POST":
        form = WoodFromBushForms(data= request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Wood from Bush Saved Successfully")
            return redirect("woodfrombush/add")
        else: 
            messages.warning(request, "Form data Error, check and try again")
    else: 
        form = WoodFromBushForms()
    return render (request, "post/woodfrombushform.html", {"form" : form})

@login_required
def wood_from_bush_list(request):
    wood_from_bushs = WoodFromBush.objects.all()
    paginator = Paginator(wood_from_bushs, 20)
    page = request.GET.get('page')
    paged_wood_from_bush = paginator.get_page(page)
    context = {
        "woodfrombushs": paged_wood_from_bush
    }
    return render(request, "lists/wood_from_bush_list.html", context)

@login_required
def operator(request):
    if request.method == "POST":
        form = Operator(data= request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Operator saved successfully")
            return redirect("operator/add")
        else:
            messages.warning (request, "Form data error, Check and try again")
    else:
         form = Operator()
    return render(request, "post/operatorform.html", {"form" : form})

@login_required
def operator_list (request):
    operator_list = Operator.objects.all()
    paginator = Paginator(operator_list, 20)
    page = request.GET.get('page')
    paged_operator = paginator.get_page(page)
    context = {
        "operator_list": paged_operator
    }
    return render(request, "lists/operator_list.html", context)