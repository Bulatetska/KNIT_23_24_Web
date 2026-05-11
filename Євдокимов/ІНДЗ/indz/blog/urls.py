from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment'),
]