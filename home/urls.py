
from django.contrib import admin
from django.urls import path
import os
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
]
