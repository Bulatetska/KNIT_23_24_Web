from django.urls import path
from .views import register, feedback

urlpatterns = [
    path("register/", register, name="register"),
    path("feedback/", feedback, name="feedback"),
]
