from django.db import models

# se craaran tablas de pruebas 
class tb_principa(models.Model):

    column1 = models.CharField(max_length=20)
    column2 = models.TextField()

class tb_2(models.Model):

    column1 = models.CharField(max_length=12)
    tb_foren = models.ForeignKey(tb_principa, on_delete= models.CASCADE)

class tb_3(models.Model):

    column1 = models.CharField(max_length=12)
    tb_foren = models.ForeignKey(tb_2, on_delete= models.CASCADE)
