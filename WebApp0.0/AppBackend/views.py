from django.shortcuts import render
from django.http import HttpResponse

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

#Rendering main.html
def  main(request):
    #Insert code for login (main.html) here

    #END CODE

    return render(request, 'main.html')

#Rendering Signup.html
def  signup(request):
    #Insert code for Sign up here

    #END CODE
    return render(request, 'Signup.html')

#Rendering ProfileManagement.html
def  ProfileManagement(request):
    #Insert code for Profile Management here
    
    #END CODE
    return render(request, 'ProfileManagement.html')
