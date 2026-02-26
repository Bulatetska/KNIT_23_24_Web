from django.contrib import admin
from django.urls import path
from Hello import views

urlpatterns = [
    path('', views.index),
]
