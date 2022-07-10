from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
from random import randint
# Create your views here.

#Rendering Index.html
def index(request):
    #Profile Management. Insert code Here

    #END CODE

    return render(request, 'Index.html')

#Rendering FuelHistory.html
def  fuelHistory(request):
    #Insert code for Fuel History Here
    data = [
        {
        'Name': 'Younus',
        'GallonsRequested': '100',
        'DeliveryAddress': 'ABCD address',
        'DeliveryDate': '10-20-2022',
        'SuggestedPrice': '1000',
        'AmountDue': '10'
        },
        {
        'Name': 'Nick',
        'GallonsRequested': '200',
        'DeliveryAddress': 'XYZ address',
        'DeliveryDate': '11-21-2022',
        'SuggestedPrice': '200',
        'AmountDue': '02'
        },
        {
        'Name': 'Leena',
        'GallonsRequested': '400',
        'DeliveryAddress': 'DEF address',
        'DeliveryDate': '11-21-2012',
        'SuggestedPrice': '20',
        'AmountDue': '50'
        }
    ]
    #END CODE

    return render(request, 'FuelHistory.html',{'data':data})

#Rendering FuelQuote.html
def  fuelQuote(request):
    #Insert code for Fuel Quote here

    #END CODE

    return render(request, 'FuelQuote.html',{'DeliveryAddress':'XYZ Address','Price':500,'Amount':5000})

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

def confirmQuote(request):
    gallonsReq=request.GET['gallonsReq']
    deliveryAddress=request.GET['deliveryAddress']
    deliverydate=request.GET['deliverydate']
    price=request.GET['price']
    AmountDue=request.GET['AmountDue']
    if int(request.GET['gallonsReq'])<1 or request.GET['gallonsReq'].isdigit()==False:
        return render(request, "FuelQuote.html",{"gallonsReq":gallonsReq,"message":"Gallons requested must be a number"})
    else:
        gallonsReq=int(request.GET['gallonsReq'])
        
    if int(request.GET['price'])<1 or request.GET['price'].isdigit()==False:
        return render(request, "FuelQuote.html",{"price":gallonsReq,"message":"Price must be a number"})
    else:
        price=int(request.GET['price'])
    
    if request.GET['AmountDue'].isdigit()==False:
        return render(request, "FuelQuote.html",{"AmountDue":gallonsReq,"message":"Amount Due must be a number"})
    else:
        AmountDue=int(request.GET['AmountDue'])
    if request.GET['AmountDue'].isdigit()==False:
        return render(request, "FuelQuote.html",{"AmountDue":gallonsReq,"message":"Amount Due must be a number"})
    else:
        AmountDue=int(request.GET['AmountDue'])

    month,day,year=deliverydate.split('-')
    isValid=True
    try:
        datetime.datetime(int(month),int(day),int(year))

    except ValueError:
        isValid=False
    if isValid==False:
        return render(request, "FuelQuote.html",{"deliverydate":gallonsReq,"message":"Delivery date is not in correct format"})
        
    
    print(gallonsReq)
    print(deliveryAddress)
    print(deliverydate)
    print(price)
    print(AmountDue)

    rand = randint(0,1000)
    timeNow = round(time.time()*1000)
    quoteNo =rand+timeNow

    return render(request, "confirmQuote.html",{'quoteNo':quoteNo})