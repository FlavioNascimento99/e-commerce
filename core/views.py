from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def home_api(request):
    return JsonResponse({"message": "Django is ON! 🚀", "status": "success"})
