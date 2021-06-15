from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth

class applicant_register(View):
    def get(self, request):
        return render(request, 'authentication/applicant_register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if password!=password2:
            messages.error(request, 'password does not match')
            return render(request, 'authentication/applicant_register.html', context)
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'password too short')
                    return render(request, 'authentication/applicant_register.html', context)
                user = User.objects.create_user(username=username, email = email)
                usertype=Applicant.objects.create(user=user)
                usertype.save()
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registration Successful')
                return render(request, 'authentication/login.html')
            messages.error(request, 'email already exists')
        messages.error(request,'user already exists')
        return redirect('login')

class recruiter_register(View):
    def get(self, request):
        return render(request, 'authentication/recruiter_register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if password!=password2:
            messages.error(request, 'password does not match')
            return render(request, 'authentication/recruiter_register.html', context)
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'password too short')
                    return render(request, 'authentication/recruiter_register.html', context)
                user = User.objects.create_user(username=username, email = email)
                usertype=Recruiter.objects.create(user=user)
                usertype.save()
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registration Successful')
                return redirect('login')
        return render( request, 'authentication/recruiter_register.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            
            if user and Applicant.objects.filter(user=user).exists():
                auth.login(request, user)
                messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                return redirect('home')
            
            elif user and Recruiter.objects.filter(user=user).exists():
                auth.login(request,user)
                messages.success(request,'welcome,'+user.username+'you are now logged in')
                return redirect('home1')
            else:
                messages.error(request,'please register')
            
            messages.error(
            request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
        request, 'Please fill all fields')
        return render(request, 'authentication/login.html')
 
def logout(request):
    auth.logout(request)
    return redirect('/')   

