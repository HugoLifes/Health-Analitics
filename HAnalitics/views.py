from django.shortcuts import render
from django.http import HttpResponse   # added

def home(request):
    return render(request, 'home.html')
def main(request):
    return render(request, 'data/main.html')
def user_info(request):
    return render(request, 'data/user_info.html')