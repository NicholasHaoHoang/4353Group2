from calendar import c
from re import S
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
    print(f"In Fuel Quote: \nCurrentUser: {request.user}")

    if request.user.is_authenticated == False or request.user.is_superuser :
        return render(request, 'login.html')
    #END CODE
    profile = Profile.objects.filter(email=request.user)

    address = profile[0].address1 +" " +profile[0].address2
    if(request.method == 'GET'):
        gallons = request.GET.get('gallonsReq')
        if gallons:
            print(f"Gallons found, Calculating with {gallons} gallons")
            priceMod = PricingModule(request.user,gallons)
            price = priceMod.calculate()
            price = round(price,2)
            print(f"Price: {price}")
        else:
            gallons = 1
            print(f"No gallons found, Calculating with {gallons} gallons")
            priceMod = PricingModule(request.user,gallons)
            price = priceMod.calculate()
            price = round(price,2)
            print(f"Price: {price}")
        return render(request, 'FuelQuote.html',{'DeliveryAddress':address,'Price':price,'Amount':0})

    return render(request, 'FuelQuote.html',{'DeliveryAddress':address,'enterprice':"Enter values to get your price",'Amount':0})

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
    print(f"{request.user} was logged out")
    request.session.flush()
    

    
    auth.logout(request)
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
                print(user)
                if user:
                    Profile.objects.create(email=email)
                else:
                    user=User.objects.filter(username=email,email=email)
                    print(user)
                    User.delete()
                    messages.info(request, 'Could not create the account')
                    return redirect('Signup.html')
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
        return render(request, '/')
        #Insert code for Profile Management here
    #current user, use in Assignment 4 to pull info
    current_user = request.user
    if request.user.is_authenticated:
        profile = Profile.objects.filter(email=current_user)
        profile_dict ={
            "profile":profile[0]
        }
        print(f"In Profile Management: \nCurrent User: {current_user}")
        name = request.POST.get('firstname')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        profile_dict["fullname"] = profile[0].name
        profile_dict["address1"] = profile[0].address1
        profile_dict["address2"] = profile[0].address2
        profile_dict["state"] = profile[0].state
        profile_dict["city"] = profile[0].city
        profile_dict["zipcode"] = profile[0].zipcode
        if request.method == 'POST':
            print(f"POST METHOD: \nDictionary: {profile_dict}")
            prof = profile
            if not profile.exists():
                #Pull from Database, Implement this part in Assignment 4
                prof = Profile.objects.create(email = current_user,name = name, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
                profile_dict['profile'] = prof
                message = "Data updated successfully, Make an order now"
                profile_dict["message"] = message
            else:
# <<<<<<< HEAD
#                 prof = Profile.objects.update(name = name, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
#                 print(prof)
#                 if prof:
#                     message = "Data updated successfully"
#                 else:
#                     message = "Data not updated successfully"
#                 # profile_dict["profile"] = prof
# =======
                prof = Profile.objects.filter(email=current_user.email).update(name = name, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
                profile_dict['profile'] = Profile.objects.filter(email=current_user)
                if prof == 1:
                    message = "Data updated successfully, Make an order now"
                else:
                    message = "Data not updated successfully"
                    return render(request,'ProfileManagement.html',profile_dict)
# >>>>>>> b5e7a8e293e978a52a9a21bf4d83353b614f5d40
                profile_dict["message"] = message
            return fuelQuote(request)
         
        else:

            return render(request,'ProfileManagement.html',profile_dict)
    else:
        messages.info(request, 'Please Login to manage your profile')
        return redirect('login.html')
    #END CODE
        
def getQuote(request):
    print("In getQuote:\n")
    if request.method == "GET":
        gallonsReq=request.GET.get('gallonsReq')
        deliveryAddress=request.GET.get('deliveryAddress')
        deliverydate=request.GET.get('deliverydate')
        priceMod = PricingModule(request.user,int(gallonsReq))
        price = priceMod.calculate()
        print(f"Price: {price}")
        AmountDue=request.GET.get('AmountDue')
        quote_dict={
            "gallonsReq":gallonsReq,
            "DeliveryAddress":deliveryAddress,
            "deliverydate":deliverydate,
            "Price":round(float(price),2),
            "AmountDue":AmountDue
        }
        print(quote_dict)
        
        if int(request.GET.get('gallonsReq'))<1 or request.GET.get('gallonsReq').isdigit()==False:
            quote_dict["message"]="Gallons requested must be an integer"
            return render(request, "FuelQuote.html",quote_dict)
        else:
            gallonsReq=float(request.GET['gallonsReq'])
            price = round(priceMod.calculate(),2)
            AmountDue = float(gallonsReq)*float(price)
            quote_dict["AmountDue"] = round(AmountDue,2)

        month,day,year=deliverydate.split('-')
        isValid=True
        try:
            datetime.datetime(int(month),int(day),int(year))

        except ValueError:
            isValid=False

        if isValid==False:
            quote_dict["message"] = "Delivery date is not in correct format"
            return render(request, quote_dict)
            
        
        print(gallonsReq)
        print(deliveryAddress)
        print(deliverydate)
        print(price)
        print(AmountDue)



        # res = FuelQuote.objects.create(
        #     email = request.user,
        #     gallonsRequested = gallonsReq,
        #     deliveryAddress = deliveryAddress,
        #     deliverydate =deliverydate,
        #     price = float(price),
        #     AmountDue = float(AmountDue)
        # )
        return render(request, "FuelQuote.html",quote_dict)
    else:
        return render(request,"FuelQuote.html")

def confirmQuote(request):
    if request.method == "GET":
        gallonsReq=request.GET.get('gallonsReq')
        deliveryAddress=request.GET.get('deliveryAddress')
        deliverydate=request.GET.get('deliverydate')
        price=request.GET.get('price')
        AmountDue=request.GET.get('AmountDue')
        quote_dict={
            "gallonsReq":gallonsReq,
            "deliveryAddress":deliveryAddress,
            "deliverydate":deliverydate,
            "price":price,
            "AmountDue":AmountDue
        }

        if int(request.GET.get('gallonsReq'))<1 or request.GET.get('AmountDue') == '' or request.GET.get('gallonsReq').isdigit()==False:
            messages.info(request, 'Gallons requested must be an integer')
            print("Debug")
            return render(request, "FuelQuote.html")
        else:
            gallonsReq=float(request.GET['gallonsReq'])

        month,day,year=deliverydate.split('-')
        isValid=True
        try:
            datetime.datetime(int(month),int(day),int(year))

        except ValueError:
            isValid=False

        if isValid==False:
            quote_dict["message"] = "Delivery date is not in correct format"
            return render(request, quote_dict)
            
        
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
            price = float(price),
            AmountDue = float(AmountDue)
        )
        
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
        if int(self.gallonsReq) > 1000:
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
        
        result = (self.margin() + 1.5)
        print("result", result)
        return result
