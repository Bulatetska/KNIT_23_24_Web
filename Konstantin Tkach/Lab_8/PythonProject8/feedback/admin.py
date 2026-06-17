from django.contrib import admin
from .models import Student, Course # Імпортуємо твої моделі

admin.site.register(Student) # Реєструємо Студентів
admin.site.register(Course)  # Реєструємо Курси