from django.urls import path, include
from . import views

user_patterns = [
    path('', views.users_list),
    path('<str:username>/', views.user_detail),
    path('<str:username>/orders/', views.user_orders),
]

urlpatterns = [
    path('', views.index),
    path('users/', include(user_patterns)),
]
