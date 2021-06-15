from django import views
from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  
    path('',views.HomeView,name='home1'),
   
    

    
]