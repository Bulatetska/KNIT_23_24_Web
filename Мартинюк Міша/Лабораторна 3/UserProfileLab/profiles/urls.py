from django.urls import include, path

from . import views

users_urlpatterns = [
    path("", views.users_list, name="users_list"),
    path("<str:username>/", views.user_detail, name="user_detail"),
    path("<str:username>/orders/", views.user_orders, name="user_orders"),
]

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", include((users_urlpatterns, "profiles"))),
]
