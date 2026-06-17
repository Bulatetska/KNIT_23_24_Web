from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('coursed.urls')),  # або 'courses.urls' залежно від назви
]