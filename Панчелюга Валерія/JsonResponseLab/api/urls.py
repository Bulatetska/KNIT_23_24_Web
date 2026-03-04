from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('users/<str:name>/', views.user_detail, name='user_detail'),
]