from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

#app_name = 'skills'

urlpatterns = [
    path('formesp/', views.FormEspView.as_view(), name='formesp'),
]