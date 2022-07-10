from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.main, name='index'),
=======
    path('', views.index, name='index'),\
>>>>>>> 20f4ae7308b8591b45fe1f349d6e126f42be15aa
    path('FuelQuote.html', views.fuelQuote, name='fuelQuote'),
    path('FuelHistory.html', views.fuelHistory, name='fuelHistory'),
    path('login.html', views.login, name='login'),
    path('Signup.html', views.signup, name='signup'),
    path('ProfileManagement.html', views.ProfileManagement, name='ProfileManagement'),
<<<<<<< HEAD
    path('confirmQuote',views.confirmQuote, name="confirmQuote")
=======
    path('logout',views.logout, name='logout')
>>>>>>> 20f4ae7308b8591b45fe1f349d6e126f42be15aa
]