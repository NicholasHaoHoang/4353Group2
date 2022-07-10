from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD

    path('', views.main, name='index'),
    path('', views.index, name='index'),\

    path('FuelQuote.html', views.fuelQuote, name='fuelQuote'),
    path('FuelHistory.html', views.fuelHistory, name='fuelHistory'),
    path('login.html', views.login, name='login'),
    path('Signup.html', views.signup, name='signup'),
    path('ProfileManagement.html', views.ProfileManagement, name='ProfileManagement'),
    path('confirmQuote',views.confirmQuote, name="confirmQuote")
    path('logout',views.logout, name='logout')