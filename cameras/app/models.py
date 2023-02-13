from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(AbstractUser):
    access = models.BooleanField()


class Operator(AbstractUser):
    access = models.BooleanField()


class Camera(models.Model):
    ip = models.TextField(max_length=16)
    port_onvife = models.TextField(max_length=16)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=1000)