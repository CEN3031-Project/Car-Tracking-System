from django.contrib import admin
from .models import ClientAccount, Car, Reservation, EmployeeAccount, AdminAccount, RentalLocation
from .forms import ClientAccountForm, CarForm

# Register all models into the admin site
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


# Use the car custom form to attach locations and only allow associated employees to view
class CarAdmin(admin.ModelAdmin):
    form = CarForm

    # Get the queryset of car objects
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # If user is an admin, can view all cars
        if request.user.is_superuser:
            return qs

        # If user is an employee, can only view cars at their location
        employee = EmployeeAccount.objects.filter(username=request.user.username).first()
        if employee and employee.location:
            return qs.filter(location=employee.location)
        return qs.none()

    # Citation: https://code.djangoproject.com/ticket/27231
    # Get the default form class from the superclass and return the current user
    def get_form(self, request, obj=None, **kwargs):
        Form = super().get_form(request, obj, **kwargs)
        return type('CarFormWrapper', (Form,), {'user': request.user})

    # Save object and ensure employees can only create or modify cars within their location
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            employee = EmployeeAccount.objects.filter(username=request.user.username).first()
            if employee and employee.location:
                obj.location = employee.location
        obj.save()

admin.site.register(Car, CarAdmin)
