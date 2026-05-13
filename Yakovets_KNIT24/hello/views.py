def create_students():
    Student.objects.get_or_create(
        full_name="Олександр Іваненко", 
        year_of_study=2, 
        student_id_card="S123456789"
    )
    Student.objects.get_or_create(
        full_name="Марія Петренко", 
        year_of_study=3, 
        student_id_card="S987654321"
    )