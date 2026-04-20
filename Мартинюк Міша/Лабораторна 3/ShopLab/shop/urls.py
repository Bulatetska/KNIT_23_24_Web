from django.urls import path

from . import views

urlpatterns = [
    path("sale/", views.sale, name="sale"),
    path("<str:category>/<str:product>/", views.product, name="product"),
    path("<str:category>/", views.category, name="category"),
]
