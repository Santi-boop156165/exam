from django.db import models

# Create your models here.
class Exam(models.Model):
    name=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    regional=models.CharField(max_length=100)
