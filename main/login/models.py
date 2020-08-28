from django.db import models

# Create your models here.

class Login(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=10)
