from django.shortcuts import render
from django.http import HttpResponse   # added

def home(request):
    return render(request, 'home.html')
