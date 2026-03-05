from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]