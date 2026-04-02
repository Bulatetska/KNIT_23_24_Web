from django.contrib import admin
from django.urls import path
from lab_7_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab/', views.student_lab_view),
    path('demo/', views.demo_orm_operations, name='orm_demo'),
]
