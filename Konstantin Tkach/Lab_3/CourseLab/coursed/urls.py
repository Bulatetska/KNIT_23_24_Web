from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('<str:course_name>/', views.course_detail, name='course_detail'),
    path('<str:course_name>/modules/', views.course_modules, name='course_modules'),
    path('<str:course_name>/modules/<int:module_id>/', views.module_detail, name='module_detail'),
]