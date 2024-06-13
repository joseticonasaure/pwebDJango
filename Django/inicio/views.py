from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def another(request):
    return render(request, 'another.html')
