from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_list),
    path('courses/<str:course_name>/', views.course_detail),
    path('courses/<str:course_name>/modules/', views.course_modules),
    path('courses/<str:course_name>/modules/<int:module_id>/', views.module_detail),
]
