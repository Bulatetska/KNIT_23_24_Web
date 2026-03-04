from django.contrib import admin
from django.urls import include, path
from profiles import views

user_patterns = [
    path("",views.users),
    path("<str:username>", views.userDetails),
    path("<str:username>/orders",views.userOrders)
]

urlpatterns = [
    path('', views.index),
    path('users/' , include(user_patterns))
]
