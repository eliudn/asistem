from django.db import models
from users import models as users
from locality import models as geo
# Create your models here.
jornadas = ['AM','PM']
class grupos (models.Model):

    #
    name        = models.CharField(max_length=20)
    matriculado = models.IntegerField()
    jornadas    = models.CharField(max_length=2, choices=jornadas)
    sede        = models.ForeignKey(geo.sede, on_delete=models.PROTECT)
    user        = models.ForeignKey(users.data_users, on_delete=models.PROTECT) 

class sesiones(models.Model):

    pass

class seguimiento(models.Model):

    pass
    