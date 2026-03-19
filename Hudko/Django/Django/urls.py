from django.contrib import admin
from django.urls import path
from shop import views
from django.views.generic import TemplateView

urlpatterns = [
    path('products/', views.products),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('', TemplateView.as_view(template_name='index.html')),
]
