from django.db import models


# Create your models here.

class User(models.Model):
    #id = models.IntegerField(primary_key=True)
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


    def __str__(self):
        fullName = self.first_name + " " + self.last_name
        return fullName

    
    
class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    insurance = models.IntegerField()
    health_card_no = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        patientName = self.user.first_name + " " + self.user.last_name
        return patientName
    

    
    

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_type = models.CharField(max_length=50)
    salary = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        employeeName = self.user.first_name + " " + self.user.last_name
        return employeeName
    
    
    

    

class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key = True)
    starttime = models.TimeField()
    appointment_date = models.DateField()
    endtime = models.TimeField()
    appointment_type = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    room_assigned = models.IntegerField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def __str__(self):
        appointmentName = self.patient.user.first_name + " " + self.appointment_type + " with Dentist " + self.employee.user.first_name
        return appointmentName

    

class Appointment_Procedure(models.Model):
    procedure_id = models.IntegerField(primary_key=True,null=False)
    procedure_date = models.DateField()
    invoice_id = models.IntegerField()
    procedure_code = models.IntegerField()
    procedure_type = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    tooth_involved = models.CharField(max_length=500)
    amount_of_procedure = models.IntegerField()
    patient_charge = models.FloatField()
    insurance_charge = models.FloatField()
    total_charge = models.FloatField()
    bill_id = models.IntegerField()
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)


    def __str__(self):
        appointmnetProcedure = self.procedure_type + "with Patient " + self.appointment.patient.user.first_name
        return app

    

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    communication = models.CharField(max_length=500)
    professionalism = models.CharField(max_length=500)
    cleanliness = models.CharField(max_length=500)
    value = models.IntegerField()
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)

    
class Treatment(models.Model):
    treatment_id = models.IntegerField(primary_key=True)
    treatment_type = models.CharField(max_length=20)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)

    def __str__(self):
        treatment = self.treatment_type 
        return treatment


   
class Patient_record(models.Model):
    patient_record_id = models.IntegerField(primary_key=True)
    medication = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    tooth = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    treatment_id = models.ForeignKey('Treatment', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def __str__(self):
        patientRecord = "Patient Record of " + self.patient.user.first_name
        return patientRecord

class Insurance_claim(models.Model):
    claim_id = models.IntegerField(primary_key=True)
    claim_amount = models.FloatField()
    insurance_company = models.CharField(max_length=50)
    
    
   
class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    patient_charge = models.IntegerField()
    insurance_charge = models.FloatField()
    total_fee_charge = models.FloatField()
    discount = models.FloatField()
    penalty = models.FloatField()
    insurance_claim_id = models.ForeignKey('Insurance_claim', on_delete=models.CASCADE)
   
class Patient_billing(models.Model):
     bill_id = models.IntegerField(primary_key=True)
     appointment_id = models.ForeignKey('Appointment', on_delete = models.CASCADE)
     patient_portion = models.FloatField()
     insurance_portion = models.FloatField()
     insurance_claim_id = models.ForeignKey('Insurance_claim', on_delete = models.CASCADE)
     payment_type = models.CharField(max_length = 50)
     total_amount = models.FloatField()
     
class Fee_Charge(models.Model):
    feed_id = models.IntegerField(primary_key=True)
    procedure_id = models.IntegerField()
    fee_code = models.IntegerField()
    charge = models.IntegerField()
    procedure_id = models.ForeignKey('Appointment_Procedure',on_delete=models.CASCADE)
    
    