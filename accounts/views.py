from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

@login_required
def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST, files=request.FILES)
        profile_form = StaffForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.username = user.first_name + str(random.randint(0, 1000))
            user.password = "something.random_here"
            user.password2 = "something.random_here"
            user.save()
            profile.user = user
            profile.save()

            messages.success(request, 'user created')
            return redirect("/staff/list/")
        else:
            messages.warning(request, "invalid data entry")

    else:
        user_form = UserForm()
        profile_form = StaffForm()

    return render(request, 'registration/register.html', 
        {
        "user_form": user_form,
        "profile_form" : profile_form
        })
            
@login_required
def staff_list (request):
    staff_list = Staff.objects.all()
    paginator = Paginator(staff_list, 20)
    page = request.GET.get('page')
    paged_staff = paginator.get_page(page)
    context = {
        "staff_list": staff_list
    }
    return render(request, "lists/staff_list.html", context)

def delete_staff(request, id):
    staff = get_object_or_404(User, id=id)
    staff.delete()
    return redirect("/staff/list/")


@login_required
def edit_staff(request, pk):
    userform = get_object_or_404(User, pk=pk)
    userprofileform = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        user_form = UserForm(data=request.POST, files=request.FILES, instance = userform)
        profile_form = StaffForm(data=request.POST, files=request.FILES, instance = userprofileform)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.username = user.first_name + str(random.randint(0, 1000))
            user.password = "something.random_here"
            user.password2 = "something.random_here"
            user.save()
            profile.user = user
            profile.save()

            messages.success(request, 'user created')
            return redirect("/staff/list/")
        else:
            messages.warning(request, "invalid data entry")

    else:
        user_form = UserForm(instance = userform)
        profile_form = StaffForm(isntance = userprofileform)

    return render(request, 'registration/register.html', 
        {
        "user_form": user_form,
        "profile_form" : profile_form
        })
           
    

def staff_detail(request, id):
    user = get_object_or_404(User, id = id)

    return render(request, "staff_detail.html",
    {
        "user": user,
        #"staff": staff,
    })