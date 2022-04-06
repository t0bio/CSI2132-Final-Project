from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import RegisterUser

def index(response):
    return render(response, "main/home.html", {})

def employee(response):
    return HttpResponse("<h1>Employee Page</h1>")

def receptionist(response):
    return HttpResponse("<h1>Receptionist Page</h1>")

def patient(response):
    return HttpResponse("<h1>Patient Page</h1>")

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


            
