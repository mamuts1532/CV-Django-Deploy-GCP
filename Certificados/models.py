from django.db import models

# Create your models here.

class CertificadosModel(models.Model):

    formacion = models.CharField(max_length=50)
    instituto = models.CharField(max_length=100)
    mes_final = models.CharField(max_length=50)
    ahno_final = models.PositiveIntegerField()
    url_certificado = models.URLField(max_length=200)

    class Meta:
       ordering = ['-ahno_final']