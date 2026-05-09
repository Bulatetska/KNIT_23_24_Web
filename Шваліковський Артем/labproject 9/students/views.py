from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    form = StudentForm()

    return render(request, 'students/student_list.html', {
        'students': students,
        'form': form
    })


# ДОДАЄМО СТВОРЕННЯ
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('student_list')


# ➤ ОНОВЛЕННЯ КУРСУ
def update_year(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        new_year = request.POST.get("year")
        student.year_of_study = new_year
        student.save()

    return redirect('student_list')


# ➤ ВИДАЛЕННЯ
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')