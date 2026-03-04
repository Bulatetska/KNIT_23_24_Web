from shop import views
from django.contrib import admin
from django.urls import include, path

shop_patterns = [
    path('/<str:category>', views.category),
    path('/<str:category>/<str:product>', views.product),
    path('/sale', views.sale),
]

urlpatterns = [
    path('', views.index),
    path('shop',include(shop_patterns))
]
