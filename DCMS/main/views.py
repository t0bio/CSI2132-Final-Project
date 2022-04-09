from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Appointment, Employee, Patient, Person
from .forms import RegisterUser, RegisterPatient, RegisterEmployee, SetAppointment
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users


def index(response):
    return render(response, "main/home.html", {})

@login_required
@allowed_users(allowed_roles=['employee'])
def employee(response):
    return render(response, "main/employee.html", {})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def receptionist(response):
     return render(response, "main/receptionistUI.html", {})

@login_required
@allowed_users(allowed_roles=['patient'])
def patient(response):
     return render(response, "main/patientUI.html", {})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def searchUser(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_user = Person.objects.filter(last_name__contains = searched)
        return render(request, "main/search_user.html", {'searched':searched, 'searched_user':searched_user})
    
    else:
        return render(request, "main/search_user.html", {})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def registerEmployee(response):
    if response.method == "POST":
        form = RegisterEmployee(response.POST)

        if form.is_valid():
            empId = form.cleaned_data["employee_id"]
            empType = form.cleaned_data["employee_type"]
            sal = form.cleaned_data["salary"]
            userInfo = form.cleaned_data["person"]

            e = Employee(employee_id = empId, employee_type = empType, salary = sal, person=userInfo)
            e.save()
    else:
        form = RegisterEmployee()
    
    return render(response, "main/registerEmployee.html", {"form":form})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def registerPatient(response):
    if response.method == "POST":
        form = RegisterPatient(response.POST)
    
        if form.is_valid():
            id = form.cleaned_data["patient_id"]
            insur = form.cleaned_data["insurance"]
            hcn = form.cleaned_data["health_card_no"]
            userInfo = form.cleaned_data["person"]

            p = Patient(patient_id = id, insurance = insur, health_card_no = hcn, person = userInfo)
            p.save()
    else:
        form = RegisterPatient()
    return render(response, "main/registerPatient.html", {"form":form})

@login_required
@allowed_users(allowed_roles=['receptionist'])
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

            u = Person(first_name = fn, middle_name = mn,  last_name = ln, 
                street_number = snum, street_name = sna, 
                house_number = hnum, city =c, province = p, 
                ssn = ssn, gender = g, email_address = ea, date_of_birth = dob)

            u.save() #Save onto Database

    else:
        form = RegisterUser()
    
    return render(response, "main/registerUser.html", {"form":form})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def show_user(request, person_id):
    user = Person.objects.get(pk=person_id)
    return render(request, "main/show_user.html", {"user":user})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def update_user(request, person_id):
    user = Person.objects.get(pk=person_id)
    form = RegisterUser(request.POST or None, instance=user )

    if form.is_valid():
        form.save()
        return redirect('receptionist')
    return render(request, "main/update_user.html", {"user":user, "form":form})

@login_required
@allowed_users(allowed_roles=['receptionist'])
def set_appointment(request):
    if request.method == "POST":
        form = SetAppointment(request.POST)

        if form.is_valid():
            app_id = form.cleaned_data["appointment_id"]
            st = form.cleaned_data["starttime"]
            app_date = form.cleaned_data["appointment_date"]
            et = form.cleaned_data["endtime"]
            app_type = form.cleaned_data["appointment_type"]
            s = form.cleaned_data["status"]
            ra = form.cleaned_data["room_assigned"]
            em = form.cleaned_data["employee"]
            pat = form.cleaned_data["patient"]


            app = Appointment(appointment_id = app_id, starttime = st,  appointment_date = app_date, 
                endtime = et, appointment_type = app_type, 
                status = s, room_assigned =ra, employee = em, 
                patient = pat)

            app.save()

    else:
        form = SetAppointment()

    return render(request, "main/set_appointment.html", {"form":form})




            
