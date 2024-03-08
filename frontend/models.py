from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://docs.djangoproject.com/en/5.0/topics/db/examples/one_to_one/
class ClientAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

      
class Car(models.Model):
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    mileage = models.PositiveIntegerField()
    cost_per_day = models.FloatField()
    cost_per_mile = models.FloatField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.model


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientAccount, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField()
    car = models.ManyToManyField(Car)

    def __str__(self):
        return self.client + ' ' + self.car

      
class EmployeeAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class AdminAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class RentalLocation(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE)
    admin = models.ForeignKey(AdminAccount, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
