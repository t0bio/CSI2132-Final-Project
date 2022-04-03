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
    procedure_date = models.DateField()
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

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    communication = models.CharField(max_length=500)
    professionalism = models.CharField(max_length=500)
    cleanliness = models.CharField(max_length=500)
    value = models.IntegerField()
    patient_id = models.ForeignKey(Patient)
    
class Treatment(models.Model):
    treatment_id = models.IntegerField(primary_key=True)
    treatment_type = models.CharField(max_length=20)
    appointment_type = models.ForeignKey(Appointment)  
    
class Patient_record(models.Model):
    patient_record_id = models.IntegerField(primary_key=True)
    patient_id = models.ForeignKey(Patient)
    medication = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    tooth = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    treatment_id = models.ForeignKey(Treatment)
  
