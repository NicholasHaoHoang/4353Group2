from xml.etree.ElementTree import QName
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
from random import randint
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from AppBackend.models import Feature, Profile, FuelQuote
# Create your views here.

#Rendering Index.html
def index(request):
    #Profile Management. Insert code Here

    #END CODE

    return render(request, 'login.html')


#Rendering FuelHistory.html
def  fuelHistory(request):
    if request.user.is_authenticated == False or request.user.is_superuser :
        print("logout")
        return render(request, 'login.html')
    else:
        #Insert code for Fuel History Here
        data = FuelQuote.objects.filter(email = request.user.email)
    #END CODE

    return render(request, 'FuelHistory.html',{'data':data})

#Rendering FuelQuote.html
def  fuelQuote(request):
    #Insert code for Fuel Quote here
    print(request.user)

    if request.user.is_authenticated == False or request.user.is_superuser :
        return render(request, 'login.html')
    #END CODE
    profile = Profile.objects.filter(email=request.user)
    print(profile[0].email)
    # profile = Profile(email=request.user)
    address = profile[0].address1 +" " +profile[0].address2
    # if(request.method == 'GET'):
    #     gallons = request.GET.get('gallonsReq')
    #     priceMod = PricingModule(request.user,gallons)
    #     price = priceMod.calculate()
    #     return render(request, 'FuelQuote.html',{'DeliveryAddress':address,'Price':1.64,'Amount':0})

    return render(request, 'FuelQuote.html',{'DeliveryAddress':address,'Price':1.85,'Amount':0})

#Rendering login.html
def  login(request):
    #Insert code for login (login.html) here
    if request.method == 'POST':
        email = request.POST.get('email_address')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/ProfileManagement.html')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login.html')
    #END CODE
    else:
        return render(request, 'login.html')

#Logout Function
def logout(request):
    request.session.flush()
    print(request.user)

    
    auth.logout(request)
    print(request.user)
    return redirect('/')


#Rendering Signup.html
def signup(request):
    #Insert code for Sign up here
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email_address')
        password = request.POST.get('password')
        confirmemail = request.POST.get('confirm_email_address')
        confirmpassword = request.POST.get('confirm_password')

        if (email == confirmemail) and (confirmpassword == password):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('Signup.html')
            elif User.objects.filter(username = name).exists():
                messages.info(request, 'Name Already Exists')
                return redirect('Signup.html')
            else:
                user = User.objects.create_user(username = email, email = email, password = password)
                user.save()
                return redirect('login.html')
        else:
            if not(confirmpassword == password):
                messages.info(request, 'Passwords do not match')
            else:
                messages.info(request, 'Email Addresses do not match')
            return redirect('signup')
    else:
        return render(request, 'Signup.html')  
    

    

#Rendering ProfileManagement.html
def  ProfileManagement(request):
    if request.user.is_authenticated == False or request.user.is_superuser :
        print("logout")
        return render(request, '/')
        #Insert code for Profile Management here
    #current user, use in Assignment 4 to pull info
    current_user = request.user
    if request.user.is_authenticated:
        profile = Profile.objects.filter(email=current_user)
        profile_dict ={
            "profile":profile
        }
        print(profile_dict)
        name = request.POST.get('firstname')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        if request.method == 'POST':
            if not profile.exists():
                #Pull from Database, Implement this part in Assignment 4
                prof = Profile.objects.create(email = current_user,name = name, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
                profile_dict["profile"] = prof
                if prof == 1:
                    message = "Data updated successfully"
                else:
                    message = "Data not updated successfully"
                profile_dict["message"] = message
                print(profile_dict["message"])
                print(profile_dict["profile"])
                return render(request,'ProfileManagement.html',profile_dict)
            else:
                prof = Profile.objects.filter(email=current_user.email).update(name = name, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
                profile_dict["profile"] = prof
                if prof == 1:
                    message = "Data updated successfully"
                else:
                    message = "Data not updated successfully"
                profile_dict["message"] = message
                print(profile_dict["message"])
                print(prof)
                return render(request,'ProfileManagement.html',profile_dict)
         
        else:

            return render(request,'ProfileManagement.html',profile_dict)
    else:
        messages.info(request, 'Please Login to manage your profile')
        return redirect('login.html')
    #END CODE
        


def confirmQuote(request):
    if request.method == "GET":
        gallonsReq=request.GET.get('gallonsReq')
        deliveryAddress=request.GET.get('deliveryAddress')
        deliverydate=request.GET.get('deliverydate')
        price=request.GET.get('price')
        AmountDue=request.GET.get('AmountDue')
        if int(request.GET.get('gallonsReq'))<1 or request.GET.get('gallonsReq').isdigit()==False:
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



        res = FuelQuote.objects.create(
            email = request.user,
            gallonsRequested = gallonsReq,
            deliveryAddress = deliveryAddress,
            deliverydate =deliverydate,
            price =price,
            AmountDue =AmountDue
        )
        # rand = randint(0,1000)
        # timeNow = round(time.time()*1000)
        # quoteNo =rand+timeNow
        
        return render(request, "confirmQuote.html",{'quoteNo':res.quoteId})
    else:
        return render(request,"FuelQuote.html")

#PricingModule Class
class PricingModule:
    def PricingModule(self,user,galls_req):
        self.current_price = 1.50
        self.gallonsReq = galls_req
        self.user = user
    def __init__(self, user, galls_req):
        self.current_price = 1.50
        self.gallonsReq = galls_req
        self.user = user

    def states_factor(self):
        cur_profile = Profile.objects.filter(email = self.user.email)
        if cur_profile[0].state == 'TX':
            return 0.02
        else:
            return 0.04

    def rate_history(self):
        all_entries = FuelQuote.objects.all()
        if not all_entries:
            historyExist = False
        else:
            historyExist = True

        if historyExist:
            return 0.01 
        else:
            return 0.0

    def gallonsReq_factor(self):
        if self.gallonsReq > 1000:
            return 0.03
        else:
            return 0.04

    def margin(self):
        location_factor = self.states_factor()
        rate_history = self.rate_history()
        gallonsReq_factor = self.gallonsReq_factor()

        company_profit = .20

        margin = round((self.current_price * (location_factor - rate_history + gallonsReq_factor + company_profit)),3)

        print("location_factor", location_factor)
        print("ratehistory_factor", rate_history)
        print("gallonsReq_factor", gallonsReq_factor)

        rounded_margin = round(margin, 3)
        print("margin", margin)
        print("rounded margin", rounded_margin)

        return rounded_margin
    
    def calculate(self):
        
        result = (self.margin() + self.current_price) * self.gallonsReq
        print("result", result)
        return result
