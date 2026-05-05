from django.shortcuts import render, redirect
from .models import Student

def student_manager(request):
    if request.method == "POST":
        if "add_student" in request.POST:
            Student.objects.create(
                full_name=request.POST.get("full_name"),
                year=request.POST.get("year"),
                ticket=request.POST.get("ticket")
            )
        
        elif "delete_student" in request.POST:
            Student.objects.filter(id=request.POST.get("student_id")).delete()
        
        elif "update_year" in request.POST:
            ticket_num = request.POST.get("ticket_number")
            new_year = request.POST.get("new_year")
            Student.objects.filter(ticket=ticket_num).update(year=new_year)
        
        return redirect('student_manager')

    students = Student.objects.all().order_by('-year')
    return render(request, 'index.html', {'students': students})