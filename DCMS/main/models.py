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


    
    