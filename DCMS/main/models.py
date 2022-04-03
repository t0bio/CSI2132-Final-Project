from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=50)
    house_number = models.IntegerField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    ssn = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    email_address = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    
class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    insurance = models.IntegerField()
    health_card_no = models.IntegerField()
    user_id = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))

class Appointment_Procedure(models.Model):
    procedure_id = models.IntegerField(primary_key=True,null=False)
    appointment_id = models.IntegerField()
    procedure_date = models.DateTimeField()
    invoice_id = models.IntegerField()
    procedure_code = models.IntegerField()
    procedure_type = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    tooth_involved = models.CharField(max_length=500)
    amount_of_procedure = models.IntegerField()
    patient_charge = models.IntegerField()
    insurance_charge = models.IntegerField()
    total_charge = models.IntegerField()
    bill_id = models.IntegerField()
    appointment_id = models.IntegerField(models.ForeignKey(Appointment, on_delete=models.CASCADE))

    
    