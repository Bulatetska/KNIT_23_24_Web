from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users_list),
    path('api/users/<str:name>/', views.user_detail),
]
