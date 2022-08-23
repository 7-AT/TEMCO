from home import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.homepage, name='home'),
    path('home', views.homepage, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus')
]
