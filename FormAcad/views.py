from django.shortcuts import render
from FormAcad.models import FormAcadModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class FormAcadView(ListView):
    model = FormAcadModel
    context_object_name = 'formacadview'
    template_name = 'FormAcad/form_acad.html'