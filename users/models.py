from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email= models.EmailField(max_length=127, unique=True)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True)

