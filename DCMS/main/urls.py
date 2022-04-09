from unicodedata import name
from django.urls import URLPattern, path
from . import views

#Define paths to our different webpages
#URL that defines which view to go to

urlpatterns = [
    #When we are in the homepage, it will render index function in views.py
    path("", views.index, name="index"),
    path("employee/", views.employee, name="employee"),
    path("receptionist/", views.receptionist, name="receptionist"),
    path("patient/", views.patient, name="patient"),
    path("register/", views.register, name="register"),
    path("registerpatient/", views.registerPatient, name = "registerpatient"),
    path("registeremployee/", views.registerEmployee, name = "registeremployee"),
    path("searchuser/", views.searchUser, name = "searchuser"), 
    path('show_user/<person_id>', views.show_user, name="show_user"),
    path('update_user/<person_id>', views.update_user, name="update_user"),
    path('set_appointment', views.set_appointment, name="set_appointment"),
    path('employee', views.employee, name = "employee"),
    path('patientUI', views.patient, name = "patientUI"),
    
]