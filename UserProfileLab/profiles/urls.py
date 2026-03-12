from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list),
    path('users/<str:username>/', views.user_detail),
    path('users/<str:username>/orders/', views.user_orders),
]