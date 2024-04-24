from django.db import models
from django.contrib.auth.models import User


# Citation: https://docs.djangoproject.com/en/5.0/topics/db/examples/one_to_one/
# Create the client account attached to the users list in the database
class ClientAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Create the model for cars, including important fields with key attachments like locations
class Car(models.Model):
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    mileage = models.PositiveIntegerField()
    cost_per_day = models.FloatField()
    cost_per_mile = models.FloatField()
    location = models.ForeignKey('RentalLocation', on_delete=models.CASCADE, related_name='cars')
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to="car_image", blank=True, null=True, default="car_image/default_car_icon.png")

    def __str__(self):
        return self.model


# Create the model for reservations and return the associated client and car selected
class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(ClientAccount, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.client) + ' ' + str(self.car)


# Create the model for employee accounts with fields tn enter their username, pasword, location, etc.
class EmployeeAccount(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.ForeignKey('RentalLocation', on_delete=models.SET_NULL, null=True, blank=True)

    # Return a display of the employee's first and last name
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # Citation: https://docs.djangoproject.com/en/5.0/ref/models/instances/
    # Save account as a Django User model instance so that admins can access permission changes on it
    def save(self, *args, **kwargs):
        if not self.pk:
            # Create a new user object if this is a new employee
            user = User.objects.create_user(
                username=self.username,
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name
            )
        else:
            # Update existing user details if this employee already exists
            user = User.objects.get(username=self.username)
            user.email = self.email
            user.first_name = self.first_name
            user.last_name = self.last_name
            user.set_password(self.password)
            user.save()
        super().save(*args, **kwargs)


# Create the admin model and return their first and last name
class AdminAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


    # Save account as a Django User model instance so that admins can access permission changes on it
    def save(self, *args, **kwargs):
        if not self.pk:
            # Create a new user object if this is a new admin
            user = User.objects.create_user(
                username=self.username,
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name
            )
        else:
            # Update existing user details if this admin already exists
            user = User.objects.get(username=self.username)
            user.email = self.email
            user.first_name = self.first_name
            user.last_name = self.last_name
            user.set_password(self.password)
            user.save()
        super().save(*args, **kwargs)


# Create the rental location model to enter locations and return its name
class RentalLocation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
