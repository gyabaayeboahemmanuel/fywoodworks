
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, response, Http404
from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'index.html')

def woodwork(request):
    return render(request, 'woodwork.html')

    
