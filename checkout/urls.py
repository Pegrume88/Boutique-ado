

from django.urls import path
import os
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    
]
