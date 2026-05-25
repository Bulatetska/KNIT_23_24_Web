from django.urls import path
from .views import user_list, user_detail, user_orders

urlpatterns = [
    path('', user_list), # /users/
    path('<str:username>/', user_detail), # /users/ivan/
    path('<str:username>/orders/', user_orders), # /users/ivan/orders/
]