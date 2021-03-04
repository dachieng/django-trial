from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html", {"name":"Dorcas"})

def add(request):
    num1 = int(request.GET["num1"])
    num2 = int(request.GET["num2"])
    result = num1 + num2 


    return render(request, "add.html", {"result", result})
