from django.contrib import admin
from django.urls import path
from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', course_list),                                      # Список
    path('courses/<str:course_name>/', course_detail),                 # Деталі курсу
    path('courses/<str:course_name>/modules/', course_modules),        # Всі модулі
    path('courses/<str:course_name>/modules/<int:module_id>/', module_detail), # Конкретний модуль
]