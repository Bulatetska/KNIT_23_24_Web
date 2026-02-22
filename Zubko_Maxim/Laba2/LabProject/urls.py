from django.contrib import admin
from django.urls import path
from hello import views  # Импортируем твои функции из приложения hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # Пустые кавычки '' означают главную страницу
]   