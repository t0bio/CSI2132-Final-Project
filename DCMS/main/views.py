from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(response, id):
    ls=User.objects.get(id=id)
    return render(response, "main/base.html", {"name":ls.name})

def employee(response):
    return HttpResponse("<h1>Employee Page</h1>")

def receptionist(response):
    return HttpResponse("<h1>Receptionist Page</h1>")

def patient(response):
    return HttpResponse("<h1>Patient Page</h1>")