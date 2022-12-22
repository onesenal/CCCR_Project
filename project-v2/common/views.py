from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from .models import Country
from django.http import HttpResponse

def index(request):

    return render(request, 'common/base.html')

def getContinental(request):
    path = request.path
    str = path[8:len(path)-1]
    
    nation_list = Country.objects.filter(continame=str).order_by('kname')
    context = {'nation_list':nation_list}
    
    return render(request, 'common/continental.html', context)

def getNation(request, nation_name, continame):
    
    nation_list = Country.objects.filter(name=nation_name)
    context = {'nation_list':nation_list}
    
    return render(request, 'common/nation.html', context)

