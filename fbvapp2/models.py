from django.db import models


class Schools(models.Model):
    name=models.CharField(max_length=50)
    teacher=models.CharField(max_length=40)
    subject=models.CharField(max_length=20)
