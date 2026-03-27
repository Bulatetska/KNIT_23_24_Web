from django.shortcuts import render
from .models import Student
a = Student(Name='Олександр Іваненко', Year=2, Student_ID='S123456789')
a.save()
b = Student(Name='Марія Петренко', Year=3, Student_ID='S987654321')
b.save()
def update_student_year(student_id, new_year):
    try:
        student = Student.objects.get(Student_ID=student_id)
        student.Year = new_year
        student.save()
        print(f"Updated {student.Name}'s year to {new_year}.")
    except Student.DoesNotExist:
        print("Student not found.")
def delete_student(student_id):
    try:
        student = Student.objects.get(Student_ID=student_id)
        if(student.Year == 5):
            student.delete()
            print(f"Deleted student with ID {student_id}.")
        else:
            print(f"Cannot delete student with ID {student_id} because they are not at the end of their final year.")
    except Student.DoesNotExist:
        print("Student not found.")
def retrieve_students_by_year():
    return Student.objects.all().order_by('-Year')
