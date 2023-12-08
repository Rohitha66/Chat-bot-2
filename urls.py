"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. adddata the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('userreg/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('ulogin/', views.userlogindef, name="userlogindef"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhomedef"),
    path('userlogout/', views.userlogoutdef, name="userlogoutdef"),
    path('adminlogout/', views.adminlogout, name="userlogoutdef"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('classification/', views.classification, name="classification"),

    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('nntrain/', views.nntrain, name="nntrain"),
    path('dttrain/', views.dttrain, name="dttrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('evaluation/', views.evaluation, name="evaluation"),
    
    path('uploaddataset/', views.uploaddataset, name="uploaddataset"),
    path('uploaddatasetaction/', views.uploadaction, name="uploadaction"),


    path('chatpage/', views.chatpage, name="chatpage"),
    path('chataction/', views.chataction, name="chataction"),
    
    
]
