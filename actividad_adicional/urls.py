from django.urls import path 
#from django.contrib.auth import views as auth_views
from . import views

#app_name = 'skills'

urlpatterns = [
    path('actividad_adicional/', views.ActividadAdicionalView.as_view(), name='actividad_adicional'),
]