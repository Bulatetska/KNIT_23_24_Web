from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list),
    path('<str:course_name>/', course_detail),
    path('<str:course_name>/modules/', module_list),
    path('<str:course_name>/modules/<int:module_id>/', module_detail),
]