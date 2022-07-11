from django.test import TestCase
from .models import Profile, Feature

# Create your tests here.
class ModelTest(TestCase):
    def test_fields(self):
        prof = Profile()
        prof.name = "Test A"
        prof.email = "test@gmail.com"
        prof.address1 = "0 test street"
        prof.city = "TestCity"
        prof.state = "TX"
        prof.zipcode = "11111"

class URLTests(TestCase):
    def test_testIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code)
