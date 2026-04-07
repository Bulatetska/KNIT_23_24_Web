from django.urls import path
from courses import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<str:course_name>/', views.course_detail, name='course_detail'),
    path('courses/<str:course_name>/modules/', views.course_modules, name='course_modules'),
    path('courses/<str:course_name>/modules/<int:module_id>/', views.module_detail, name='module_detail'),
]