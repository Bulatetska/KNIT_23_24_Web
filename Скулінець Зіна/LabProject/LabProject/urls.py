from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), 
    path('users/', include('hello.urls')),
    
    # Маршрути магазину мають бути ТУТ (до закриваючої дужки)
    path('shop/', views.shop_home),
    path('shop/sale/', views.sale_view),
    path('shop/<str:category>/', views.category_view),
    path('shop/<str:category>/<str:product>/', views.product_view),
    path('api/users/', views.user_api_list),
    path('api/users/<str:name>/', views.user_api_detail),
    path('courses/', views.course_list),
    path('courses/<str:course_name>/', views.course_detail),
    path('courses/<str:course_name>/modules/', views.module_list),
    path('courses/<str:course_name>/modules/<int:module_id>/', views.module_detail),
] # Ось ця дужка має бути в самому кінці