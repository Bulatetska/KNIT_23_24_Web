from .models import Student, Course
from django.db.models import Count


def get_third_year_students():
    students = Student.objects.filter(year_of_study=3).values(
        'full_name',
        'year_of_study'
    )

    return list(students)

def check_student_exists(student_id):

    exists = Student.objects.filter(student_id=student_id).exists()

    if exists:
        return "Студент знайдений у базі"
    else:
        return "Студента не знайдено"

def students_group_by_year():

    data = Student.objects.values('year_of_study') \
        .annotate(count=Count('id')) \
        .order_by('year_of_study')

    return list(data)

def students_raw_query():

    sql = """
        SELECT *
        FROM students_student
        WHERE year_of_study > 2
    """

    return list(Student.objects.raw(sql))

def long_courses_dict():

    courses = Course.objects.filter(duration_hours__gt=100)

    return {
        course.course_name: course.duration_hours
        for course in courses
    }