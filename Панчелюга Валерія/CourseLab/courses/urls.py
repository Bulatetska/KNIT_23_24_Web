from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<str:course_name>/', views.course_detail, name='course_detail'),
    path('<str:course_name>/modules/', views.module, name='module'),
    path('<str:course_name>/modules/<str:module_id>/', views.module_detail, name='module_detail'),
]