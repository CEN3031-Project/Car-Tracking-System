from django.contrib import admin
from .models import ClientAccount, Car, Reservation, EmployeeAccount, AdminAccount, RentalLocation
from .forms import ClientAccountForm

# Register all models into the admin site
admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(EmployeeAccount)
admin.site.register(AdminAccount)
admin.site.register(RentalLocation)

# Use the client custom form into the admin site to ensure there is an email field
class ClientAccountAdmin(admin.ModelAdmin):
    form = ClientAccountForm
    list_display = ['user', 'get_email']

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email Address'
admin.site.register(ClientAccount, ClientAccountAdmin)
