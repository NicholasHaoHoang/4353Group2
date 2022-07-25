from django.test import TestCase
from .models import Profile, Feature, FuelQuote

# Create your tests here.
class ModelTest(TestCase):
    def create_profile(self):
        prof = Profile()
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


    

class URLTests(TestCase):
    def test_testIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_testFuelQuote(self):
        response = self.client.get('/FuelQuote.html')
        self.assertEqual(response.status_code,200)

    def test_FuelHistory(self):
        response = self.client.get('/FuelHistory.html')
        self.assertEqual(response.status_code,200)

    def test_testLogin(self):
        response = self.client.get('/login.html')
        self.assertEqual(response.status_code,200)

    def test_testSignup(self):
        response = self.client.get('/Signup.html')
        self.assertEqual(response.status_code,200)

    # def test_testProfileManagement(self):
    #     response = self.client.get('/ProfileManagement.html')
    #     self.assertEqual(response.status_code,200)

    # def test_testConfirmQuote(self):
    #     response = self.client.get('/confirmQuote')
    #     self.assertEqual(response.status_code,200)
    
