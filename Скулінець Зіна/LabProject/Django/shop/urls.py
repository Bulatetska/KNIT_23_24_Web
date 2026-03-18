from django.contrib import admin
from django.urls import path
from shop.views import products 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products), 
]