from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    summary = models.CharField(max_length=2000)
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    previous_work=models.CharField(max_length=2000)
    skills=models.CharField(max_length=2000)
