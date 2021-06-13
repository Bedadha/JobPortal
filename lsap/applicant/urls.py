from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  
    path('',views.HomeView,name='home'),
    path('applied',views.applied_jobs,name='applied'),
    path('jobdetail/<int:id>',views.details_of_job,name='jobdetail'),
    path('apply/<int:id>',views.apply,name='apply'),
    path('search',views.search,name='search')


    
]