from django.urls import path
from .views import *

urlpatterns = [
    path('users/', api_user_list),
    path('users/<str:name>/', api_user_detail),
]