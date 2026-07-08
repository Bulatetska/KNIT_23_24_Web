from django.contrib import admin
from django.urls import path
from api.views import get_users, get_user_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', get_users),            # Для списку http://127.0.0.1:8000/api/users/
    path('api/users/<str:name>/', get_user_detail), # Для деталей http://127.0.0.1:8000/api/users/Ivan/
]