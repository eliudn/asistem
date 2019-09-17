from django.db import models

# Create your models here.
class departamento(models.Model):
    cod  = models.CharField(max_length= 4, unique=True)
    name = models.CharField(max_length=40)

class municipio(models.Model):
    cod       = models.CharField(max_length=6, unique=True)
    name      = models.CharField(max_length=50)
    id_depart = models.ForeignKey(departamento, on_delete=models.CASCADE)