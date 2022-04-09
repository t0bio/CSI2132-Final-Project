from django.contrib import admin
from .models import Person,Employee,Patient,Appointment, Appointment_Procedure, Patient_record, Treatment

#Review,  Patient_billing, Patient_record, Fee_Charge, Insurance_claim, Invoice

# Register your models here.
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Appointment_Procedure)
admin.site.register(Patient_record)


#admin.site.register(Review)
admin.site.register(Treatment)
#admin.site.register(Patient_billing)

#admin.site.register(Fee_Charge)
#admin.site.register(Insurance_claim)
#admin.site.register(Invoice)