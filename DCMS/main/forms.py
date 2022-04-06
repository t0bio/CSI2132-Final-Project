from cProfile import label
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django import forms

from .models import User

class RegisterUser(forms.Form):
    first_name = forms.CharField(label="First Name", max_length = 50)
    middle_name = forms.CharField(label="Middle Name", max_length = 50)
    last_name = forms.CharField(label = "Last Name", max_length=50)
    street_number = forms.IntegerField(label = "Street Number")
    street_name = forms.CharField(label = "Street Name", max_length=50)
    house_number = forms.IntegerField()
    city = forms.CharField(label = "City", max_length=50)
    province = forms.CharField(label="Province", max_length=50)
    ssn = forms.CharField(label="SSN", max_length=50)
    gender = forms.CharField(label="Gender", max_length=25)
    email_address = forms.EmailField()
    date_of_birth = forms.DateField()

class RegisterPatient(forms.Form):
    patient_id = forms.IntegerField(label= "Patient ID")
    insurance = forms.IntegerField(label = "Insurance Number")
    health_card_num = forms.IntegerField(label = "Health Card Number")
    user = forms.ModelChoiceField(queryset= User.objects.all())

class RegisterEmployee(forms.Form):
    employee_id = forms.IntegerField(label = "Employee ID")
    employee_type = forms.CharField(label = "Employee Type", max_length=50)
    salary = forms.IntegerField()
    user = forms.ModelChoiceField(queryset= User.objects.all())

    