from django.shortcuts import render
from FormEsp.models import FormEspModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class FormEspView(ListView):
    model = FormEspModel
    context_object_name = 'formespview'
    template_name = 'FormEsp/form_esp.html'
