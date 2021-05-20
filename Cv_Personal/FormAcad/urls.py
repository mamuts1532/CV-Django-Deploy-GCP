from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

#app_name = 'skills'

urlpatterns = [
    path('formacad/', views.FormAcadView.as_view(), name='formacad'),
]