from pyexpat import model
from unittest.util import _MAX_LENGTH
from django import forms

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
    email_address = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()