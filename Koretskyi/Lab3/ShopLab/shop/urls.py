from django.urls import path
from . import views

urlpatterns = [
    path('sale/', views.sale),
    path('<str:category>/', views.category),
    path('<str:category>/<str:product>/', views.product),
]