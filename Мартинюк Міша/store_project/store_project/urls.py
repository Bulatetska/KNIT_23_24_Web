from django.contrib import admin
from django.urls import include, path

from shop.views import about, feedback, products, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('feedback/', feedback, name='feedback'),
    path('products', products, name='products'),
    path('', include('blog.urls')),
]
