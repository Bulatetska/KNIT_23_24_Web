from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'full_name',
            'year_of_study',
            'student_id'
        ]