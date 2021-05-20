from django.db import models

# Create your models here.

class FormAcadModel(models.Model):

    formacion = models.CharField(max_length=50)
    instituto = models.CharField(max_length=100)
    fecha_inicio = models.PositiveIntegerField()
    fecha_final = models.PositiveIntegerField()

    class Meta:
       ordering = ['-fecha_final']
