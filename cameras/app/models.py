from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Operator(AbstractUser):
    access = models.BooleanField(null=True)


class Camera(models.Model):
    ip = models.TextField(max_length=16)
    port_onvife = models.TextField(max_length=16)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=1000)

class Precet(models.Model):
    number = models.IntegerField()
    id_camera = models.ForeignKey(Camera,on_delete=models.CASCADE)
    preset = models.TextField(max_length=10000)


# class UV_camera(models.Model):
#     state = models.BooleanField(null=True)
#     com = models.IntegerField()
#     reg = models.IntegerField()
#     slaveaddress = models.IntegerField()
#     url = models.TextField(max_length=300)



# РЛС

# AIS

# SOUND

# UV

# MEDIA_SEVER




