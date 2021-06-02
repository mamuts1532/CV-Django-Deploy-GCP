from django.shortcuts import render
from actividad_adicional.models import AcvidadAdicionalModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class ActividadAdicionalView(TemplateView):

    model = AcvidadAdicionalModel
    context_object_name = 'actividadadicional'
    template_name = 'actividad_adicional/actividad_adicional.html'

    def get_context_data(self, **kwargs):
        context = super(ActividadAdicionalView, self).get_context_data(**kwargs)
        context['Actividad'] = AcvidadAdicionalModel.objects.all()
        return context