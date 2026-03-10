from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Головна
    path('', views.home),
    
    # Завдання 1 (через include)
    path('users/', include('hello.urls')),
    
    # Завдання 2 (Магазин)
    path('shop/', views.shop_home),
    path('shop/sale/', views.sale_view),
    path('shop/<str:category>/', views.category_view),
    path('shop/<str:category>/<str:product>/', views.product_view),
    
    # Завдання 3 (JSON API)
    path('api/users/', views.get_users_json),
    path('api/users/<str:name>/', views.get_user_detail_json),
    
    # Завдання 4 (Курси)
    path('courses/', views.course_list),
    path('courses/<str:course_name>/', views.course_detail),
    path('courses/<str:course_name>/modules/', views.module_list),
    path('courses/<str:course_name>/modules/<int:module_id>/', views.module_detail),
]