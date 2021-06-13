from django.db import models
from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import  render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import  redirect
from .models import *
from recruiter.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User=get_user_model()

def HomeView(request):
    jobs=Job.objects.all()
    context={
        'query':jobs
    }
    return render(request,'applicant/home.html',context)

@login_required
def applied_jobs(request):
    user=request.user
    job=AppliedJobs.objects.filter(user=user)
    context={
        'jobs':job
    }
    print(job)
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

def search(request):
    query=request.GET.get('search')
    list=[]
    job_type=Job.objects.filter(job_type__icontains=query)
    company_name=Job.objects.filter(company_name__icontains=query)
    for i in job_type:
        list.append(i)
    for i in company_name:
        list.append(i)
    return render(request,'applicant/search.html',{'list':list})
    
    
    
    
    

    
    



    
    


