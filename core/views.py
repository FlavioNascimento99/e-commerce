from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request, 'home.html')

def home_api(request):
    return HttpRequest("Django's ON")