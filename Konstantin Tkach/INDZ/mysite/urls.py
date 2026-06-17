from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ОСЬ ТУТ має бути .urls, а не .register
    path('', include('catalog.urls')),
]