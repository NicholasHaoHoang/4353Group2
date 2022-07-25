from django.test import TestCase
from .models import Profile, Feature

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

    

class URLTests(TestCase):
    def test_testIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
