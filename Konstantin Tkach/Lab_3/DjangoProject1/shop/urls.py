from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_index'),
    path('<str:category>/', views.category, name='category'),
    path('<str:category>/<str:product>/', views.product, name='product'),
    path('sale/', views.sale, name='sale'),
]