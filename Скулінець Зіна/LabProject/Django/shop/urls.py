from django.contrib import admin
from django.urls import path
from . import views  # ЦЕ ОБОВ'ЯЗКОВО!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('feedback/', views.feedback, name='feedback'),
]