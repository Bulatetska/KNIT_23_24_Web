"""
URL configuration for ShopLab project.

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
from django.contrib import admin
from django.urls import path, include
from shop.views import category, category_products, home, sale, products


shop_patterns = [
    path('sale', sale),
    path('<str:category>', category),
    path('<str:category>/<str:product>', category_products),
    
]

urlpatterns = [
    path('',home),
    path('product', products),
    path('shop/', include(shop_patterns))
]
