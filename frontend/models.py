from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://docs.djangoproject.com/en/5.0/topics/db/examples/one_to_one/
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username