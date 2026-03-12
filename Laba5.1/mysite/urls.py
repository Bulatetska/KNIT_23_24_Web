from django.contrib import admin
from django.urls import path
from register import views  # проверь, что тут имя твоего приложения

urlpatterns = [
    path('admin/', admin.site.urls),  # Исправь здесь
    path('register/', views.register),
]