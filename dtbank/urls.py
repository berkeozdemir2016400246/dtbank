"""dtbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.serveLogin, name='login'),
    path('user', views.serveUser, name='user'),
    path('dbmanager', views.serveDbManager, name='dbmanager'),
    path('dbmanager/createuser', views.serveCreateUser, name='createuser'),
    path('dbmanager/deletedrug', views.serveDeleteDrug, name='deletedrug'),
    path('dbmanager/deleteProtein', views.serveDeleteProtein, name='deleteprotein'),
    path('dbmanager/updateDrug', views.serveUpdateDrug, name='updatedrug'),
    path('dbmanager/updateReaction', views.serveUpdateReaction, name='updatereaction'),
]
