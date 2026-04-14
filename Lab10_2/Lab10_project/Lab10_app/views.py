from django.shortcuts import render
from .models import Student, Course

def create_all():
    if Student.objects.count() == 0:
        Student.objects.create(name="Аліса", year_of_study=2, stud_id="S001")
        Student.objects.create(name="Боб", year_of_study=3, stud_id="S002")
        Student.objects.create(name="Чарлі", year_of_study=1, stud_id="S003")
        Student.objects.create(name="Стас", year_of_study=3, stud_id="S004")
        Student.objects.create(name="Олена", year_of_study=4, stud_id="S005")
        Student.objects.create(name="Антон", year_of_study=5, stud_id="S006")
        Student.objects.create(name="Аліна", year_of_study=2, stud_id="S007")
        Student.objects.create(name="Марія", year_of_study=3, stud_id="S008")
        Student.objects.create(name="Діана", year_of_study=1, stud_id="S009")
        Student.objects.create(name="Іван", year_of_study=2, stud_id="S010")
        Student.objects.create(name="Петро", year_of_study=3, stud_id="S011")
        Student.objects.create(name="Любомир", year_of_study=5, stud_id="S012")
    if Course.objects.count() == 0:
        Course.objects.create(name="Математика", hours=120)
        Course.objects.create(name="Фізика", hours=100)
        Course.objects.create(name="Інформатика", hours=150)
        Course.objects.create(name="Хімія", hours=80)
        Course.objects.create(name="Біологія", hours=90)

def index(request):
    all = Student.objects.all()
    all.delete()
    create_all()
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'spiski': 'Список студентів','spiski2': 'Список курсів', 'students': students, 'courses': courses})

def only_3_year_students(request):
    create_all()
    students = Student.objects.filter(year_of_study=3)
    return render(request, 'index.html', {'spiski': 'Студенти 3-го курсу', 'students': students})

def check_student(request):
    message = ''

    if request.method == "POST":
        stud_id = request.POST.get("stud_id")

        if Student.objects.filter(stud_id=stud_id).exists():
            message = "Студент знайдений"
        else:
            message = "Студент не знайдений"

    return render(request, "get_by_stud_id.html", {
        "message": message
    })