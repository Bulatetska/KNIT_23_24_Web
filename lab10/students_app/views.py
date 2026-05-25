from django.shortcuts import render
from django.db.models import Count
from .models import Student, Course

def index(request):
    # Додаємо тестові дані, якщо база порожня
    if not Student.objects.exists():
        Student.objects.create(full_name="Іванов Іван", year_of_study=3, student_id="ВНУ-001")
        Student.objects.create(full_name="Шевченко Тарас", year_of_study=1, student_id="ВНУ-002")
        Student.objects.create(full_name="Франко Іван", year_of_study=4, student_id="ВНУ-003")
    if not Course.objects.exists():
        Course.objects.create(name="Програмування на C++", duration_hours=120)
        Course.objects.create(name="Основи Python", duration_hours=80)
        Course.objects.create(name="Кібербезпека", duration_hours=150)

    result_data = None
    task_title = ""

    # Обробка натискань на кнопки
    if request.method == 'POST':
        task = request.POST.get('task')
        
        if task == 'task1':
            task_title = "Завдання 1: Студенти 3 курсу"
            qs = Student.objects.filter(year_of_study=3).values('full_name', 'year_of_study')
            result_data = [f"{s['full_name']} ({s['year_of_study']} курс)" for s in qs]
            
        elif task == 'task2':
            task_title = "Завдання 2: Перевірка студентського квитка"
            ticket = request.POST.get('ticket_id', '').strip()
            exists = Student.objects.filter(student_id=ticket).exists()
            result_data = f"Студент з квитком '{ticket}' {'ЗНАЙДЕНИЙ' if exists else 'НЕ ЗНАЙДЕНИЙ'} у базі."
            
        elif task == 'task3':
            task_title = "Завдання 3: Кількість студентів по курсах"
            qs = Student.objects.values('year_of_study').annotate(count=Count('id')).order_by('year_of_study')
            result_data = [f"Курс {group['year_of_study']}: {group['count']} студент(ів)" for group in qs]
            
        elif task == 'task4':
            task_title = "Завдання 4: Студенти старше 2 курсу (через SQL raw)"
            qs = Student.objects.raw("SELECT * FROM students_app_student WHERE year_of_study > 2")
            result_data = [f"{s.full_name} ({s.year_of_study} курс)" for s in qs]
            
        elif task == 'task5':
            task_title = "Завдання 5: Курси > 100 годин (як словник)"
            # Використовуємо values_list для швидкого перетворення у словник {Назва: Тривалість}
            qs = Course.objects.filter(duration_hours__gt=100).values_list('name', 'duration_hours')
            result_data = dict(qs)

    return render(request, 'students_app/index.html', {'result_data': result_data, 'task_title': task_title})
