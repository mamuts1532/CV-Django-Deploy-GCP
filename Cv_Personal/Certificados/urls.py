from django.urls import path 
#from django.contrib.auth import views as auth_views
from . import views

#app_name = 'skills'

urlpatterns = [
    path('certificados/', views.CertificadosView.as_view(), name='certificados'),
]