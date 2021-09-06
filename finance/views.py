from finance.models import MachineWork
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, response, Http404
from django.template import loader
# Create your views here.
def machinework(request):
    # machin = get_object_or_404(Question, pk = question_id)
    return render('finance/machinework',)