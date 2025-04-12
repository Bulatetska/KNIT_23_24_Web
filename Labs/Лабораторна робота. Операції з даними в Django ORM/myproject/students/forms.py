from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'year', 'student_card']

class UpdateYearForm(forms.Form):
    student_card = forms.CharField(max_length=50, label="Номер студентського квитка")
    new_year = forms.IntegerField(label="Новий рік навчання")