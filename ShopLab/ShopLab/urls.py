from django.urls import path
from shop.views import *

urlpatterns = [
    path('', shop_home),
    path('shop/sale/', sale_view), # Статичний шлях ставимо ВИЩЕ динамічного
    path('shop/<str:category>/', category_view),
    path('shop/<str:category>/<str:product>/', product_view),
]