from django.contrib import admin
from django.urls import path, include
from profiles import views as profiles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profiles_views.index, name='index'),           # з першого завдання
    path('users/', include('profiles.urls')),               # з першого завдання
    path('shop/', include('shop.urls')),                    # ДОДАЙТЕ ЦЕЙ РЯДОК
]