from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    edept=models.CharField(max_length=50)