from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student, name='create_student'),
    path('update/', views.update_year, name='update_year'),
    path('delete/', views.delete_finished, name='delete_finished'),
    path('list/', views.list_students, name='list_students'),
]