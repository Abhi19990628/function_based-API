from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=50)
    auther=models.CharField(max_length=40)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    duration=models.FloatField()
