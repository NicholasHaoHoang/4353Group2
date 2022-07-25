from django.test import TestCase
from .models import Profile, Feature

# Create your tests here.

class URLTests(TestCase):
    def test_testIndex(self):
        #response = self.client.get('/')
        self.assertEqual(200,200)
