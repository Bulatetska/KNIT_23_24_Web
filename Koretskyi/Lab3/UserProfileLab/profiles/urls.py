from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list),
    path('<username>/', views.user_detail),
    path('<username>/orders/', views.user_orders),
]