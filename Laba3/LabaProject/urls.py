from django.contrib import admin
from django.urls import path, include
from profiles.views import home_page 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page), 
    path('', include('profiles.urls')), 
    path('shop/', include('shop.urls')), 
    path('api/', include('api.urls')),   
    path('courses/', include('courses.urls')), 
]