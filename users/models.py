from django.db import models
from django.contrib.auth.models import User
# ASISTEM
from locality import models as geo

# Create your models here.
class type_id(models.Model):


    name   = models.CharField(max_length=40)
    detail = models.TextField(blank=True)


class data_users(models.Model):

    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user  = models.CharField(max_length=20, unique=True)
    id_type  = models.ForeignKey(type_id, on_delete = models.PROTECT)
    municipo = models.ForeignKey(geo.municipio, on_delete = models.PROTECT)
