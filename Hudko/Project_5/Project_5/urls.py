
from django.urls import path

from userform import views
urlpatterns = [
    path('', views.register),
]
