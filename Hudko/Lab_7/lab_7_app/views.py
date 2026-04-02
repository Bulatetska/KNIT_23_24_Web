from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Student, Course

def create_students():
    Student.objects.update_or_create(
        student_id='S123456789',
        defaults={'full_name': 'Олександр Іваненко', 'year_of_study': 2}
    )
    Student.objects.update_or_create(
        student_id='S987654321',
        defaults={'full_name': 'Марія Петренко', 'year_of_study': 3}
    )

def update_student_year(s_id, new_year):
    updated_count = Student.objects.filter(student_id=s_id).update(year_of_study=new_year)
    return updated_count > 0

def delete_graduates():
    deleted, _ = Student.objects.filter(year_of_study=5).delete()
    return deleted

def student_lab_view(request):
    create_students()
    update_student_year('S123456789', 3)
    
    deleted_num = delete_graduates()
    
    students = Student.objects.all().order_by('-year_of_study')
    
    response_text = f"<h1>Випускники</h1>"
    response_text += f"<h2>Видалено випускників: {deleted_num}</h2>"
    response_text += "<ul>"
    for s in students:
        response_text += f"<li>{s.full_name} — {s.year_of_study} курс (ID: {s.student_id})</li>"
    response_text += "</ul>"
    
    return HttpResponse(response_text)


def demo_orm_operations(request):
    students_3rd_year = Student.objects.filter(year_of_study=3).values('full_name', 'year_of_study')

    def check_student_by_id(id_number):
        if Student.objects.filter(student_id=id_number).exists():
            return f"Студент з квитком №{id_number} знайдений."
        return f"Студента №{id_number} не знайдено."
    
    check_result = check_student_by_id('S987654321')

    grouping_stats = Student.objects.values('year_of_study').annotate(
        total=Count('id')
    ).order_by('year_of_study')

    raw_students = Student.objects.raw("SELECT * FROM lab_7_app_student WHERE year_of_study > 2")

    def get_long_courses_dict():
        return dict(Course.objects.filter(duration_hours__gt=100).values_list('course_name', 'duration_hours'))
    
    courses_dict = get_long_courses_dict()

    context = {
        'students_3rd_year': students_3rd_year,
        'check_result': check_result,
        'grouping_stats': grouping_stats,
        'raw_students': raw_students,
        'courses_dict': courses_dict,
    }

    return render(request, 'demo.html', context)