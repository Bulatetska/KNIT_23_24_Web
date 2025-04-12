from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, UpdateYearForm
from django.contrib import messages

# 1. Створення студентів
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Студента створено!")
            return redirect('create_student')
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})

# 2. Оновлення року навчання
def update_year(request):
    if request.method == 'POST':
        form = UpdateYearForm(request.POST)
        if form.is_valid():
            card = form.cleaned_data['student_card']
            year = form.cleaned_data['new_year']
            try:
                student = Student.objects.get(student_card=card)
                student.year = year
                student.save()
                messages.success(request, "Рік навчання оновлено.")
            except Student.DoesNotExist:
                messages.error(request, "Студента не знайдено.")
            return redirect('update_year')
    else:
        form = UpdateYearForm()
    return render(request, 'students/update_year.html', {'form': form})

# 3. Видалення студентів з year=5
def delete_finished(request):
    if request.method == 'POST':
        count, _ = Student.objects.filter(year=5).delete()
        messages.success(request, f"Видалено {count} студент(ів).")
        return redirect('delete_finished')
    return render(request, 'students/delete_finished.html')

# 4. Перегляд списку студентів (відсортовано)
def list_students(request):
    students = Student.objects.all().order_by('-year')
    return render(request, 'students/list_students.html', {'students': students})
