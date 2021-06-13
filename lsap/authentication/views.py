from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
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
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registration Successful')
                return render(request, 'authentication/login.html')
            messages.error(request, 'email already exists')
        messages.error(request,'user already exists')
        return render( request, 'authentication/applicant_register.html')

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
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registration Successful')
                return render(request, 'authentication/recruiter_register.html')
        return render( request, 'authentication/recruiter_register.html')
    
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                return redirect('home')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')

