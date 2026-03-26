from django.contrib import admin
from django.urls import path

from shop.views import about, feedback, index, products, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('feedback/', feedback, name='feedback'),
    path('products', products, name='products'),
]
