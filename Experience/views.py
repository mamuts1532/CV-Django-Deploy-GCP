from django.shortcuts import render
from Experience.models import ExperienceModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class ExperienceView(ListView):
    model = ExperienceModel
    context_object_name = 'experienceview'
    template_name = 'Experience/experience.html'
