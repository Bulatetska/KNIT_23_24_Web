from django.contrib import admin
from django.urls import path
from feedback.views import feedback_view

urlpatterns = [
    path('admin/', admin.site.urls), # Це стандартне
    path('feedback/', feedback_view), # Твоя нова сторінка
]