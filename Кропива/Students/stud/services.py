from .models import Student

def update_student_year(student_id, new_year):
    Student.objects.filter(student_id=student_id).update(year=new_year)