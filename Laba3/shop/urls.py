from django.urls import path  # ВОТ ЭТОЙ СТРОКИ НЕ ХВАТАЛО
from .views import *

urlpatterns = [
    path('', shop_home),
    path('sale/', sale_view),
    path('<str:category>/', category_view),
    path('<str:category>/<str:product>/', product_view),
]