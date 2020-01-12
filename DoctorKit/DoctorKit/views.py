from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "User name cannot be more than 10 letters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "User name should contain only letters and numbers")
            return redirect('/')
        
        if pass1 != pass2:
            messages.error(request, "Passwords don't match")
            return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been sucessfully created !!!")
        return redirect('/')
        
    else:
        return HttpResponse('404- Page not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
    
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid login credentials! Please try again.')
            return redirect('/')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('/')
    