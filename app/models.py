from django.db import models

# Create your models here.
class Employee(models.Model):
 fullname=models.CharField(max_length=100)
 emp_code=models.CharField(max_length=10)
 mobile=models.CharField(max_length=10)
 address=models.TextField(max_length=100)
 position=models.CharField(max_length=10)