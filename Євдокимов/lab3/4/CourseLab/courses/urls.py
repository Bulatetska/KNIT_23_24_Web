from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list),
    path('<str:course_name>/', views.course_detail),
    path('<str:course_name>/modules/', views.modules),
    path('<str:course_name>/modules/<int:module_id>/', views.module_detail),
]