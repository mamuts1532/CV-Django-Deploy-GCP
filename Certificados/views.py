from django.shortcuts import render
from Certificados.models import CertificadosModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class CertificadosView(ListView):
    model = CertificadosModel
    context_object_name = 'certificadosview'
    template_name = 'Certificados/certificados.html'
