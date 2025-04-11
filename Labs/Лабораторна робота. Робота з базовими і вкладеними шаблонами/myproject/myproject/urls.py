from django.contrib import admin
from django.urls import path
from main import views  # імпортуємо представлення з додатку main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]