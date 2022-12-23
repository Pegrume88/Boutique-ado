

from django.urls import path
import os
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    
]
