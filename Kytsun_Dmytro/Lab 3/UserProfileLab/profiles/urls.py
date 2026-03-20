from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('<str:username>/', views.user_detail, name='user-detail'),
    path('<str:username>/orders/', views.user_orders, name='user-orders'),
]