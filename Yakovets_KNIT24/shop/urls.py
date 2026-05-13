from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_students),
    path('update/<str:card>/', views.update_year),
    path('remove/', views.remove_graduates),
    path('sorted/', views.sorted_students),
]
