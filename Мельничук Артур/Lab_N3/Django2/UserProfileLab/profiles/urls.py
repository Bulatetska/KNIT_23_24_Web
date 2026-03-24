from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list),
    path('<str:username>/', views.user_detail),
    path('<str:username>/orders/', views.user_orders),
]