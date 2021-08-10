from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('' , views.enter , name = "enter"),
    path('home/' , views.home , name = "home"),
    path('home/login' , views.login , name = "login"),
    path('home/signup' , views.signup , name = "signup"),
    path('home/logout' , views.logout , name = "logout")
]
