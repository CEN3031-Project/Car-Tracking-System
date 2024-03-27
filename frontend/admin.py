from django.contrib import admin
from .models import ClientAccount, Car, Reservation, EmployeeAccount, AdminAccount, RentalLocation

# Register your models here.
admin.site.register(ClientAccount)
admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(EmployeeAccount)
admin.site.register(AdminAccount)
admin.site.register(RentalLocation)
