from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Dental Clinic Home Page</h1>")

def employee(response):
    return HttpResponse("<h1>Employee Page</h1>")

def receptionist(response):
    return HttpResponse("<h1>Receptionist Page</h1>")

def patient(response):
    return HttpResponse("<h1>Patient Page</h1>")