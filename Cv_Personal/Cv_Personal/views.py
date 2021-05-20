from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class Shesst2_CV(TemplateView):
    template_name = 'formacion_academica.html'

class Shesst3_CV(TemplateView):
    template_name = 'formacion_academica_ce.html'

class Shesst4_CV(TemplateView):
    template_name = 'formacion_academica_ct.html'

class Shesst5_CV(TemplateView):
    template_name = 'experiencia.html'

