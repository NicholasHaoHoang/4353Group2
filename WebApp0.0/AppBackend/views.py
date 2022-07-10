from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from .models import Feature

# Create your views here.

#Rendering Index.html
def index(request):
    #Profile Management. Insert code Here

    #END CODE

    return render(request, 'Index.html')

#Rendering FuelHistory.html
def  fuelHistory(request):
    #Insert code for Fuel History Here

    #END CODE

    return render(request, 'FuelHistory.html')

#Rendering FuelQuote.html
def  fuelQuote(request):
    #Insert code for Fuel Quote here

    #END CODE

    return render(request, 'FuelQuote.html')

#Rendering login.html
def  login(request):
    #Insert code for login (login.html) here

    #END CODE

    return render(request, 'login.html')

#Rendering Signup.html
def  signup(request):
    #Insert code for Sign up here
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email_address')
        password = request.POST.get('password')
        confirmemail = request.POST.get('confirm_email_address')
        confirmpassword = request.POST.get('confirm_password')

        if (email == confirmemail) and (confirmpassword == password):
            if User.object.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(name = name).exists():
                messages.info(request, 'Name Already Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = name, email = email, password = password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'Signup.html')  
    
    #END CODE
    

#Rendering ProfileManagement.html
def  ProfileManagement(request):
    #Insert code for Profile Management here
    
    #END CODE
    return render(request, 'ProfileManagement.html')
