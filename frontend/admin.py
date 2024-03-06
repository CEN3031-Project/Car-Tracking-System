from django.contrib import admin
from .models import Car, Reservarion, EmployeeAccount, AdminAccount, RentalLocation

# Register your models here.
admin.site.register(Car)
admin.site.register(Reservarion)
admin.site.register(EmployeeAccount)
admin.site.register(AdminAccount)
admin.site.register(RentalLocation)
