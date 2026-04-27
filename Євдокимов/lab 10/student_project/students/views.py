from django.shortcuts import render
from django.db.models import Count
from .models import Student, Course


def dashboard(request):
    # 🔍 пошук студента
    ticket = request.GET.get('ticket')
    found_student = None
    message = None

    if ticket:
        found_student = Student.objects.filter(ticket_number=ticket).first()
        if not found_student:
            message = "Студента не знайдено"

    # 🎓 студенти 3 курсу
    third_year = Student.objects.filter(year=3).values('full_name', 'year', 'ticket_number')

    # 📊 групування
    grouped = Student.objects.values('year').annotate(total=Count('id'))

    # 💾 raw SQL
    raw_students = Student.objects.raw(
        "SELECT * FROM students_student WHERE year > 2"
    )

    # 📚 курси > 100
    courses = Course.objects.filter(hours__gt=100).values('name', 'hours')

    return render(request, 'students/dashboard.html', {
        'third_year': third_year,
        'grouped': grouped,
        'raw_students': raw_students,
        'courses': courses,
        'found_student': found_student,
        'message': message
    })