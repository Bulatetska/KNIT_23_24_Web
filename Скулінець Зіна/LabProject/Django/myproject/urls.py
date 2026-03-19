from django.contrib import admin
from django.urls import path, include
from shop.views import products # Переконайся, що імпорт правильний

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products),
    path('', include('shop.urls')),
]