from gzip import READ
from site import USER_BASE
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Patient, User
from .forms import RegisterUser, RegisterPatient, RegisterEmployee

def index(response):
    return render(response, "main/home.html", {})

def employee(response):
    return HttpResponse("<h1>Employee Page</h1>")

def receptionist(response):
     return render(response, "main/receptionistUI.html", {})

def patient(response):
    return HttpResponse("<h1>Patient Page</h1>")

def searchUser(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_user = User.objects.filter(last_name__contains = searched)
        return render(request, "main/search_user.html", {'searched':searched, 'searched_user':searched_user})
    
    else:
        return render(request, "main/search_user.html", {})


def registerEmployee(response):
    if response.method == "POST":
        form = RegisterEmployee(response.POST)

        if form.is_valid():
            empId = form.cleaned_data["employee_id"]
            empType = form.cleaned_data["employee_type"]
            sal = form.cleaned_data["salary"]
            userInfo = form.cleaned_data["user"]

            e = Employee(employee_id = empId, employee_type = empType, salary = sal, user=userInfo)
            e.save()
    else:
        form = RegisterEmployee()
    
    return render(response, "main/registerEmployee.html", {"form":form})


def registerPatient(response):
    if response.method == "POST":
        form = RegisterPatient(response.POST)
    
        if form.is_valid():
            id = form.cleaned_data["patient_id"]
            insur = form.cleaned_data["insurance"]
            hcn = form.cleaned_data["health_card_num"]
            userInfo = form.cleaned_data["user"]

            p = Patient(patient_id = id, insurance = insur, health_card_no = hcn, user = userInfo)
            p.save()
    else:
        form = RegisterPatient()
    return render(response, "main/registerPatient.html", {"form":form})


def register(response):
    if response.method == "POST":
        form = RegisterUser(response.POST)

        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            mn = form.cleaned_data["middle_name"]
            ln = form.cleaned_data["last_name"]
            snum = form.cleaned_data["street_number"]
            sna = form.cleaned_data["street_name"]
            hnum = form.cleaned_data["house_number"]
            c = form.cleaned_data["city"]
            p = form.cleaned_data["province"]
            ssn = form.cleaned_data["ssn"]
            g = form.cleaned_data["gender"]
            ea = form.cleaned_data["email_address"]
            dob = form.cleaned_data["date_of_birth"]

            u = User(first_name = fn, middle_name = mn,  last_name = ln, 
                street_number = snum, street_name = sna, 
                house_number = hnum, city =c, province = p, 
                ssn = ssn, gender = g, email_address = ea, date_of_birth = dob)

            u.save() #Save onto Database

    else:
        form = RegisterUser()
    
    return render(response, "main/registerUser.html", {"form":form})


            
