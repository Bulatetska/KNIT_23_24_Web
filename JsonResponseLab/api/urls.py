from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('users/<str:name>/', views.user_detail),
]