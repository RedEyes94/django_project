from django.shortcuts import render
from .models import Roll
# Create your views here.

def tests(request):
    return render(request, 'templates_lists/templates_lists.html')

def rolls(request):
    rolls = Roll.objects.all()
    return render(request, 'templates_lists/tutorial_bootstrap.html',{'rolls':rolls})

def contattaci(request):
    return render(request, 'templates_lists/contattaci.html')

def login(request):
    return render(request, 'gui/home/login.html')