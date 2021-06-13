from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('applicant', applicant_register.as_view(), name = 'applicant'),
   path('recruiter', recruiter_register.as_view(), name = 'recruiter'),
   path('login', LoginView.as_view(), name = 'login'),
]