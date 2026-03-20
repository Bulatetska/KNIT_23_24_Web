from django.urls import path
from . import views

urlpatterns = [
    path('sale/', views.sale, name='sale'),
    path('<str:category>/', views.category, name='category'),
    path('<str:category>/<str:product>/', views.product, name='product'),
]