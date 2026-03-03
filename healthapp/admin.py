from django.contrib import admin
from healthapp.models import *
#also you can import using an asterisk(*)
#from healthapp.models import *


# Register your models here.

admin.site.register(Patient)
admin.site.register(Myappointment)
admin.site.register(Transaction)