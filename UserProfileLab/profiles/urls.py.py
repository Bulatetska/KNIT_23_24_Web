from django.urls import path
from . import views
import include

# Вкладені маршрути для користувачів
user_patterns = [
    path('', views.user_list, name='user_list'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('<str:username>/orders/', views.user_orders, name='user_orders'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include(user_patterns)),
]