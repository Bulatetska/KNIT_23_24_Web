from api import views
from django.urls import path

urlpatterns = [
    path('api/users/', views.users),
    path('api/users/<str:name>', views.userDetails),
]
