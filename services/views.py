
from django.core import paginator
from django.db.models.fields import files
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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

def delete_salary(request, id):
    salary = get_object_or_404(Salary, id = id)
    salary.delete()
    return redirect ("/salary/list")
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

def delete_exepenses_view(request, id):
    expenses = get_object_or_404(GeneralExpence, id=id)
    expenses.delete()
    return redirect("/generalexpenses/list/")

@login_required
def general_expenses_list(request):
    generalexpenses = GeneralExpence.objects.all()

    #search  functionality
    date_recorded = request.GET.get('date_recorded')

    if date_recorded is not '' and date_recorded is not None:
        generalexpenses = generalexpenses.filter(date_recorded__icontains = date_recorded)
        total_expenses = generalexpenses.aggregate(Total = Sum('amount'))
    else: 
        total_expenses = generalexpenses.aggregate(Total = Sum('amount'))
        date_recorded = "Every Date"


    paginator = Paginator(generalexpenses, 20)
    page = request.GET.get('page')
    paged_general_expenses = paginator.get_page(page)
    context = {
        
        "generalexpenses": paged_general_expenses,
        "total_expenses" : total_expenses,
        "date_recorded": date_recorded
    }
    return render(request, "lists/general_expenses_list.html", context)
    
def machinework(request): 
    if request.method == "POST":
        form = MachineWorkForms (data= request.POST, files=request.FILES)
        if form.is_valid ():
            form.save()
            messages.success(request, "Machine Work added")
            return redirect("/machinework/add")
        else:
            messages.warning(request, "Form data error, check and try again")
    else: 
        form = MachineWorkForms()
    return render (request, "post/machineworkforms.html", {"form" : form})
  
@login_required
def machine_work_list(request):
    machine_works = MachineWork.objects.all()

     #search codes
    work_date = request.GET.get('work_date')
    if work_date is not '' and work_date is not None:
        machine_works = machine_works.filter(date_recorded__icontains = work_date)
        machine_works_total = machine_works.aggregate(Total = Sum('amount',))
    else:
        machine_works_total = MachineWork.objects.aggregate(Total = Sum('amount',))  
    
    paginator = Paginator(machine_works, 20)
    page = request.GET.get('page')
    paged_machine_work = paginator.get_page(page)
    context = {
        "machine_works": paged_machine_work,
        "machine_works_total": machine_works_total,
        "work_date": work_date,
    }
    return render(request, "lists/machine_work_list.html", context)
def delete_machine_work(request, id):
    machine_work = get_object_or_404(MachineWork, id = id)
    machine_work.delete()
    return redirect("/machinework/list")


@login_required
def woodfrombush (request): 
    if request.method == "POST":
        form = WoodFromBushForms(data= request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Wood from Bush Saved Successfully")
            return redirect("/woodfrombush/add")
        else: 
            messages.warning(request, "Form data Error, check and try again")
    else: 
        form = WoodFromBushForms()
    return render (request, "post/woodfrombushform.html", {"form" : form})

@login_required
def wood_from_bush_list(request):
    wood_from_bushs = WoodFromBush.objects.all()

    #search codes
    work_date = request.GET.get('work_date')
    if work_date is not '' and work_date != None:
        wood_from_bushs = wood_from_bushs.filter(date_purchased__icontains = work_date)
        wood_from_bushs_total = wood_from_bushs.aggregate(Total = Sum('price'))
    else: 
        wood_from_bushs_total = wood_from_bushs.aggregate (Total = Sum('price'))

    paginator = Paginator(wood_from_bushs, 20)
    page = request.GET.get('page')
    paged_wood_from_bush = paginator.get_page(page)
    context = {
        "woodfrombushs": paged_wood_from_bush,
        "wood_from_bushs_total":wood_from_bushs_total
    }
    return render(request, "lists/wood_from_bush_list.html", context)

def delete_wood_from_bush(request, id):
    bushwood = get_object_or_404( WoodFromBush, id =id)
    bushwood.delete()
    return redirect("/woodfrombush/list/")


@login_required
def operator(request):
    if request.method == "POST":
        form = OperatorForms(data= request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Operator saved successfully")
            return redirect("/operator/add")
        else:
            messages.warning (request, "Form data error, Check and try again")
    else:
        form = OperatorForms()
    return render (request, "post/operatorform.html", {"form" : form})

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
def delete_operator(request, id):
    operator = get_object_or_404( Operator, id =id)
    operator.delete()
    return redirect("/operator/list/")

@login_required
def furniture_inventory(request):
    if request.method == "POST":
        form = FurnitureInventoryForms(data= request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Furniture Recorded")
            return redirect("/furniture/list/")
        else:
            messages.warning(request, "Form data error, check and try aagain")
    else: 
        form = FurnitureInventoryForms()
    return render (request, "post/furnitureinventoryform.html", { "form" : form})

@login_required
def furniture_list (request):
    total_expenses = 0
    furniture_list = FurnitureInventory.objects.all()
 #search codes
    item_name = request.GET.get('item_name')
    if item_name is not '' and item_name is not None:
        furniture_list = furniture_list.filter(item_name__icontains = item_name)
   
    for i in furniture_list:
        total_expenses = i.unit_expenses_on_work * i.quantity
    
    paginator = Paginator(furniture_list, 20)

    page = request.GET.get('page')
    paged_furniture = paginator.get_page(page)
    context = {
        "furniture_list": paged_furniture,
        "total_expenses": total_expenses
    }
    return render(request, "lists/funiture_inventory_list.html", context)

def delete_furniture_view(request, id):
    furniture_inventory = get_object_or_404( FurnitureInventory, id =id)
    furniture_inventory.delete()
    return redirect("/furniture/list/")