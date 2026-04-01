from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop/sale/', views.sale),
    path('shop/<str:category>/<str:product>/', views.product_view),
    path('shop/<str:category>/', views.category_view),
]
