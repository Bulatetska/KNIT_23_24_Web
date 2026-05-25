from django.contrib import admin
from django.urls import path, include
from profiles.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # Головна
    path('users/', include('profiles.urls')), # Групування через include
]