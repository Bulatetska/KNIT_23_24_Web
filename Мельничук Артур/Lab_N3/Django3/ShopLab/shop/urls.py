from django.urls import path
from . import views

urlpatterns = [
    path('sale/', views.sale),
    path('<str:category>/', views.category_detail),
    path('<str:category>/<str:product>/', views.product_detail),
]