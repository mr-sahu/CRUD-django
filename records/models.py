from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    country=models.CharField(max_length=20,null=True)