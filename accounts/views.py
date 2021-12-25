from django.core.checks import messages
from django.shortcuts import render
from .forms import *
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
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
            
