from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='index'),
    path('FuelQuote.html', views.fuelQuote, name='fuelQuote'),
    path('FuelHistory.html', views.fuelHistory, name='fuelHistory'),
    path('main.html', views.main, name='main'),
    path('Signup.html', views.signup, name='signup'),
    path('ProfileManagement.html', views.ProfileManagement, name='ProfileManagement'),
    path('confirmQuote',views.confirmQuote, name="confirmQuote")
]