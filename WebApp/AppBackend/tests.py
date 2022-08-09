from django.test import TestCase, Client
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.urls import reverse, resolve
import json
from .models import Profile, Feature, FuelQuote
from .views import *

# Create your tests here.
class ModelTest(TestCase):
    def create_profile(self):
        prof = Profile()
        prof.id = "-1"
        prof.name = "Test A"
        prof.email = "test@gmail.com"
        prof.address1 = "0 test street"
        prof.city = "TestCity"
        prof.state = "TX"
        prof.zipcode = "11111"

        return prof
    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
#--------------------------------------------------------------------------------
    def create_Feature(self, name = "TestName", details = "This is test details"):
        return Feature.objects.create(name = name, details=details)

    def test_feature_creation(self):
        w = self.create_Feature()
        self.assertTrue(isinstance(w, Feature))
#--------------------------------------------------------------------------------
    def create_FuelQuote(self, email="test@email.com", gallonsRequested= "0", deliveryAddress="0 street", deliverydate = "1/1/2000", price="0", AmountDue="0"):
        return FuelQuote.objects.create(email=email,gallonsRequested=gallonsRequested, deliveryAddress=deliveryAddress,deliverydate=deliverydate, price=price,AmountDue=AmountDue)
    def test_FuelQuote_creation(self):
        w = self.create_FuelQuote()
        self.assertTrue(isinstance(w, FuelQuote))

#younus added
#--------------------------------------------------------------------------------
    def create_FuelHistory(self, email="test@email.com"):
        return FuelQuote.objects.filter(email = email)
    def test_FuelHistory_creation(self):
        w = self.create_FuelQuote()
        print(type(w))
        self.assertTrue(isinstance(w, FuelQuote))
#--------------------------------------------------------------------------------
   

class URLTests(TestCase):
    def test_testIndex(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
    
    def test_URLIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_testFuelQuote(self):
        url = reverse('fuelQuote')
        self.assertEqual(resolve(url).func, fuelQuote)

    def test_URLFuelQuote(self):
        response = self.client.get('/FuelQuote.html')
        self.assertEqual(response.status_code,200)

    def test_FuelHistory(self):
        url = reverse('fuelHistory')
        self.assertEqual(resolve(url).func, fuelHistory)

    def test_URLFuelHistory(self):
        response = self.client.get('/FuelHistory.html')
        self.assertEqual(response.status_code,200)

    def test_testLogin(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_URLLogin(self):
        response = self.client.get('/login.html')
        self.assertEqual(response.status_code,200)

    def test_testSignup(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_URLSignup(self):
        response = self.client.get('/Signup.html')
        self.assertEqual(response.status_code,200)

    def test_testProfileManagement(self):
        url = reverse('ProfileManagement')
        self.assertEqual(resolve(url).func, ProfileManagement)

    def test_testconfirmQuote(self):
        url = reverse('confirmQuote')
        self.assertEqual(resolve(url).func, confirmQuote)
    
    def test_testlogout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_URLlogout(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

class testPricingModule(TestCase):
    def setUp(self):
        self.testuser=User.objects.create_user(username= 'dummy', password='test')
        self.testProf = Profile( name = "test", email = "t@email.com", address1 = "1 street", city = "houston", state ="TX", zipcode="77777")
        self.pm = PricingModule(self.testuser,11)
        self.pm.user.state = 'LA'
        self.pm.user.gallonsReq = 11
        self.pm.user.current_price = 11

    def test_init(self):
        self.pm.__init__(self.testuser,11)
        self.assertEqual(self.pm.current_price, 1.50)
        self.assertEqual(self.pm.gallonsReq, 11)
        self.assertEqual(self.pm.user, self.testuser)
    
    # def test_states_factor(self):
    #     self.pm.user.state = 'TX'
    #     self.assertEqual(0.02, self.pm.states_factor())
    #     self.pm.user.state = 'AL'
    #     self.assertEqual(0.04, self.pm.states_factor())

    def test_rate_history(self):
        ae = FuelQuote.objects.none()
        self.assertEqual(0.0, self.pm.rate_history())
        res = FuelQuote.objects.create(
            email = 'test@email.com',
            gallonsRequested = 1,
            deliveryAddress = '1 street',
            deliverydate ='1/1/2000',
            price = 10,
            AmountDue = 10
        )
        ae = FuelQuote.objects.all()
        self.assertEqual(0.01, self.pm.rate_history())
            



    def test_gallonsReq_factor(self):
        self.pm.gallonsReq = 1001
        self.assertEqual(0.03, self.pm.gallonsReq_factor())
        self.pm.gallonsReq = 0
        self.assertEqual(0.04, self.pm.gallonsReq_factor())
    
    # def test_margin(self):
    #     self.pm.user.state = 'AL' #location_factor should be 0.04
    #     self.pm.current_price = 10
    #     res = FuelQuote.objects.create(
    #         email = 'test@email.com',
    #         gallonsRequested = 1,
    #         deliveryAddress = '1 street',
    #         deliverydate ='1/1/2000',
    #         price = 10,
    #         AmountDue = 10
    #     )#rate_history should be 0.01
    #     self.pm.user.gallonsReq = 10 #gallonsReq_factor should be 0.04
    #     margin = round((self.pm.current_price * (0.04 - 0.01 + 0.04 + 0.20)),3)
    #     rounded_margin = round(margin,3)
    #     self.assertEqual(rounded_margin,self.pm.margin())


        

    # def test_calculate(self):
    #     self.pm.current_price = 2
    #     self.pm.gallonsReq = 2
    #     self.assertEqual(((self.pm.margin() + self.pm.current_price)),self.pm.calculate())


        

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')
        self.confirmQuote_url = reverse('confirmQuote')
        self.getQuotes_url = reverse('getQuote')
        self.testUser = User.objects.create(
            username = 'test',
            email = 'test@email.com',
            password = 'secret'
        )
         

    def test_login_get(self):
        testuser=User.objects.create_user(username= 'dummy', password='test')
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_post(self):

        response = self.client.post(self.login_url, {
            'email': 'test@email.com',
            'username': 'test',
            'password': 'secret'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.testUser.username, 'test')
        self.assertEquals(self.testUser.password, 'secret')
        self.assertEquals(self.testUser.email, 'test@email.com')

    def test_signup_post(self):
        #password not match case
        response = self.client.post(self.signup_url, {
            'email': 'test@email.com',
            'confirmemail':'test@email.com',
            'name': 'test',
            'password': 'secret',
            'confirmpassword': 'secret1'
        })
        #password & email match case
        response = self.client.post(self.signup_url, {
            'email': 'test@email.com',
            'confirmemail':'test@email.com',
            'name': 'test',
            'password': 'secret',
            'confirmpassword': 'secret'
        })
        #email not match case
        response = self.client.post(self.signup_url, {
            'email': 'test1@email.com',
            'confirmemail':'test@email.com',
            'name': 'test',
            'password': 'secret',
            'confirmpassword': 'secret'
        })
        User.objects.create()
        self.assertEquals(response.status_code, 302)



    def test_fuelQuote_get(self):
        #no galon
        response = self.client.get(self.confirmQuote_url, {
            'gallonsReq': '',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': '122'
        })
        print(response)
        #no AmountDue
        response = self.client.get(self.confirmQuote_url, {
            'gallonsReq': '10',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': ''
        })
        print(response)
       #No delivery date
        response = self.client.post(self.confirmQuote_url, {
            'gallonsReq': '10',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '',
            'price': '1.91',
            'AmountDue': ''
        })
        print(response)
        #gallons < 0
        response = self.client.post(self.confirmQuote_url, {
            'gallonsReq': '0',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': ''
        })
        print(response)
        #date format wrong
        response = self.client.post(self.confirmQuote_url, {
            'gallonsReq': '0',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-0817',
            'price': '1.91',
            'AmountDue': ''
        })
        print(response)
        #correct case
        response = self.client.post(self.confirmQuote_url, {
            'gallonsReq': '10',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': '100'
        })
        print(response)
        User.objects.create()
        self.assertEquals(response.status_code, 200)


    def test_getQuote_get(self):
        #no gallon req
        try:
            response = self.client.get(self.getQuotes_url, {
                'gallonsReq': '',
                'deliveryAddress':'76771 abc 131',
                'deliverydate': '2022-08-17',
                'price': '1.91',
                'AmountDue': ''
            })
        except:
            print("Exception no gallonsReq")
       
        #No delivery date
        response = self.client.post(self.getQuotes_url, {
            'gallonsReq': '10',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '',
            'price': '1.91',
            'AmountDue': ''
        })
        #gallons < 0
        response = self.client.post(self.getQuotes_url, {
            'gallonsReq': '0',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': ''
        })
        #date format wrong
        response = self.client.post(self.getQuotes_url, {
            'gallonsReq': '0',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-0817',
            'price': '1.91',
            'AmountDue': ''
        })
        #correct case
        response = self.client.post(self.getQuotes_url, {
            'gallonsReq': '10',
            'deliveryAddress':'76771 abc 131',
            'deliverydate': '2022-08-17',
            'price': '1.91',
            'AmountDue': ''
        })
        User.objects.create()
        self.assertEquals(response.status_code, 200)


