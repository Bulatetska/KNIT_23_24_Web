from django.urls import path, include
from . import views

# Окремий список для вкладених маршрутів, як вимагає Завдання 1
user_patterns = [
    path('', views.user_detail),        # http://127.0.0.1:8000/users/<username>/
    path('orders/', views.user_orders), # http://127.0.0.1:8000/users/<username>/orders/
]

urlpatterns = [
    path('', views.user_list),                 # http://127.0.0.1:8000/users/
    path('<str:username>/', include(user_patterns)), # Вкладені маршрути через include()
]