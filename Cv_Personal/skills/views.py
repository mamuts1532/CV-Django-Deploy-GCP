from django.shortcuts import render
from skills.models import SkillsModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class Test_Skills(ListView):
    model = SkillsModel
    context_object_name = 'skillview'
    template_name = 'skills/habilidades.html'
    queryset = SkillsModel.objects.order_by('-measure')


# class SkillsListView(ListView):
#     model = SkillsModel
#     context_object_name = 'skillview'

