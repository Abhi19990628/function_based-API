from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    fathername=models.CharField(max_length=50)
    mothername=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    