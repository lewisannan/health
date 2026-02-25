from django.contrib import admin
from healthapp.models import Patient,Myappointment
#also you can import using an asterisk(*)
#from healthapp.models import *


# Register your models here.

admin.site.register(Patient)
admin.site.register(Myappointment)