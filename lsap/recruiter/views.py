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
    jobs=Job.objects.all()
    paginator=Paginator(jobs,5)
    page_number  = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        'page_obj':page_obj,
        'jobs':jobs
    }
    return render(request,'recruiter/home.html',context)
