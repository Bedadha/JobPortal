from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
   path('applicant', applicant_register.as_view(), name = 'applicant'),
   path('recruiter', recruiter_register.as_view(), name = 'recruiter'),
   path('login', LoginView.as_view(), name = 'login'),
   path('logout',views.logout,name='logout'),

]