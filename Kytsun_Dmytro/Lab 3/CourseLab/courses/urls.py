from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('<str:course_name>/', views.course_detail, name='course-detail'),
    path('<str:course_name>/modules/', views.module_list, name='module-list'),
    path('<str:course_name>/modules/<int:module_id>/', views.module_detail, name='module-detail'),
]