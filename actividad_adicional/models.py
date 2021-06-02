from django.db import models

# Create your models here.

class AcvidadAdicionalModel(models.Model):

    actividad = models.CharField(max_length=1000)
