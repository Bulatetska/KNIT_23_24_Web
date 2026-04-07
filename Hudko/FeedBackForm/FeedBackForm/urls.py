from django.contrib import admin
from django.urls import path, include
from feedbackapp import views

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
]