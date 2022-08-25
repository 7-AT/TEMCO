from home import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.homepage, name='home'),
    path('home', views.homepage, name='home'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('contactus', views.contactus, name='contactus')
]
