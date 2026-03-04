from django.urls import path
from . import views
urlpatterns = [
    path('', views.users, name='users'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('<str:username>/orders/', views.user_orders, name='user_orders'),
]