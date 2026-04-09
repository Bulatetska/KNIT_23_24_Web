from django.shortcuts import render
from .models import Student, Course

def create_all():
    if Student.objects.count() == 0:
        Student.objects.create(name="Аліса", year_of_study=2)
        Student.objects.create(name="Боб", year_of_study=3)
        Student.objects.create(name="Чарлі", year_of_study=1)
        Student.objects.create(name="Стас", year_of_study=3)
        Student.objects.create(name="Олена", year_of_study=4)
        Student.objects.create(name="Антон", year_of_study=5)
        Student.objects.create(name="Аліна", year_of_study=2)
        Student.objects.create(name="Марія", year_of_study=3)
        Student.objects.create(name="Діана", year_of_study=1)
        Student.objects.create(name="Іван", year_of_study=2)
        Student.objects.create(name="Петро", year_of_study=3)
        Student.objects.create(name="Любомир", year_of_study=5)
    if Course.objects.count() == 0:
        Course.objects.create(name="Математика", hours=120)
        Course.objects.create(name="Фізика", hours=100)
        Course.objects.create(name="Інформатика", hours=150)
        Course.objects.create(name="Хімія", hours=80)
        Course.objects.create(name="Біологія", hours=90)
def index(request):
    create_all()
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
