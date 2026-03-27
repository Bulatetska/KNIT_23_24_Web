"""
URL configuration for CourseLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from courses.views import course_details, courses, modules, modules_details
module_patterns = [
    path('', modules),
    path('<int:module_id>/', modules_details),
]
course_patterns = [
    path('', course_details),
    path('modules/', include(module_patterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', courses),
    path('courses/<str:course_name>/', include(course_patterns)),
]