from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from django.contrib import messages



# Create your views here.


def login(request):
    

    return render(request,'login.html')

def Manager(request):
    return render(request,'index.html')