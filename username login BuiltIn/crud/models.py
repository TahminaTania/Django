from django.db import models

# Create your models here.

class user(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=200)



