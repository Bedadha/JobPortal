from recruiter.forms import JobDetails
import recruiter
from django.shortcuts import render
from .models import *
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
import json
# Create your views here.


def HomeView(request):
    jobs=Job.objects.filter(recruiter=request.user)
    paginator=Paginator(jobs,5)
    page_number  = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        'page_obj':page_obj,
        'jobs':jobs
    }
    return render(request,'recruiter/home.html',context)

@login_required
def postjob(request):
    recruiter=request.user
    if request.method=='POST':
        form=JobDetails(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.recruiter=recruiter
            data.save()
            return redirect('home1')
    else:
        form=JobDetails()
    return render(request,'recruiter/post_job.html',{'form':form})

def details_of_job(request,id):
    job=Job.objects.get(pk=id)

    
    context={
        'job':job,
    }   
    return render(request,'recruiter/jobdetail.html',context)
@login_required
def applicant(request,id):
    job=Job.objects.get(pk=id)
    applicant=Applicants.objects.filter(job=job)
    paginator=Paginator(applicant,20)
    page_number  = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        'page_obj':page_obj,
        'applicants':applicant,
        'job':job
    }
    return render(request,'recruiter/applicants.html',context)
@login_required
def selected(request,id):
    job=Job.objects.get(pk=id)
    applicant=SelectedApplicants.objects.filter(job=job)
    paginator=Paginator(applicant,20)
    page_number  = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        'page_obj':page_obj,
        'applicants':applicant,
        'job':job
    }
    return render(request,'recruiter/selected.html',context)
@login_required
def slelectapplicant(request,job_id,applicant_id):
    job=Job.objects.get(pk=job_id)
    applicant=Applicants.objects.filter(job=job,applicant=applicant_id)
    user=User(applicant_id)
    selected=True
    select=SelectedApplicants(job=job,applicant=user)
    select.save()
    applicant.delete()
    return redirect('home1')
    
@login_required
def removeapplicant(request,job_id,applicant_id):
    job=Job.objects.get(pk=job_id)
    selected=SelectedApplicants.objects.filter(job=job,applicant=applicant_id)
    user=User(applicant_id)

    selected.delete()
    return redirect('home1')


    


    
