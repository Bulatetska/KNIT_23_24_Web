from django.urls import path
from .views import *

urlpatterns = [
    path('users/', user_list),
    path('users/<str:username>/', user_detail),
    path('users/<str:username>/orders/', user_orders),
]