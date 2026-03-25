from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_students),
    path('update/', views.update_student),
    path('delete/', views.delete_graduates),
    path('list/', views.list_students),
]