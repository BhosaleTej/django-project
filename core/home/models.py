from django.db import models
from django.contrib.auth.models import User  
# for inbuild models usage.

from django.contrib.auth.models import AbstractUser
# for creating custom models.

from .manager import UserManager

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=400)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name




class customuser(AbstractUser):

    username = None
    phone_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()