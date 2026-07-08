from django.shortcuts import render, redirect
from .models import Student

def get_sorted_students(direction='desc'):
    """Повертає студентів, відсортованих за роком у вказаному напрямку"""
    if direction == 'desc':
        return Student.objects.all().order_by('-year')  # Від 5 до 1
    return Student.objects.all().order_by('year')       # Від 1 до 5

def index(request):
    students = Student.objects.all()
    # За замовчуванням наступний клік має сортувати зворотно
    next_sort_dir = 'desc'

    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'add':
            Student.objects.create(name=request.POST.get('name'), year=request.POST.get('year'), student_id=request.POST.get('student_id'))
            return redirect('index')
        elif action == 'update':
            Student.objects.filter(student_id=request.POST.get('student_id_update')).update(year=request.POST.get('new_year'))
            return redirect('index')
        elif action == 'remove_graduated':
            Student.objects.filter(year=5).delete()
            return redirect('index')
        elif action == 'sort':
            # Читаємо, який напрямок зараз запросив користувач (через приховане поле)
            req_dir = request.POST.get('sort_dir', 'desc')
            
            # Отримуємо відсортований список
            students = get_sorted_students(req_dir)
            
            # Змінюємо напрямок на протилежний для наступного кліку
            next_sort_dir = 'asc' if req_dir == 'desc' else 'desc'
            
            return render(request, 'students/index.html', {'students': students, 'sort_dir': next_sort_dir})

    # Передаємо змінну sort_dir у шаблон для правильного стану кнопки
    return render(request, 'students/index.html', {'students': students, 'sort_dir': next_sort_dir})
