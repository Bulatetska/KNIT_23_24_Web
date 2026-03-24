from django.contrib import admin
from django.urls import path, include
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('users/', include('profiles.urls')),
]