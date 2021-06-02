from django.contrib import admin
from django.urls import path,include
from . import views,models
from django.contrib.auth import views as auth_login

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',auth_login.LoginView.as_view(template_name='login.html'),name='login'),
    path('welcome',views.welcome,name='welcome'),
    path('logout/',auth_login.LogoutView.as_view(),name='logout'),
    path('bye',views.logout,name='bye'),






]
