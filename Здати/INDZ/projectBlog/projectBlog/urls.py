from django.urls import path, include
from django.contrib import admin
from blog import views

post_patterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('post/', include(post_patterns)),
]