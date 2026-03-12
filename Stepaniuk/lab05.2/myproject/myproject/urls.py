from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedback_app.urls')),  # всі запити йдуть у feedback_app
]