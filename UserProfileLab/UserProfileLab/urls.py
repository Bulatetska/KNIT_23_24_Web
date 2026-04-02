"""
URL configuration for UserProfileLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from collections import UserList
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from profiles.views import user_details, user_list, user_orders,home

user_patterns = [
    path('', user_list),
    path('<str:username>', user_details),
    path('<str:username>/orders', user_orders),
]

urlpatterns = [
    path('', home),
    path('users/', include(user_patterns)),  
]