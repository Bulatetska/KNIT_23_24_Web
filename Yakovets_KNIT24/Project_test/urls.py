from django.urls import path
from shop.views import register

urlpatterns = [
    path('register/', register, name='register'),
]