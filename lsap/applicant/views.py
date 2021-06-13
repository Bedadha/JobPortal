from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import views
# Create your views here.
from .models import *
from recruiter.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


def HomeView(request):
    jobs=Job.objects.all()
    context={
        'query':jobs
    }
    return render(request,'applicant/home.html',context)


def applied_jobs(request):
    job=AppliedJobs.objects.filter(user=request.user)
    context={
        'jobs':job
    }
    return render(request,'applicant/applied.html',context)

def details_of_job(request,id):
    job=Job.objects.get(pk=id)
    applied=False
    if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
        applied=True
    
    context={
        'job':job,
        'applied':applied
    }   
    return render(request,'applicant/jobdetail.html',context)


def apply(request,id):
    user=request.user
    job=Job.objects.get(pk=id)
    applied=True
    apply=Applicants(job=job,applicant=user)
    add_to_applied=AppliedJobs(user=user,job=job)
    apply.save()
    add_to_applied.save()
    
    return render(request,'applicant/jobdetail.html',{'job':job,'applied':applied})
    
    
    
    

    
    



    
    


