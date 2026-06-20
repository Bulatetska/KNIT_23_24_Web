from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/', views.delete_view),
]