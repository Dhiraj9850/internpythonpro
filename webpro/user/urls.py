from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = "user"),
    path('signup',views.handleSignup,name="handleSignup"),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout', views.handlelLogout, name="handleLogout")
]