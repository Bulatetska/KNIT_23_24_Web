from django.contrib import admin
from django.urls import path
from myprogram.views import student_manager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_manager, name='student_manager'),
]